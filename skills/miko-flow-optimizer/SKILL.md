---
name: miko-flow-optimizer
metadata:
  version: 0.1.0
  status: ADOPTED
description: 以 Input→Process→Output、依賴、責任、摩擦、閘門與回退條件分析 MIKO 的工程、文件、Skill、稽核或交接流程。用於流程理順、責任切割、避免重工、降低寫入風險與自動化前評估；只產生可驗證的流程設計，不執行或修改流程。 本候選補上統一七欄與 P／C／J 驗收責任；不代表正式採用或 Runtime 生效。
---

# 流程-依賴責任與閘門最佳化

> 狀態：`ADOPTED`；本地正式採用，未啟用 Manus Runtime。
> 角色：`IMPLEMENTER` 只產出流程分析；`REVIEWER` 可提出修訂；`INDEPENDENT_AUDITOR` 必須另行冷讀，不能把本 Skill 自評當成獨立驗收。

## 1. 目的與適用範圍

把既有流程轉成可讀、可驗收、可交接的設計，找出缺輸入、責任斷點、重複、無限迴圈、過早寫入與不可回退步驟。適用於工程、文件、Skill、治理、稽核、交接與自動化前規劃；不負責執行流程。

## 2. 觸發與不適用

**觸發：** 流程最佳化、流程重排、降低重工、責任切割、依賴分析、寫入前風險評估、回退設計、交接流程設計。

**不載入：** 只需執行已核准流程、單純摘要、純提示詞設計、效能瓶頸實測或需要實際外部寫入的任務；應交由對應 Skill。

## 3. 硬邊界與責任

- 只讀取使用者提供或本輪明確讀取的資料；未讀來源標 `NOT_READ`。
- 狀態只能使用 `PASS`、`FAIL`、`UNKNOWN`、`NOT_READ`、`NOT_RUN` 或 `BLOCKED`；未知或未執行不得寫成 `PASS`。
- 不呼叫外部服務、不寫 GitHub／Drive／Notion／設定、不發信、不提交、不推送、不下單。
- 不把「看起來更簡潔」當最佳化證據；沒有基準或實測指標就標 `UNKNOWN`。
- LIVE、交易、Broker、付款、刪除或其他不可逆操作只分析風險，不提供放行指令。
- 外部寫入必須獨立列出目標、欄位、唯一 writer、確認閘門、讀回、回退與負責人。

## 4. 必要輸入與工作流程

1. **界定範圍：** 列出流程名稱、目標、納入／排除範圍、來源、版本、日期與驗收條件；重述理解，只有會改變設計的缺口才問一題。
2. **建立基線：** 逐步填 `Step｜Input｜Process｜Output｜Owner｜Reads｜Writes｜Gate｜Status`；缺欄不得補造。
3. **分析依賴：** 區分硬依賴、資料依賴、責任交接、外部觸發與歷史習慣；檢查循環、孤兒輸入與無出口。
4. **盤點摩擦：** 每項記錄 `位置｜類型｜證據｜影響｜建議`；類型包含重複、等待、漏驗證、過早寫入、不可回退與責任重疊。
5. **提出重排：** 每一項列原位置、新位置、收益、保留的硬依賴、失效風險、最小測試與回退方式；至少保留不改方案作比較。
6. **收斂交付：** 產生 Before／After、依賴箭頭、閘門、失敗出口、驗證指標與未決事項；不執行所設計的流程。

## 5. 標準輸出

```markdown
# 流程分析：<名稱>
## 1. 結論與狀態
- 任務四態：完成／完成但有疑慮／需要資料／卡住
- 建議：<保留、重排或不改>
- 適用範圍／失效條件：<內容>
## 2. 來源與基線
- 已讀取：<來源、版本、commit、日期>
- NOT_READ／UNKNOWN：<逐項列出>
## 3. 原始流程與 I→P→O 表
## 4. 依賴、責任與衝突
## 5. 摩擦與風險
## 6. Before／After 與不採方案
## 7. 寫入確認閘門、失敗出口與回退
## 8. 最小驗證與回歸測試
## 9. 交接
- 完成／未完成／待決／阻塞／交付位置／驗收者／SHA／讀回
## 10. 未生效聲明
- 本次未執行流程、未修改正本、未寫入外部服務、未啟用 Runtime。
```

## 6. 驗收與狀態

正向：每一步有輸入、處理、輸出、Owner、Gate 與狀態。負向：缺 Input、缺 Output、責任重疊、循環依賴、無限重試或不可逆寫入沒有確認時必須 FAIL。邊界：來源未讀、外部工具不可用、流程含 LIVE 時必須保留 `NOT_READ`／`BLOCKED`／`UNKNOWN`，不可升格 `PASS`。回歸：原流程的必要步驟、限制、例外與回退條件均須可追溯；刪除或廢止必須另列理由與復原方案。

## 7. 完成判準

只有流程差異、責任邊界、證據、最小驗證、回退條件與未決事項都明確，且沒有未處理的循環或無出口，才可標記候選分析完成；這不代表流程已採用、執行或生效。

## Batch B 格式與責任補強（候選升級）

> 本區是候選版新增內容；原有正文保留。`P` 是可重播程式步驟，`C` 是固定檢查步驟，`J` 是需保存判斷依據的判斷步驟。

### 責任邊界

- 角色：`FLOW_ANALYST`。
- 產出：流程基線、依賴圖、責任矩陣、Before／After、最小驗證與回退方案。
- 不產出／不執行：不執行流程、不修改正本、不擔任 Skill writer。
- `final_integrator`：未由上游明確指定時標 `UNKNOWN`，不得自行補造。
- `runtime_status`：`NOT_RUN`；本候選不代表正式採用。

### 七欄流程／Gate 表

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| FLOW-01 | J | 收到流程最佳化需求 | 界定目標、納入／排除範圍、來源、唯一 writer 與 final integrator | 未讀來源自行補齊流程 | 需求摘要、來源清單、UNKNOWN 清單 | 缺關鍵資料標 NEEDS_INPUT |
| FLOW-02 | P | 範圍與來源已確認 | 產生 Step、Input、Process、Output、Owner、Reads、Writes、Gate、Status 基線表 | 手動捏造計算結果 | 基線檔、命令輸出、Exit Code | 腳本失敗標 BLOCKED |
| FLOW-03 | C | 基線表已產生 | 檢查循環依賴、孤兒輸入、無出口與責任重疊 | 只以流程看起來簡潔判定 PASS | 依賴檢查表、反例與差異 | 發現循環標 FAIL |
| FLOW-04 | J | 缺口與摩擦已列出 | 提出重排方案與不改方案，列收益、風險、測試與回退 | 不自行選定正式方案 | Before／After、方案取捨、回退方案 | 方案無法比較標 UNKNOWN |
| FLOW-05 | C | 候選流程已完成 | 核對每步輸入、輸出、Owner、Gate、狀態與交接欄位 | 把分析結果當已執行結果 | 驗收矩陣與交接稿 | 缺欄位標 FAIL |

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
- `owns`：流程分析、瓶頸辨識與候選流程設計。
- `does_not_own`：不直接修改正式 Skill、正本或外部服務。
- `handoff_to`：Skill 實作交 `make-skill`；最終整合交核心。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：流程分析、瓶頸定位與候選最佳化。

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
