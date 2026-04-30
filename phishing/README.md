# CyberShield — Phishing URL Detector
SCO Hackathon 2026

URL ni real-vaqtda tahlil qilib, phishing yoki xavfsiz ekanligini aniqlaydi.

---

## O'rnatish

**1. Python 3.10+ kerak** — [python.org](https://python.org) dan yuklab oling.

**2. Virtual muhit yarating:**
```
python -m venv venv
venv\Scripts\activate
```

**3. Kerakli paketlarni o'rnating:**
```
pip install -r requirements.txt
```

**4. `feature.py` ni yuklab oling (bir marta):**
```
setup.bat
```

**5. Model faylini qo'ying:**

`models/` papkasiga `xgb_phishing30.json` faylini joylashtiring.  
*(Model fayli alohida beriladi — Google Drive yoki USB orqali)*

---

## Ishlatish

### Streamlit (grafik interfeys) — tavsiya etiladi
```
streamlit run app.py
```
Brauzer avtomatik ochiladi → URL kiriting → "Tekshirish" tugmasini bosing.

### Terminal orqali
```
python check_url.py https://example.com
```

Bir nechta URL bir vaqtda:
```
python check_url.py https://google.com https://paypal-secure.login-verify.com
```

Interaktiv rejim (URL birin-ketin kiriting):
```
python check_url.py
```

---

## Papka tuzilmasi

```
phishing_checker/
├── app.py              — Streamlit grafik interfeys
├── check_url.py        — Terminal orqali ishlatish
├── requirements.txt    — Kerakli paketlar
├── setup.bat           — feature.py yuklab olish (bir marta)
├── models/
│   └── xgb_phishing30.json   — Model fayli (alohida beriladi)
└── repo/
    └── feature.py      — URL tahlil moduli (setup.bat orqali yuklanadi)
```

---

## Texnik ma'lumot

- **Model:** XGBoost (347 daraxt, Optuna bilan optimallashtrilgan)
- **Dataset:** 11,054 URL, 30 feature
- **Aniqlik:** ~97% (test to'plamida)
- **Tahlil vaqti:** 10–25 sekund (sahifa yuklash + domen tekshiruvi)
