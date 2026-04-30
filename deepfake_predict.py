"""
Deepfake face image classifier (DeepEye).

Architecture:
  MobileNetV2 (frozen, ImageNet weights, 224x224)
  -> GlobalAveragePooling2D
  -> Dense(128, relu)
  -> Dense(1, sigmoid)         # 0 = real, 1 = fake

Weights: deepfake_model_v3_final.h5 (saved with Keras 3 — uses 'batch_shape'
kwarg that Keras 2 / tf_keras refuses to deserialize). transformers /
sentence_transformers force TF_USE_LEGACY_KERAS=1 in-process, so neither
tf.keras nor `keras` reliably resolve to Keras 3 at runtime.

Workaround: rebuild the architecture in code, load weights only by name.
"""

import io
import os
import numpy as np
from PIL import Image

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Input
from tensorflow.keras.models import Model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'deepfake_model_v3_final.h5')

IMG_SIZE = 224

_model = None


def _build_model():
    inp = Input(shape=(IMG_SIZE, IMG_SIZE, 3), name='input_layer')
    base = MobileNetV2(input_tensor=inp, include_top=False, weights=None)
    base.trainable = False
    x = GlobalAveragePooling2D()(base.output)
    x = Dense(128, activation='relu')(x)
    out = Dense(1, activation='sigmoid')(x)
    return Model(inp, out)


def load_model():
    global _model
    if _model is None:
        m = _build_model()
        m.load_weights(MODEL_PATH, by_name=True, skip_mismatch=True)
        _model = m
    return _model


def predict_image_bytes(img_bytes: bytes) -> dict:
    if not img_bytes:
        return {'error': 'Rasm bo\'sh'}

    try:
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB').resize((IMG_SIZE, IMG_SIZE))
        arr = np.array(img, dtype='float32')
        arr = preprocess_input(arr)
        arr = np.expand_dims(arr, axis=0)

        model = load_model()
        prob = float(model.predict(arr, verbose=0)[0][0])
        label = 'FAKE' if prob >= 0.5 else 'REAL'

        return {
            'label': label,
            'fake_probability': round(prob * 100, 2),
            'real_probability': round((1 - prob) * 100, 2),
        }
    except Exception as e:
        return {'error': f'Tahlil amalga oshmadi: {str(e)}'}
