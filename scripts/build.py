"""Build the static website without third-party dependencies."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
for name in ('index.html', 'almansur.html', 'nurperzent.html', 'styles.css'):
    shutil.copy2(ROOT / name, OUT / name)
print('Build OK: 3 HTML pages and shared stylesheet -> dist/')
