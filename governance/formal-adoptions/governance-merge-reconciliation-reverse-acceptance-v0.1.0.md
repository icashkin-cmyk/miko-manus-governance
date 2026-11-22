# governance-merge-reconciliation-reverse-acceptance v0.1.0 正式採用紀錄

- 採用狀態：`ADOPTED`
- 採用範圍：目前 repository 的本地正式 `skills/` 路徑
- 正式 Skill：`skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md`
- 候選來源：`89bac619463fc7576cbfe017179e7e6adb90768a`（候選分支 `manus/batch-b-seven-column-pcj-candidate-20261117`）
- 採用版本：`v0.1.0`
- 批准人：`MIKO`
- 批准日期：`2026-11-23`（Asia/Taipei）
- 批准範圍：僅本地正式 `skills/` 路徑；不包含 Project Settings 寫入、Runtime 啟用、外部 Connector、Merge、Release 或正式 Tag
- 本地採用 commit：由本次採用 Commit 建立後以 Git 讀回確認
- Runtime：`NOT_RUN`
- Project Settings：`NOT_RUN`
- Push：本次採用 Commit 將推送至目前候選分支；不推送 `main`
- Merge／Release／正式 Tag：`NOT_RUN`

## 採用前提與驗收結果

1. 候選 Skill 已完成 YAML frontmatter、結構、RT-01～RT-12 可重播反向行為測試、硬禁止與狀態升格拒絕測試。
2. `quick_validate.py`、反向行為測試、G9 本地生命週期驗收與 mapping completeness check 均已取得 Exit Code 0；原始輸出保留於 `evidence/merge-reconciliation-reverse-acceptance-20261123/`。
3. 第二次獨立冷讀結果為 `PASS_WITH_GAPS`：AC-01～AC-05、AC-08 為 `PASS_WITH_GAPS`，AC-06 為 `PASS`，AC-07 為 `NOT_RUN`；獨立性已確認。採用範圍刻意限定為本地 `skills/`，因此 Runtime／Project Settings 未驗證不被升格為通過，也不阻止本地採用。
4. 來源凍結、雙向 mapping、候選 Diff、SHA-256、回復證據與遠端候選分支讀回證據均保留；尚未完成的追溯細化與 Runtime 驗證維持未決，不得在後續報告中寫成完整 PASS。
5. 正式採用不等於遠端 Merge、Release、正式 Tag、Project Settings 儲存或 Runtime 生效。

## 證據

- 採用前快照：`evidence/merge-reconciliation-reverse-acceptance-20261123/pre-adoption-snapshot/SKILL.md`
- 採用前 SHA-256：`evidence/merge-reconciliation-reverse-acceptance-20261123/pre-adoption-sha256.txt`
- 採用後 SHA-256：`evidence/merge-reconciliation-reverse-acceptance-20261123/post-adoption-sha256.txt`
- 採用 Diff：`evidence/merge-reconciliation-reverse-acceptance-20261123/adoption.diff`
- 行為驗收：`evidence/merge-reconciliation-reverse-acceptance-20261123/behavior_acceptance-post-repair.txt`
- G9 本地驗收：`evidence/merge-reconciliation-reverse-acceptance-20261123/g9-post-repair.txt`
- Runtime 阻塞紀錄：`evidence/merge-reconciliation-reverse-acceptance-20261123/runtime-readback-blocked-20261123.md`

## 回復方式

若本地採用需要回復，先保存當前採用 Commit 與工作樹狀態，再將 `skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md` 回復至採用前快照，重新執行 quick validation、反向行為測試、mapping check 與 G9；不得刪除本採用紀錄、採用前快照、Diff 或原始驗收證據。回復前後均須記錄命令、Exit Code、SHA-256 與 Git HEAD。

## 未決事項

- `Project Settings` 完整內容、Manus Runtime 觸發、Router 命中與行為讀回：`NOT_RUN`。
- Merge、Release、正式 Tag 與正式遠端發布：`NOT_RUN`。
- 獨立冷讀指出的逐檔完整版本／Commit／SHA-256 索引、逐原子條款 mapping 與更完整測試矩陣仍屬 `PASS_WITH_GAPS`，不得宣稱已完全消除。
