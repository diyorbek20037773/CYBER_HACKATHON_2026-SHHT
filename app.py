import os
# Force Keras 3 — transformers (used by spam module) defaults TF_USE_LEGACY_KERAS=1,
# which downgrades tf.keras and `keras` to tf_keras 2.x and breaks loading the
# deepfake model (saved with Keras 3, uses `batch_shape` kwarg).
os.environ['TF_USE_LEGACY_KERAS'] = '0'

import logging
import traceback
from flask import Flask, render_template, request, jsonify, send_from_directory

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s: %(message)s',
)
log = logging.getLogger('cyber_shield')

# ── Lazy module loading ───────────────────────────────────────────────────────
# Some heavy stacks (tensorflow, torch+sentence-transformers) may fail to
# import on memory-constrained hosts. Wrap each in try/except so a single
# missing dependency does not break the whole platform.

_modules = {}

def _safe_import(key, fn):
    try:
        _modules[key] = fn()
        log.info('Loaded module: %s', key)
    except Exception as e:
        log.error('Failed to load %s: %s', key, e)
        log.debug(traceback.format_exc())
        _modules[key] = e

def _phish():
    from predict import predict_url
    return predict_url

def _spam():
    from spam_predict import predict_text
    return predict_text

def _deepfake():
    from deepfake_predict import predict_image_bytes
    return predict_image_bytes

def _malmem():
    from malmem_predict import predict_csv_bytes
    return predict_csv_bytes

_safe_import('phish',    _phish)
# Load deepfake BEFORE spam — spam imports transformers which may mutate
# the `keras` package state and break deepfake's Keras 3 model load.
_safe_import('deepfake', _deepfake)
_safe_import('spam',     _spam)
_safe_import('malmem',   _malmem)


# ── Pre-warm models on boot ──────────────────────────────────────────────────
# Force-load weights at startup so the first user request does not pay the
# multi-second (or multi-minute, for TextShield's 480MB HF download) cost.
def _warm():
    try:
        from spam_predict import load_model as _load_spam
        _load_spam()
        log.info('Warmed: spam (sentence-transformer + classifier)')
    except Exception as e:
        log.error('Warm spam failed: %s', e)
    try:
        from deepfake_predict import load_model as _load_df
        _load_df()
        log.info('Warmed: deepfake (Keras MobileNetV2)')
    except Exception as e:
        log.error('Warm deepfake failed: %s', e)
    try:
        from malmem_predict import load_resources as _load_mm
        _load_mm()
        log.info('Warmed: malmem (XGBoost x2 + label encoder)')
    except Exception as e:
        log.error('Warm malmem failed: %s', e)
    try:
        from predict import load_model as _load_phish
        _load_phish()
        log.info('Warmed: phish (XGBoost URL)')
    except Exception as e:
        log.error('Warm phish failed: %s', e)


if os.environ.get('CYBER_SHIELD_SKIP_WARM') != '1':
    _warm()


def call_model(key, *args, **kwargs):
    fn = _modules.get(key)
    if isinstance(fn, Exception) or fn is None:
        return {'error': f"Model '{key}' yuklanmadi: {fn}"}
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        log.exception('Model %s failed at runtime', key)
        return {'error': f'Tahlil amalga oshmadi: {e}'}


app = Flask(__name__)


def get_team():
    return [
        {
            "name":     os.environ.get("MEMBER1_NAME", ""),
            "role":     os.environ.get("MEMBER1_ROLE", ""),
            "linkedin": os.environ.get("MEMBER1_LINKEDIN", "#"),
            "github":   os.environ.get("MEMBER1_GITHUB", "#"),
            "telegram": os.environ.get("MEMBER1_TELEGRAM", "#"),
            "photo":    "member1.jpg",
        },
        {
            "name":     os.environ.get("MEMBER2_NAME", ""),
            "role":     os.environ.get("MEMBER2_ROLE", ""),
            "linkedin": os.environ.get("MEMBER2_LINKEDIN", "#"),
            "github":   os.environ.get("MEMBER2_GITHUB", "#"),
            "telegram": os.environ.get("MEMBER2_TELEGRAM", "#"),
            "photo":    "member2.jpg",
        },
        {
            "name":     os.environ.get("MEMBER3_NAME", ""),
            "role":     os.environ.get("MEMBER3_ROLE", ""),
            "linkedin": os.environ.get("MEMBER3_LINKEDIN", "#"),
            "github":   os.environ.get("MEMBER3_GITHUB", "#"),
            "telegram": os.environ.get("MEMBER3_TELEGRAM", "#"),
            "photo":    "member3.jpg",
        },
        {
            "name":     os.environ.get("MEMBER4_NAME", "Karimov Azizjon"),
            "role":     os.environ.get("MEMBER4_ROLE", "ML Engineer"),
            "linkedin": os.environ.get("MEMBER4_LINKEDIN", "#"),
            "github":   os.environ.get("MEMBER4_GITHUB", "#"),
            "telegram": os.environ.get("MEMBER4_TELEGRAM", "#"),
            "photo":    "member4.jpg",
        },
    ]


@app.route('/')
def index():
    return render_template('index.html', team=get_team())


@app.route('/health')
def health():
    status = {}
    for k, v in _modules.items():
        if isinstance(v, Exception):
            status[k] = {'loaded': False, 'error': str(v)}
        else:
            status[k] = {'loaded': True}
    return jsonify(status)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True) or {}
    url = data.get('url', '')
    return jsonify(call_model('phish', url))


@app.route('/predict_spam', methods=['POST'])
def predict_spam():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '')
    return jsonify(call_model('spam', text))


@app.route('/predict_deepfake', methods=['POST'])
def predict_deepfake_route():
    file = request.files.get('image')
    if file is None:
        return jsonify({'error': 'Rasm yuklanmagan'})
    return jsonify(call_model('deepfake', file.read()))


@app.route('/predict_malmem', methods=['POST'])
def predict_malmem_route():
    file = request.files.get('csv')
    if file is None:
        return jsonify({'error': 'CSV yuklanmagan'})
    return jsonify(call_model('malmem', file.read()))


@app.route('/live_ram')
def live_ram():
    """Live host RAM stats + top 5 processes by RSS. For demo/visualization."""
    try:
        import psutil
        vm = psutil.virtual_memory()
        procs = []
        for p in psutil.process_iter(['pid', 'name', 'memory_info', 'memory_percent']):
            try:
                info = p.info
                procs.append({
                    'pid':  info['pid'],
                    'name': info['name'] or '?',
                    'rss_mb':  round(info['memory_info'].rss / (1024 * 1024), 1),
                    'percent': round(info['memory_percent'] or 0.0, 2),
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        procs.sort(key=lambda x: x['rss_mb'], reverse=True)
        top = procs[:5]
        suspicious = vm.percent >= 90 or any(p['percent'] > 30 for p in top)
        return jsonify({
            'total_gb':   round(vm.total / (1024 ** 3), 2),
            'used_gb':    round(vm.used / (1024 ** 3), 2),
            'free_gb':    round(vm.available / (1024 ** 3), 2),
            'percent':    vm.percent,
            'top':        top,
            'suspicious': suspicious,
            'process_count': len(procs),
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/sample/<path:filename>')
def sample_csv(filename):
    samples_dir = os.path.join(os.path.dirname(__file__), 'memory_checker', 'samples')
    return send_from_directory(samples_dir, filename, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=False, port=port)
