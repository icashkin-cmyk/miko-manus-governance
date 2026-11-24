#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir
import csv,json,sys
ROOT=Path(__file__).resolve().parents[1]
MAP=ROOT/'evidence/governance-layer-v01/router/g3-router-mapping.tsv'
OUT=output_dir('governance-layer-v01/router')
rows=list(csv.DictReader(MAP.open(encoding='utf-8'),delimiter='\t'))
errors=[]
ids=[r['stable_id'] for r in rows]
if sorted(ids)!=['K03','K51'] or len(ids)!=len(set(ids)): errors.append('unique_mapping')
for r in rows:
 if r['status']!='PROPOSED': errors.append(r['stable_id']+':candidate_boundary')
 p=ROOT/r['source']
 if not p.exists(): errors.append(r['stable_id']+':source_missing')
 else:
  t=p.read_text(encoding='utf-8')
  if 'PROPOSED' not in t or '尚未正式採用' not in t: errors.append(r['stable_id']+':card_boundary')
  if r['stable_id']=='K03' and '任務優先級與資源配置' not in t: errors.append('K03_semantics')
  if r['stable_id']=='K51' and '累積式演進與歷史版本保護' not in t: errors.append('K51_semantics')
def route(text):
 hits=[r['stable_id'] for r in rows if any(k in text for k in r['trigger_keywords'].split('|'))]
 return ('ROUTE',hits[0]) if len(hits)==1 else ('CONFLICT',None) if len(hits)>1 else ('NO_ROUTE',None)
cases=[('K03','請處理多項任務的時限衝突與資源不足',('ROUTE','K03')),('K51','請重構並保留原本內容及歷史版本',('ROUTE','K51')),('NONE','普通翻譯請求',('NO_ROUTE',None)),('CONFLICT','任務排序後再升級並保留歷史',('CONFLICT',None))]
results=[]
for cid,text,expected in cases:
 actual=route(text); ok=actual==expected; results.append({'id':cid,'expected':expected,'actual':actual,'status':'PASS' if ok else 'FAIL'})
 if not ok: errors.append(cid)
# Independent boundary assertion: no result is allowed to claim Runtime loaded.
runtime_not_run=True
result={'auditor':'INDEPENDENT_AUDITOR','gate':'G3','mapping_count':len(rows),'cases':results,'runtime':'NOT_RUN','overall':'PASS' if not errors and all(x['status']=='PASS' for x in results) and runtime_not_run else 'FAIL','limitations':['This validates candidate mapping and deterministic routing only; it does not validate Manus Runtime loading or external tool execution.']}
(OUT/'g3-router-independent-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in results: print(f"{x['id']}\t{x['status']}\texpected={x['expected']}\tactual={x['actual']}")
print('RUNTIME=NOT_RUN')
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
