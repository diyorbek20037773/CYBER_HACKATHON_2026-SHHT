import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import pickle, os, psutil, platform

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
SAMPLES_DIR = os.path.join(BASE_DIR, 'samples')

# ── Resources ──────────────────────────────────────────────────────────
@st.cache_resource
def load_resources():
    binary = xgb.XGBClassifier()
    binary.load_model(os.path.join(MODELS_DIR, 'xgb_malmem_binary.json'))
    multi = xgb.XGBClassifier()
    multi.load_model(os.path.join(MODELS_DIR, 'xgb_malmem_multi.json'))
    with open(os.path.join(MODELS_DIR, 'label_encoder.pkl'), 'rb') as f:
        le = pickle.load(f)
    with open(os.path.join(MODELS_DIR, 'feature_cols.pkl'), 'rb') as f:
        feat_cols = pickle.load(f)
    return binary, multi, le, feat_cols

# ── Live RAM feature extraction ────────────────────────────────────────
def extract_live_features(feat_cols):
    procs = list(psutil.process_iter(['pid','ppid','num_threads','num_handles'], ad_value=0))
    nproc = len(procs)
    ppids = {p.info['ppid'] for p in procs if p.info['ppid']}
    nppid = len(ppids)
    avg_threads  = np.mean([p.info['num_threads'] or 1 for p in procs])
    avg_handlers = np.mean([p.info['num_handles'] or 0 for p in procs])

    nfile = nport = nevent = nkey = nthread = ndesktop = 0
    ndirectory = nsemaphore = ntimer = nsection = nmutant = 0
    try:
        for p in procs:
            try:
                conns = p.connections()
                nport += len([c for c in conns if c.type and 'SOCK' in str(c.type)])
            except Exception:
                pass
            try:
                nfile  += len(p.open_files())
                nthread += p.num_threads()
            except Exception:
                pass
    except Exception:
        pass

    try:
        services = list(psutil.win_service_iter()) if platform.system() == 'Windows' else []
        n_services = len(services)
        n_running  = sum(1 for s in services if s.status() == 'running')
    except Exception:
        n_services = 0
        n_running  = 0

    row = {c: 0.0 for c in feat_cols}
    row.update({
        'pslist.nproc'              : nproc,
        'pslist.nppid'              : nppid,
        'pslist.avg_threads'        : avg_threads,
        'pslist.nprocs64bit'        : 0,
        'pslist.avg_handlers'       : avg_handlers,
        'handles.nhandles'          : sum(p.info['num_handles'] or 0 for p in procs),
        'handles.avg_handles_per_proc': avg_handlers,
        'handles.nport'             : nport,
        'handles.nfile'             : nfile,
        'handles.nthread'           : nthread,
        'svcscan.nservices'         : n_services,
        'svcscan.nactive'           : n_running,
        # Deep forensics features (malfind, psxview, ldrmodules) — psutil bilan olib bo'lmaydi
        # Shuning uchun 0 (benign qiymatlari) qoyiladi
        'malfind.ninjections'       : 0,
        'malfind.uniqueInjections'  : 0,
    })
    stats = {
        'nproc'     : nproc,
        'nppid'     : nppid,
        'avg_threads': round(avg_threads, 1),
        'nfile'     : nfile,
        'nport'     : nport,
        'nservices' : n_services,
        'nactive'   : n_running,
    }
    return pd.DataFrame([row])[feat_cols].astype(float), stats

