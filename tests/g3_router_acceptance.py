#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir
import csv,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
MAP=ROOT/'evidence/governance-layer-v01/router/g3-router-mapping.tsv'
OUT=output_dir('governance-layer-v01/router')
rows=list(csv.DictReader(MAP.open(encoding='utf-8'),delimiter='\t'))
errors=[]
if [r['stable_id'] for r in rows] != ['K03','K51']: errors.append('mapping must contain K03 then K51 exactly once')
for r in rows:
 p=ROOT/r['source']
 if not p.exists(): errors.append(r['stable_id']+':missing_source')
 if r['status']!='PROPOSED': errors.append(r['stable_id']+':status_not_proposed')
 if not r['trigger_keywords'] or not r['prohibited']: errors.append(r['stable_id']+':missing_trigger_or_boundary')

def route(text):
 hits=[]
 for r in rows:
  if any(k in text for k in r['trigger_keywords'].split('|')): hits.append(r['stable_id'])
 if len(hits)==1: return {'decision':'ROUTE','primary':hits[0]}
 if len(hits)>1: return {'decision':'CONFLICT','primary':None,'candidates':hits}
 return {'decision':'NO_ROUTE','primary':None}

cases=[
 ('positive_k03','同時有三項任務，存在時限衝突，需要做任務優先級排序','ROUTE','K03'),
 ('positive_k51','請升級 Skill 並保留原本內容，加入版本沿革與回歸測試','ROUTE','K51'),
 ('negative_unrelated','請翻譯一段普通文字','NO_ROUTE',None),
 ('boundary_k03','資源不足','ROUTE','K03'),
 ('boundary_k51','不要覆蓋','ROUTE','K51'),
 ('conflict_both','請排序多項任務並升級、保留歷史版本','CONFLICT',None),
]
case_results=[]
for cid,text,expected,primary in cases:
 got=route(text); ok=got['decision']==expected and (primary is None or got.get('primary')==primary)
 case_results.append({'id':cid,'expected':expected,'actual':got,'status':'PASS' if ok else 'FAIL'})
 if not ok: errors.append(cid)
# Negative mutation checks: remove each mapping row and prove its positive case cannot still route to that ID.
mut=[]
for sid in ['K03','K51']:
 reduced=[r for r in rows if r['stable_id']!=sid]
 text=next(x[1] for x in cases if x[3]==sid)
 hits=[r['stable_id'] for r in reduced if any(k in text for k in r['trigger_keywords'].split('|'))]
 mut.append({'id':'remove_'+sid,'detected_missing_route':sid not in hits})
 if sid in hits: errors.append('mutation_remove_'+sid)
result={'tester':'TESTER','gate':'G3','mapping_count':len(rows),'cases':case_results,'mutation_tests':mut,'overall':'PASS' if not errors and all(x['status']=='PASS' for x in case_results) and all(x['detected_missing_route'] for x in mut) else 'FAIL','runtime':'NOT_RUN'}
(OUT/'g3-router-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in case_results: print(f"{x['id']}\t{x['status']}\texpected={x['expected']}\tactual={x['actual']}")
print('MUTATION_TESTS='+('PASS' if all(x['detected_missing_route'] for x in mut) else 'FAIL'))
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
