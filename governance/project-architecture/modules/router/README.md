# Router 模組候選契約

- ID：`G03`
- 狀態：`PROPOSED`／`NOT_ADOPTED`
- Runtime：`NOT_RUN`

## 責任

依任務目的、觸發條件、權限、依賴與狀態選擇適用的 Knowledge Card、Skill 與工具；輸出可追溯的路由決定與未選用理由。

## 不負責

Router 不執行 Skill、不修改正式規則、不授予權限、不取代 MIKO 決策、不把檔案存在當成可用能力。

## Acceptance Criteria

1. 每個輸入最多產生一個主路由，衝突時標 `CONFLICT`。
2. 路由結果包含來源、版本、觸發與禁止事項。
3. 未驗證 Runtime 時不得標示已載入。
4. 負向測試能抓出錯誤路由與跨邊界調用。
