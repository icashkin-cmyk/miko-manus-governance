#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir
import subprocess,json,sys,tempfile,shutil,hashlib
ROOT=Path(__file__).resolve().parents[1]; OUT=output_dir('governance-layer-v01/g9')
if not (ROOT / '.git').exists():
    result={'tester':'TESTER','gate':'G9','checks':[],'overall':'BLOCKED','formal_remote_release':'NOT_RUN','formal_remote_tag':'NOT_RUN','runtime':'NOT_RUN','reason':'Git metadata unavailable; lifecycle and recovery checks require a repository checkout.'}
    (OUT/'g9-lifecycle-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('OVERALL=BLOCKED')
    print('REASON=Git metadata unavailable; lifecycle checks NOT_RUN')
    sys.exit(2)
checks=[]
def add(i,ok,d): checks.append({'id':i,'status':'PASS' if ok else 'FAIL','detail':d})
h=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True); add('G9-01',h.returncode==0 and len(h.stdout.strip())==40,'candidate commit exists')
with tempfile.TemporaryDirectory() as td:
 archive=Path(td)/'candidate.tar'; a=subprocess.run(['git','archive','--format=tar','--output',str(archive),'HEAD'],cwd=ROOT,text=True,capture_output=True); add('G9-02',a.returncode==0 and archive.exists(),'local candidate archive')
 extract=Path(td)/'extract'; extract.mkdir(); e=subprocess.run(['tar','-xf',str(archive),'-C',str(extract)],text=True,capture_output=True); add('G9-03',e.returncode==0 and (extract/'VERSION').exists(),'archive readback')
 # Recovery drill in an isolated temporary git repository.
 rec=Path(td)/'recovery'; shutil.copytree(extract,rec); g=subprocess.run(['git','init','-q'],cwd=rec,text=True,capture_output=True); subprocess.run(['git','config','user.email','test@example.invalid'],cwd=rec); subprocess.run(['git','config','user.name','recovery-test'],cwd=rec); subprocess.run(['git','add','.'],cwd=rec); c=subprocess.run(['git','commit','-qm','recovery baseline'],cwd=rec,text=True,capture_output=True); (rec/'RECOVERY_MUTATION').write_text('temporary\n'); rb=subprocess.run(['git','reset','--hard','HEAD'],cwd=rec,text=True,capture_output=True); cleanrun=subprocess.run(['git','clean','-fdq'],cwd=rec,text=True,capture_output=True); clean=not (rec/'RECOVERY_MUTATION').exists(); add('G9-04',g.returncode==0 and c.returncode==0 and rb.returncode==0 and cleanrun.returncode==0 and clean,'isolated recovery drill')
 # Local tag process only; no remote tag or formal release is created.
 commit=subprocess.run(['git','rev-parse','HEAD'],cwd=rec,text=True,capture_output=True); tag=subprocess.run(['git','tag','candidate-g9-test',commit.stdout.strip()],cwd=rec,text=True,capture_output=True); add('G9-05',commit.returncode==0 and tag.returncode==0,'isolated candidate tag process')
remote=subprocess.run(['git','remote','get-url','origin'],cwd=ROOT,text=True,capture_output=True); add('G9-06',remote.returncode==0 and bool(remote.stdout.strip()),'remote identity readback')
result={'tester':'TESTER','gate':'G9','checks':checks,'overall':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','formal_remote_release':'NOT_RUN','formal_remote_tag':'NOT_RUN','runtime':'NOT_RUN','note':'Only isolated local archive, readback, recovery and tag process were tested; no external push, merge, release or formal adoption was performed.'}
(OUT/'g9-lifecycle-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for x in checks: print(f"{x['id']}\t{x['status']}\t{x['detail']}")
print('FORMAL_REMOTE_RELEASE=NOT_RUN');print('OVERALL='+result['overall']);sys.exit(0 if result['overall']=='PASS' else 1)
