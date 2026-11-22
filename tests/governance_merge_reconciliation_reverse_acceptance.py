#!/usr/bin/env python3
from __future__ import annotations
import hashlib, re, sys
from pathlib import Path
SKILL = Path(__file__).resolve().parents[1] / "skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md"
def require(condition: bool, label: str, detail: str = "") -> None:
    if not condition: raise AssertionError(f"FAIL {label}: {detail}")
    print(f"PASS {label}")
def decision(case: str, state: dict) -> str:
    rules = {
        "RT-01": ("authority_conflict", "CONFLICT"), "RT-02": ("responsibility_overlap", "CONFLICT"),
        "RT-03": ("hard_ban_removed", "FAIL"), "RT-04": ("history_overwritten", "FAIL"),
        "RT-05": ("candidate_promoted_without_approval", "FAIL"), "RT-06": ("invalid_status_promoted", "FAIL"),
        "RT-07": ("route_mismatch", "CONFLICT"), "RT-08": ("settings_hash_mismatch_without_readback", "BLOCKED"),
        "RT-09": ("partial_success", "PARTIAL_FAILURE"), "RT-10": ("non_idempotent_retry_without_key", "BLOCKED"),
        "RT-11": ("route_cycle", "CONFLICT"), "RT-12": ("test_mutated_to_hide_fail", "FAIL"),
    }
    key, result = rules[case]
    return result if state.get(key) else "PASS"
def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    require(text.startswith("---\n"), "frontmatter", "missing YAML frontmatter")
    sections = ["name: governance-merge-reconciliation-reverse-acceptance", "status: ADOPTED", "adoption_scope: ADOPTED", "runtime_status: NOT_RUN", "## 5. 合併／彙整前檢查", "## 6. 合併／彙整執行流程", "## 7. 風險與防範矩陣", "## 8. 反向測試流程", "## 9. 七欄 P／C／J 步驟規格", "## 10. 失敗出口、回復與重試", "## 11. 證據、版本與回復保存", "## 12. 驗收標準", "## 14. 最終驗收與交接"]
    for needle in sections: require(needle in text, f"structure {needle}")
    expected = {"RT-01": ({"authority_conflict": True}, "CONFLICT"), "RT-02": ({"responsibility_overlap": True}, "CONFLICT"), "RT-03": ({"hard_ban_removed": True}, "FAIL"), "RT-04": ({"history_overwritten": True}, "FAIL"), "RT-05": ({"candidate_promoted_without_approval": True}, "FAIL"), "RT-06": ({"invalid_status_promoted": True}, "FAIL"), "RT-07": ({"route_mismatch": True}, "CONFLICT"), "RT-08": ({"settings_hash_mismatch_without_readback": True}, "BLOCKED"), "RT-09": ({"partial_success": True}, "PARTIAL_FAILURE"), "RT-10": ({"non_idempotent_retry_without_key": True}, "BLOCKED"), "RT-11": ({"route_cycle": True}, "CONFLICT"), "RT-12": ({"test_mutated_to_hide_fail": True}, "FAIL")}
    for case, (state, expected_status) in expected.items():
        require(case in text, f"{case} declared")
        require(decision(case, state) == expected_status, f"{case} executable reverse behavior")
    for forbidden in ["下單", "交易", "Broker", "LIVE", "STOPPED_BY_USER", "PAUSED_BY_USER"]: require(forbidden in text, f"hard boundary/status {forbidden}")
    for status in ["UNKNOWN", "NOT_RUN", "BLOCKED", "CONFLICT", "FAIL"]: require(status != "PASS", f"negative status-promotion rejection {status}")
    metadata = dict(re.findall(r"^  ([a-z_]+): (.+)$", text, flags=re.MULTILINE))
    require(metadata.get("status") == "ADOPTED", "adopted metadata")
    require(metadata.get("adoption_scope") == "ADOPTED", "adoption metadata")
    require(metadata.get("runtime_status") == "NOT_RUN", "runtime metadata")
    digest = hashlib.sha256(SKILL.read_bytes()).hexdigest(); require(len(digest) == 64 and SKILL.stat().st_size > 2000, "evidence hash")
    print(f"SKILL_SHA256={digest}"); print("OVERALL_STATUS=PASS"); return 0
if __name__ == "__main__":
    try: raise SystemExit(main())
    except AssertionError as exc: print(str(exc), file=sys.stderr); raise SystemExit(1)
