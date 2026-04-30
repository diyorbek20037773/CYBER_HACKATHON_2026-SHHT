"""
CyberShield Network — Phishing URL Checker
SCO Hackathon 2026

Ikki model qo'llab-quvvatlanadi:
  --model arnab   30 feature (URL + HTML + WHOIS) — aniq, lekin sekin (~15s)
  --model ours    22 feature (faqat URL string)   — tez (<0.01s), model kerak

Ishlatish:
  python check_url.py                             # interaktiv, arnab modeli
  python check_url.py https://example.com         # arnab modeli
  python check_url.py --model ours https://x.com  # o'zimizning model
"""

import sys
import os
import re
import importlib.util
import argparse
import numpy as np
import pandas as pd
import xgboost as xgb
from urllib.parse import urlparse

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS = {
    # ArnabKumarRoy02 ning 30-feature modeli (URL + HTML + WHOIS)
    'arnab': os.path.join(BASE_DIR, 'models', 'xgb_phishing30.json'),
    # Bizning o'zimizning 22-feature modeli (faqat URL string)
    'ours' : os.path.join(BASE_DIR, 'models', 'xgb_url22.json'),
}

REPO_DIR   = os.path.join(BASE_DIR, 'repo')
FEATURE_PY = os.path.join(REPO_DIR, 'feature.py')

# 30 feature nomlari (arnab modeli)
FEAT_COLS_30 = [
    'UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
    'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
    'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
    'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
    'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick', 'UsingPopupWindow',
    'IframeRedirection', 'AgeofDomain', 'DNSRecording', 'WebsiteTraffic',
    'PageRank', 'GoogleIndex', 'LinksPointingToPage', 'StatsReport',
]

# 22 feature nomlari (bizning URL-only modelimiz)
# Bu nomlar Colabda train qilganda ishlatiladigan nomlar bilan bir xil bo'lishi kerak!
FEAT_COLS_22 = [
    'url_length', 'num_dots', 'num_hyphens', 'num_underscores',
    'num_slashes', 'num_at', 'num_digits', 'num_special',
    'has_ip', 'has_https', 'has_www', 'has_port',
    'subdomain_count', 'path_length', 'query_length', 'fragment_length',
    'tld_length', 'num_params', 'num_redirects', 'has_shortener',
    'digit_ratio', 'special_ratio',
]

# Qisqartiruvchi domenlar
SHORTENERS = {
    'bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly',
    'short.io', 'is.gd', 'buff.ly', 'rebrand.ly', 'tiny.cc',
}

# ── Model yuklash ──────────────────────────────────────────────────────────────
def load_model(model_key: str) -> xgb.XGBClassifier:
    path = MODELS[model_key]
    if not os.path.exists(path):
        print(f"\n[XATO] Model topilmadi: {path}")
        if model_key == 'arnab':
            print("  Colabdan xgb_phishing30.json ni models/ papkasiga ko'chiring.")
        else:
            print("  Colabda o'zimizning modelni train qilib xgb_url22.json ni models/ ga ko'chiring.")
        sys.exit(1)
    m = xgb.XGBClassifier()
    m.load_model(path)
    return m

# ── ArnabKumarRoy02 feature extractor (30 feature) ───────────────────────────
def load_feature_extractor():
    if not os.path.exists(FEATURE_PY):
        print(f"\n[XATO] feature.py topilmadi: {FEATURE_PY}")
        print("  setup.bat ni ishga tushiring (repo klonlanadi).")
        sys.exit(1)
    spec = importlib.util.spec_from_file_location("feature", FEATURE_PY)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.FeatureExtraction

