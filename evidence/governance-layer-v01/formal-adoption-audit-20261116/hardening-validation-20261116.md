# Governance acceptance hardening v0.1.1 驗收摘要

## 範圍

本分支處理五項高優先級修正：驗收輸出隔離、失敗時非零結束碼、無 Git bundle 的明確阻塞、正式採用批准欄位，以及完整 Git 歷史 C3 掃描。

## 實跑結果

| 項目 | 實際結果 | 證據／限制 |
|---|---|---|
| Stage 1 inventory | PASS；21/21；ERROR_COUNT=0；Exit Code 0 | 預設輸出在 `out/acceptance/stage-01/`，未改寫追蹤 evidence |
| G3、G6、G7、G9 | PASS；各 Exit Code 0 | 預設輸出在 `out/acceptance/governance-layer-v01/` |
| G0–G9 | PASS；OVERALL=PASS；Exit Code 0 | 只代表本地候選驗收 |
| 獨立驗收 | PASS；OVERALL=PASS；Exit Code 0 | 獨立 C1–C16 讀回通過 |
| C1–C16 | PASS；16/16；C3 命中 0；Exit Code 0 | 本輪工作樹實跑 |
| 負向 G3 突變 | PASS；故意改壞 K51 映射後 Exit Code 1 | 恢復原始映射後再驗收 |
| 無 Git bundle Stage 1 | PASS；Exit Code 0 | commit 欄位為 `NOT_RUN`，不丟 traceback |
| 無 Git bundle G9 | BLOCKED；Exit Code 2 | 明確說明生命週期驗收需要 Git metadata |
| Git 歷史 C3 | FAIL；掃描 270 個 commit、1,962 筆命中 | 歷史中已有本機路徑／範例內容；保護歷史原則下未重寫歷史 |

## 正式採用欄位

正式採用紀錄已補上批准人 `MIKO`、批准日期 `2026-11-16（Asia/Taipei）` 與僅限本地 `skills/` 路徑的批准範圍。Runtime、外部 Connector、遠端 Release、正式 Tag 與 Merge 仍為 `NOT_RUN`。

## 判定

本分支的現行工作樹與本地驗收 hardening 已通過；完整 Git 歷史安全仍為 FAIL，不能宣稱公開歷史已清理。解除條件是由 MIKO 決定歷史封存／公開範圍與是否允許另案歷史清理；在此之前不得標記歷史 C3 PASS。
