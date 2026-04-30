// ==================== TRANSLATIONS ====================
const translations = {
    uz: {
        nav_home: "Bosh sahifa", nav_cc: "Command", nav_video: "Video", nav_data: "Dataset", nav_eda: "EDA",
        nav_models: "Modellar", nav_shap: "SHAP", nav_demo: "URL Demo", nav_spam: "Spam Demo",
        nav_deepfake: "Deepfake", nav_malmem: "Memory",
        nav_results: "Natijalar", nav_achievements: "Yutuqlar", nav_team: "Jamoa",
        hero_badge: "AI-Powered Security",
        hero_subtitle: "Unified AI Cyber-Defense Platform — Phishing URL, Spam matnlari, Deepfake va RAM malware aniqlash bir markazda",
        cs_url_title: "Phishing URL Tekshirish", cs_url_btn: "Tekshirishni boshlash",
        cs_spam_title: "Spam / Phishing-text", cs_spam_btn: "Matnni tahlil qilish",
        cs_df_title: "Deepfake Detector", cs_df_btn: "Rasmni tahlil qilish",
        cs_mm_title: "RAM Xotira Tahlili", cs_mm_btn: "CSV ni tahlil qilish",
        nav_models: "Modellar",
        mi_sub: "CYBER SHIELD platformasi ishlatadigan 4 ta AI model",
        mi_dataset: "Dataset:", mi_features: "Featurelar:", mi_arch: "Arxitektura:",
        mi_input: "Kirish:", mi_output: "Chiqish:",
        model_colab: "Google Colab Notebook",
        hero_stat1: "URL namunalari", hero_stat3: "Feature",
        video_title: "Demo Video", video_sub: "Tizimning real ishlashini tomosha qiling",
        video_explore: "Loyihani batafsil ko'rish",
        dataset_title: "Dataset", dataset_desc: "URL, HTML va WHOIS belgilari asosida tayyorlangan namunalar",
        ds_train: "Train qatorlar", ds_test: "Test qatorlar",
        ds_cols: "Featurelar", ds_fraud: "Phishing nisbati",
        ds_normal_pct: "Legit 55.7%", ds_fraud_pct: "Phishing 44.3%",
        ds_main_cols: "Asosiy featurelar:",
        eda_title: "Ma'lumotlar tahlili (EDA)", eda_chart1: "Phishing vs Legit",
        eda_chart2: "Eng muhim featurelar", eda_chart3: "URL uzunligi taqsimoti",
        eda_chart4: "HTTPS holati",
        feat_title: "Feature Engineering", feat_added: "Asosiy feature guruhlari",
        feat_removed: "Encoding qiymatlari",
        feat_url: "URL uzunligi, IP, @, //, prefix/suffix, sub-domain",
        feat_html: "Iframe, popup, right-click, status bar, script linklar",
        feat_domain: "DomainRegLen, AgeofDomain, DNSRecording",
        feat_sec: "HTTPS, NonStdPort, Favicon, ServerFormHandler",
        feat_rep: "PageRank, GoogleIndex, WebsiteTraffic, StatsReport",
        feat_content: "RequestURL, AnchorURL, LinksInScriptTags, InfoEmail",
        feat_pipe1: "URL → Feature Extraction → XGBoost → Probability",
        feat_result: "Natija: <strong>30 feature</strong> → modelga kiradi",
        models_title: "Modellar solishtiruvi",
        models_sub: "Har bir model bir xil train/test split ustida sinaldi",
        tbl_model: "Model",
        shap_title: "Model tushuntirish (SHAP)",
        shap_sub: "Qaysi featurelar phishing aniqlashga eng ko'p ta'sir qiladi?",
        shap_placeholder: "SHAP grafigi",
        shap_what: "SHAP nima?",
        shap_desc: "SHAP (SHapley Additive exPlanations) — har bir feature modelning qaroriga qancha ta'sir qilganini ko'rsatadi.",
        shap_f1: "HTTPS — TLS bo'lmasa xavf yuqori",
        shap_f2: "AnchorURL — boshqa domen linklari ko'p",
        shap_f3: "PrefixSuffix — domen ichida \"-\" belgisi",
        shap_f4: "SubDomains — ko'p sub-domen shubhali",
        shap_f5: "AgeofDomain — yangi domen xavfli",
        demo_title: "Live Demo",
        demo_sub: "URL kiriting va phishing ekanligini tekshiring",
        form_url: "URL manzil",
        form_hint: "Sahifa HTML va WHOIS ma'lumotlari ham tahlil qilinadi (~10 sek).",
        form_btn: "Tekshirish",
        results_title: "Model Natijalari", results_conclusion: "Xulosa",
        res_1: "4 xil model sinab ko'rildi — <strong>XGBoost</strong> eng yaxshi natija berdi",
        res_2: "30 feature: URL + HTML + WHOIS belgilarini birlashtirgan",
        res_3: "SHAP orqali model qarori tushuntirildi",
        res_4: "Real-time URL skanerlash demo ishlab turibdi",
        ach_title: "Hakaton Yutuqlari", ach_sub: "Real musobaqalarda qo'lga kiritilgan g'alabalar",
        ach_1st: "1-O'RIN",
        ach1_title: "Umummilliy AI Hackathon",
        ach1_desc: "500 dan ortiq iqtidorli yoshlar ishtirok etgan musobaqada jamoamiz hakamlar tomonidan faxrli <strong>1-o'ringa</strong> loyiq topildi va <strong>MacBook M4</strong> noutbuklari bilan mukofotlandi.",
        ach1_prize: "MacBook M4 noutbuk",
        ach2_title: "\"REAL HOLAT\" Hakatoni — School 21",
        ach2_desc: "100 dan ortiq ishtirokchidan saralangan 36 jamoa bellashgan finalda <strong>\"DOPPIX\"</strong> jamoasi nomi ostida <strong>1-o'rinni</strong> egalladik.",
        ach2_prize: "260 million so'm mukofot fondi + Development Grant",
        team_title: "Jamoa", team_colab: "Google Colab Notebook",
        team_github: "GitHub Repo", team_youtube: "YouTube Kanal",
        footer_text: "Hakaton loyihasi",
        result_phish: "PHISHING ANIQLANDI!", result_safe: "XAVFSIZ URL",
        result_prob: "Phishing ehtimolligi:", all_models: "Tahlil qilingan featurelar:",
        analyzing: "Tahlil qilinmoqda...",
        spam_title: "Spam / Phishing-text Detector",
        spam_sub: "Multilingual NLP model — xabar matnini spam yoki normal sifatida tasniflaydi",
        spam_label: "Matn (UZ / RU / EN ...)",
        spam_hint: "SentenceTransformer (MiniLM-L12, 384-dim) + FC classifier (256→512→256→128→32→2)",
        spam_btn: "Tekshirish",
        spam_result_spam: "SPAM ANIQLANDI!", spam_result_normal: "NORMAL XABAR",
        spam_prob: "Spam ehtimolligi:", spam_breakdown: "Sinflar bo'yicha taqsimot:",
        spam_metrics_title: "Model aniqlik metrikalari",
        spam_m1: "Encoder: <strong>paraphrase-multilingual-MiniLM-L12-v2</strong> — 50+ til",
        spam_m2: "Embedding o'lchami: <strong>384</strong>, max_seq_length: 128",
        spam_m3: "Classifier: 6 qatlamli FC + LayerNorm + Dropout(0.2)",
        spam_m4: "Tasnif: <strong>0 = normal</strong>, <strong>1 = spam</strong>",
        df_title: "DeepEye — Deepfake Yuz Detektori",
        df_sub: "Transfer Learning (MobileNetV2) — yuz rasmini Real yoki Fake sifatida tasniflaydi",
        df_arch_title: "Arxitektura",
        df_a1: "ImageNet og'irliklari, frozen base — yuz mikro-artefaktlarni filtrlaydi",
        df_a2: "CNN xaritalarini vektorga aylantiradi",
        df_a3: "\"Fikrlash xonasi\" — deepfake belgilarini o'rganadi",
        df_a4: "0..1 ehtimollik — 0 = Real, 1 = Fake",
        df_train_title: "Training",
        df_t1: "Kaggle yuz rasmlari — <strong>140,000</strong> ta sifatli namuna",
        df_t2: "Avval tezkor o'qitish &rarr; <strong>89%</strong>",
        df_t3: "Keyin Learning Rate <strong>0.0001</strong> bilan chuqur fine-tuning",
        df_t4: "<code>deepfake_model_v2.h5</code> &mdash; barcha og'irliklar va qoidalar",
        df_label: "Yuz rasmi yuklang (jpg / png)",
        df_hint: "Rasm 224x224 ga o'lchanadi va MobileNetV2 preprocessing dan o'tadi.",
        df_btn: "Tahlil qilish",
        df_real: "REAL — Haqiqiy rasm", df_fake: "FAKE — Deepfake aniqlandi!",
        df_prob: "Fake ehtimolligi:", df_breakdown: "Sinflar bo'yicha taqsimot:",
        mm_title: "MemGuard — RAM Xotira Tahlili",
        mm_sub: "XGBoost binary + multi class — Benign, Ransomware, Spyware yoki Trojan",
        mm_class_title: "4 sinf",
        mm_c1: "Xavfsiz holat — malware aniqlanmadi",
        mm_c2: "Fayllarni shifrlaydi, to'lov so'raydi",
        mm_c3: "Ma'lumot o'g'irlaydi, kuzatadi",
        mm_c4: "Yashirin nazorat va backdoor",
        mm_pipe_title: "Pipeline",
        mm_p1: "VolMemLyzer chiqaradigan CSV — pslist / dlllist / handles / malfind / svcscan ustunlari",
        mm_p2: "Binary XGBoost &rarr; malware ehtimoli",
        mm_p3: "Multi-class XGBoost &rarr; aniq sinf",
        mm_samples: "Namunalar",
        mm_label: "VolMemLyzer CSV fayli",
        mm_hint: "Yuqoridagi namuna fayllarni yuklab oling va sinab ko'ring.",
        mm_btn: "Tahlil qilish",
        mm_safe: "HAMMASI XAVFSIZ", mm_threat: "XAVFLI YOZUV ANIQLANDI",
        mm_total: "Jami yozuv:", mm_mal: "Xavfli:", mm_breakdown: "Turlari bo'yicha:"
    },
    ru: {
        nav_home: "Главная", nav_cc: "Командный", nav_video: "Видео", nav_data: "Датасет", nav_eda: "EDA",
        nav_models: "Модели", nav_shap: "SHAP", nav_demo: "URL Демо", nav_spam: "Спам Демо",
        nav_deepfake: "Дипфейк", nav_malmem: "Память",
        nav_results: "Результаты", nav_achievements: "Достижения", nav_team: "Команда",
        hero_badge: "Безопасность на базе ИИ",
        hero_subtitle: "Единая AI кибер-защита — фишинг URL, спам-тексты, дипфейки и анализ ОЗУ в одном месте",
        cs_url_title: "Проверка фишинг URL", cs_url_btn: "Начать проверку",
        cs_spam_title: "Спам / Фишинг-текст", cs_spam_btn: "Анализировать текст",
        cs_df_title: "Дипфейк Детектор", cs_df_btn: "Анализировать фото",
        cs_mm_title: "Анализ ОЗУ", cs_mm_btn: "Анализировать CSV",
        nav_models: "Модели",
        mi_sub: "4 AI модели платформы CYBER SHIELD",
        mi_dataset: "Датасет:", mi_features: "Признаки:", mi_arch: "Архитектура:",
        mi_input: "Вход:", mi_output: "Выход:",
        model_colab: "Google Colab Notebook",
        hero_stat1: "URL образцов", hero_stat3: "Признаков",
        video_title: "Демо Видео", video_sub: "Посмотрите как работает система",
        video_explore: "Подробнее о проекте",
        dataset_title: "Датасет", dataset_desc: "Образцы на основе URL, HTML и WHOIS-признаков",
        ds_train: "Train строки", ds_test: "Test строки",
        ds_cols: "Признаков", ds_fraud: "Доля фишинга",
        ds_normal_pct: "Легит 55.7%", ds_fraud_pct: "Фишинг 44.3%",
        ds_main_cols: "Основные признаки:",
        eda_title: "Анализ данных (EDA)", eda_chart1: "Фишинг vs Легит",
        eda_chart2: "Главные признаки", eda_chart3: "Распределение длины URL",
        eda_chart4: "Состояние HTTPS",
        feat_title: "Feature Engineering", feat_added: "Группы признаков",
        feat_removed: "Значения кодировки",
        feat_url: "Длина URL, IP, @, //, префикс/суффикс, поддомен",
        feat_html: "Iframe, popup, right-click, status bar, script-ссылки",
        feat_domain: "DomainRegLen, AgeofDomain, DNSRecording",
        feat_sec: "HTTPS, NonStdPort, Favicon, ServerFormHandler",
        feat_rep: "PageRank, GoogleIndex, WebsiteTraffic, StatsReport",
        feat_content: "RequestURL, AnchorURL, LinksInScriptTags, InfoEmail",
        feat_pipe1: "URL → Feature Extraction → XGBoost → Probability",
        feat_result: "Итог: <strong>30 признаков</strong> → подаётся в модель",
        models_title: "Сравнение моделей",
        models_sub: "Все модели обучены на одинаковом разбиении",
        tbl_model: "Модель",
        shap_title: "Объяснение модели (SHAP)",
        shap_sub: "Какие признаки сильнее всего влияют на обнаружение фишинга?",
        shap_placeholder: "График SHAP",
        shap_what: "Что такое SHAP?",
        shap_desc: "SHAP (SHapley Additive exPlanations) — показывает, насколько каждый признак влияет на решение модели.",
        shap_f1: "HTTPS — отсутствие TLS = высокий риск",
        shap_f2: "AnchorURL — много ссылок на чужие домены",
        shap_f3: "PrefixSuffix — символ \"-\" в домене",
        shap_f4: "SubDomains — много поддоменов подозрительно",
        shap_f5: "AgeofDomain — новый домен опасен",
        demo_title: "Живое Демо",
        demo_sub: "Введите URL и проверьте на фишинг",
        form_url: "URL адрес",
        form_hint: "HTML и WHOIS страницы тоже анализируются (~10 сек).",
        form_btn: "Проверить",
        results_title: "Результаты модели", results_conclusion: "Вывод",
        res_1: "Протестировано 4 модели — <strong>XGBoost</strong> показал лучший результат",
        res_2: "30 признаков: URL + HTML + WHOIS",
        res_3: "Решения модели объяснены через SHAP",
        res_4: "Демо реал-тайм сканирования работает",
        ach_title: "Победы на хакатонах", ach_sub: "Реальные победы в соревнованиях",
        ach_1st: "1-МЕСТО",
        ach1_title: "Национальный AI Hackathon",
        ach1_desc: "В соревновании с 500+ участниками жюри присудило нашей команде <strong>1-е место</strong> и наградило ноутбуками <strong>MacBook M4</strong>.",
        ach1_prize: "MacBook M4",
        ach2_title: "Хакатон \"РЕАЛ ХОЛАТ\" — School 21",
        ach2_desc: "Из 100+ участников отобрали 36 команд; в финале команда <strong>\"DOPPIX\"</strong> заняла <strong>1-е место</strong>.",
        ach2_prize: "260 млн сум + Development Grant",
        team_title: "Команда", team_colab: "Google Colab Notebook",
        team_github: "GitHub Repo", team_youtube: "YouTube Канал",
        footer_text: "Хакатон-проект",
        result_phish: "ОБНАРУЖЕН ФИШИНГ!", result_safe: "БЕЗОПАСНЫЙ URL",
        result_prob: "Вероятность фишинга:", all_models: "Извлечённые признаки:",
        analyzing: "Анализируется...",
        spam_title: "Спам / Фишинг-текст Детектор",
        spam_sub: "Multilingual NLP модель — классифицирует сообщение как спам или нормальное",
        spam_label: "Текст (UZ / RU / EN ...)",
        spam_hint: "SentenceTransformer (MiniLM-L12, 384-dim) + FC classifier (256→512→256→128→32→2)",
        spam_btn: "Проверить",
        spam_result_spam: "ОБНАРУЖЕН СПАМ!", spam_result_normal: "ОБЫЧНОЕ СООБЩЕНИЕ",
        spam_prob: "Вероятность спама:", spam_breakdown: "Распределение по классам:",
        spam_metrics_title: "Метрики точности модели",
        spam_m1: "Encoder: <strong>paraphrase-multilingual-MiniLM-L12-v2</strong> — 50+ языков",
        spam_m2: "Размер эмбеддинга: <strong>384</strong>, max_seq_length: 128",
        spam_m3: "Classifier: 6-слойный FC + LayerNorm + Dropout(0.2)",
        spam_m4: "Классы: <strong>0 = normal</strong>, <strong>1 = spam</strong>",
        df_title: "DeepEye — Детектор дипфейков",
        df_sub: "Transfer Learning (MobileNetV2) — классифицирует лицо как Real или Fake",
        df_arch_title: "Архитектура",
        df_a1: "Веса ImageNet, frozen base — фильтрует микро-артефакты лица",
        df_a2: "Преобразует CNN-карты в вектор",
        df_a3: "\"Комната размышлений\" — учится отличать дипфейк-признаки",
        df_a4: "0..1 вероятность — 0 = Real, 1 = Fake",
        df_train_title: "Обучение",
        df_t1: "Лица с Kaggle — <strong>140,000</strong> качественных образцов",
        df_t2: "Сначала быстрое обучение &rarr; <strong>89%</strong>",
        df_t3: "Затем глубокий fine-tuning с LR <strong>0.0001</strong>",
        df_t4: "<code>deepfake_model_v2.h5</code> &mdash; все веса и правила",
        df_label: "Загрузите фото лица (jpg / png)",
        df_hint: "Изображение приводится к 224x224 и проходит MobileNetV2 preprocessing.",
        df_btn: "Анализировать",
        df_real: "REAL — Настоящее фото", df_fake: "FAKE — Обнаружен дипфейк!",
        df_prob: "Вероятность дипфейка:", df_breakdown: "Распределение по классам:",
        mm_title: "MemGuard — Анализ оперативной памяти",
        mm_sub: "XGBoost binary + multi-class — Benign, Ransomware, Spyware или Trojan",
        mm_class_title: "4 класса",
        mm_c1: "Безопасное состояние — вредоносов нет",
        mm_c2: "Шифрует файлы, требует выкуп",
        mm_c3: "Крадёт данные, следит",
        mm_c4: "Скрытый контроль и backdoor",
        mm_pipe_title: "Pipeline",
        mm_p1: "CSV из VolMemLyzer — pslist / dlllist / handles / malfind / svcscan",
        mm_p2: "Binary XGBoost &rarr; вероятность вредоноса",
        mm_p3: "Multi-class XGBoost &rarr; конкретный класс",
        mm_samples: "Примеры",
        mm_label: "CSV файл VolMemLyzer",
        mm_hint: "Скачайте пример выше и проверьте.",
        mm_btn: "Анализировать",
        mm_safe: "ВСЁ БЕЗОПАСНО", mm_threat: "ОБНАРУЖЕНА УГРОЗА",
        mm_total: "Всего записей:", mm_mal: "Вредоносных:", mm_breakdown: "По типам:"
    },
    en: {
        nav_home: "Home", nav_cc: "Command", nav_video: "Video", nav_data: "Dataset", nav_eda: "EDA",
        nav_models: "Models", nav_shap: "SHAP", nav_demo: "URL Demo", nav_spam: "Spam Demo",
        nav_deepfake: "Deepfake", nav_malmem: "Memory",
        nav_results: "Results", nav_achievements: "Achievements", nav_team: "Team",
        hero_badge: "AI-Powered Security",
        hero_subtitle: "Unified AI Cyber-Defense Platform — phishing URL, spam text, deepfake and RAM malware detection in one place",
        cs_url_title: "Phishing URL Check", cs_url_btn: "Start scan",
        cs_spam_title: "Spam / Phishing-text", cs_spam_btn: "Analyse text",
        cs_df_title: "Deepfake Detector", cs_df_btn: "Analyse image",
        cs_mm_title: "RAM Memory Analysis", cs_mm_btn: "Analyse CSV",
        nav_models: "Models",
        mi_sub: "4 AI models powering the CYBER SHIELD platform",
        mi_dataset: "Dataset:", mi_features: "Features:", mi_arch: "Architecture:",
        mi_input: "Input:", mi_output: "Output:",
        model_colab: "Google Colab Notebook",
        hero_stat1: "URL samples", hero_stat3: "Features",
        video_title: "Demo Video", video_sub: "Watch the system in action",
        video_explore: "Explore the project",
        dataset_title: "Dataset", dataset_desc: "Samples built from URL, HTML and WHOIS signals",
        ds_train: "Train rows", ds_test: "Test rows",
        ds_cols: "Features", ds_fraud: "Phishing rate",
        ds_normal_pct: "Legit 55.7%", ds_fraud_pct: "Phishing 44.3%",
        ds_main_cols: "Main features:",
        eda_title: "Exploratory Data Analysis (EDA)", eda_chart1: "Phishing vs Legit",
        eda_chart2: "Top features", eda_chart3: "URL length distribution",
        eda_chart4: "HTTPS status",
        feat_title: "Feature Engineering", feat_added: "Feature groups",
        feat_removed: "Encoding values",
        feat_url: "URL length, IP, @, //, prefix/suffix, sub-domain",
        feat_html: "Iframe, popup, right-click, status bar, script links",
        feat_domain: "DomainRegLen, AgeofDomain, DNSRecording",
        feat_sec: "HTTPS, NonStdPort, Favicon, ServerFormHandler",
        feat_rep: "PageRank, GoogleIndex, WebsiteTraffic, StatsReport",
        feat_content: "RequestURL, AnchorURL, LinksInScriptTags, InfoEmail",
        feat_pipe1: "URL → Feature Extraction → XGBoost → Probability",
        feat_result: "Result: <strong>30 features</strong> → fed into model",
        models_title: "Model Comparison",
        models_sub: "All models trained on the same split",
        tbl_model: "Model",
        shap_title: "Model Explainability (SHAP)",
        shap_sub: "Which features influence phishing detection the most?",
        shap_placeholder: "SHAP chart",
        shap_what: "What is SHAP?",
        shap_desc: "SHAP (SHapley Additive exPlanations) — shows how much each feature contributes to the model's decision.",
        shap_f1: "HTTPS — missing TLS is high risk",
        shap_f2: "AnchorURL — many external links",
        shap_f3: "PrefixSuffix — \"-\" inside domain",
        shap_f4: "SubDomains — many sub-domains suspicious",
        shap_f5: "AgeofDomain — new domain is risky",
        demo_title: "Live Demo",
        demo_sub: "Enter a URL and check if it is phishing",
        form_url: "URL address",
        form_hint: "Page HTML and WHOIS will also be analysed (~10 sec).",
        form_btn: "Check",
        results_title: "Model Results", results_conclusion: "Conclusion",
        res_1: "4 models tested — <strong>XGBoost</strong> achieved the best results",
        res_2: "30 features: URL + HTML + WHOIS combined",
        res_3: "Model decisions explained using SHAP",
        res_4: "Real-time URL scan demo is live",
        ach_title: "Hackathon Wins", ach_sub: "Real competition victories",
        ach_1st: "1st PLACE",
        ach1_title: "National AI Hackathon",
        ach1_desc: "Out of 500+ participants the jury awarded our team <strong>1st place</strong> with <strong>MacBook M4</strong> laptops as the prize.",
        ach1_prize: "MacBook M4 laptop",
        ach2_title: "\"REAL HOLAT\" Hackathon — School 21",
        ach2_desc: "100+ participants narrowed to 36 teams; team <strong>\"DOPPIX\"</strong> took <strong>1st place</strong> in the final.",
        ach2_prize: "260M UZS prize + Development Grant",
        team_title: "Team", team_colab: "Google Colab Notebook",
        team_github: "GitHub Repo", team_youtube: "YouTube Channel",
        footer_text: "Hackathon project",
        result_phish: "PHISHING DETECTED!", result_safe: "SAFE URL",
        result_prob: "Phishing probability:", all_models: "Extracted features:",
        analyzing: "Analysing...",
        spam_title: "Spam / Phishing-text Detector",
        spam_sub: "Multilingual NLP model — classifies a message as spam or normal",
        spam_label: "Text (UZ / RU / EN ...)",
        spam_hint: "SentenceTransformer (MiniLM-L12, 384-dim) + FC classifier (256→512→256→128→32→2)",
        spam_btn: "Check",
        spam_result_spam: "SPAM DETECTED!", spam_result_normal: "NORMAL MESSAGE",
        spam_prob: "Spam probability:", spam_breakdown: "Class breakdown:",
        spam_metrics_title: "Model accuracy metrics",
        spam_m1: "Encoder: <strong>paraphrase-multilingual-MiniLM-L12-v2</strong> — 50+ languages",
        spam_m2: "Embedding size: <strong>384</strong>, max_seq_length: 128",
        spam_m3: "Classifier: 6-layer FC + LayerNorm + Dropout(0.2)",
        spam_m4: "Classes: <strong>0 = normal</strong>, <strong>1 = spam</strong>",
        df_title: "DeepEye — Deepfake Face Detector",
        df_sub: "Transfer Learning (MobileNetV2) — classifies a face image as Real or Fake",
        df_arch_title: "Architecture",
        df_a1: "ImageNet weights, frozen base — filters facial micro-artefacts",
        df_a2: "Reduces CNN maps to a vector",
        df_a3: "\"Reasoning room\" — learns deepfake patterns",
        df_a4: "0..1 probability — 0 = Real, 1 = Fake",
        df_train_title: "Training",
        df_t1: "Kaggle face dataset — <strong>140,000</strong> quality samples",
        df_t2: "Initial fast training &rarr; <strong>89%</strong>",
        df_t3: "Deep fine-tuning at LR <strong>0.0001</strong>",
        df_t4: "<code>deepfake_model_v2.h5</code> &mdash; all weights and rules",
        df_label: "Upload a face image (jpg / png)",
        df_hint: "Image is resized to 224x224 and run through MobileNetV2 preprocessing.",
        df_btn: "Analyse",
        df_real: "REAL — Genuine photo", df_fake: "FAKE — Deepfake detected!",
        df_prob: "Fake probability:", df_breakdown: "Class breakdown:",
        mm_title: "MemGuard — RAM Memory Analysis",
        mm_sub: "XGBoost binary + multi-class — Benign, Ransomware, Spyware or Trojan",
        mm_class_title: "4 classes",
        mm_c1: "Safe state — no malware detected",
        mm_c2: "Encrypts files, demands ransom",
        mm_c3: "Steals data, monitors activity",
        mm_c4: "Stealth control and backdoor",
        mm_pipe_title: "Pipeline",
        mm_p1: "VolMemLyzer CSV — pslist / dlllist / handles / malfind / svcscan columns",
        mm_p2: "Binary XGBoost &rarr; malware probability",
        mm_p3: "Multi-class XGBoost &rarr; exact class",
        mm_samples: "Samples",
        mm_label: "VolMemLyzer CSV file",
        mm_hint: "Download a sample above and try it out.",
        mm_btn: "Analyse",
        mm_safe: "ALL CLEAN", mm_threat: "THREAT DETECTED",
        mm_total: "Total rows:", mm_mal: "Malicious:", mm_breakdown: "By type:"
    }
};