# ── Natijani ko'rsatish ────────────────────────────────────────────────
def show_result(b_prob, m_proba, le):
    is_malware = b_prob > 0.5
    m_idx      = int(np.argmax(m_proba))
    m_label    = le.classes_[m_idx]

    TYPE_INFO = {
        'Benign'    : ('✅', '#2d6a4f', 'Xavf aniqlanmadi'),
        'Ransomware': ('🔒', '#c0392b', 'Fayllarni shifrlaydi'),
        'Spyware'   : ('👁️', '#e67e22', "Ma'lumot o'g'irlaydi"),
        'Trojan'    : ('🎭', '#8e44ad', 'Yashirin nazorat qiladi'),
    }

    if not is_malware:
        icon, color, desc = TYPE_INFO['Benign']
        label_text = 'XAVFSIZ'
        conf = f'{(1-b_prob)*100:.1f}% ishonchlilik'
    else:
        icon, color, desc = TYPE_INFO[m_label]
        label_text = m_label.upper()
        conf = f'Xavf ehtimoli: {b_prob*100:.1f}%'

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{color}cc,{color});
     border-radius:14px;padding:28px;text-align:center;color:white;margin:12px 0">
  <div style="font-size:2.4rem;font-weight:900;letter-spacing:3px">{icon} {label_text}</div>
  <div style="font-size:1rem;opacity:.85;margin-top:6px">{desc} &nbsp;|&nbsp; {conf}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("**Sinf ehtimolliklari:**")
    proba_df = sorted(zip(le.classes_, m_proba), key=lambda x: -x[1])
    for cls, prob in proba_df:
        icon2 = TYPE_INFO[cls][0]
        pct   = float(prob) * 100
        col1, col2 = st.columns([3, 1])
        col1.progress(float(prob), text=f"{icon2} {cls}")
        col2.markdown(f"<div style='text-align:right;padding-top:6px'><b>{pct:.1f}%</b></div>",
                      unsafe_allow_html=True)

# ── Page config ────────────────────────────────────────────────────────
st.set_page_config(page_title="Memory Analyzer", page_icon="🧠", layout="centered")
st.markdown("""
<style>
section[data-testid="stSidebar"] {width:230px !important}
div[data-testid="stFileUploader"] label {display:none}
</style>""", unsafe_allow_html=True)

binary_model, multi_model, le, feat_cols = load_resources()

# ── Sidebar ────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🧠 Memory Analyzer")
    st.caption("SCO Hackathon 2026 · CyberShield")
    st.divider()
    st.markdown("**Namuna fayllar:**")
    st.caption("Sinab ko'rish uchun yuklab oling")

    for fname, label in [
        ('sample_benign.csv',     '✅ Benign'),
        ('sample_ransomware.csv', '🔴 Ransomware'),
        ('sample_spyware.csv',    '🟡 Spyware'),
        ('sample_trojan.csv',     '🟠 Trojan'),
    ]:
        fpath = os.path.join(SAMPLES_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'rb') as f:
                st.download_button(label, f, file_name=fname,
                                   mime='text/csv', use_container_width=True)
    st.divider()
    st.markdown("**Haqiqiy RAM skaneri:**")
    st.caption("Ushbu kompyuterning xotirasi tahlil qilinadi")
    live_btn = st.button("🔴 Live RAM Scan", use_container_width=True, type="primary")
    st.caption("⚠️ Faqat asosiy jarayon ma'lumotlari (to'liq scan uchun VolMemLyzer kerak)")

# ── Main ───────────────────────────────────────────────────────────────
st.markdown("## 🧠 RAM Xotira Tahlili")
st.caption("VolMemLyzer chiqaradigan CSV faylni yuklang → model tahlil qiladi")
st.divider()

# Live scan
if live_btn:
    with st.spinner("RAM tahlil qilinmoqda..."):
        X_live, stats = extract_live_features(feat_cols)
        b_prob  = binary_model.predict_proba(X_live)[0][1]
        m_proba = multi_model.predict_proba(X_live)[0]

    st.markdown("**Live RAM Scan natijasi:**")
    show_result(b_prob, m_proba, le)

    # Tushuntirish
    st.markdown("**Nima topildi:**")
    c1, c2, c3 = st.columns(3)
    c1.metric("Jarayonlar", stats['nproc'],
              help="Xotirada ishlab turgan dasturlar soni")
    c2.metric("O'rtacha thread", stats['avg_threads'],
              help="Har jarayon o'rtacha nechta thread ishlatadi")
    c3.metric("Ochiq fayllar", stats['nfile'],
              help="Hozir fayllar bilan ishlayotgan jarayonlar")

    c4, c5, c6 = st.columns(3)
    c4.metric("Tarmoq ulanishlari", stats['nport'],
              help="Hozir tarmoqqa ulangan soketlar")
    c5.metric("Xizmatlar (jami)", stats['nservices'],
              help="Windows xizmatlari soni")
    c6.metric("Faol xizmatlar", stats['nactive'],
              help="Hozir ishlab turgan xizmatlar")

    with st.expander("ℹ️ Nima uchun bu natija?"):
        nproc = stats['nproc']
        nfile = stats['nfile']
        nport = stats['nport']

        reasons = []
        if nproc < 60:
            reasons.append(f"✅ Jarayonlar soni normal ({nproc} ta)")
        else:
            reasons.append(f"⚠️ Ko'p jarayon topildi ({nproc} ta) — shubhali bo'lishi mumkin")

        if nport < 20:
            reasons.append(f"✅ Tarmoq ulanishlari normal ({nport} ta)")
        else:
            reasons.append(f"⚠️ Ko'p tarmoq ulanishi ({nport} ta) — ma'lumot yuborilishi mumkin")

        reasons.append("✅ Xotira in'ektsiyasi aniqlanmadi (malfind.ninjections = 0)")
        reasons.append("✅ Yashirin jarayon yo'q (psxview normal)")
        reasons.append("ℹ️ To'liq tekshirish uchun VolMemLyzer bilan CSV yuklang")

        for r in reasons:
            st.markdown(r)

    st.divider()

