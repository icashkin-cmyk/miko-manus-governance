---
name: miko-governance-layer-acceptance
version: 0.1.0
status: ADOPTED
description: 執行 MIKO Manus 治理架構 G0–G9 的全生命週期驗收，包含基線、架構、治理核心、Router、Knowledge Cards、Skill 盤點、Tools Contract、端到端 Dry-run、獨立驗收與候選生命週期回復演練。用於治理架構候選交付前的可重跑驗收；不得將離線候選 PASS 誤報為正式發布、正式採用或 Manus Runtime 已啟用。
---

# MIKO Governance Layer Acceptance v0.1.0

## 1. Skill 身分與範圍

- 狀態：`ADOPTED`；本檔是本地正式採用 Skill，不代表 Manus Runtime 已啟用。
- 適用對象：MIKO Manus 治理架構候選 repository。
- 驗收範圍：G0、G1、G2、G3、G4、G5、G6、G7、G8、G9。
- 主要角色：
  - `IMPLEMENTER`：建立或修正候選內容與測試。
  - `TESTER`：依指令實際執行測試並保存 stdout、stderr、Exit Code。
  - `INDEPENDENT_AUDITOR`：重新讀取工作樹、重新執行必要測試，不接受製作者的 PASS 宣稱。
- 執行原則：先完成前一 Gate 且保留證據，才可進入下一 Gate；任一 Gate `FAIL`、`UNKNOWN`、`NOT_RUN` 或 `BLOCKED` 時，不得宣稱整體完成。

## 2. 何時使用

在以下情況載入本 Skill：

1. 使用者要求驗收 MIKO Manus 治理架構、G0–G9、完整架構、Tools Contract、E2E、獨立驗收或生命週期。
2. 使用者要求確認候選架構是否可交付、可推送、可發布或可進入下一 Gate。
3. 使用者要求將驗收流程保存成可重跑 Skill。
4. 使用者要求檢查自驗與獨立驗收是否真正分離。

不在以下情況自行啟用：只做一般文件閱讀、只查詢單一檔案、正式 GitHub Merge／Release／Tag、Runtime 啟用或需要外部授權的 Connector 操作；後者必須另外取得精確授權。

## 3. 硬邊界

- 不修改原始 MIKO repository。
- 不把 `PROPOSED` 候選內容當成正式採用規則。
- 不以文件完整代替 Runtime 實測。
- 不以模擬 Connector 代替實際外部授權測試。
- 不執行 Push、Merge、正式 Tag、Release、正式採用或 Runtime 啟用，除非使用者另行明確授權且該步驟已完成對應驗收。
- 金鑰、密碼、Token 一律不得索取、複述或保存，使用 `<KEY>`。
- `NOT_RUN`、`NOT_READ`、`UNKNOWN`、`BLOCKED` 不得轉成 `PASS`。
- G9 本地候選生命週期演練與正式遠端發布必須分開記錄。

## 4. 共通驗收紀錄格式

每個子項目至少保存以下欄位：

| 欄位 | 要求 |
|---|---|
| Gate ID／Test ID | 唯一識別，例如 `G6.09` |
| 測試對象 | 檔案、模組、工具或工作流 |
| Repository／Branch／Commit | 實際驗收基線 |
| 前置條件 | 執行前必須成立的條件 |
| 輸入 | 原始輸入或測試資料 |
| 執行命令 | 完整可複製命令 |
| 預期結果／實際結果 | 不得只寫摘要 |
| stdout／stderr | 原始輸出檔位置 |
| Exit Code | 實際整數退出碼 |
| 證據位置 | 原始輸出及檔案位置 |
| SHA-256 | 輸出與重要產物 Hash |
| Tester／Auditor | 實際角色與執行者 |
| Status | `PASS`／`FAIL`／`NOT_RUN`／`NOT_READ`／`UNKNOWN`／`BLOCKED` |
| 缺陷／回復 | 失敗影響與可執行回復方法 |
| 日期時間 | 實際執行時間，使用 Asia/Taipei |

沒有實際執行命令、輸出與 Exit Code，只能標記 `NOT_RUN`。

## 5. 共同執行順序

### 5.1 開工基線

