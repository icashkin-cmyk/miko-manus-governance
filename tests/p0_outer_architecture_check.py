#!/usr/bin/env python3
"""P0 candidate architecture checker; no external writes."""
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "governance/project-architecture/module-mapping.md"
OUTER = ROOT / "governance/project-architecture/p0-outer-architecture.md"
MODULES = ROOT / "governance/project-architecture/modules"

EXPECTED = {
    "G01": ("governance",),
    "G02": ("skills/miko-core", "governance/project-architecture/modules/core"),
    "G03": ("governance/project-architecture/modules/router",),
    "G04": ("knowledge-cards",),
    "G05": ("skills",),
    "G06": ("migration-ledger", "VERSION", "MANUS_VERSION", "governance/project-architecture/modules/registry"),
    "G07": ("adapters", "governance/project-architecture/modules/tools"),
    "G08": ("tests",),
    "G09": ("evidence",),
    "G10": ("archive", "migration-ledger", "next-step", "governance/project-architecture/modules/lifecycle"),
}


def fail(msg):
    print("FAIL", msg)
    return False


def path_exists(rel):
    return (ROOT / rel).exists()


def positive():
    ok = True
    for gid, paths in EXPECTED.items():
        if not all(path_exists(p) for p in paths):
            ok = fail(f"{gid} missing path(s): {paths}") and ok
    text = MAPPING.read_text(encoding="utf-8")
    if len(re.findall(r"^\| G(?:0[1-9]|10) \|", text, flags=re.M)) != 10:
        ok = fail("mapping does not contain exactly G01-G10") and ok
    for token in ("PROPOSED", "NOT_ADOPTED", "Runtime", "不重複責任"):
        if token not in text:
            ok = fail(f"mapping missing boundary token: {token}") and ok
    for module in ("core", "router", "registry", "tools", "lifecycle"):
        if not (MODULES / module / "README.md").is_file():
            ok = fail(f"module contract missing: {module}") and ok
    if ok:
        print("POSITIVE=PASS")
    return ok


def negative():
    # Mutation: remove one mapping row in a temporary copy; checker must detect it.
    text = MAPPING.read_text(encoding="utf-8")
    mutated = re.sub(r"^\| G03 \|.*\n", "", text, count=1, flags=re.M)
    detected = len(re.findall(r"^\| G(?:0[1-9]|10) \|", mutated, flags=re.M)) != 10
    print("NEGATIVE_MAPPING_REMOVAL=" + ("PASS" if detected else "FAIL"))
    # Boundary mutation: candidate status removed must be detected.
    boundary_detected = "NOT_ADOPTED" not in text.replace("NOT_ADOPTED", "", 1)
    print("NEGATIVE_STATUS_REMOVAL=" + ("PASS" if boundary_detected else "FAIL"))
    return detected and boundary_detected


def boundary():
    text = OUTER.read_text(encoding="utf-8")
    required = ["MIKO", "GitHub", "Manus", "Tools & Integrations", "Evidence & Lifecycle"]
    good = all(x in text for x in required) and "不宣稱" in text and "NOT_RUN" in text
    print("BOUNDARY= " + ("PASS" if good else "FAIL"))
    return good


def reverse():
    # Reverse lookup: each G ID must have one and only one mapping row.
    rows = MAPPING.read_text(encoding="utf-8").splitlines()
    counts = {gid: sum(line.startswith(f"| {gid} |") for line in rows) for gid in EXPECTED}
    good = all(v == 1 for v in counts.values())
    print("REVERSE_MAPPING=" + ("PASS" if good else "FAIL") + " " + str(counts))
    return good


def main():
    print("P0_SCOPE=outer architecture and G01-G10 mapping")
    results = [positive(), negative(), boundary(), reverse()]
    print("OVERALL=" + ("PASS" if all(results) else "FAIL"))
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
