# Tools & Integrations 模組候選契約

- ID：`G07`
- 現有承接：`adapters/`
- 狀態：`PROPOSED`／`NOT_ADOPTED`
- 連線與 Runtime：`NOT_RUN`

## 責任

保存工具、API、檔案與應用程式的能力描述、輸入輸出、授權需求、限制、失敗出口與驗證方式。工具從屬於 Manus，不是第二個治理核心。

## 禁止

不得把工具規格當成已連線、已授權或已成功；不得保存金鑰、Token 或密碼；不得繞過權限或執行硬禁止操作。

## Acceptance Criteria

1. 每個工具有唯一名稱與用途。
2. 權限、輸入、輸出與失敗狀態完整。
3. 未實測標 `NOT_RUN`。
4. 外部寫入、LIVE、Broker、付款與不可逆操作維持既有硬邊界。
