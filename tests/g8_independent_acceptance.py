#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'evidence/governance-layer-v01/g8'; OUT.mkdir(parents=True,exist_ok=True)
items=[('G3',['tests/g3_router_independent_audit.py']),('G6',['tests/g6_tools_acceptance.py']),('G7',['tests/g7_e2e_acceptance.py'])]
checks=[]
for gid,cmd in items:
 p=subprocess.run([sys.executable,'-I','-B',*cmd],cwd=ROOT,text=True,capture_output=True)
 checks.append({'id':gid,'exit_code':p.returncode,'status':'PASS' if p.returncode==0 else 'FAIL'})
ci=subprocess.run([sys.executable,'-I','-B','tests/check_repo.py'],cwd=ROOT,text=True,capture_output=True)
checks.append({'id':'C1-C16','exit_code':ci.returncode,'status':'PASS' if ci.returncode==0 and '合計：16/16 PASS' in ci.stdout else 'FAIL'})
result={'auditor':'INDEPENDENT_AUDITOR','gate':'G8','checks':checks,'overall':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','runtime':'NOT_RUN','limitation':'Independent local acceptance; no external Runtime activation claim.'}
(OUT/'g8-independent-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in checks: print(f"{x['id']}\t{x['status']}\texit={x['exit_code']}")
print('OVERALL='+result['overall']);sys.exit(0 if result['overall']=='PASS' else 1)
