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
required={f'K{i:02d}' for i in range(1,51)}
add('IA-02', required <= (formal|proposed) and (ROOT/'knowledge-cards/proposals/kcards/K51.md').exists(), f'K01-K50 count={len(required & (formal|proposed))}; K51={(ROOT/"knowledge-cards/proposals/kcards/K51.md").exists()}')
conf=(ROOT/'evidence/governance-layer-v01/kcards/K03-conflict.json').read_text(encoding='utf-8') if (ROOT/'evidence/governance-layer-v01/kcards/K03-conflict.json').exists() else ''
add('IA-03', 'RESOLVED' in conf and 'K51' in conf and '任務優先級與資源配置' in conf, 'K03 decision and K51 renumbering are preserved')
add('IA-04', all((ROOT/x).exists() for x in ['tests/check_repo.py','tests/stage1_inventory_check.py','tests/stage2_asset_classification_check.py']), 'test entrypoints')
# Independent G3 rerun: read the mapping and execute the independent Router audit.
g3p=subprocess.run([sys.executable,'-I','-B','tests/g3_router_independent_audit.py'],cwd=ROOT,text=True,capture_output=True)
g3j=(ROOT/'evidence/governance-layer-v01/router/g3-router-independent-audit.json')
g3d=json.loads(g3j.read_text(encoding='utf-8')) if g3j.exists() else {}
add('IA-07', g3p.returncode==0 and g3d.get('overall')=='PASS' and g3d.get('mapping_count')==2 and g3d.get('runtime')=='NOT_RUN', 'independent G3 mapping and route cases')
# Independent rerun of C1-C16; evidence is saved separately.
p=subprocess.run([sys.executable,'-I','-B','tests/check_repo.py'],cwd=ROOT,text=True,capture_output=True)
def clean(s):
    home='/'+ 'home/' + 'ubuntu/'
    for token in [home+'work/miko-manus-governance-p0-live',home+'work/miko-manus-governance',home]:
        s=s.replace(token,'<REPO_ROOT>')
    return '\n'.join(line.rstrip() for line in s.splitlines())+'\n'
(OUT/'independent-c1-c16.stdout').write_text(clean(p.stdout),encoding='utf-8')
(OUT/'independent-c1-c16.stderr').write_text(clean(p.stderr),encoding='utf-8')
add('IA-05', p.returncode==0 and 'PASS C3' in p.stdout and '合計：16/16 PASS' in p.stdout, f'check_repo exit={p.returncode}')
# Static gate truthfulness: runtime NOT_RUN remains explicit even after K03 resolution.
summary=json.loads((OUT/'g0-g9-results.json').read_text(encoding='utf-8')) if (OUT/'g0-g9-results.json').exists() else {}
add('IA-06', summary.get('counts',{}).get('NOT_RUN',0)>0 and summary.get('counts',{}).get('CONFLICT',0)==0, 'runtime NOT_RUN remains explicit; K03 conflict is resolved')
result={'auditor':'INDEPENDENT_AUDITOR','checks':checks,'overall':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','limitation':'This audit validates evidence integrity and K03 identity resolution; it does not convert runtime NOT_RUN into PASS.'}
(OUT/'independent-g0-g9-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in checks: print(f"{x['id']}\t{x['status']}\t{x['detail']}")
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
