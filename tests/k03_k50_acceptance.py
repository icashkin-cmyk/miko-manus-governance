#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
CARD_DIR=ROOT/'knowledge-cards/proposals/kcards'
OUT=ROOT/'evidence/governance-layer-v01/kcards'
OUT.mkdir(parents=True,exist_ok=True)
required=[f'K{i:02d}' for i in range(3,51)]
fields=['在以下情況下使用','內容','【執行要求】','【禁止事項】','【完成判準】','【失敗處理】']
rows=[]
def check(name,text,expected):
 errors=[]
 if f'# {name} ' not in text: errors.append('title')
 if '狀態：PROPOSED' not in text: errors.append('status')
 if '來源：' not in text: errors.append('source')
 for f in fields:
  if f not in text: errors.append(f)
 m=re.search(r'內容\n(.*?)(?:\n⸻|\n文件結尾|\Z)',text,re.S)
 n=len(m.group(1).strip()) if m else -1
 if n<80: errors.append('content_too_short')
 if n>1000: errors.append('content_over_1000')
 if 'UNKNOWN' not in text and '資訊不足' not in text: errors.append('unknown_boundary')
 if 'NOT_RUN' not in text and '未執行' not in text: errors.append('not_run_boundary')
 return {'id':name,'status':'PASS' if not errors else 'FAIL','content_chars':n,'errors':errors}
for name in required:
 p=CARD_DIR/(name+'.md')
 rows.append(check(name,p.read_text(encoding='utf-8') if p.exists() else '',name) if p.exists() else {'id':name,'status':'FAIL','content_chars':-1,'errors':['missing_file']})
# Negative mutation tests prove the validator detects missing field, overlong content, and wrong status.
base=(CARD_DIR/'K03.md').read_text(encoding='utf-8')
mutations={
 'missing_field':base.replace('【禁止事項】','【禁止事項_REMOVED】',1),
 'overlong':base.replace('⸻','X'*1200+'\n⸻',1),
 'wrong_status':base.replace('狀態：PROPOSED','狀態：PASS',1),
}
mutation_results={k:check('K03',v,'K03')['status']=='FAIL' for k,v in mutations.items()}
result={'tester':'TESTER','scope':'K03-K50','rows':rows,'mutation_tests':mutation_results,'overall':'PASS' if all(r['status']=='PASS' for r in rows) and all(mutation_results.values()) else 'FAIL'}
(OUT/'k03-k50-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in rows: print(f"{r['id']}\t{r['status']}\tcontent_chars={r['content_chars']}\terrors={','.join(r['errors'])}")
print('MUTATION_TESTS='+('PASS' if all(mutation_results.values()) else 'FAIL'))
print('OVERALL='+result['overall'])
sys.exit(0 if result['overall']=='PASS' else 1)
