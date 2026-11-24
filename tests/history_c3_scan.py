#!/usr/bin/env python3
"""Scan every reachable Git commit for public-path and email leakage.

This is intentionally separate from the working-tree C3 check. It never checks
out commits and writes results to ignored out/acceptance by default.
"""
from pathlib import Path
import sys
import json, os, re, subprocess, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir

ROOT = Path(__file__).resolve().parents[1]
OUT = output_dir('history-c3')

def run(*args):
    return subprocess.run(list(args), cwd=ROOT, text=True, capture_output=True, check=False)

def private_words():
    return [x.strip() for x in re.split(r'[,，、\r\n]', os.environ.get('MIKO_PRIVATE_WORDS', '')) if x.strip()]

if not (ROOT / '.git').exists():
    result = {'scanner': 'history_c3_scan', 'status': 'BLOCKED', 'reason': 'Git metadata is unavailable; complete history cannot be enumerated.', 'commits_scanned': 0, 'hits': []}
    (OUT / 'history-c3.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('STATUS=BLOCKED')
    print('REASON=Git metadata unavailable; history scan NOT_RUN')
    sys.exit(2)

commits = run('git', 'rev-list', '--all').stdout.splitlines()
patterns = [re.compile(r'[\w.+-]+@[\w-]+\.(?:com|tw|net|org)'), re.compile('/' + 'home/'), re.compile('/' + 'Users/'), re.compile('<HOME>/' + '[A-Z]')]
patterns += [re.compile(re.escape(w)) for w in private_words()]
hits = []
for commit in commits:
    listing = run('git', 'ls-tree', '-r', '-z', '--name-only', commit)
    for raw in listing.stdout.split('\0'):
        if not raw:
            continue
        data = subprocess.run(['git', 'show', f'{commit}:{raw}'], cwd=ROOT, capture_output=True, check=False).stdout
        text = data.decode('utf-8', 'ignore')
        for pat in patterns:
            if pat.search(text):
                hits.append({'commit': commit, 'path': raw, 'pattern': pat.pattern})
                break
result = {'scanner': 'history_c3_scan', 'status': 'PASS' if not hits else 'FAIL', 'commits_scanned': len(commits), 'hits': hits, 'private_word_count': len(private_words())}
(OUT / 'history-c3.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'COMMITS_SCANNED={len(commits)}')
print(f'HITS={len(hits)}')
print('STATUS=' + result['status'])
sys.exit(0 if not hits else 1)
