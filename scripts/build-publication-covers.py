"""Regenerate publication cards from the defile-dataset reference library.

Requires Poppler (pdftoppm) and WebP (cwebp).
Run: python3 scripts/build-publication-covers.py ../defile-dataset
"""

import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(sys.argv[1])
site = Path(__file__).resolve().parents[1]
sources = list(csv.DictReader((root / 'references/sources.csv').open()))
reports = []
with tempfile.TemporaryDirectory() as tmp:
    for source in sources:
        if source['status'] not in ('downloaded', 'provided'):
            continue
        if source['category'] != 'annual-report' and source['id'] not in (
            'defile-paper-1996-I', 'defile-paper-1996-II', 'defile-paper-2019', 'defile-paper-2020'
        ):
            continue
        name = source['id'].removeprefix('defile-')
        subprocess.run(['pdftoppm', '-f', '1', '-singlefile', '-scale-to', '800', '-png', str(root / source['path']), f'{tmp}/cover'], check=True, capture_output=True)
        subprocess.run(['cwebp', '-quiet', '-q', '82', f'{tmp}/cover.png', '-o', str(site / 'public/publications' / f'{name}.webp')], check=True)
        if source['category'] == 'annual-report':
            reports.append({'year': int(source['year']), 'url': source['url'], 'cover': f'{name}.webp', 'pages': int(source['pages'])})
(site / 'src/data').mkdir(exist_ok=True)
(site / 'src/data/reports.json').write_text(json.dumps(sorted(reports, key=lambda r: -r['year']), indent=2) + '\n')
