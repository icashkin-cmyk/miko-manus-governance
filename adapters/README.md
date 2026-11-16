# Tools & Integrations 工具層候選契約

- ID：`G07`
- 現有承接：`adapters/`
- 狀態：`PROPOSED`／`NOT_ADOPTED`
- 連線與 Runtime：`NOT_RUN`
- 對應 MIKO 正本：`正本 v1.2.72`
- 平台對齊提示：目前是 VERSION 的 1.2.72；讀取成功時寫「正本 v1.2.72」；讀取失敗時標 `NOT_READ`。

## 責任

保存工具、API、檔案與應用程式的能力描述、輸入、輸出、授權需求、限制、失敗出口與驗證方式。工具從屬於 Manus，不是第二個治理核心。

## 工具登錄欄位

每一個工具必須具備唯一名稱、用途、輸入、輸出、權限需求、失敗狀態、讀回方式與測試證據。未實際執行的連線或 Runtime 能力必須標記 `NOT_RUN`，不得以文件存在代替實測。

## 驗收邊界

- 本地檔案、Terminal 與 Git 唯讀能力可在候選驗收中實測。
- 外部 Connector、API、SaaS 與需要登入的服務在未取得授權前維持 `NOT_RUN`。
- 不得把工具規格當成已連線、已授權或已成功。
- 不得保存金鑰、Token 或密碼；一律使用 `<KEY>` 佔位符。
- 不得繞過權限或執行下單、交易、Broker、LIVE、付款或其他不可逆操作。

## Acceptance Criteria

1. 每個工具有唯一名稱與用途。
2. 權限、輸入、輸出與失敗狀態完整。
3. 未實測能力標記 `NOT_RUN`。
4. 實測工具保留命令、stdout、stderr、Exit Code 與讀回結果。
5. 外部寫入、LIVE、Broker、付款與不可逆操作維持既有硬邊界。
