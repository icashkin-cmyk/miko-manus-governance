---
name: miko-governance-layer-acceptance
description: 執行 MIKO Manus 治理架構 G0–G9 的全生命週期驗收，包含基線、架構、治理核心、Router、Knowledge Cards、Skill 盤點、Tools Contract、端到端 Dry-run、獨立驗收與候選生命週期回復演練。用於治理架構候選交付前的可重跑驗收；不得將離線候選 PASS 誤報為正式發布、正式採用或 Manus Runtime 已啟用。 本候選補上統一七欄與 P／C／J 驗收責任；不代表正式採用或 Runtime 生效。
metadata:
  version: 0.1.1-cumulative-candidate
  previous_version: 0.1.0
  status: CANDIDATE
  adoption_scope: NOT_ADOPTED
  runtime_status: NOT_RUN
  source_commit: a940f2407ca561e8f516bdf8d4d26d6525674c9f
  historical_reference: false
---

# 治理-G0至G9生命週期驗收

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

確認 `manus-core` 存在並包含閉環、治理、權限、`UNKNOWN`、`NOT_RUN`、獨立驗收與回復規則。不得只檢查標題存在。

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

## Batch B 格式與責任補強（候選升級）

> 本區是候選版新增內容；原有正文保留。`P` 是可重播程式步驟，`C` 是固定檢查步驟，`J` 是需保存判斷依據的判斷步驟。

### 責任邊界

- 角色：`GATE_ACCEPTANCE_COORDINATOR`。
- 產出：G0–G9 Gate 結果、原始輸出、Exit Code、Hash 與交接報告。
- 不產出／不執行：不取代 INDEPENDENT_AUDITOR，不自行正式採用，不啟用 Runtime。
- `final_integrator`：未由上游明確指定時標 `UNKNOWN`，不得自行補造。
- `runtime_status`：`NOT_RUN`；本候選不代表正式採用。

### 七欄流程／Gate 表

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| GATE-01 | P | 候選驗收開始 | 保存 repository、branch、HEAD、VERSION、README、CHANGELOG 與 remote identity | 只讀舊報告代替本輪讀回 | 基線命令、stdout、stderr、Exit Code、Hash | 身份不一致標 FAIL |
| GATE-02 | C | G0–G5 測試完成 | 核對架構、治理核心、Router、Knowledge Cards 與 Skill inventory | 把靜態盤點當 Runtime PASS | 逐 Gate 矩陣與缺陷清單 | 任一 Gate 未完成不得前進 |
| GATE-03 | P | G6 工具驗收開始 | 執行工具存在、拒絕授權、錯誤輸入、邊界與失敗測試 | 用模擬 Connector 冒充授權成功 | 命令、輸出、Exit Code、Hash | 測試失敗保存證據並回流 |
| GATE-04 | C | G7 E2E 完成 | 核對需求→Router→Card→Skill→Tool→權限→輸出完整鏈 | 只測單一 Skill 或只看最終輸出 | 端到端輸入、路由、輸出與錯誤證據 | 鏈中任一段缺證據標 FAIL |
| GATE-05 | C | G8 獨立驗收開始 | 由獨立驗收者冷讀並重跑必要測試 | 接受 Tester 自述 PASS | Independent report、差異、重跑輸出 | 獨立性不足標 BLOCKED |
| GATE-06 | J | G9 生命週期驗收完成 | 分開判定候選回復、遠端讀回、正式發布、採用與 Runtime | 把候選 PASS 當正式採用或 Runtime 生效 | 生命週期矩陣與狀態聲明 | 未授權或未實測標 NOT_RUN／UNKNOWN |

### 候選驗收條件

- expected：每個必要步驟都有輸入、操作、禁止事項、證據與失敗出口。
- forbidden：把 `UNKNOWN`、`NOT_RUN`、`BLOCKED` 或 ACK 升格為 `PASS`。
- 相近反例：只通過格式檢查但未執行行為測試；只由製作者自評；未指定 writer 或驗收者卻宣稱完成。
- AC-BATCH-B-01：七欄表存在且每欄有實質內容。
- AC-BATCH-B-02：每列類型只使用 `P`、`C` 或 `J`。
- AC-BATCH-B-03：P 步有可重播命令；C／J 步有固定判定與證據。
- AC-BATCH-B-04：原有功能與限制可由原始快照、diff 與回歸測試追溯。
- AC-BATCH-B-05：未正式採用、未啟用 Runtime 與未執行外部 Connector 均明確標示。

## 1. 問問題｜Batch B 相容性驗收

確認本候選版本保留原始責任，新增七欄表、P／C／J 類型、唯一 writer、驗收者與 final integrator；未知資料不得補造。

## 2. 解決｜Batch B 相容性驗收

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| FORMAT-01 | C | 候選 Skill 建立後 | 核對 frontmatter、H1、四節、七欄表與 P／C／J 標型 | 只看檔案存在就宣稱合格 | quick_validate、skill_lint、stdout、stderr、Exit Code | 任一格式失敗標 FAIL，停止後續 Gate |
| FORMAT-02 | P | 需要保存候選證據 | 執行 `sha256sum <candidate-file>` 並保存輸出 | 只看檔名或大小代替 Hash | 命令、stdout、stderr、Exit Code、SHA-256 | 命令失敗標 BLOCKED，保留候選版本 |
| FORMAT-03 | C | 格式檢查通過 | 核對角色、writer、驗收者、final integrator 與禁止事項 | 自行補造未讀責任人或授權 | 責任矩陣與未知清單 | 責任不明標 UNKNOWN 或 BLOCKED |
| FORMAT-04 | J | 進入行為驗收前 | 判定本 Skill 的正向、負向、邊界與回歸題目 | 把格式 PASS 當行為 PASS | 測題表、判定理由與狀態 | 缺題目或證據標 NOT_RUN |

