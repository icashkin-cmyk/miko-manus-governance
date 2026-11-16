#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
CARD_DIR=ROOT/'knowledge-cards/proposals/kcards'
OUT=ROOT/'evidence/governance-layer-v01/kcards'
OUT.mkdir(parents=True,exist_ok=True)
ids=[f'K{i:02d}' for i in range(3,51)]
fields=['在以下情況下使用','內容','【執行要求】','【禁止事項】','【完成判準】','【失敗處理】']
rows=[]
for name in ids:
 p=CARD_DIR/(name+'.md'); errors=[]
 if not p.exists():
  rows.append({'id':name,'status':'FAIL','errors':['missing_file']}); continue
 t=p.read_text(encoding='utf-8')
 if not t.startswith(f'# {name} '): errors.append('title_or_id')
 if 'PROPOSED' not in t or '尚未正式採用' not in t: errors.append('candidate_boundary')
 for f in fields:
  if f not in t: errors.append(f)
 m=re.search(r'內容\n(.*?)(?:\n⸻|\n文件結尾|\Z)',t,re.S)
 n=len(m.group(1).strip()) if m else -1
 if not 80<=n<=1000: errors.append(f'content_chars={n}')
 if not any(x in t for x in ['UNKNOWN','資訊不足']): errors.append('unknown')
 if not any(x in t for x in ['NOT_RUN','未執行']): errors.append('not_run')
 rows.append({'id':name,'status':'PASS' if not errors else 'FAIL','content_chars':n,'errors':errors})
# Independent negative checks against a read-only copy of K03.
base=(CARD_DIR/'K03.md').read_text(encoding='utf-8')
neg=[]
for label,mut in [('remove_execution',base.replace('【執行要求】','',1)),('oversize',base.replace('⸻','Z'*1200+'\n⸻',1)),('adopted',base.replace('PROPOSED','ADOPTED',1))]:
 m=re.search(r'內容\n(.*?)(?:\n⸻|\n文件結尾|\Z)',mut,re.S); n=len(m.group(1).strip()) if m else -1
 failed=(label=='remove_execution' and '【執行要求】' not in mut) or (label=='oversize' and n>1000) or (label=='adopted' and 'PROPOSED' not in mut)
 neg.append({'case':label,'detected':failed})
result={'auditor':'INDEPENDENT_AUDITOR','scope':'K03-K50','rows':rows,'negative_cases':neg,'overall':'PASS' if all(r['status']=='PASS' for r in rows) and all(x['detected'] for x in neg) else 'FAIL','limitation':'This is independent candidate-card validation; it does not establish formal adoption or Runtime loading.'}
(OUT/'k03-k50-independent-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in rows: print(f"{r['id']}\t{r['status']}\tcontent_chars={r.get('content_chars','')}\terrors={','.join(r.get('errors',[]))}")
print('NEGATIVE_CASES='+('PASS' if all(x['detected'] for x in neg) else 'FAIL'))
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
