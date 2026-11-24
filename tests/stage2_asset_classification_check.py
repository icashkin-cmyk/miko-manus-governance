#!/usr/bin/env python3
"""Stage 2 asset classification acceptance for the current 25-skill inventory.

The test regenerates Stage 1 output before reading it, so it never relies on a
stale committed evidence snapshot. It writes disposable results under
out/acceptance unless MIKO_ACCEPTANCE_OUT is explicitly set.
"""
from pathlib import Path
import csv
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CURRENT_CORE = 'manus-core'
HISTORICAL_CORE = 'miko-core'
ALLOWED_CATEGORIES = {'core-governance', 'governance-skill', 'workflow-skill', 'domain-skill'}
GOVERNANCE = {
    'ai-engineering-anti-fraud-test-credibility', 'batch-task-completion-and-single-report',
    'independent-audit', 'knowledge-card-format', 'make-skill', 'miko-flow-optimizer',
    'miko-governance-layer-acceptance', 'miko-project-note-specialist', 'miko-prompt-optimizer',
    'three-party-review', 'version-evolution-preservation',
}
WORKFLOW = {'dghp-work-handoff', 'safe-implementation', 'tw-backtest-workflow'}
DOMAIN = {
    'dghp-beauty', 'dghp-food', 'dghp-metaphysical-integrated-analysis', 'dghp-travel',
    'gmail-cleanup', 'label-foreign-text', 'photo-inspection-log', 'tw-alert-check',
    'visual-content-intelligence', 'ingredient-source-analysis',
}
FIELDS = [
    'stable_id', 'name', 'semantic_category', 'primary_asset_type', 'canonical_path',
    'source_path', 'source_present', 'source_exception', 'test_path', 'evidence_path',
    'owner', 'runtime_status', 'adoption_status',
]


def output_root():
    return Path(__import__('os').environ.get('MIKO_ACCEPTANCE_OUT', str(ROOT / 'out' / 'acceptance')))


def run_stage1():
    cmd = [sys.executable, '-I', '-B', str(ROOT / 'tests' / 'stage1_inventory_check.py')]
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def classify(name):
    if name == CURRENT_CORE:
        return 'core-governance', 'GOVERNANCE_OWNER；Manus 僅提出候選與證據'
    if name in GOVERNANCE:
        return 'governance-skill', 'GOVERNANCE_OWNER with IMPLEMENTER/TESTER/INDEPENDENT_AUDITOR evidence separation'
    if name in WORKFLOW:
        return 'workflow-skill', 'IMPLEMENTER under manus-core boundaries'
    return 'domain-skill', 'Domain owner/IMPLEMENTER under manus-core boundaries'


def main():
    errors = []
    g1 = run_stage1()
    if g1.returncode != 0:
        errors.append('G1 Stage 1 failed: ' + g1.stdout.strip().replace('\n', ' | '))
    inv_path = output_root() / 'stage-01' / 'skill-inventory-current.json'
    if not inv_path.exists():
        errors.append('missing current Stage 1 inventory: ' + str(inv_path))
        inv = {'records': []}
    else:
        inv = json.loads(inv_path.read_text(encoding='utf-8'))

    inventory = inv.get('records', [])
    inv_ids = [r.get('directory_name', '') for r in inventory]
    if len(inv_ids) != len(set(inv_ids)):
        errors.append('inventory duplicate directory_name')
    if HISTORICAL_CORE in inv_ids:
        errors.append('historical core must not be current inventory core')
    if CURRENT_CORE not in inv_ids:
        errors.append('missing current manus-core in Stage 1 inventory')

    rows = []
    for record in inventory:
        name = record['directory_name']
        category, owner = classify(name)
        canonical = f'skills/{name}/SKILL.md'
        source_path = f'source-archive/{name}/'
        is_core_exception = name == CURRENT_CORE and canonical == 'skills/manus-core/SKILL.md'
        source_present = bool(record.get('source_archive_present', False))
        if not (ROOT / canonical).exists():
            errors.append('missing canonical ' + name)
        if not source_present and not is_core_exception:
            errors.append('missing source ' + name)
        if name not in GOVERNANCE | WORKFLOW | DOMAIN | {CURRENT_CORE}:
            errors.append('unclassified asset ' + name)
        rows.append({
            'stable_id': name,
            'name': record.get('name', name),
            'semantic_category': category,
            'primary_asset_type': 'Skill',
            'canonical_path': canonical,
            'source_path': source_path,
            'source_present': str(source_present),
            'source_exception': 'CURRENT_CORE_NO_ARCHIVE' if is_core_exception and not source_present else '',
            'test_path': f'tests/manus-candidate/{name}/ or tests/stage-01/',
            'evidence_path': f'evidence/{name}/ or evidence/stage-01/',
            'owner': owner,
            'runtime_status': 'UNKNOWN',
            'adoption_status': 'CANDIDATE',
        })

    if len(rows) != len(inventory):
        errors.append(f'row_count={len(rows)} inventory_count={len(inventory)}')
    ids = [r['stable_id'] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append('duplicate stable_id')
    if CURRENT_CORE not in ids:
        errors.append('missing canonical manus-core')
    if HISTORICAL_CORE in ids:
        errors.append('historical core must not be canonical current core')
    for row in rows:
        if row['semantic_category'] not in ALLOWED_CATEGORIES:
            errors.append('invalid category ' + row['stable_id'])
        if row['runtime_status'] != 'UNKNOWN':
            errors.append('runtime overclaim ' + row['stable_id'])
        if row['adoption_status'] != 'CANDIDATE':
            errors.append('adoption overclaim ' + row['stable_id'])
        if not row['owner']:
            errors.append('missing ownership ' + row['stable_id'])

    out_dir = output_root() / 'stage-02'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_tsv = out_dir / 'asset-classification.tsv'
    with out_tsv.open('w', encoding='utf-8', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'commit': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
        'input_gate': 'G1 PASS' if g1.returncode == 0 else 'G1 FAIL',
        'expected_records': len(inventory),
        'actual_records': len(rows),
        'current_core': CURRENT_CORE,
        'historical_core_status': 'HISTORICAL_CORE_READ',
        'errors': errors,
        'result': 'PASS' if not errors else 'FAIL',
    }
    (out_dir / 'stage2-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('INPUT_GATE=' + ('G1_PASS' if g1.returncode == 0 else 'G1_FAIL'))
    print('EXPECTED_RECORDS=' + str(len(inventory)))
    print('ACTUAL_RECORDS=' + str(len(rows)))
    print('UNIQUE_STABLE_IDS=' + str(len(set(ids))))
    print('CURRENT_CORE=' + CURRENT_CORE)
    print('RUNTIME_STATUS=UNKNOWN_FOR_ALL')
    print('ADOPTION_STATUS=CANDIDATE_FOR_ALL')
    print('ERROR_COUNT=' + str(len(errors)))
    for error in errors:
        print('ERROR: ' + error)
    print('RESULT=' + ('PASS' if not errors else 'FAIL'))
    return 0 if not errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
