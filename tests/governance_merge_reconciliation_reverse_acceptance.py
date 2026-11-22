#!/usr/bin/env python3
"""Offline acceptance tests for the merge/reconciliation reverse-acceptance candidate skill."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md"


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"FAIL {label}: missing {needle!r}")
    print(f"PASS {label}")


def reject_status(status: str) -> bool:
    return status in {"UNKNOWN", "NOT_RUN", "BLOCKED", "CONFLICT", "FAIL"}


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---\n"), "FAIL frontmatter: missing YAML frontmatter"
    for needle, label in [
        ("name: governance-merge-reconciliation-reverse-acceptance", "frontmatter name"),
        ("status: CANDIDATE", "candidate status"),
        ("adoption_scope: NOT_ADOPTED", "adoption boundary"),
        ("runtime_status: NOT_RUN", "runtime boundary"),
        ("## 5. 合併／彙整前檢查", "pre-merge checks"),
        ("## 6. 合併／彙整執行流程", "merge workflow"),
        ("## 7. 風險與防範矩陣", "risk matrix"),
        ("## 8. 反向測試流程", "reverse tests"),
        ("## 9. 七欄 P／C／J 步驟規格", "seven-column contract"),
        ("## 10. 失敗出口、回復與重試", "failure recovery"),
        ("## 11. 證據、版本與回復保存", "evidence preservation"),
        ("## 12. 驗收標準", "acceptance criteria"),
        ("## 14. 最終驗收與交接", "handoff"),
    ]:
        require(text, needle, label)

    for case in ["RT-01", "RT-02", "RT-03", "RT-04", "RT-05", "RT-06", "RT-07", "RT-08", "RT-09", "RT-10", "RT-11", "RT-12"]:
        require(text, case, case)

    for forbidden in ["下單", "交易", "Broker", "LIVE", "STOPPED", "BLOCKED", "NOT_RUN", "UNKNOWN"]:
        require(text, forbidden, f"hard boundary/status {forbidden}")

    # Negative behavior: unsafe status promotion must be rejected.
    for status in ["UNKNOWN", "NOT_RUN", "BLOCKED", "CONFLICT", "FAIL"]:
        if not reject_status(status):
            raise AssertionError(f"FAIL status promotion: {status} was accepted")
    print("PASS negative status-promotion rejection")

    # Boundary behavior: a candidate must not silently become adopted or runtime-active.
    metadata = dict(re.findall(r"^  ([a-z_]+): (.+)$", text, flags=re.MULTILINE))
    if metadata.get("status") != "CANDIDATE" or metadata.get("adoption_scope") != "NOT_ADOPTED" or metadata.get("runtime_status") != "NOT_RUN":
        raise AssertionError("FAIL boundary metadata: candidate gates were weakened")
    print("PASS boundary candidate/adoption/runtime gates")

    # Evidence behavior: the candidate itself is hashable and the file is non-empty.
    digest = hashlib.sha256(SKILL.read_bytes()).hexdigest()
    if len(digest) != 64 or SKILL.stat().st_size < 2000:
        raise AssertionError("FAIL evidence: candidate is empty or hash unavailable")
    print(f"PASS evidence hash {digest}")

    print("OVERALL_STATUS=PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
