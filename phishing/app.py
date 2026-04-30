import streamlit as st
import importlib.util
import numpy as np
import pandas as pd
import xgboost as xgb
import os
import time

# ── Paths ──────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'xgb_phishing30.json')
FEATURE_PY = os.path.join(BASE_DIR, 'repo', 'feature.py')

FEAT_COLS = [
    'UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
    'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
    'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
    'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
    'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick', 'UsingPopupWindow',
    'IframeRedirection', 'AgeofDomain', 'DNSRecording', 'WebsiteTraffic',
    'PageRank', 'GoogleIndex', 'LinksPointingToPage', 'StatsReport',
]

# ── Cache: model va feature extractor bir marta yuklanadi ──────────────
@st.cache_resource
def load_resources():
    model = xgb.XGBClassifier()
    model.load_model(MODEL_PATH)

    spec = importlib.util.spec_from_file_location("feature", FEATURE_PY)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    return model, mod.FeatureExtraction

# ── Page config ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CyberShield — Phishing Detector",
    page_icon="🛡️",
    layout="centered",
)

st.markdown("""
<style>
.result-safe {
    background: linear-gradient(135deg, #1a472a, #2d6a4f);
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    color: white;
}
.result-phish {
    background: linear-gradient(135deg, #7b0000, #c62828);
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    color: white;
}
.result-title {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}
.result-sub {
    font-size: 1.1rem;
    opacity: 0.85;
}
.step-box {
    background: #1e1e2e;
    border-radius: 10px;
    padding: 14px 18px;
    margin: 6px 0;
    color: #cdd6f4;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────
st.markdown("## 🛡️ CyberShield")
st.markdown("##### Phishing URL Detector — SCO Hackathon 2026")
st.divider()

# ── Input ──────────────────────────────────────────────────────────────
url = st.text_input(
    "URL kiriting",
    placeholder="https://example.com",
    label_visibility="collapsed",
)

check_btn = st.button("🔍  Tekshirish", use_container_width=True, type="primary")

# ── Analysis ───────────────────────────────────────────────────────────
if check_btn:
    url = url.strip()
    if not url:
        st.warning("URL kiriting.")
        st.stop()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        model, FeatureExtraction = load_resources()
    except Exception as e:
        st.error(f"Model yuklanmadi: {e}")
        st.stop()

    st.divider()
    st.markdown("**Tahlil bosqichlari:**")

    steps = [
        ("🌐", "Domen tekshirilmoqda..."),
        ("📄", "Sahifa tarkibi o'rganilmoqda..."),
        ("🔒", "Xavfsizlik ko'rsatkichlari aniqlanmoqda..."),
        ("📊", "Ma'lumotlar tahlil qilinmoqda..."),
        ("🤖", "Natija hisoblanmoqda..."),
    ]

    step_placeholders = []
    for icon, text in steps:
        ph = st.empty()
        step_placeholders.append((ph, icon, text))

    # Bosqichlarni ketma-ket ko'rsatamiz, feature extraction bilan parallel
    result_placeholder = st.empty()
    error_placeholder  = st.empty()

    # Feature extraction (blocking) — bosqichlarni animatsiya qilib ko'rsatamiz
    try:
        # 1-bosqich
        step_placeholders[0][0].markdown(
            f'<div class="step-box">⏳ {steps[0][1]}</div>', unsafe_allow_html=True)

        obj = FeatureExtraction(url)

        # Qolgan bosqichlarni tez ko'rsatamiz
        for i, (ph, icon, text) in enumerate(step_placeholders):
            ph.markdown(
                f'<div class="step-box">{icon} {text.replace("moqda...", "ldi ✓")}</div>',
                unsafe_allow_html=True)
            time.sleep(0.3)

        feats = np.array(obj.getFeaturesList()).reshape(1, -1)
        X     = pd.DataFrame(feats, columns=FEAT_COLS)
        prob  = model.predict_proba(X)[0][1]
        pct   = prob * 100
        label = "PHISHING" if prob > 0.5 else "XAVFSIZ"

        st.divider()

        if label == "PHISHING":
            confidence_text = (
                "Yuqori xavf" if pct > 80 else
                "O'rta xavf"  if pct > 60 else
                "Past xavf"
            )
            result_placeholder.markdown(f"""
<div class="result-phish">
  <div class="result-title">⚠️ PHISHING</div>
  <div class="result-sub">{confidence_text} — {pct:.1f}% ehtimollik</div>
</div>
""", unsafe_allow_html=True)
        else:
            confidence_text = (
                "Ishonchli" if pct < 20 else
                "Asosan xavfsiz" if pct < 40 else
                "Shubhali bo'lishi mumkin"
            )
            result_placeholder.markdown(f"""
<div class="result-safe">
  <div class="result-title">✅ XAVFSIZ</div>
  <div class="result-sub">{confidence_text} — {100-pct:.1f}% ishonchlilik</div>
</div>
""", unsafe_allow_html=True)

        # Progress bar
        st.markdown("")
        bar_color = "#c62828" if label == "PHISHING" else "#2d6a4f"
        st.markdown(f"""
<div style="margin-top:16px">
  <div style="display:flex; justify-content:space-between; color:#888; font-size:0.85rem; margin-bottom:4px">
    <span>Xavfsiz</span><span>Phishing</span>
  </div>
  <div style="background:#2a2a3e; border-radius:8px; height:12px; overflow:hidden">
    <div style="width:{pct:.1f}%; height:100%; background:{bar_color}; border-radius:8px; transition:width 0.5s"></div>
  </div>
  <div style="text-align:center; color:#888; font-size:0.8rem; margin-top:4px">{pct:.1f}%</div>
</div>
""", unsafe_allow_html=True)

        st.markdown(f"<div style='color:#555; font-size:0.8rem; margin-top:12px'>Tekshirilgan URL: <code>{url}</code></div>",
                    unsafe_allow_html=True)

    except Exception as e:
        for ph, icon, text in step_placeholders:
            ph.empty()
        error_placeholder.error(f"Tahlil amalga oshmadi: {e}")
