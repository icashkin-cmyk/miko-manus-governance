#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence/governance-layer-v01'
OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def add(i,ok,detail):
    checks.append({'id':i,'status':'PASS' if ok else 'FAIL','detail':detail})

# Independent file/tree checks; no use of g0-g9-results.json for decisions.
add('IA-01', (ROOT/'VERSION').exists() and (ROOT/'MANUS_VERSION').exists() and (ROOT/'README.md').exists(), 'baseline files')
formal={p.stem for p in (ROOT/'knowledge-cards').glob('K[0-9][0-9].md')}
proposed={p.stem for p in (ROOT/'knowledge-cards/proposals/kcards').glob('K[0-9][0-9].md')}
add('IA-02', len(formal|proposed)==50, f'K unique count={len(formal|proposed)}')
conf=(ROOT/'evidence/governance-layer-v01/kcards/K03-conflict.json').read_text(encoding='utf-8') if (ROOT/'evidence/governance-layer-v01/kcards/K03-conflict.json').exists() else ''
add('IA-03', 'CONFLICT' in conf and 'MIKO' in conf, 'K03 identity conflict is preserved')
add('IA-04', all((ROOT/x).exists() for x in ['tests/check_repo.py','tests/stage1_inventory_check.py','tests/stage2_asset_classification_check.py']), 'test entrypoints')
# Independent rerun of C1-C16; evidence is saved separately.
p=subprocess.run([sys.executable,'-I','-B','tests/check_repo.py'],cwd=ROOT,text=True,capture_output=True)
(OUT/'independent-c1-c16.stdout').write_text(p.stdout,encoding='utf-8')
(OUT/'independent-c1-c16.stderr').write_text(p.stderr,encoding='utf-8')
add('IA-05', p.returncode==0 and 'PASS C3' in p.stdout and '合計：16/16 PASS' in p.stdout, f'check_repo exit={p.returncode}')
# Static gate truthfulness: no accepted summary may claim overall PASS while unresolved gates remain.
summary=json.loads((OUT/'g0-g9-results.json').read_text(encoding='utf-8')) if (OUT/'g0-g9-results.json').exists() else {}
add('IA-06', summary.get('counts',{}).get('NOT_RUN',0)>0 or summary.get('counts',{}).get('CONFLICT',0)>0, 'non-PASS gates remain explicitly recorded')
result={'auditor':'INDEPENDENT_AUDITOR','checks':checks,'overall':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','limitation':'This audit validates evidence integrity and truthfulness; it does not convert runtime NOT_RUN or K03 CONFLICT into PASS.'}
(OUT/'independent-g0-g9-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in checks: print(f"{x['id']}\t{x['status']}\t{x['detail']}")
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