let currentLang = 'uz';

function applyTranslations(lang) {
    const t = translations[lang];
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (t[key] !== undefined) el.innerHTML = t[key];
    });
    document.documentElement.lang = lang;
}

document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        currentLang = btn.getAttribute('data-lang');
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyTranslations(currentLang);
        localStorage.setItem('lang', currentLang);
    });
});

const savedLang = localStorage.getItem('lang') || 'uz';
currentLang = savedLang;
document.querySelector(`.lang-btn[data-lang="${savedLang}"]`)?.classList.add('active');
document.querySelectorAll('.lang-btn').forEach(b => {
    if (b.getAttribute('data-lang') !== savedLang) b.classList.remove('active');
});
applyTranslations(savedLang);

// ==================== EDA CHARTS ====================

// Phishing vs Legit pie
const fraudPieCtx = document.getElementById('fraudPieChart');
if (fraudPieCtx) {
    new Chart(fraudPieCtx, {
        type: 'doughnut',
        data: {
            labels: ['Legit (55.7%)', 'Phishing (44.3%)'],
            datasets: [{
                data: [55.7, 44.3],
                backgroundColor: ['rgba(0, 243, 255, 0.7)', 'rgba(255, 180, 171, 0.75)'],
                borderColor: ['rgba(0, 243, 255, 0.3)', 'rgba(255, 180, 171, 0.3)'],
                borderWidth: 1,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { color: '#988d9f', font: { size: 11, family: 'Fira Code' } }
                }
            }
        }
    });
}