1. 讀取固定 commit 的 `VERSION`、`README.md`、`CHANGELOG.md`、`MANUS_VERSION`。
2. 確認 branch、remote identity、工作樹與目標 repository。
3. 確認完整工作清單、Gate 總數與非範圍。
4. 保存基線 Hash；不以舊報告的 PASS 代替本輪讀回。

### 5.2 測試與閉環

1. `IMPLEMENTER` 建立或修正候選內容。
2. `TESTER` 執行正向、負向、邊界、異常、回歸與必要 Mutation Testing。
3. 失敗時只修一個可驗收目標，保存 diff 與失敗證據後重測。
4. `INDEPENDENT_AUDITOR` 冷讀候選工作樹並重新執行必要測試。
5. 全部必要 AC 通過後保存報告、Hash、交接與下一 Gate 條件。

## 6. G0–G5 基線驗收

### G0：Repository 身分與版本基線

檢查 repository、branch、HEAD、`VERSION`、`MANUS_VERSION`、README、CHANGELOG、remote identity 與工作樹。所有身份資料一致才可 `PASS`。

### G1：外層架構

確認外圈架構、唯一決策根、唯一 canonical repository、AI 平台責任、權限與 Evidence 層，以及 G01–G10 模組映射均存在且責任不重疊。

### G2：治理核心

確認 `miko-core` 存在並包含閉環、治理、權限、`UNKNOWN`、`NOT_RUN`、獨立驗收與回復規則。不得只檢查標題存在。

### G3：Router

驗證 Router 只選擇、不執行 Skill、不授予權限、不修改正本。至少測試：正向命中、無命中 `NO_ROUTE`、多重命中 `CONFLICT`、錯誤輸入、Mutation Testing 與獨立重跑。Runtime 載入另標 `NOT_RUN`。

### G4：Knowledge Cards

盤點 K01–K50 穩定識別項，保留原始卡、候選卡、來源、版本、差異與 Hash。若有名稱衝突，必須先裁決並保留沿革；不得靜默覆寫。K51 等延伸卡須單獨記錄，不得冒充 K01–K50。

### G5：Skills Inventory

建立完整 Skill 清單與總數，逐筆核對 canonical 路徑、來源快照、觸發條件、測試入口與證據。靜態盤點 PASS 不等於 Runtime 載入 PASS；Runtime 未實測標 `UNKNOWN` 或 `NOT_RUN`。

## 7. G6：Tools Contract 離線驗收

先完成不需外部授權的離線測試。逐項驗收：

| ID | 驗收內容 |
|---|---|
| G6.1 | Tool Registry 清冊與唯一識別 |
| G6.2 | 名稱、用途、禁止用途與權限邊界 |
| G6.3 | Input Contract、型別與必填條件 |
| G6.4 | Output Contract、錯誤格式與回傳欄位 |
| G6.5 | Dependency 與前置條件 |
| G6.6 | 工具存在與可用性檢查 |
| G6.7 | 授權檢查與未授權拒絕 |
| G6.8 | 正常輸入 Positive Test |
| G6.9 | 錯誤輸入與缺參數 Negative Test |
| G6.10 | 空值、超限、錯誤型別 Boundary Test |
| G6.11 | 逾時、服務錯誤與中途失敗 |
| G6.12 | 安全降級、停止條件與替代工具失敗 |
| G6.13 | stdout、stderr、Exit Code、版本與 Hash |
| G6.14 | Gate Review：未完成項不得宣稱 PASS |

至少執行：工具存在且正常、工具不存在、工具不可用、未授權、拒絕授權、缺參數、型別錯誤、超限、逾時、錯誤格式、中途失敗、降級失敗與輸出不符合需求。External Connector 與 Manus Runtime 保持 `NOT_RUN`，不得模擬成已連通。

## 8. G7：End-to-End Workflow Dry-run

G7 不得只測 Router 或單一 Skill，必須保存整條鏈：需求辨識 → 任務分類 → Router → Knowledge Card → Skill → Tool → 權限 → 執行 → 整合 → 品質檢查 → 錯誤處理 → 交付。

至少覆蓋：文字需求→文件整理、原始資料→分析→報告、研究需求→來源整理→結論、影片→內容分析→摘要、圖片→辨識→編輯需求、CSV→清理→分析→輸出、程式需求→修改→測試、多 Skill 協作、多 Tool 串接、多 Skill 同時命中、無適用 Skill、工具不可用、未授權、中途失敗與需求變更。

