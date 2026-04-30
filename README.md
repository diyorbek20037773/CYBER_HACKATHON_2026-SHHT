# CYBER SHIELD

🎬 **Demo video** — bosing va ko'ring (rasm YouTube'ga olib boradi):

[![CYBER SHIELD demo](https://img.youtube.com/vi/XyddedqgFs8/maxresdefault.jpg)](https://www.youtube.com/watch?v=XyddedqgFs8 "CYBER SHIELD demo")

AI-asoslangan kiberxavfsizlik platformasi. 4 ta mustaqil model bilan phishing URL, spam matn, deepfake rasm va RAM ichidagi malware'ni aniqlaydi. Live RAM monitor host xotirasini real vaqtda kuzatadi.

## Modullar

| Model       | Vazifa                                | Stack                                  |
| ----------- | ------------------------------------- | -------------------------------------- |
| PhishGuard  | Phishing URL aniqlash                 | XGBoost · 30 feature (URL+HTML+WHOIS)  |
| TextShield  | Spam / phishing matn (50+ til)        | SentenceTransformer MiniLM-L12 + 6L FC |
| DeepEye     | Deepfake yuz rasm                     | MobileNetV2 → GAP → Dense (224×224)    |
| MemGuard    | RAM dump'dagi malware (Ransomware/Spyware/Trojan) | XGBoost (binary + multiclass) |
| Live RAM    | Hostning jonli RAM holati + top jarayonlar | psutil (har 2 sek) |

## Lokal ishga tushirish

```bash
python -m venv venv
source venv/Scripts/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Server: http://127.0.0.1:5000

## API Endpoint'lar

| Method | Path                | Body / Param          | Javob                                      |
| ------ | ------------------- | --------------------- | ------------------------------------------ |
| GET    | `/`                 | —                     | UI (index.html)                            |
| GET    | `/health`           | —                     | Har bir modulning yuklanish holati         |
| POST   | `/predict`          | `{"url": "..."}`      | `{label, phishing_probability, features}`  |
| POST   | `/predict_spam`     | `{"text": "..."}`     | `{label, spam_probability}`                |
| POST   | `/predict_deepfake` | form-data: `image`    | `{label, fake_probability}`                |
| POST   | `/predict_malmem`   | form-data: `csv`      | `{rows, malware_count, type_counts}`       |
| GET    | `/live_ram`         | —                     | `{percent, used_gb, top: [...]}`           |

## Texnologiyalar

- **Backend:** Flask 3.1, Gunicorn (prod)
- **ML:** XGBoost, TensorFlow/Keras 3, sentence-transformers, scikit-learn
- **Frontend:** Vanilla JS, Chart.js, globe.gl
- **Live monitor:** psutil

## Litsenziya

Hackathon 2026 demo loyihasi.