// Top important features (importance bar)
const categoryCtx = document.getElementById('categoryChart');
if (categoryCtx) {
    new Chart(categoryCtx, {
        type: 'bar',
        data: {
            labels: ['HTTPS', 'AnchorURL', 'PrefixSuffix', 'SubDomains', 'WebsiteTraffic',
                     'AgeofDomain', 'RequestURL', 'LinksInScriptTags', 'PageRank', 'DomainRegLen'],
            datasets: [{
                label: 'Importance',
                data: [0.21, 0.17, 0.12, 0.10, 0.08, 0.07, 0.06, 0.05, 0.04, 0.04],
                backgroundColor: 'rgba(0, 243, 255, 0.6)',
                borderColor: 'rgba(0, 243, 255, 0.9)',
                borderWidth: 1,
                borderRadius: 0
            }]
        },
        options: {
            responsive: true,
            indexAxis: 'y',
            plugins: { legend: { display: false } },
            scales: {
                x: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { color: 'rgba(57, 255, 20, 0.05)' }
                },
                y: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { display: false }
                }
            }
        }
    });
}

// URL length distribution (legit vs phishing)
const hourCtx = document.getElementById('hourChart');
if (hourCtx) {
    new Chart(hourCtx, {
        type: 'line',
        data: {
            labels: ['<30', '30-50', '50-75', '75-100', '100-150', '150-200', '200+'],
            datasets: [
                {
                    label: 'Legit',
                    data: [12, 38, 28, 14, 6, 1.5, 0.5],
                    borderColor: 'rgba(0, 243, 255, 0.9)',
                    backgroundColor: 'rgba(0, 243, 255, 0.08)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 2
                },
                {
                    label: 'Phishing',
                    data: [3, 12, 22, 26, 23, 10, 4],
                    borderColor: 'rgba(255, 180, 171, 0.9)',
                    backgroundColor: 'rgba(255, 180, 171, 0.08)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 2
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: '#988d9f', font: { family: 'Fira Code', size: 11 } }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { color: 'rgba(57, 255, 20, 0.05)' }
                },
                y: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { color: 'rgba(57, 255, 20, 0.05)' }
                }
            }
        }
    });
}

