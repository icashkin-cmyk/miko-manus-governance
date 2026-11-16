# G6–G9 驗收流程 Skill 化驗收紀錄

- Skill：`miko-governance-layer-acceptance`
- 路徑：`knowledge-cards/proposals/skills/miko-governance-layer-acceptance/SKILL.md`
- 狀態：`PROPOSED`；尚未正式採用、尚未安裝、尚未 Runtime 生效。
- 範圍：完整 G0–G9，而非只記錄 G6–G9。
- Skill validator：`PASS`，209 行，必要契約 21 項全數存在。
- G6：`PASS`
- G7：`PASS`
- G8：`PASS`
- G9：`PASS`（本地候選生命週期與回復演練；正式遠端發布仍 `NOT_RUN`）
- G0–G9：`PASS`
- INDEPENDENT_AUDITOR：`PASS`
- C1–C16：`16/16 PASS`
- C3 命中：`0`

## 責任分離

`IMPLEMENTER` 負責候選 Skill 與測試入口；`TESTER` 實際執行 G6–G9 與完整回歸；`INDEPENDENT_AUDITOR` 重新讀取工作樹並重跑獨立驗收。Skill 不接受文件內自述作為唯一證據。

## 邊界

External Connector、Manus Runtime、正式 Tag、Release、Merge、正式採用與 Runtime Functional Test 未被本輪離線候選驗收冒充為已完成，均依實際狀態保留 `NOT_RUN` 或未授權邊界。

## 證據

原始 stdout、stderr、Exit Code、Skill validator、獨立驗收及 C1–C16 輸出均保存於本目錄。Skill 本文與證據檔另以 `acceptance-skill-integrity.sha256` 保存 Hash。