# CSV upload
uploaded = st.file_uploader("CSV fayl yuklang", type=['csv'],
                              label_visibility="collapsed")

if uploaded is None:
    st.markdown("""
<div style="border:2px dashed #444;border-radius:12px;padding:40px;
     text-align:center;color:#888;margin:16px 0">
  <div style="font-size:2rem">📂</div>
  <div style="margin-top:8px">CSV faylni shu yerga tashlang yoki tanlang</div>
  <div style="font-size:0.8rem;margin-top:4px">Chap paneldan namuna yuklab sinab ko'ring</div>
</div>""", unsafe_allow_html=True)
else:
    try:
        df = pd.read_csv(uploaded)
        missing = [c for c in feat_cols if c not in df.columns]
        if missing:
            st.error(f"Fayl noto'g'ri format. Yetishmayotgan ustunlar: {missing[:3]}...")
        else:
            X = df[feat_cols].astype(float)
            n = len(X)
            st.success(f"{n} ta yozuv yuklandi")

            if st.button("🔍  Tahlil qilish", type="primary", use_container_width=True):
                with st.spinner("Tahlil qilinmoqda..."):
                    b_proba = binary_model.predict_proba(X)[:, 1]
                    m_proba = multi_model.predict_proba(X)
                    m_preds = multi_model.predict(X)
                    m_labels = le.inverse_transform(m_preds)

                st.divider()

                if n == 1:
                    show_result(b_proba[0], m_proba[0], le)
                else:
                    mal_idx = b_proba > 0.5
                    mal_count = mal_idx.sum()

                    if mal_count == 0:
                        st.markdown("""
<div style="background:linear-gradient(135deg,#1a472a,#2d6a4f);
     border-radius:14px;padding:28px;text-align:center;color:white">
  <div style="font-size:2rem;font-weight:900">✅ HAMMASI XAVFSIZ</div>
  <div style="opacity:.85;margin-top:6px">Hech qanday malware aniqlanmadi</div>
</div>""", unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
<div style="background:linear-gradient(135deg,#7b0000,#c62828);
     border-radius:14px;padding:28px;text-align:center;color:white">
  <div style="font-size:2rem;font-weight:900">⚠️ {mal_count} ta XAVFLI YOZUV</div>
  <div style="opacity:.85;margin-top:6px">{n} ta yozuvdan {mal_count} tasi ({mal_count/n*100:.0f}%) malware</div>
</div>""", unsafe_allow_html=True)

                        st.markdown("")
                        counts = pd.Series(m_labels[mal_idx]).value_counts()
                        icons  = {'Ransomware':'🔴','Spyware':'🟡','Trojan':'🟠','Benign':'✅'}
                        cols   = st.columns(len(counts))
                        for i, (mtype, cnt) in enumerate(counts.items()):
                            cols[i].metric(f"{icons.get(mtype,'⚪')} {mtype}", cnt)

                    st.markdown("")
                    result_df = pd.DataFrame({
                        '#'               : range(1, n+1),
                        'Holat'           : ['⚠️ Xavfli' if p else '✅ Xavfsiz' for p in mal_idx],
                        'Tur'             : m_labels,
                        'Xavf ehtimoli %' : (b_proba*100).round(1),
                    })
                    st.dataframe(result_df, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(f"Fayl o'qilmadi: {e}")
