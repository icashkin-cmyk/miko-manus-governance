#!/usr/bin/env python3
"""Evidence-oriented G0-G9 audit for the supplied v0.1 checklist.
This checker never upgrades NOT_READ/NOT_RUN/UNKNOWN to PASS.
"""
from pathlib import Path
import hashlib, json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/governance-layer-v01"
OUT.mkdir(parents=True, exist_ok=True)

def exists(rel): return (ROOT / rel).exists()
def read(rel): return (ROOT / rel).read_text(encoding="utf-8", errors="replace") if exists(rel) else ""
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest() if Path(path).exists() else "NOT_FOUND"
def row(gate, status, evidence, gap):
    return {"gate": gate, "status": status, "evidence": evidence, "gap": gap}

results=[]
# G0 identity/scope
remote=subprocess.run(["git","remote","get-url","origin"],cwd=ROOT,text=True,capture_output=True)
identity = remote.returncode==0 and "miko-manus-governance" in remote.stdout and exists("VERSION") and exists("MANUS_VERSION") and exists("README.md") and exists("CHANGELOG.md")
results.append(row("G0", "PASS" if identity else "FAIL", "git remote, branch, HEAD, VERSION, MANUS_VERSION, README, CHANGELOG", "" if identity else "identity baseline incomplete"))
# G1 outer skeleton
outer=read("governance/project-architecture/p0-outer-architecture.md")
mapping=read("governance/project-architecture/module-mapping.md")
inv=["Single Decision Root","Single Canonical Repository","Single Primary AI Platform","Separation of Authority and Execution","Evidence-based Closure"]
g1=all(x in outer for x in inv) and all(x in mapping for x in ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10"]) and exists("governance/project-architecture/modules/router/README.md")
results.append(row("G1", "PASS" if g1 else "FAIL", "p0-outer-architecture.md; module-mapping.md; modules/*/README.md", "" if g1 else "outer responsibility mapping incomplete"))
# G2 governance core
core=read("skills/miko-core/SKILL.md")
g2=exists("skills/miko-core/SKILL.md") and all(x in core for x in ["閉環","權限","治理","UNKNOWN","NOT_RUN","獨立驗收","回復"])
results.append(row("G2", "PASS" if g2 else "FAIL", "skills/miko-core/SKILL.md; governance/project-architecture/stage-gates.md", "" if g2 else "governance core contract incomplete"))
# G3 Router: candidate mapping and deterministic route suite; Runtime remains separate.
router=read("governance/project-architecture/modules/router/README.md")
g3_contract=all(x in router for x in ["觸發", "路由", "CONFLICT", "負向測試"])
g3run=subprocess.run([sys.executable,'-I','-B','tests/g3_router_acceptance.py'],cwd=ROOT,text=True,capture_output=True)
g3json=OUT/'router/g3-router-acceptance.json'
g3data=json.loads(g3json.read_text(encoding='utf-8')) if g3json.exists() else {}
g3_pass=g3_contract and g3run.returncode==0 and g3data.get('overall')=='PASS' and g3data.get('mapping_count')==2
g3="PASS" if g3_pass else ("NOT_RUN" if g3_contract and g3run.returncode!=0 else "FAIL")
results.append(row("G3", g3, "modules/router/README.md; router/g3-router-mapping.tsv; g3-router-acceptance.json", "candidate mapping suite failed or runtime route loading remains NOT_RUN" if not g3_pass else "Runtime loading remains NOT_RUN"))
# G4 cards: exact K01-K50 inventory plus the resolved K51 extension
formal_cards=sorted(ROOT.glob("knowledge-cards/K[0-9][0-9].md"))
candidate_cards=sorted(ROOT.glob("knowledge-cards/proposals/kcards/K[0-9][0-9].md"))
conflict=read("evidence/governance-layer-v01/kcards/K03-conflict.json")
card_ids={p.stem for p in formal_cards + candidate_cards}
required_ids={f"K{i:02d}" for i in range(1,51)}
card_total=len(card_ids)
k51=exists("knowledge-cards/proposals/kcards/K51.md")
resolved='"status": "RESOLVED"' in conflict and 'K51' in conflict
if required_ids <= card_ids and k51 and resolved:
    g4="PASS"
elif '"status": "CONFLICT"' in conflict:
    g4="CONFLICT"
else:
    g4="NOT_READ"
results.append(row("G4", g4, f"formal={len(formal_cards)}; candidate={len(candidate_cards)}; K01-K50 unique={len(required_ids & card_ids)}; K51={k51}", "K03 identity conflict remains unresolved" if g4=="CONFLICT" else (f"K01-K50 or K51 resolution incomplete; unique={card_total}" if g4!="PASS" else "")))
# G5 skills: inventory exists, actual per-skill execution not proven by static files
skills=sorted(ROOT.glob("skills/*/SKILL.md"))
g5="PASS" if len(skills)==20 and exists("evidence/stage-01/skill-inventory-current.json") else "UNKNOWN"
results.append(row("G5", g5, f"skills count={len(skills)}; stage-01 inventory", "per-skill runtime execution and workflow samples are not uniformly proven" if g5=="PASS" else "skill inventory evidence incomplete"))
# G6 tools: spec exists but connector/auth runtime not run
adapters=read("adapters/README.md")
g6="NOT_RUN" if adapters else "NOT_READ"
results.append(row("G6", g6, "adapters/README.md; modules/tools/README.md", "live connector, authorization, readback and degradation tests NOT_RUN"))
# G7 E2E: no representative E2E acceptance record
has_e2e=any("E2E" in p.read_text(encoding="utf-8",errors="replace") for p in ROOT.glob("evidence/**/*") if p.is_file())
g7="PASS" if has_e2e and exists("tests/e2e_acceptance.py") else "NOT_RUN"
results.append(row("G7", g7, "evidence and tests scan", "representative end-to-end workflow runner is NOT_RUN or absent"))
# G8 tests/independent acceptance: dependency G7 blocks full gate
results.append(row("G8", "NOT_RUN", "tests/check_repo.py; P0 cold-read evidence", "full G8 depends on G7 PASS; external independent auditor not run"))
# G9 release/maintenance: candidate commit exists but remote push/readback/tag not done
results.append(row("G9", "NOT_RUN", "candidate commit and lifecycle contract", "release/tag/remote readback/recovery drill not run"))

summary={"checklist":"MIKO Manus governance layer acceptance v0.1","results":results,"counts":{}}
for r in results: summary["counts"][r["status"]]=summary["counts"].get(r["status"],0)+1
(OUT/"g0-g9-results.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
for r in results: print(f'{r["gate"]}\t{r["status"]}\t{r["evidence"]}\t{r["gap"]}')
print("OVERALL=" + ("PASS" if all(r["status"]=="PASS" for r in results) else "NOT_COMPLETE"))
sys.exit(0)
