# P0 外圈架構候選規格

- 狀態：`PROPOSED`／`NOT_ADOPTED`
- 來源：MIKO 提供的 Pasted_content_27.txt；本地 Manus 候選工作區
- 正本基線：MIKO `v1.2.72`
- 遠端 GitHub：`icashkin-cmyk/miko-manus-governance`
- Runtime：`NOT_RUN`

## 外圈五層

| 層 | 唯一主要責任 | 不應負責 |
|---|---|---|
| MIKO | 最終決策、授權、重大取捨與最終驗收 | 不必親自執行每個工具操作 |
| GitHub | 正式規格、版本、知識、程式碼與變更權威 | 不負責理解需求或實際執行任務 |
| Manus | 唯一主要 AI 工作平台；理解、治理檢查、路由、執行、測試與交付 | 不得自行擴權、升格正式規則或冒充獨立驗收 |
| Tools & Integrations | Manus 所調用的外部工具、API、檔案與應用程式 | 不建立第二個治理核心或正式版本權威 |
| Evidence & Lifecycle | 保存授權、版本、命令、結果、測試、讀回、封存與回復紀錄 | 不因保存證據而取得正式規則權威 |

## 五條外圈不變量

1. `Single Decision Root`：MIKO 是最終決策與授權者。
2. `Single Canonical Repository`：本專案 GitHub repository 是本架構的正式候選基線。
3. `Single Primary AI Platform`：Manus 是唯一主要 AI 工作平台。
4. `Separation of Authority and Execution`：執行權不等於正式規則修改權或採用權。
5. `Evidence-based Closure`：沒有實際測試、證據及必要讀回，不得宣稱整體完成。

## 邊界

本文件只驗收外圈責任與承接位置；不宣稱 Router、K01–K50、各領域 Skill 或工具 Runtime 已啟用。內圈模組契約放在 `modules/`，其存在只代表候選規格已建立，不代表正式採用或 Runtime 生效。
