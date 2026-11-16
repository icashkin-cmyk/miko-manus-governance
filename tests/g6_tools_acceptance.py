#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir
import json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parents[1]; OUT=output_dir('governance-layer-v01/g6')
contract=(ROOT/'adapters/README.md').read_text(encoding='utf-8') if (ROOT/'adapters/README.md').exists() else ''
checks=[]
def add(i,ok,detail): checks.append({'id':i,'status':'PASS' if ok else 'FAIL','detail':detail})
add('G6-01', all(x in contract for x in ['唯一名稱','用途','權限','輸入','輸出','NOT_RUN']), 'adapter contract fields')
add('G6-02', (ROOT/'adapters').is_dir() and (ROOT/'adapters/README.md').exists(), 'adapter registry path')
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'readback.txt'; p.write_text('G6_READBACK_OK\n',encoding='utf-8'); add('G6-03',p.read_text(encoding='utf-8')=='G6_READBACK_OK\n','file write/readback')
 r=subprocess.run([sys.executable,'-c','print("G6_TERMINAL_OK")'],text=True,capture_output=True); add('G6-04',r.returncode==0 and r.stdout.strip()=='G6_TERMINAL_OK','terminal execution')
 g=subprocess.run(['git','rev-parse','--is-inside-work-tree'],cwd=ROOT,text=True,capture_output=True); add('G6-05',g.returncode==0 and g.stdout.strip()=='true','git read-only probe')
# Failure/degradation and forbidden boundary tests.
add('G6-06', 'NOT_RUN' in contract and '不得把工具規格當成已連線' in contract, 'unverified connector remains NOT_RUN')
add('G6-07', all(x in contract for x in ['LIVE','Broker','付款','不可逆']), 'forbidden boundary')
result={'tester':'TESTER','gate':'G6','checks':checks,'external_connectors':'NOT_RUN','overall':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','runtime':'NOT_RUN'}
(OUT/'g6-tools-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in checks: print(f"{x['id']}\t{x['status']}\t{x['detail']}")
print('EXTERNAL_CONNECTORS=NOT_RUN'); print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
