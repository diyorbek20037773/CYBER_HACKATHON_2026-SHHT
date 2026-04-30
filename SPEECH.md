# CYBER SHIELD — Hakaton uchun nutq matni

> Taxminiy davomiyligi: **5–7 daqiqa**
> Til: O'zbek
> Jamoa: **CYBER SHIELD**

---

## 1. Salomlashuv va kirish (≈ 30 sek)

Assalomu alaykum, hurmatli hakamlar va ishtirokchilar!

Biz — **CYBER SHIELD** jamoasimiz. Bugun sizga kiberxavfsizlik sohasida ishlab chiqqan to'rt qatlamli AI-platformamizni taqdim etamiz.

---

## 2. Muammo (≈ 45 sek)

Bugungi raqamli dunyoda inson har kuni **to'rt xil tahdidga** duch keladi:

1. **Phishing havolalar** — bank, Telegram, ijtimoiy tarmoq akkauntlarini o'g'irlash uchun yuboriladigan qalbaki saytlar.
2. **Spam va firibgar matnlar** — SMS, e-mail, messenger orqali keladigan ijtimoiy muhandislik xabarlari.
3. **Deepfake rasmlar va videolar** — siyosiy, moliyaviy va shaxsiy obro'ga zarar yetkazuvchi soxta media.
4. **Ransomware / malware** — kompyuter xotirasiga yashirinib, ma'lumotlarni shifrlovchi va to'lov talab qiluvchi zararli dasturlar.

Bu tahdidlarning har biri uchun alohida vositalar bor, lekin **bitta joyda, bitta interfeysda** ishlovchi yechim deyarli yo'q.

---

## 3. Bizning yechim — CYBER SHIELD (≈ 30 sek)

Biz **bitta web platforma** ichiga **to'rtta mustaqil AI modelni** birlashtirdik. Foydalanuvchi brauzerdan kiradi, kerakli modulni tanlaydi va bir necha soniya ichida natija oladi.

Platforma **Flask** asosida qurilgan, modellar **lazy-load** rejimida ishlaydi — kerak bo'lganda yuklanadi, RAM tejaydi.

---

## 4. To'rt model — texnik yadro (≈ 2.5 daq)

### 4.1. PhishGuard — URL Phishing Detector

- **Model:** XGBoost (30 ta xususiyat).
- **Kirish:** istalgan URL.
- **Xususiyatlar:** IP-manzil ishlatilishi, URL uzunligi, `@` belgisi, sub-domenlar soni, HTTPS sertifikat, domen yoshi, Google indeksi, sahifa reytingi va h.k.
- **Chiqish:** `SAFE` yoki `PHISHING` + foiz ehtimollik.
- **Fayl:** `predict.py`, `feature.py`, `models/xgb_phishing30.json`.

### 4.2. TextShield — Multilingual Spam / Phishing Text

- **Stack:** `Sentence-Transformer` (paraphrase-multilingual-MiniLM-L12-v2, 384 o'lchov) + maxsus **PyTorch klassifikator**.
- **Arxitektura:** 384 → 256 → 512 → 256(LayerNorm) → 128 → 32 → 2.
- **Imkoniyat:** o'zbek, rus, ingliz va yana 50+ tilda ishlaydi — multilingual embedding tufayli.
- **Chiqish:** `NORMAL` yoki `SPAM` + ehtimollik.
- **Fayl:** `spam_predict.py`, `NLP.pth`.

### 4.3. DeepEye — Deepfake Image Detector

- **Stack:** TensorFlow / Keras, **MobileNetV2** (ImageNet og'irliklari) + Dense(128) + Sigmoid.
- **Kirish:** 224×224 yuz rasmi.
- **Chiqish:** `REAL` yoki `FAKE` + ehtimollik foizi.
- **Fayl:** `deepfake_predict.py`, `deepfake_model_v2.h5`.

### 4.4. MemGuard — Malware / Ransomware Memory Analyzer

- **Stack:** **Ikki XGBoost modeli** — VolMemLyzer xotira-dump xususiyatlari ustida.
  - **Binar model** — zararlimi yoki yo'q.
  - **Multiclass model** — `Benign / Ransomware / Spyware / Trojan` toifalashi.
- **Kirish:** `.csv` xotira-dump fayli.
- **Chiqish:** har bir qatordagi tahdid turi va foizlari, umumiy statistika.
- **Fayl:** `malmem_predict.py`, `memory_checker/models/`.

---

## 5. Texnologik stack qisqacha (≈ 20 sek)

- **Backend:** Python, Flask.
- **ML/DL:** XGBoost, PyTorch, TensorFlow, Sentence-Transformers, scikit-learn.
- **Frontend:** HTML / CSS / JS (neon-yashil minimal cyber dizayn).
- **Deploy:** Procfile orqali Heroku/Render-ga tayyor.

---

## 6. Jamoa (≈ 30 sek)

- **Eldor Musayev** — Team Lead, Cyber Engineer.
- **Ubaydullayev G'iyosiddin** — ML Engineer.
- **Ibragimov Diyorbek** — Full Stack Developer.

Har bir a'zo o'z sohasida kuchli, biz ML va kiberxavfsizlikni bitta yechimda birlashtirdik.

---

## 7. Yutuqlarimiz (≈ 30 sek)

Jamoamiz allaqachon yirik musobaqalarda sinovdan o'tgan:

- **National AI Hackathon (Termiz, 31 mart – 3 aprel)** — 500+ ishtirokchi orasida **1-o'rin**, MacBook M4 sovrini.
- **"REAL HOLAT" Hakaton (School 21, 14–15 mart)** — 100+ jamoa orasidan saralanib, finalda **1-o'rin** va **260 mln so'mlik mukofot fondi**dan ulush, Strategik Islohotlar Agentligi va GIZ hamkorligida.

Demak, **CYBER SHIELD** — bir kechada qurilgan loyiha emas, balki tajribali jamoaning navbatdagi mahsuloti.

---

## 8. Demo va xulosa (≈ 30 sek)

Hozir sizga jonli demoni ko'rsatamiz:

1. Phishing URL kiritamiz → natija.
2. Spam matn kiritamiz (o'zbekcha) → natija.
3. Deepfake rasm yuklaymiz → natija.
4. Xotira-dump CSV yuklaymiz → ransomware aniqlash.

Xulosa: **CYBER SHIELD** — bitta darvoza, to'rt qalqon. Oddiy foydalanuvchidan SOC-analitikgacha foydalana oladigan **modulli AI kiberxavfsizlik platformasi**.

E'tiboringiz uchun rahmat! Savollaringizga tayyormiz.

---

## Q&A uchun zaxira faktlar

- Modellar **on-demand** yuklanadi (`load_model()` lazy pattern) → server start tez.
- TextShield `paraphrase-multilingual-MiniLM-L12-v2` tufayli **50+ tilni** qo'llaydi.
- PhishGuard 30 ta featureni **real vaqtda** ekstraksiya qiladi (DNS, WHOIS, HTML parse).
- MemGuard ikki bosqichli — avval binar, keyin multiclass: **false-positive** kamaytiradi.
- Platforma to'liq **REST API** sifatida ham ishlatilishi mumkin (`/predict`, `/predict_spam`, `/predict_deepfake`, `/predict_malmem`).