// HTTPS status comparison
const amtCtx = document.getElementById('amtChart');
if (amtCtx) {
    new Chart(amtCtx, {
        type: 'bar',
        data: {
            labels: ['HTTPS yo\'q', 'Shubhali', 'HTTPS bor'],
            datasets: [
                {
                    label: 'Legit',
                    data: [4, 8, 88],
                    backgroundColor: 'rgba(0, 243, 255, 0.55)',
                    borderColor: 'rgba(0, 243, 255, 0.3)',
                    borderWidth: 1,
                    borderRadius: 0
                },
                {
                    label: 'Phishing',
                    data: [62, 23, 15],
                    backgroundColor: 'rgba(255, 180, 171, 0.6)',
                    borderColor: 'rgba(255, 180, 171, 0.3)',
                    borderWidth: 1,
                    borderRadius: 0
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: '#988d9f', font: { family: 'Fira Code', size: 11 } }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { display: false }
                },
                y: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { color: 'rgba(57, 255, 20, 0.05)' },
                    title: { display: true, text: '%', color: '#988d9f' }
                }
            }
        }
    });
}

// Model comparison chart
const modelCtx = document.getElementById('modelCompareChart');
if (modelCtx) {
    new Chart(modelCtx, {
        type: 'bar',
        data: {
            labels: ['XGBoost', 'Random Forest', 'Gradient Boosting', 'Logistic Regression'],
            datasets: [
                {
                    label: 'F1 Score',
                    data: [0.97, 0.96, 0.94, 0.91],
                    backgroundColor: 'rgba(57, 255, 20, 0.7)',
                    borderColor: 'rgba(57, 255, 20, 0.3)',
                    borderWidth: 1,
                    borderRadius: 0
                },
                {
                    label: 'ROC-AUC',
                    data: [0.9942, 0.9905, 0.9818, 0.9612],
                    backgroundColor: 'rgba(0, 243, 255, 0.6)',
                    borderColor: 'rgba(0, 243, 255, 0.3)',
                    borderWidth: 1,
                    borderRadius: 0
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: '#988d9f', font: { family: 'Fira Code', size: 11 } }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 11 } },
                    grid: { display: false }
                },
                y: {
                    min: 0,
                    max: 1.05,
                    ticks: { color: '#988d9f', font: { family: 'Fira Code', size: 10 } },
                    grid: { color: 'rgba(57, 255, 20, 0.05)' }
                }
            }
        }
    });
}

