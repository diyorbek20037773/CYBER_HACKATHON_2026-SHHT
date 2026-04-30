"""
Multilingual Spam / Phishing-text Classifier.

Stack:
  - Sentence-Transformer  : paraphrase-multilingual-MiniLM-L12-v2 (384-dim)
  - Classifier head       : FC 384 -> 256 -> 512 -> 256(LN) -> 128 -> 32 -> 2

Weights file: NLP.pth (state_dict of the classifier head only).
"""

import os
import torch
import torch.nn as nn
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'NLP.pth')

CLASS_DICT = {0: 'NORMAL', 1: 'SPAM'}


class Classifier(nn.Module):
    def __init__(self, input_size: int = 384, num_classes: int = 2):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 256)
        self.fc2 = nn.Linear(256, 512)
        self.fc3 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 128)
        self.fc5 = nn.Linear(128, 32)
        self.fc6 = nn.Linear(32, num_classes)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.layer_norm = nn.LayerNorm(256)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.layer_norm(x)
        x = self.relu(self.fc4(x))
        x = self.relu(self.fc5(x))
        x = self.dropout(x)
        return self.fc6(x)


_encoder = None
_classifier = None
_device = None


def load_model():
    global _encoder, _classifier, _device
    if _classifier is not None:
        return _encoder, _classifier, _device

    _device = 'cuda' if torch.cuda.is_available() else 'cpu'

    enc = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    enc.max_seq_length = 128
    enc.to(_device)

    clf = Classifier(384, 2).to(_device)
    state = torch.load(MODEL_PATH, map_location=_device, weights_only=True)
    clf.load_state_dict(state)
    clf.eval()

    _encoder, _classifier = enc, clf
    return _encoder, _classifier, _device


def predict_text(text: str) -> dict:
    text = (text or '').strip()
    if not text:
        return {'error': 'Matn bo\'sh'}

    try:
        enc, clf, device = load_model()
        emb = enc.encode(text, convert_to_tensor=True, device=device)
        emb = emb.unsqueeze(0)

        with torch.inference_mode():
            logits = clf(emb)
            probs = torch.softmax(logits, dim=1)[0]
            pred = int(torch.argmax(logits, dim=1).item())

        return {
            'text': text,
            'label': CLASS_DICT[pred],
            'spam_probability': round(float(probs[1]) * 100, 2),
            'normal_probability': round(float(probs[0]) * 100, 2),
        }
    except Exception as e:
        return {'error': f'Tahlil amalga oshmadi: {str(e)}'}
