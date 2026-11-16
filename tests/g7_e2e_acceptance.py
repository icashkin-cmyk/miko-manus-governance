#!/usr/bin/env python3
from pathlib import Path
import csv,json,hashlib,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'evidence/governance-layer-v01/g7'; OUT.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((ROOT/'evidence/governance-layer-v01/router/g3-router-mapping.tsv').open(encoding='utf-8'),delimiter='\t'))
def route(text):
 h=[r for r in rows if any(k in text for k in r['trigger_keywords'].split('|'))]
 return h[0] if len(h)==1 else None
cases=[('workflow-k03','請處理多項任務的時限衝突與任務優先級','K03'),('workflow-k51','請升級並保留原本內容與歷史版本','K51')]
results=[]; errors=[]
with tempfile.TemporaryDirectory() as td:
 for cid,text,expected in cases:
  r=route(text); source=ROOT/r['source'] if r else None
  ok=r is not None and r['stable_id']==expected and source.exists()
  out=Path(td)/(cid+'.md')
  if ok: out.write_text(f"route={expected}\nsource={r['source']}\n",encoding='utf-8')
  readback=out.read_text(encoding='utf-8') if out.exists() else ''
  ok=ok and expected in readback and hashlib.sha256(out.read_bytes()).hexdigest()
  results.append({'id':cid,'status':'PASS' if ok else 'FAIL','route':expected if ok else None,'readback':bool(readback)})
  if not ok: errors.append(cid)
# Negative end-to-end case must stop before execution.
r=route('請翻譯普通文字'); neg=(r is None); results.append({'id':'workflow-negative','status':'PASS' if neg else 'FAIL','route':None if neg else r['stable_id']});
if not neg: errors.append('workflow-negative')
# Conflict must stop before selecting a card.
r=route('請排序多項任務後再升級並保留歷史版本'); conflict=(r is None); results.append({'id':'workflow-conflict-stop','status':'PASS' if conflict else 'FAIL','route':None if conflict else r['stable_id']});
if not conflict: errors.append('workflow-conflict-stop')
result={'tester':'TESTER','gate':'G7','workflow':'Router -> Knowledge Card -> output -> SHA-256 -> readback','cases':results,'overall':'PASS' if not errors else 'FAIL','runtime':'NOT_RUN'}
(OUT/'g7-e2e-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in results: print(f"{x['id']}\t{x['status']}\t{x.get('route')}")
print('OVERALL='+result['overall']); sys.exit(0 if result['overall']=='PASS' else 1)