// ==================== DEMO PREDICTION ====================
const form = document.getElementById('predictionForm');
if (form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const url = formData.get('url');

        const t = translations[currentLang];
        const btn = form.querySelector('.cs-btn');
        const originalHtml = btn.innerHTML;
        btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${t.analyzing}`;
        btn.disabled = true;

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url })
            });

            const result = await response.json();
            displayResult(result);
        } catch (error) {
            alert('Xatolik: ' + error.message);
        } finally {
            btn.innerHTML = originalHtml;
            btn.disabled = false;
        }
    });
}

function displayResult(result) {
    const resultCard = document.getElementById('resultCard');
    const mainResult = document.getElementById('mainResult');
    const modelResults = document.getElementById('modelResults');
    const t = translations[currentLang];

    resultCard.style.display = 'block';

    if (result.error) {
        mainResult.innerHTML = `
            <div class="result-main normal">
                <div class="result-icon-big"><i class="fas fa-exclamation-circle"></i></div>
                <div class="result-text">ERROR</div>
                <div class="result-prob">${result.error}</div>
            </div>
        `;
        modelResults.innerHTML = '';
        return;
    }

    const isPhish = result.label === 'PHISHING';

    mainResult.innerHTML = `
        <div class="result-main ${isPhish ? 'fraud' : 'normal'}">
            <div class="result-icon-big">
                <i class="fas ${isPhish ? 'fa-exclamation-triangle' : 'fa-check-circle'}"></i>
            </div>
            <div class="result-text">${isPhish ? t.result_phish : t.result_safe}</div>
            <div class="result-prob">${t.result_prob} ${result.phishing_probability}%</div>
            <div style="margin-top:0.5rem; font-size:0.85rem; opacity:0.7; word-break:break-all">
                ${result.url}
            </div>
        </div>
    `;

    const feats = result.features || {};
    const entries = Object.entries(feats);
    // Prioritize phish indicators (-1), then safe (+1). Cap at 4.
    const phish = entries.filter(([, v]) => v === -1);
    const safe  = entries.filter(([, v]) => v === 1);
    const top   = [...phish, ...safe].slice(0, 4);
    const total = entries.length;

    let html = `<h4 style="margin-bottom: 0.8rem; color: var(--text-secondary);">
        Asosiy belgilar <span style="opacity:0.6;font-weight:400">(${top.length}/${total})</span>
    </h4>`;
    for (const [name, val] of top) {
        const cls   = val === -1 ? 'prob-fraud' : 'prob-normal';
        const label = val === -1 ? 'Phish' : 'Safe';
        html += `
            <div class="model-result-item">
                <span class="model-result-name">${name}</span>
                <span class="model-result-prob ${cls}">${label} (${val})</span>
            </div>
        `;
    }
    modelResults.innerHTML = html;
}

// ==================== SPAM / NLP DEMO ====================
const spamForm = document.getElementById('spamForm');
if (spamForm) {
    spamForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fd = new FormData(spamForm);
        const text = fd.get('text');
        const t = translations[currentLang];
        const btn = spamForm.querySelector('.cs-btn');
        const orig = btn.innerHTML;
        btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${t.analyzing}`;
        btn.disabled = true;
        try {
            const r = await fetch('/predict_spam', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            displaySpamResult(await r.json());
        } catch (err) {
            alert('Error: ' + err.message);
        } finally {
            btn.innerHTML = orig;
            btn.disabled = false;
        }
    });
}