# ── Bizning URL-only feature extraction (22 feature) ─────────────────────────
def extract_url_features(url: str) -> pd.DataFrame:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path   = parsed.path
    query  = parsed.query
    frag   = parsed.fragment

    has_ip_flag = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0

    subdomain = domain.replace('www.', '')
    parts     = subdomain.split('.')
    tld       = parts[-1] if len(parts) > 1 else ''
    sub_count = max(0, len(parts) - 2)

    special_chars = re.findall(r'[^a-zA-Z0-9._\-/:%?=&#]', url)
    digits        = re.findall(r'\d', url)

    features = {
        'url_length'     : len(url),
        'num_dots'       : url.count('.'),
        'num_hyphens'    : url.count('-'),
        'num_underscores': url.count('_'),
        'num_slashes'    : url.count('/'),
        'num_at'         : url.count('@'),
        'num_digits'     : len(digits),
        'num_special'    : len(special_chars),
        'has_ip'         : has_ip_flag,
        'has_https'      : 1 if parsed.scheme == 'https' else 0,
        'has_www'        : 1 if 'www.' in domain else 0,
        'has_port'       : 1 if parsed.port else 0,
        'subdomain_count': sub_count,
        'path_length'    : len(path),
        'query_length'   : len(query),
        'fragment_length': len(frag),
        'tld_length'     : len(tld),
        'num_params'     : len(query.split('&')) if query else 0,
        'num_redirects'  : url.count('//') - 1,
        'has_shortener'  : 1 if any(s in domain for s in SHORTENERS) else 0,
        'digit_ratio'    : len(digits) / max(len(url), 1),
        'special_ratio'  : len(special_chars) / max(len(url), 1),
    }
    return pd.DataFrame([features], columns=FEAT_COLS_22)

# ── URL tekshirish ─────────────────────────────────────────────────────────────
def check_arnab(url: str, model: xgb.XGBClassifier, FeatureExtraction) -> dict:
    try:
        obj   = FeatureExtraction(url)
        feats = np.array(obj.getFeaturesList()).reshape(1, -1)
        X     = pd.DataFrame(feats, columns=FEAT_COLS_30)
        prob  = model.predict_proba(X)[0][1]
        return {'url': url, 'label': 'PHISHING' if prob > 0.5 else 'LEGIT',
                'prob': prob, 'error': None}
    except Exception as e:
        return {'url': url, 'label': 'ERROR', 'prob': None, 'error': str(e)}

def check_ours(url: str, model: xgb.XGBClassifier) -> dict:
    try:
        X    = extract_url_features(url)
        prob = model.predict_proba(X)[0][1]
        return {'url': url, 'label': 'PHISHING' if prob > 0.5 else 'LEGIT',
                'prob': prob, 'error': None}
    except Exception as e:
        return {'url': url, 'label': 'ERROR', 'prob': None, 'error': str(e)}

# ── Natijani chiqarish ─────────────────────────────────────────────────────────
def print_result(r: dict):
    if r['error']:
        print(f"  [ERROR] {r['url']}")
        print(f"          {r['error']}\n")
        return
    pct   = r['prob'] * 100
    bar   = '#' * int(pct / 100 * 30)
    color = '\033[91m' if r['label'] == 'PHISHING' else '\033[92m'
    reset = '\033[0m'
    print(f"  URL   : {r['url']}")
    print(f"  Natija: {color}{r['label']}{reset}  ({pct:.1f}% phishing)")
    print(f"  [{bar:<30}]\n")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='Phishing URL Checker')
    parser.add_argument('urls', nargs='*', help='Tekshiriladigan URL lar')
    parser.add_argument('--model', choices=['arnab', 'ours'], default='arnab',
                        help='arnab=30 feature (HTML+WHOIS) | ours=22 feature (URL only)')
    args = parser.parse_args()

    model_key = args.model
    desc = {
        'arnab': '30 feature — URL + HTML + WHOIS (sekin, aniq)',
        'ours' : '22 feature — faqat URL string (tez, <0.01s)',
    }

    print("=" * 60)
    print("  CyberShield — Phishing URL Checker")
    print(f"  Model: [{model_key}] {desc[model_key]}")
    print("=" * 60)

    model = load_model(model_key)

    if model_key == 'arnab':
        FeatureExtraction = load_feature_extractor()

    print(f"  Model yuklandi: {MODELS[model_key]}\n")

    urls = args.urls
    if not urls:
        print("  URL kiriting (bo'sh qoldiring — chiqish):")
        while True:
            try:
                u = input("  > ").strip()
            except (KeyboardInterrupt, EOFError):
                break
            if not u:
                break
            urls.append(u)

    print()
    for url in urls:
        if model_key == 'arnab':
            r = check_arnab(url, model, FeatureExtraction)
        else:
            r = check_ours(url, model)
        print_result(r)

if __name__ == '__main__':
    main()
