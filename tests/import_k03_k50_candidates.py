#!/usr/bin/env python3
from pathlib import Path
import os
import hashlib, json, re, shutil

ROOT=Path(__file__).resolve().parents[1]
SRC=Path(os.environ.get('K_CARD_SOURCE', 'Pasted_content_24.txt'))
OUT=ROOT/'knowledge-cards/proposals/kcards'
EVID=ROOT/'evidence/governance-layer-v01/kcards'
ARCH=ROOT/'source-archive/governance-layer-v01'
OUT.mkdir(parents=True,exist_ok=True); EVID.mkdir(parents=True,exist_ok=True); ARCH.mkdir(parents=True,exist_ok=True)
text=SRC.read_text(encoding='utf-8')
shutil.copy2(SRC, ARCH/'Pasted_content_24.txt')
heads=list(re.finditer(r'^K(\d{2})｜([^\n]+)$', text, flags=re.M))
assert [int(m.group(1)) for m in heads]==list(range(3,51)), 'source must contain K03-K50 in order'
manifest=[]
for i,m in enumerate(heads):
    num=m.group(1); title=m.group(2).strip(); start=m.start(); end=heads[i+1].start() if i+1<len(heads) else len(text)
    raw=text[start:end].strip()
    # Keep the supplied body, adding only candidate metadata and a stable source pointer.
    body=(f'# K{num} {title}\n\n'
          f'> 狀態：PROPOSED（來源附件候選稿；尚未正式採用、尚未 Runtime 載入）\n'
          f'> 來源：source-archive/governance-layer-v01/Pasted_content_24.txt；來源段落起點：K{num}\n\n'
          + raw + '\n')
    path=OUT/f'K{num}.md'; path.write_text(body,encoding='utf-8')
    h=hashlib.sha256(path.read_bytes()).hexdigest()
    manifest.append({'id':f'K{num}','title':title,'path':str(path.relative_to(ROOT)),'status':'PROPOSED','source':'source-archive/governance-layer-v01/Pasted_content_24.txt','sha256':h,'source_sha256':hashlib.sha256(raw.encode()).hexdigest()})
(Path(EVID/'k03-k50-manifest.json')).write_text(json.dumps({'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'count':len(manifest),'cards':manifest},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (EVID/'k03-k50-mapping.tsv').open('w',encoding='utf-8') as f:
    f.write('id\ttitle\tpath\tstatus\tsha256\n')
    for r in manifest: f.write(f"{r['id']}\t{r['title']}\t{r['path']}\t{r['status']}\t{r['sha256']}\n")
print(f'IMPORTED={len(manifest)}')
print(f'SOURCE_SHA256={hashlib.sha256(SRC.read_bytes()).hexdigest()}')
print('STATUS=PROPOSED')