function displaySpamResult(result) {
    const card = document.getElementById('spamResultCard');
    const main = document.getElementById('spamMainResult');
    const detail = document.getElementById('spamModelResults');
    const t = translations[currentLang];
    card.style.display = 'block';

    if (result.error) {
        main.innerHTML = `
            <div class="result-main normal">
                <div class="result-icon-big"><i class="fas fa-exclamation-circle"></i></div>
                <div class="result-text">ERROR</div>
                <div class="result-prob">${result.error}</div>
            </div>`;
        detail.innerHTML = '';
        return;
    }

    const isSpam = result.label === 'SPAM';
    main.innerHTML = `
        <div class="result-main ${isSpam ? 'fraud' : 'normal'}">
            <div class="result-icon-big">
                <i class="fas ${isSpam ? 'fa-exclamation-triangle' : 'fa-check-circle'}"></i>
            </div>
            <div class="result-text">${isSpam ? t.spam_result_spam : t.spam_result_normal}</div>
            <div class="result-prob">${t.spam_prob} ${result.spam_probability}%</div>
        </div>`;

    detail.innerHTML = `
        <h4 style="margin-bottom: 0.8rem; color: var(--text-secondary);">${t.spam_breakdown}</h4>
        <div class="model-result-item">
            <span class="model-result-name">SPAM</span>
            <span class="model-result-prob prob-fraud">${result.spam_probability}%</span>
        </div>
        <div class="model-result-item">
            <span class="model-result-name">NORMAL</span>
            <span class="model-result-prob prob-normal">${result.normal_probability}%</span>
        </div>`;
}

