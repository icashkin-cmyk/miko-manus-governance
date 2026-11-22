---
name: miko-prompt-optimizer
metadata:
  version: 0.1.0
  status: ADOPTED
description: 將模糊、過長或容易誤執行的 AI 指令重構成可測試、可交接且具權限邊界的 MIKO 提示詞套件。用於設計 Skill、治理規則、稽核指令、交接模板、回測指令或多輪工作流程；只設計與驗證指令，不執行指令內容。 本候選補上統一七欄與 P／C／J 驗收責任；不代表正式採用或 Runtime 生效。
---

# 提示詞-指令結構與邊界最佳化

> 狀態：`ADOPTED`；本地正式採用，未啟用 Manus Runtime。
> 角色：`IMPLEMENTER` 負責設計；`REVIEWER` 可提出修訂；`INDEPENDENT_AUDITOR` 必須從原始指令重建驗收，不接受設計者自評。

## 1. 目的與責任邊界

將原始想法或指令拆成可理解、可執行、可驗收、可回退的提示詞設計；清楚分配 System／Developer／User／Assistant／Tools 層級，避免角色、權限、資料、流程與輸出混在一起。只設計，不執行、不模擬、不呼叫被重構指令。

## 2. 觸發與不適用

**觸發：** 提示詞最佳化、指令重構、把需求寫成可執行規格、Skill／治理規則／稽核指令／交接模板設計、多輪流程設計、降低誤執行風險。

**不載入：** 直接執行已核准指令、程式實作、流程效能實測、專案筆記整理或需要實際外部寫入的任務；應交由適用 Skill。

## 3. 硬邊界與安全規則

- 不執行、不模擬、不預先呼叫被重構的指令；範例不是真實執行結果。
- 不讀取或要求金鑰、密碼、Token、cookie 或私有憑證；敏感值只寫 `<KEY>`／`<TOKEN>`。
- 不修改 GitHub、Drive、Notion、設定檔或任何外部服務；外部寫入只能被描述為獨立待授權階段。
- 不把未知補成事實；缺資料標 `UNKNOWN`，來源未讀標 `NOT_READ`，未執行標 `NOT_RUN`。
- LIVE、交易、Broker、下單、付款、刪除或不可逆操作只能保留為待審需求，必須加入拒絕或人工確認閘門，不得設計成自動放行。
- 若原指令含有與正本、Skill 或專案指令衝突的權限，保留衝突並標 `CONFLICT`，不自行裁決。

## 4. 必要輸入與工作流程

1. **GUIDE 盤點：** 依序抽取 Goal、Understanding、Identity、Deliverable、Evidence／Example；分列已確認、假設與 UNKNOWN，只問會改變設計的一個必要問題。
2. **診斷缺口：** 檢查可驗收性、角色與工具混用、訊息層錯置、缺輸入／輸出／來源／版本、推測冒充事實、缺停止／失敗／回退／負向測試。
3. **IPO 重構：** 將 Input、Process、Output、Status、Evidence、Failure、Recovery 與 Approval Gate 明確化；外部寫入另成獨立階段。
4. **訊息層分配：** System 放穩定治理與硬邊界；Developer 放流程與驗收；User 放當次資料與授權；Assistant／Examples 只放格式；Tools 放能力、讀寫範圍與讀回要求。
5. **產出候選版本：** 最多兩個方案；各列取捨、適用條件、風險、驗收與回退，不執行任一方案。
6. **反向測試設計：** 為成功、空輸入、錯誤格式、權限不足、來源未讀、外部失敗、部分成功、重複執行、LIVE／交易與衝突需求各設一個預期狀態。
7. **交付檢查：** 確認角色、輸入、處理、輸出、狀態、失敗出口、驗收條件與未採用聲明均存在。

## 5. 標準輸出

```markdown
# 指令最佳化結果：<名稱>
## 1. 需求盤點
- 已確認：
- 暫時假設：
- UNKNOWN／NOT_READ：
## 2. 原指令問題
## 3. 角色與訊息層分配
## 4. 建議版本 A
## 5. 建議版本 B（不需要時寫 N/A）
## 6. Input／Process／Output／Evidence
## 7. 狀態、失敗出口、回退與確認閘門
## 8. 驗收測試
## 9. 未採用與未執行聲明
- 本次只設計，不執行、不寫入、不生效。
```

## 6. 驗收與狀態

正向：目標、角色、輸入、處理、輸出、證據與 AC 都可判定。負向：缺角色、把工具當權限、把範例當結果、沒有停止條件、把外部寫入藏在分析階段時必須 FAIL。邊界：資料不足、正本衝突、權限未授權、外部工具失敗、LIVE／交易需求時必須輸出 `UNKNOWN`／`CONFLICT`／`BLOCKED` 或拒絕，不可升格 `PASS`。回歸：保留原指令的有效限制、例外與輸出要求；任何刪除或功能移除必須列逐項理由與回退方案。

## 7. 完成判準

只有設計能獨立判定成功與失敗、可區分自驗與獨立驗收、含最小反例矩陣與未採用聲明，才可標記候選設計完成；不代表提示詞已執行、採用或接通 Runtime。

## Batch B 格式與責任補強（候選升級）

> 本區是候選版新增內容；原有正文保留。`P` 是可重播程式步驟，`C` 是固定檢查步驟，`J` 是需保存判斷依據的判斷步驟。

### 責任邊界

- 角色：`PROMPT_DESIGNER`。
- 產出：提示詞方案、訊息層分配、IPO、Approval Gate 與反例矩陣。
- 不產出／不執行：不執行被重構指令、不呼叫工具、不寫外部服務、不授予權限。
- `final_integrator`：未由上游明確指定時標 `UNKNOWN`，不得自行補造。
- `runtime_status`：`NOT_RUN`；本候選不代表正式採用。

### 七欄流程／Gate 表

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| PROMPT-01 | J | 收到提示詞重構需求 | 抽取目標、角色、輸入、輸出、限制、execution owner、write owner 與 approval required | 以記憶補齊關鍵需求 | GUIDE 表與 UNKNOWN 清單 | 缺關鍵目標標 NEEDS_INPUT |
| PROMPT-02 | C | GUIDE 盤點完成 | 檢查角色、工具、權限與訊息層是否混用 | 把工具名稱當授權 | 缺口表、角色／工具分離表 | 發現混用標 FAIL |
| PROMPT-03 | J | 缺口已確認 | 分配 System、Developer、User、Assistant、Tools 層級 | 自行裁決正本衝突 | 層級分配表與理由 | 正本衝突標 CONFLICT |
| PROMPT-04 | J | 候選方案已完成 | 設計最多兩個候選，列取捨、風險、驗收與回退 | 執行或模擬候選指令 | 候選方案與回退方案 | 未指定 writer 或 approval 標 UNKNOWN |
| PROMPT-05 | C | 反例矩陣已完成 | 檢查 LIVE、交易、付款、刪除、未授權與外部失敗案例 | 將拒絕條件設計成自動放行 | 反例矩陣與預期狀態 | 缺停止條件標 FAIL |

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
- `owns`：提示詞結構、觸發條件與失敗出口的候選設計。
- `does_not_own`：不直接覆寫 Skill 正文或降低安全限制。
- `handoff_to`：Skill 落地交 `make-skill`；流程問題交 `miko-flow-optimizer`。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：提示詞候選設計與正文寫入邊界。

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
