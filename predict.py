"""
Phishing URL prediction service.
Loads the XGBoost 30-feature model and runs feature extraction on a URL.
"""

import os
import numpy as np
import pandas as pd
import xgboost as xgb

from feature import FeatureExtraction

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'xgb_phishing30.json')

FEAT_COLS = [
    'UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
    'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
    'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
    'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
    'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick', 'UsingPopupWindow',
    'IframeRedirection', 'AgeofDomain', 'DNSRecording', 'WebsiteTraffic',
    'PageRank', 'GoogleIndex', 'LinksPointingToPage', 'StatsReport',
]

_model = None


def load_model():
    global _model
    if _model is None:
        m = xgb.XGBClassifier()
        m.load_model(MODEL_PATH)
        _model = m
    return _model


def predict_url(url: str) -> dict:
    url = (url or '').strip()
    if not url:
        return {'error': 'URL bo\'sh'}

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        model = load_model()
        obj = FeatureExtraction(url)
        feats = np.array(obj.getFeaturesList()).reshape(1, -1)
        X = pd.DataFrame(feats, columns=FEAT_COLS)
        prob = float(model.predict_proba(X)[0][1])
        pct = round(prob * 100, 2)
        label = 'PHISHING' if prob > 0.5 else 'SAFE'
        return {
            'url': url,
            'label': label,
            'phishing_probability': pct,
            'safe_probability': round((1 - prob) * 100, 2),
            'features': dict(zip(FEAT_COLS, [int(v) for v in obj.getFeaturesList()])),
        }
    except Exception as e:
        return {'url': url, 'error': f'Tahlil amalga oshmadi: {str(e)}'}