// ==================== DEEPFAKE DEMO ====================
const dfForm = document.getElementById('deepfakeForm');
if (dfForm) {
    dfForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const file = dfForm.querySelector('input[name="image"]').files[0];
        if (!file) return;
        const fd = new FormData();
        fd.append('image', file);

        const t = translations[currentLang];
        const btn = dfForm.querySelector('.cs-btn');
        const orig = btn.innerHTML;
        btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${t.analyzing}`;
        btn.disabled = true;
        try {
            const r = await fetch('/predict_deepfake', { method: 'POST', body: fd });
            displayDeepfakeResult(await r.json());
        } catch (err) {
            alert('Error: ' + err.message);
        } finally {
            btn.innerHTML = orig;
            btn.disabled = false;
        }
    });
}

function displayDeepfakeResult(result) {
    const card = document.getElementById('deepfakeResultCard');
    const main = document.getElementById('deepfakeMainResult');
    const detail = document.getElementById('deepfakeModelResults');
    const t = translations[currentLang];
    card.style.display = 'block';

    if (result.error) {
        main.innerHTML = `
            <div class="result-main normal">
                <div class="result-icon-big"><i class="fas fa-exclamation-circle"></i></div>
                <div class="result-text">ERROR</div>
                <div class="result-prob">${result.error}</div>
            </div>`;
        detail.innerHTML = '';
        return;
    }

    const isFake = result.label === 'FAKE';
    main.innerHTML = `
        <div class="result-main ${isFake ? 'fraud' : 'normal'}">
            <div class="result-icon-big">
                <i class="fas ${isFake ? 'fa-user-slash' : 'fa-user-check'}"></i>
            </div>
            <div class="result-text">${isFake ? t.df_fake : t.df_real}</div>
            <div class="result-prob">${t.df_prob} ${result.fake_probability}%</div>
        </div>`;

    detail.innerHTML = `
        <h4 style="margin-bottom: 0.8rem; color: var(--text-secondary);">${t.df_breakdown}</h4>
        <div class="model-result-item">
            <span class="model-result-name">FAKE</span>
            <span class="model-result-prob prob-fraud">${result.fake_probability}%</span>
        </div>
        <div class="model-result-item">
            <span class="model-result-name">REAL</span>
            <span class="model-result-prob prob-normal">${result.real_probability}%</span>
        </div>`;
}

// ==================== MEMGUARD / MALMEM DEMO ====================
const mmForm = document.getElementById('malmemForm');
if (mmForm) {
    mmForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const file = mmForm.querySelector('input[name="csv"]').files[0];
        if (!file) return;
        const fd = new FormData();
        fd.append('csv', file);

        const t = translations[currentLang];
        const btn = mmForm.querySelector('.cs-btn');
        const orig = btn.innerHTML;
        btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${t.analyzing}`;
        btn.disabled = true;
        try {
            const r = await fetch('/predict_malmem', { method: 'POST', body: fd });
            displayMalmemResult(await r.json());
        } catch (err) {
            alert('Error: ' + err.message);
        } finally {
            btn.innerHTML = orig;
            btn.disabled = false;
        }
    });
}

function displayMalmemResult(result) {
    const card = document.getElementById('malmemResultCard');
    const main = document.getElementById('malmemMainResult');
    const detail = document.getElementById('malmemModelResults');
    const t = translations[currentLang];
    card.style.display = 'block';

    if (result.error) {
        main.innerHTML = `
            <div class="result-main normal">
                <div class="result-icon-big"><i class="fas fa-exclamation-circle"></i></div>
                <div class="result-text">ERROR</div>
                <div class="result-prob">${result.error}</div>
            </div>`;
        detail.innerHTML = '';
        return;
    }

    const isThreat = result.malware_count > 0;
    main.innerHTML = `
        <div class="result-main ${isThreat ? 'fraud' : 'normal'}">
            <div class="result-icon-big">
                <i class="fas ${isThreat ? 'fa-skull-crossbones' : 'fa-shield-alt'}"></i>
            </div>
            <div class="result-text">${isThreat ? t.mm_threat : t.mm_safe}</div>
            <div class="result-prob">${t.mm_total} ${result.total} &nbsp;|&nbsp; ${t.mm_mal} ${result.malware_count}</div>
        </div>`;

    let html = '';
    if (Object.keys(result.type_counts || {}).length) {
        html += `<h4 style="margin-bottom: 0.6rem; color: var(--text-secondary);">${t.mm_breakdown}</h4>`;
        for (const [k, v] of Object.entries(result.type_counts)) {
            html += `
                <div class="model-result-item">
                    <span class="model-result-name">${k}</span>
                    <span class="model-result-prob prob-fraud">${v}</span>
                </div>`;
        }
    }

    if (result.rows && result.rows.length) {
        html += `<h4 style="margin:1rem 0 0.6rem; color: var(--text-secondary);">Rows (max 50):</h4>`;
        for (const row of result.rows) {
            const cls = row.is_malware ? 'prob-fraud' : 'prob-normal';
            const lbl = row.is_malware ? row.label : 'Benign';
            html += `
                <div class="model-result-item">
                    <span class="model-result-name">#${row.index} ${lbl}</span>
                    <span class="model-result-prob ${cls}">${row.malware_probability}%</span>
                </div>`;
        }
    }
    detail.innerHTML = html;
}

