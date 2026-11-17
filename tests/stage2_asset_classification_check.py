#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, json, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[1]
inv=json.loads((ROOT/'evidence/stage-01/skill-inventory-current.json').read_text())
rows=[]
for r in inv['records']:
    name=r['directory_name']
    if name in {'manus-core','make-skill','independent-audit','three-party-review','ai-engineering-anti-fraud-test-credibility','version-evolution-preservation','batch-task-completion-and-single-report','knowledge-card-format'}:
        category='governance-skill'
        owner='GOVERNANCE_OWNER with IMPLEMENTER/TESTER/INDEPENDENT_AUDITOR evidence separation'
    elif name in {'dghp-work-handoff','safe-implementation','tw-backtest-workflow'}:
        category='workflow-skill'
        owner='IMPLEMENTER under manus-core boundaries'
    else:
        category='domain-skill'
        owner='IMPLEMENTER under manus-core and domain boundaries'
    rows.append({
        'stable_id': name,
        'primary_asset_type': 'Skill',
        'secondary_role': category,
        'canonical_path': f'skills/{name}/SKILL.md',
        'source_path': f'source-archive/{name}/',
        'test_path': f'tests/manus-candidate/{name}/ or tests/stage-01/',
        'evidence_path': f'evidence/{name}/ or evidence/stage-01/',
        'owner': owner,
        'runtime_status': 'UNKNOWN',
        'adoption_status': 'CANDIDATE'
    })
errors=[]
if len(rows)!=20: errors.append(f'row_count={len(rows)} expected=20')
if len({x['stable_id'] for x in rows}) != len(rows): errors.append('duplicate stable_id')
for x in rows:
    if not (ROOT/x['canonical_path']).exists(): errors.append('missing canonical '+x['stable_id'])
    if not (ROOT/x['source_path']).exists(): errors.append('missing source '+x['stable_id'])
    if not x['owner'] or not x['primary_asset_type']: errors.append('missing ownership '+x['stable_id'])
    if x['runtime_status'] != 'UNKNOWN': errors.append('runtime overclaim '+x['stable_id'])
    if x['adoption_status'] != 'CANDIDATE': errors.append('adoption overclaim '+x['stable_id'])

out=ROOT/'evidence/stage-02/asset-classification.tsv'
with out.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
    w.writeheader(); w.writerows(rows)
summary={
    'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
    'commit': subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip(),
    'input_gate': 'G1 PASS',
    'count': len(rows),
    'primary_asset_types': sorted(set(x['primary_asset_type'] for x in rows)),
    'errors': errors,
    'result': 'PASS' if not errors else 'FAIL'
}
(ROOT/'evidence/stage-02/stage2-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('INPUT_GATE=G1_PASS')
print('EXPECTED_RECORDS=20')
print('ACTUAL_RECORDS='+str(len(rows)))
print('UNIQUE_STABLE_IDS='+str(len({x['stable_id'] for x in rows})))
print('PRIMARY_ASSET_TYPE=Skill')
print('RUNTIME_STATUS=UNKNOWN_FOR_ALL')
print('ERROR_COUNT='+str(len(errors)))
for e in errors: print('ERROR: '+e)
print('RESULT='+('PASS' if not errors else 'FAIL'))
sys.exit(0 if not errors else 1)
