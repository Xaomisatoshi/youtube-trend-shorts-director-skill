#!/usr/bin/env python3
"""Prüft eine UTF-8-Textdatei mit einer Voice-over-Zeile pro Szene."""
import argparse
from pathlib import Path
import re
p = argparse.ArgumentParser()
p.add_argument('file')
p.add_argument('--scenes', type=int, default=6)
p.add_argument('--max-words', type=int, default=14)
args = p.parse_args()
lines = [l.strip() for l in Path(args.file).read_text(encoding='utf-8').splitlines() if l.strip()]
counts = [len([w for w in re.split(r'\s+', re.sub(r'(^|\s)[^\wÄÖÜäöüß]+(?=\s|$)', ' ', l)) if any(c.isalnum() for c in w)]) for l in lines]
for n,c in enumerate(counts,1):
    print(f'Szene {n}: {c} Wörter — {"PASS" if c <= args.max_words else "FAIL"}')
print(f'Szenen: {len(lines)}/{args.scenes}; Gesamt: {sum(counts)}')
if len(lines) != args.scenes or any(c > args.max_words for c in counts):
    raise SystemExit(1)