## 3. 後設｜Batch B 相容性驗收

最強反例：格式工具通過，但原有功能、禁止事項或失敗出口被刪除；候選版必須以原始快照、逐行 diff 與回歸測試反證。

## 4. 檢查｜Batch B 相容性驗收

- expected：七欄表每欄有內容；P／C／J 類型正確；P 步有可重播命令；原有功能可追溯。
- forbidden：把 `UNKNOWN`、`NOT_RUN`、`BLOCKED` 或 ACK 升格為 `PASS`。
- 相近反例：只跑 lint、不跑行為題；只由製作者自評；未指定 writer 卻宣稱完成。
- AC-BATCH-B-01：五個候選 Skill 的格式檢查 Exit Code 均為 0。
- AC-BATCH-B-02：五個候選 Skill 的必要正向、負向、邊界與回歸題均有結果。
- AC-BATCH-B-03：原始版本、diff、Hash 與回復路徑均可讀。
- AC-BATCH-B-04：正式採用、Runtime、外部 Connector、Push 與 Merge 狀態分開記錄。

## 累積式優化｜責任邊界、限制與衝突路由 2026-11-17

### 統一治理邊界
- 本 Skill 只負責下列 `owns` 工作；`does_not_own` 所列工作不由本 Skill 自行決定。
- 命中邊界時依 `handoff_to` 轉交，不靜默擴張責任、不覆寫其他 Skill 結論。
- 外部 Connector、付款、刪除、Push、Merge、Release、正式採用與 Runtime 啟用不因本 Skill 的領域判斷而自動授權；由 `manus-core` 管理授權、唯一 writer、讀回與回復。
- 本 Skill 可提出候選 `PASS`／`FAIL`／`UNKNOWN`／`NOT_RUN`／`BLOCKED`，但 `final_integrator` 固定為 `manus-core`；`may_adopt: false`、`may_enable_runtime: false`。
- 任務專屬禁止、STOPPED、PAUSED 或使用者當次較嚴格限制，優先於一般常設授權。
- 規則、版本或來源衝突時標 `CONFLICT`，停止相依步驟並保存原文、位置、影響、差異與回復方式；不得以替代來源繞過授權或停止條件。

| 欄位 | 本 Skill 邊界 |
|---|---|
| `final_integrator` | `manus-core` |
| `may_adopt` | `false` |
| `may_enable_runtime` | `false` |
| `external_write_owner` | `manus-core`／指定唯一 writer |
| `conflict_priority` | 任務專屬硬限制 > manus-core 一般規則 > 本 Skill 建議 |

### 本 Skill 路由
- `owns`：G0-G9 與治理驗收關卡、證據矩陣與狀態判定。
- `does_not_own`：不把自評、文件完整或 NOT_RUN 升格為正式採用／Runtime。
- `handoff_to`：G8 呼叫 `independent-audit`；角色模式交 `three-party-review`；最終決策交核心／治理者。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：G0-G9 關卡分離與採用邊界。

### 5B 多重邊界與唯一主路由
- 當同一請求同時命中本 Skill 與其他 Skill 時，本 Skill 只處理自己的 `owns` 範圍，指定唯一主路由、輔助路由與 `handoff_to`；不得雙重寫入或自行成為最終裁決者。
- 無法判定主責時標 `CONFLICT`，保存觸發規則、route chain、責任者與待決，不以猜測選路。

### 5E 部分成功與例外
- 已完成與未完成步驟必須分開記錄；部分成功不得標整體 `PASS`。來源、輸出或讀回不完整時標 `UNKNOWN`、`NOT_RUN` 或 `BLOCKED`，依實際證據判定。
- 必須保存已完成副作用、未完成範圍、stdout、stderr、Exit Code、錯誤與下一步；不得以替代來源掩蓋缺口。

### 5X 授權、停止與不可逆操作
- 一般授權不解除任務專屬限制；`STOPPED_BY_USER`、`PAUSED_BY_USER`、`BLOCKED`、使用者當次禁止與不可逆操作限制優先。
- 外部寫入、付款、刪除、發送、Push、Merge、正式採用與 Runtime 啟用須交 `manus-core`／指定唯一 writer；不得用替代路由繞過授權。

### 5R 回復、冪等與重試
- 首次失敗與回復失敗都必須保存；非冪等操作沒有去重鍵或讀回證據時，禁止重試、禁止重複寫入，停止並要求人工裁決。
- 回復須指向明確版本、檔案或狀態；保存原始錯誤、回復錯誤、部分副作用、diff、Hash 與可執行的回復步驟，不得無限重試。

### 5C 循環路由與衝突整合
- 必須記錄完整路由鏈並偵測重複訪問；發現循環或相互矛盾結論時標 `CONFLICT` 或 `BLOCKED`，在可逆狀態停止並交 `manus-core`。
- 本 Skill 不得覆寫其他 Skill 或稽核者結論；最終整合者固定為 `manus-core`，本節不授予正式採用或 Runtime 權限。

### 本次補強驗收
- 內容類型：`繼承＋強化`；歷史版本：已保存於 `evidence/fifth-pass-repair-20261118/pre-upgrade-snapshot/`。
- 狀態：候選升級，尚未正式採用、尚未 Runtime 生效。
