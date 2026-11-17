#!/usr/bin/env python3
"""Evidence-oriented G0-G9 audit for the supplied v0.1 checklist.
This checker never upgrades NOT_READ/NOT_RUN/UNKNOWN to PASS.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acceptance_runtime import output_dir
import hashlib, json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = output_dir("governance-layer-v01")

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
core=read("skills/manus-core/SKILL.md")
g2=exists("skills/manus-core/SKILL.md") and all(x in core for x in ["閉環","權限","治理","UNKNOWN","NOT_RUN","獨立驗收","回復"])
results.append(row("G2", "PASS" if g2 else "FAIL", "skills/manus-core/SKILL.md; governance/project-architecture/stage-gates.md", "" if g2 else "governance core contract incomplete"))
# G3 Router: candidate mapping and deterministic route suite; Runtime remains separate.
router=read("governance/project-architecture/modules/router/README.md")
g3_contract=all(x in router for x in ["觸發", "路由", "CONFLICT", "負向測試"])
g3run=subprocess.run([sys.executable,'-I','-B','tests/g3_router_acceptance.py'],cwd=ROOT,text=True,capture_output=True)
g3json=OUT/'router/g3-router-acceptance.json'
g3data=json.loads(g3json.read_text(encoding='utf-8')) if g3json.exists() else {}
g3_pass=g3_contract and g3run.returncode==0 and g3data.get('overall')=='PASS' and g3data.get('mapping_count')==2
g3="PASS" if g3_pass else "FAIL"
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
g5="PASS" if len(skills)==21 and exists("evidence/stage-01/skill-inventory-current.json") else "UNKNOWN"
results.append(row("G5", g5, f"skills count={len(skills)}; stage-01 inventory", "per-skill runtime execution and workflow samples are not uniformly proven" if g5=="PASS" else "skill inventory evidence incomplete"))
# G6 tools: local probes may pass; external connectors remain explicitly NOT_RUN.
adapters=read("adapters/README.md")
def result_overall(rel):
    p=ROOT/rel
    if not p.exists(): return None
    try: return json.loads(p.read_text(encoding="utf-8")).get("overall")
    except Exception: return None
g6="PASS" if result_overall("evidence/governance-layer-v01/g6/g6-tools-acceptance.json")=="PASS" else ("NOT_RUN" if adapters else "NOT_READ")
results.append(row("G6", g6, "adapters/README.md; g6/g6-tools-acceptance.json", "external connectors remain NOT_RUN" if g6=="PASS" else "G6 acceptance evidence missing or failed"))
# G7 representative local E2E workflow.
g7="PASS" if result_overall("evidence/governance-layer-v01/g7/g7-e2e-acceptance.json")=="PASS" else "NOT_RUN"
results.append(row("G7", g7, "g7/g7-e2e-acceptance.json", "representative E2E workflow failed or is NOT_RUN"))
# G8 independent acceptance.
g8="PASS" if result_overall("evidence/governance-layer-v01/g8/g8-independent-acceptance.json")=="PASS" else "NOT_RUN"
results.append(row("G8", g8, "g8/g8-independent-acceptance.json", "independent full acceptance failed or is NOT_RUN"))
# G9 candidate lifecycle and recovery drill; formal remote release remains separate.
g9="PASS" if result_overall("evidence/governance-layer-v01/g9/g9-lifecycle-acceptance.json")=="PASS" else "NOT_RUN"
results.append(row("G9", g9, "g9/g9-lifecycle-acceptance.json", "candidate lifecycle evidence failed or is NOT_RUN"))

summary={"checklist":"MIKO Manus governance layer acceptance v0.1","results":results,"counts":{}}
for r in results: summary["counts"][r["status"]]=summary["counts"].get(r["status"],0)+1
(OUT/"g0-g9-results.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
for r in results: print(f'{r["gate"]}\t{r["status"]}\t{r["evidence"]}\t{r["gap"]}')
overall = "PASS" if all(r["status"]=="PASS" for r in results) else "NOT_COMPLETE"
print("OVERALL=" + overall)
sys.exit(0 if overall == "PASS" else 1)
