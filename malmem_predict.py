"""
Memory-dump malware classifier (MemGuard).

Two XGBoost models trained on VolMemLyzer features:
  - xgb_malmem_binary.json  : malware vs benign
  - xgb_malmem_multi.json   : Benign / Ransomware / Spyware / Trojan

CSV input must contain VolMemLyzer feature columns (see memory_checker/samples/*.csv).
"""

import io
import os
import pickle

import numpy as np
import pandas as pd
import xgboost as xgb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'memory_checker', 'models')

_resources = None


def load_resources():
    global _resources
    if _resources is None:
        binary = xgb.XGBClassifier()
        binary.load_model(os.path.join(MODELS_DIR, 'xgb_malmem_binary.json'))

        multi = xgb.XGBClassifier()
        multi.load_model(os.path.join(MODELS_DIR, 'xgb_malmem_multi.json'))

        with open(os.path.join(MODELS_DIR, 'label_encoder.pkl'), 'rb') as f:
            le = pickle.load(f)
        with open(os.path.join(MODELS_DIR, 'feature_cols.pkl'), 'rb') as f:
            feat_cols = pickle.load(f)

        _resources = (binary, multi, le, feat_cols)
    return _resources


def predict_csv_bytes(csv_bytes: bytes) -> dict:
    if not csv_bytes:
        return {'error': 'CSV bo\'sh'}

    try:
        binary, multi, le, feat_cols = load_resources()
        df = pd.read_csv(io.BytesIO(csv_bytes))

        missing = [c for c in feat_cols if c not in df.columns]
        if missing:
            return {'error': f"Yetishmayotgan ustunlar: {missing[:5]}"}

        X = df[feat_cols].astype(float)
        b_proba = binary.predict_proba(X)[:, 1]
        m_proba = multi.predict_proba(X)
        m_preds = multi.predict(X)
        m_labels = le.inverse_transform(m_preds)
        classes = [str(c) for c in le.classes_]

        rows = []
        for i, (b, mp, ml) in enumerate(zip(b_proba, m_proba, m_labels)):
            is_mal = bool(b > 0.5)
            class_probs = {cls: round(float(p) * 100, 2) for cls, p in zip(classes, mp)}
            rows.append({
                'index': i + 1,
                'is_malware': is_mal,
                'label': str(ml) if is_mal else 'Benign',
                'malware_probability': round(float(b) * 100, 2),
                'class_probabilities': class_probs,
            })

        n = len(rows)
        mal_count = sum(1 for r in rows if r['is_malware'])

        type_counts = {}
        for r in rows:
            if r['is_malware']:
                type_counts[r['label']] = type_counts.get(r['label'], 0) + 1

        return {
            'total': n,
            'malware_count': mal_count,
            'safe_count': n - mal_count,
            'type_counts': type_counts,
            'classes': classes,
            'rows': rows[:50],
        }
    except Exception as e:
        return {'error': f'Tahlil amalga oshmadi: {str(e)}'}