// ==================== MODEL SIDEBAR ACTIVE STATE ====================
const modelBars = document.querySelectorAll('.model-bar');
const modelSections = {
    'url': 'demo',
    'nlp': 'spam-demo',
    'deepfake': 'deepfake-demo',
    'malmem': 'malmem-demo'
};
window.addEventListener('scroll', () => {
    const y = window.scrollY + 200;
    let activeKey = null;
    for (const [key, id] of Object.entries(modelSections)) {
        const el = document.getElementById(id);
        if (el && y >= el.offsetTop && y < el.offsetTop + el.offsetHeight) {
            activeKey = key;
        }
    }
    modelBars.forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-model') === activeKey);
    });
});

// ==================== AEGIS COMMAND CENTER GLOBE ====================
const globeEl = document.getElementById('cyber-globe');
if (globeEl && typeof Globe !== 'undefined') {
    const targetLat = 41.2995, targetLng = 69.2401;
    const incomingAttacks = [
        { startLat: 39.9042, startLng: 116.4074, endLat: targetLat, endLng: targetLng, color: '#ff0000' },
        { startLat: 55.7558, startLng: 37.6173,  endLat: targetLat, endLng: targetLng, color: '#ff5500' },
        { startLat: 38.9072, startLng: -77.0369, endLat: targetLat, endLng: targetLng, color: '#ff0000' },
        { startLat: 51.5074, startLng: -0.1278,  endLat: targetLat, endLng: targetLng, color: '#ffcc00' },
        { startLat: -23.5505, startLng: -46.6333, endLat: targetLat, endLng: targetLng, color: '#ff0000' },
        { startLat: 35.6762, startLng: 139.6503, endLat: targetLat, endLng: targetLng, color: '#ff5500' },
        { startLat: 28.6139, startLng: 77.2090,  endLat: targetLat, endLng: targetLng, color: '#ffcc00' }
    ];

    const myGlobe = Globe()(globeEl)
        .globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')
        .backgroundColor('#000')
        .arcsData(incomingAttacks)
        .arcStartLat(d => d.startLat)
        .arcStartLng(d => d.startLng)
        .arcEndLat(d => d.endLat)
        .arcEndLng(d => d.endLng)
        .arcColor(d => [d.color, d.color])
        .arcDashLength(0.4)
        .arcDashGap(1)
        .arcDashInitialGap(() => Math.random())
        .arcDashAnimateTime(1500)
        .ringsData([
            { lat: targetLat, lng: targetLng, color: '#00ff00', maxR: 5 },
            ...incomingAttacks.map(d => ({ lat: d.startLat, lng: d.startLng, color: '#ff0000', maxR: 3 }))
        ])
        .ringColor(d => t => `rgba(${d.color === '#00ff00' ? '0,255,0' : '255,0,0'},${1 - t})`)
        .ringMaxRadius(d => d.maxR)
        .ringPropagationSpeed(3)
        .ringRepeatPeriod(700);

    myGlobe.pointOfView({ lat: targetLat, lng: targetLng, altitude: 2.0 });
    if (myGlobe.controls) {
        myGlobe.controls().autoRotate = true;
        myGlobe.controls().autoRotateSpeed = 0.3;
    }

    function resizeGlobe() {
        myGlobe.width(globeEl.clientWidth).height(globeEl.clientHeight);
    }
    resizeGlobe();
    window.addEventListener('resize', resizeGlobe);
}

// ==================== SMOOTH SCROLL + ACTIVE NAV ====================
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('.slide');
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.style.color = link.getAttribute('href') === '#' + current ? '#39FF14' : '#988d9f';
    });
});

// ==================== LIVE RAM MONITOR ====================
(function () {
    const startBtn = document.getElementById('liveRamStart');
    const stopBtn  = document.getElementById('liveRamStop');
    const card     = document.getElementById('liveRamCard');
    const mainEl   = document.getElementById('liveRamMain');
    const procsEl  = document.getElementById('liveRamProcs');
    if (!startBtn || !stopBtn || !card) return;

    let timer = null;

    async function tick() {
        try {
            const r = await fetch('/live_ram');
            const d = await r.json();
            if (d.error) {
                mainEl.innerHTML = `<div class="result-main normal">
                    <div class="result-text">ERROR</div>
                    <div class="result-prob">${d.error}</div></div>`;
                procsEl.innerHTML = '';
                return;
            }
            const cls  = d.suspicious ? 'fraud' : 'normal';
            const icon = d.suspicious ? 'fa-exclamation-triangle' : 'fa-shield-alt';
            const verdict = d.suspicious ? 'TAHDID' : 'NORMAL';
            mainEl.innerHTML = `
                <div class="result-main ${cls}">
                    <div class="result-icon-big"><i class="fas ${icon}"></i></div>
                    <div class="result-text">${verdict}</div>
                    <div class="result-prob">RAM: ${d.percent}% (${d.used_gb} / ${d.total_gb} GB)</div>
                    <div style="margin-top:0.4rem; font-size:0.85rem; opacity:0.7;">
                        Bo'sh: ${d.free_gb} GB &nbsp;|&nbsp; Jarayonlar: ${d.process_count}
                    </div>
                </div>`;
            let html = `<h4 style="margin-bottom:0.6rem; color:var(--text-secondary);">
                Top 5 jarayon (RAM bo'yicha)</h4>`;
            for (const p of d.top) {
                const pcls = p.percent > 30 ? 'prob-fraud' : 'prob-normal';
                html += `
                    <div class="model-result-item">
                        <span class="model-result-name">${p.name} <span style="opacity:0.5">#${p.pid}</span></span>
                        <span class="model-result-prob ${pcls}">${p.rss_mb} MB (${p.percent}%)</span>
                    </div>`;
            }
            procsEl.innerHTML = html;
        } catch (e) {
            mainEl.innerHTML = `<div class="result-main normal">
                <div class="result-text">ERROR</div>
                <div class="result-prob">${e.message}</div></div>`;
        }
    }

    startBtn.addEventListener('click', () => {
        card.style.display = 'block';
        startBtn.style.display = 'none';
        stopBtn.style.display  = 'inline-flex';
        tick();
        timer = setInterval(tick, 2000);
    });

    stopBtn.addEventListener('click', () => {
        if (timer) { clearInterval(timer); timer = null; }
        startBtn.style.display = 'inline-flex';
        stopBtn.style.display  = 'none';
    });
})();
