#!/usr/bin/env python3
"""Validate the three proposal skills without executing their described workflows."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROPOSALS = ROOT / "knowledge-cards/proposals/skills"
ARCHIVE = ROOT / "evidence/skill-upgrade-20261117/source-archive"
NAMES = ["miko-flow-optimizer", "miko-project-note-specialist", "miko-prompt-optimizer"]
REQUIRED = ["目的", "觸發", "硬邊界", "工作流程", "標準輸出", "驗收", "完成判準"]
FORBIDDEN = ["正式採用", "Runtime 已啟用", "已執行外部寫入"]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def exact_heading(text: str, number: int, title: str) -> bool:
    return bool(re.search(rf"^## {number}\\. {re.escape(title)}$", text, re.M))

def main() -> int:
    results = []
    for name in NAMES:
        candidate = PROPOSALS / name / "SKILL.md"
        source = ARCHIVE / f"{name}.original.SKILL.md"
        text = candidate.read_text(encoding="utf-8") if candidate.exists() else ""
        checks = {
            "candidate_exists": candidate.is_file(),
            "source_exists": source.is_file(),
            "frontmatter_name": bool(re.search(r"^name: " + re.escape(name) + r"$", text, re.M)),
            "description_present": bool(re.search(r"^description: .+", text, re.M)),
            "proposed_state": "PROPOSED" in text and "NOT_ADOPTED" in text,
            "no_runtime_claim": "Runtime 已啟用" not in text,
            "required_sections": all(term in text for term in REQUIRED),
            "status_boundaries": all(term in text for term in ["UNKNOWN", "NOT_READ", "NOT_RUN", "BLOCKED"]),
            "no_external_execution": "不執行" in text or "不寫入外部" in text,
            "source_hash_recordable": source.is_file(),
        }
        results.append({"skill": name, "checks": checks, "result": "PASS" if all(checks.values()) else "FAIL"})
    overall = all(item["result"] == "PASS" for item in results)
    report = {"test_id": "THREE-SKILL-CANDIDATE-001", "result": "PASS" if overall else "FAIL", "items": results}
    out = ROOT / "out/skill-upgrade-20261117"
    out.mkdir(parents=True, exist_ok=True)
    (out / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if overall else 1

if __name__ == "__main__":
    raise SystemExit(main())