每個工作流保存原始輸入、辨識結果、路由、卡片、Skill、Tool、授權、每階段輸出、錯誤、最終成品、品質結果與 Exit Code。離線 E2E PASS 不代表 Runtime 或外部 Connector 已接通。

## 9. G8：Independent Acceptance

G8 必須在 G7 證據封存後進行，且由 `INDEPENDENT_AUDITOR`：

1. 重新讀取候選工作樹與 commit。
2. 不直接接受 Tester 的 PASS。
3. 自行核對原始 stdout、stderr、Exit Code 與 Hash。
4. 重新執行 G6、G7 必要測試。
5. 執行正向、負向、邊界、整合、E2E 與 Mutation Testing。
6. 故意移除欄位、改錯 Router、取消授權、讓工具失效及製造衝突，確認測試能偵測。
7. 檢查版本矛盾、路由矛盾、權限失效、狀態誤報、舊版覆蓋與回復缺陷。
8. 產出獨立報告，明確列出與 Tester 的差異。

G8 PASS 的必要條件是 G6、G7 結果可獨立重現，所有未完成項已揭露，且沒有重大未解決缺陷。

## 10. G9：候選生命週期與正式發布分離

### 10.1 可在本地離線完成的候選驗收

- 發布前 baseline、範圍、HEAD、工作樹與 Hash。
- 候選 archive 建立與解壓讀回。
- 隔離副本 recovery drill。
- 隔離 candidate tag 流程。
- 遠端 identity 讀取，不代表已發布。

### 10.2 必須另行授權的正式操作

以下各項分開驗收，不得合併成一個 PASS：正式 Git Tag、GitHub Release、Remote read-back、Merge、正式採用決策、Manus Runtime integration／load／read-back／functional test，以及正式 rollback 與版本一致性。

未取得授權或未實測時，分別標 `NOT_AUTHORIZED`、`NOT_RUN` 或 `UNKNOWN`。候選生命週期 PASS 不代表正式發布、正式採用或 Runtime PASS。

## 11. 建議重跑命令

在候選 repository 根目錄執行，所有命令均須把原始輸出保存至 evidence：

```bash
python3 -I -B tests/governance_layer_acceptance_v01.py
python3 -I -B tests/governance_layer_independent_audit_v01.py
python3 -I -B tests/g3_router_acceptance.py
python3 -I -B tests/g3_router_independent_audit.py
python3 -I -B tests/g6_tools_acceptance.py
python3 -I -B tests/g7_e2e_acceptance.py
python3 -I -B tests/g8_independent_acceptance.py
python3 -I -B tests/g9_lifecycle_acceptance.py
python3 -I -B tests/check_repo.py
```

每次變更後必須重新執行受影響 Gate、獨立驗收與 C1–C16。不要只讀舊 JSON 或沿用舊 PASS。

## 12. 交付判定

只有同時符合以下條件，才能將「本地候選 G0–G9 驗收」標記 `PASS`：

1. G0–G9 每一 Gate 有實際執行證據。
2. G8 獨立驗收不是只讀 Tester 摘要。
3. C1–C16 實際 Exit Code 為 0，且 C3 命中為 0。
4. 所有必要 stdout、stderr、Exit Code、版本、commit 與 SHA-256 已保存。
5. External Connector、Runtime、Release、Merge 與採用狀態未被誤報。
6. 工作樹與最新 commit 已讀回核對。
7. 未完成、未知、阻塞與回復方式均已列出。

此 `PASS` 只代表本地候選驗收合格；不代表正式採用、遠端發布、合併、Runtime 生效或外部工具已授權。

## 13. 證據與維護

- 建議證據根目錄：`evidence/governance-layer-v01/`。
- G6：`g6/`；G7：`g7/`；G8：`g8/`；G9：`g9/`。
- 原始測試器位於候選 repository 的 `tests/`，本 Skill 不複製第二套驗收邏輯。
- 每次升級採累積式演進：保留舊版、diff、來源、日期、commit、SHA-256 與回復方式。
- 若測試器與本 Skill 規則衝突，先標記 `CONFLICT`，不得自行改名繞過；由治理裁決後再修正並重跑。
- 本 Skill 的正式採用狀態為 `ADOPTED`；安裝與 Runtime 載入狀態目前為 `NOT_RUN`，除非另有實際證據。
