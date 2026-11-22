# 治理-合併彙整衝突與反向驗收｜候選驗收報告

## 1. 結果

已建立候選 Skill：`governance-merge-reconciliation-reverse-acceptance`。

- Skill 狀態：`CANDIDATE`
- 採用狀態：`NOT_ADOPTED`
- Runtime 狀態：`NOT_RUN`
- 本地候選正文：`skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md`
- Skill 正文：224 行、13,798 bytes
- 目標：處理多份規則、Skill、Project Instructions、治理文件或版本的合併／彙整／同步／升級風險，並執行合併後反向驗收。

## 2. 已納入內容

- 合併／彙整前來源盤點、權威排序、範圍凍結與雙向 mapping。
- 規則遺漏、語意衝突、責任重疊、歷史覆蓋、權限放寬、候選誤升格、假 PASS、Router／Runtime 分叉、部分成功、不可回復與無限重試風險矩陣。
- 12 項反向測試：權威衝突、責任重疊、硬禁止遺漏、舊版覆蓋、狀態升格、UNKNOWN／NOT_RUN／BLOCKED 假 PASS、Router 不一致、Settings 未讀回、部分成功、重複執行、循環路由與測試器規避。
- P／C／J 七欄步驟規格。
- `NOT_READ`、`UNKNOWN`、`NOT_RUN`、`BLOCKED`、`CONFLICT`、`FAIL`、`REWORK_REQUIRED` 失敗出口。
- 快照、Diff、SHA-256、原始 stdout／stderr、Exit Code、回復演練與有限重試規則。
- 下單、交易、Broker、LIVE、台指期硬禁止；台指期固定 `STOPPED_BY_USER`，回測固定 `PAUSED_BY_USER`。
- 明確聲明本 Skill 不負責正式採用、Project Settings 寫入、Push、Merge、Release 或 Runtime 啟用。

## 3. 測試結果

| 測試 | 命令／證據 | 結果 |
|---|---|---|
| Skill 結構驗證 | `python3 /home/ubuntu/skills/skill-creator/scripts/quick_validate.py --path skills/governance-merge-reconciliation-reverse-acceptance` | PASS；Exit Code 0 |
| 自訂行為驗收 | `python3 tests/governance_merge_reconciliation_reverse_acceptance.py` | 36 PASS、0 FAIL；Exit Code 0 |
| 反向案例覆蓋 | `RT-01` 至 `RT-12` | 12/12 PASS |
| 負向狀態升格 | UNKNOWN／NOT_RUN／BLOCKED／CONFLICT／FAIL 不得升格 PASS | PASS |
| 邊界狀態 | CANDIDATE／NOT_ADOPTED／NOT_RUN 保持未升格 | PASS |
| Diff | `candidate.diff` | 已保存 |
| SHA-256 | `sha256.txt` | 已保存 |

## 4. 修正歷史

第一輪測試發現正文未明確列出「下單」硬禁止；已補入硬禁止矩陣，重跑後通過。

第二輪測試發現正文未明確包含 `STOPPED_BY_USER`；已補入台指期／回測固定狀態，重跑後通過。

原始初始化模板未被當成正式內容覆蓋，已保存於：
`evidence/merge-reconciliation-reverse-acceptance-20261123/pre-upgrade-snapshot/SKILL.md`

## 5. 證據索引

- 候選 Skill：`skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md`
- 自訂驗收器：`tests/governance_merge_reconciliation_reverse_acceptance.py`
- 初始模板快照：`pre-upgrade-snapshot/SKILL.md`
- 初始模板 Hash：`pre-upgrade-snapshot-sha256.txt`
- 前後 Hash：`sha256.txt`
- 完整 Diff：`candidate.diff`
- 結構驗收輸出：`quick_validate-final.txt`
- 行為驗收輸出：`behavior_acceptance-final.txt`
- Exit Code：`test-exit-codes-final.txt`
- 驗收摘要：`validation-summary.txt`

候選 Skill SHA-256：
`5e9c256343660c8609543d093f1bac9a4e8a11532ac5ac5a454dfdaaa67a7860`

## 6. 未驗證與限制

- `Project Settings` 未讀回，未寫入任何目標專案設定。
- Manus Runtime 載入、Skill 觸發、Router 實際路由與 Runtime 行為未執行，維持 `NOT_RUN`／`UNKNOWN`。
- 未執行外部 Connector、Push、Merge、Release 或正式 Tag。
- 未進行真正獨立稽核；本輪是 Manus 自我驗收，不能標記 `INDEPENDENT_AUDIT`。
- 本次未修改既有 Skill；工作樹其他未提交變更未被處理。

## 7. 任務四態

`完成但有疑慮`

理由：本地候選 Skill 與可重跑測試已完成且通過，但正式採用、Project Settings、Runtime 與獨立驗收尚未完成，不能宣稱正式上線。

## 8. 下一步

1. 如需正式採用，先由 `independent-audit` 或指定獨立驗收者冷讀並重跑反向測試。
2. 核對版本、分支、Project Settings 與適用治理紀錄。
3. 取得必要授權後，才可評估寫入、Push、Merge、Release 或 Runtime 啟用；每一步都需遠端／Runtime 讀回證據。
