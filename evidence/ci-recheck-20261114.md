# CI Recheck｜未通過證據

- 來源：使用者提供的 `Pasted_content_19.txt`
- 測試入口：`python3 -I -B tests/check_repo.py`
- 實際結果：`15/16 PASS`
- Exit Code：`1`
- 整體判定：`FAIL`
- 失敗項目：`C3`
- C3 問題：公開檔案掃描命中本機路徑／私人關鍵字規則；附件列出的命中位置包含 `knowledge-cards/proposals/.../audit-packet/ledger/` 下的 `entries.json` 與 `err.md`。
- C1～C2、C4～C16：附件顯示為 PASS，但不能抵銷 C3 FAIL。

## 對目前 Draft PR 的影響

1. 目前 Draft PR 不得標示為整體 PASS。
2. 目前 Stage 1／Stage 2 的本地靜態子檢查，只能標示為局部檢查；不足以取代完整 `check_repo.py`。
3. Stage 2 依賴 Stage 1，應維持 `NOT_READY`。
4. 下一輪必須先重現 C3、清理或隔離不應公開的資料，重新執行完整 C1～C16，並由獨立驗收者重新讀取與驗證。
5. 未取得新的完整實際證據前，狀態維持 `REVISE`，不得標成 `COMPLETE`、`ADOPT` 或 `RUNTIME`。
