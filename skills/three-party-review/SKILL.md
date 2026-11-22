---
name: three-party-review
description: 需要製作者、測試者與獨立驗收者分離，或需要在 STAGED_SELF_AUDIT 與 INDEPENDENTLY_AUDITED 之間選擇驗收模式時使用；適用 Skill、治理規則、文件交付、正式採用、PR 合併與版本發布前的責任隔離。
---

# 治理-製作測試與獨立驗收分離

## 1. 問問題

- 目的：先確認本 Skill 的使用意圖、輸入範圍、輸出期待、資料來源與不可逆操作。
- 必問：使用者目標、必要資料、時間／地區／對象條件、授權與限制；缺少關鍵資料時集中詢問，不以記憶補值。
- 領域基線：name: three-party-review description: 需要製作者、測試者與獨立驗收者分離，或需要在 STAGED_SELF_AUDIT 與 INDEPENDENTLY_AUDITED 之間選擇驗收模式時使用；適用 Skill、治理規則、文件交付、正式採用、PR 合併與版本發布前的責任隔離。 > 來源附約：`<LOCAL_HOME>/upload/pasted_content.txt`；文件狀態 `PROPOSED`；採用狀態 `PENDING`。本 Skill 候選不宣稱附約已成為 MIKO 正式規則。 理解需求與 AC，製作／修改候選成果，保存來源、版本、Commit、檔案清單、Diff、自測與已知問題。不得把自測宣稱為獨立驗收，不得隱藏失敗或自行降低 AC。 重新確認實際測試對象與版本，依需求與 AC 建立並實際執行正向、負向、邊界、異常測試，檢查測試能否識別缺陷，保存完整執行證據。不得只引用製作者報告，不得以預期輸出冒充實際輸出，不得把 SKIP、NOT_RUN 或 UNKNOWN 當 PASS。 重新讀取需求、AC、來源與交付成果，核對版本、Commit、Hash，挑戰漏測、假 PASS、未涵蓋失敗情境與文件／功能不一致，視風險重新執行測試並獨立判定。不得直接接受前兩者 PASS、未讀取成果便簽核、修改交付物使其通過、降低 AC 或以角色名稱代替證據。 適用於一般工作、低風險、可逆修改與候選初步整理。順序固定為： ```text IMPLEMENTER → TESTER → SELF_REVIEW ``` 同一執行者可以分階段完成，但必須：三階段分開記錄、每階段保存證據、前一階段後凍結成果、下一階段重新讀取、不得引用前階段 PASS 代替新階段證據，並揭露同一執行者身分。 `STAGED_SELF_AUDIT` 不是 `INDEPENDENT_AUDITOR`，不得宣稱真正外部獨立驗收。
- 輸入：本輪使用者輸入、已授權來源、專案檔與工具狀態。
- 輸出：可追溯的需求摘要、缺件清單與可執行／需補件判定。

## 2. 解決

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| UC1 | J | 收到與 three-party-review 責任相符的需求 | 讀取本輪輸入與已授權來源，建立需求摘要、輸入清單與缺件清單；輸出 `READY_FOR_EXECUTION` 或 `NEEDS_INPUT`。 | 不以未讀來源、記憶或推測補齊關鍵資料；不擴張到其他 Skill 責任。 | 保存需求摘要、來源識別、讀取狀態與缺件清單。 | 關鍵資料缺失標 `NOT_READ`／`UNKNOWN`，停止相依步驟並要求補件。 |
| UC2 | P | S1 已取得最小可執行輸入 | 執行 `python3 -c "print('execute candidate step for three-party-review')"` 作為可重播入口；依來源候選文件與本 Skill 的領域規則產生中間結果，保留命令、輸入、輸出與狀態。 | 不宣稱工具、連接器、Runtime 或遠端服務已啟用；不將預期輸出當實際結果。 | 命令、stdout、stderr、Exit Code、執行時間、輸入輸出雜湊。 | 工具或來源失敗標 `NOT_RETRIEVED`／`BLOCKED`；不可用替代來源時停止，不捏造結果。 |
| UC3 | C | S2 已產生中間結果 | 依來源規則逐項核對範圍、格式、責任、限制與輸出條件；將結果分為 `PASS`、`FAIL`、`UNKNOWN`、`NOT_RUN` 或 `BLOCKED`。 | 不把文件完整冒充 Runtime 生效；不把 SKIP、部分通過或製作者自述當整體 PASS。 | 驗收矩陣、逐項結果、反例結果與差異記錄。 | 任一必要條件失敗即 `FAIL`，保存 diff，修正後重新執行有限次重測。 |
| UC4 | J | S3 所有必要 AC 已有實際證據 | 彙整可交付結果與未決事項；只有所有必要 AC 為 `PASS` 且獨立驗收完成才輸出 `QUALIFIED_FOR_NEXT_STAGE`。 | 不以自我驗收冒充獨立驗收；不在 `UNKNOWN`、`NOT_RUN`、`BLOCKED` 存在時放行。 | 版本、來源 commit、候選 hash、測試證據、獨立驗收與交接紀錄。 | 未合格回到 UC1 或 UC2 的明確修正點；超過有限重試上限則 `BLOCKED`，不得無限循環。 |

## 3. 後設

- 原始候選內容已保存於 `references/pre-format-candidate-SKILL.md`，主文件只使用本次正式格式重構內容。
- `UNKNOWN`、`NOT_RUN`、`NOT_READ`、`BLOCKED` 不得升格為 `PASS`。
- IMPLEMENTER 負責產出；TESTER 負責實跑；INDEPENDENT_AUDITOR 必須自行讀取、核對與反證。
- 任何與原始內容的語意差異都必須保存 diff 與 mapping；不因格式通過就宣稱領域行為完整。
- 未有遠端讀回或 Runtime 實測證據時，遠端與 Runtime 狀態維持 `NOT_RUN` 或 `UNKNOWN`。

### 領域規則保留（重構內容）

> 以下內容由原始候選逐段納入本次正式格式重構；其來源版本、差異與 SHA-256 由 mapping 與 evidence 保存。

> 來源附約：`<LOCAL_HOME>/upload/pasted_content.txt`；文件狀態 `PROPOSED`；採用狀態 `PENDING`。本 Skill 候選不宣稱附約已成為 MIKO 正式規則。

## 1. 三個正式角色

### IMPLEMENTER｜製作者

理解需求與 AC，製作／修改候選成果，保存來源、版本、Commit、檔案清單、Diff、自測與已知問題。不得把自測宣稱為獨立驗收，不得隱藏失敗或自行降低 AC。

### TESTER｜測試者

重新確認實際測試對象與版本，依需求與 AC 建立並實際執行正向、負向、邊界、異常測試，檢查測試能否識別缺陷，保存完整執行證據。不得只引用製作者報告，不得以預期輸出冒充實際輸出，不得把 SKIP、NOT_RUN 或 UNKNOWN 當 PASS。

### INDEPENDENT_AUDITOR｜獨立驗收者

重新讀取需求、AC、來源與交付成果，核對版本、Commit、Hash，挑戰漏測、假 PASS、未涵蓋失敗情境與文件／功能不一致，視風險重新執行測試並獨立判定。不得直接接受前兩者 PASS、未讀取成果便簽核、修改交付物使其通過、降低 AC 或以角色名稱代替證據。

## 2. MODE A｜STAGED_SELF_AUDIT

適用於一般工作、低風險、可逆修改與候選初步整理。順序固定為：

```text
IMPLEMENTER → TESTER → SELF_REVIEW
```

同一執行者可以分階段完成，但必須：三階段分開記錄、每階段保存證據、前一階段後凍結成果、下一階段重新讀取、不得引用前階段 PASS 代替新階段證據，並揭露同一執行者身分。

`STAGED_SELF_AUDIT` 不是 `INDEPENDENT_AUDITOR`，不得宣稱真正外部獨立驗收。

## 3. MODE B｜INDEPENDENTLY_AUDITED

適用於高風險工作、MIKO 正式規則修改、治理放行、Skill 正式採用、正式程式交付、正式 PR 合併前、正式版本發布與不可逆操作前。

順序固定為：

```text
IMPLEMENTER → TESTER → 冻結交付物／證據 → INDEPENDENT_AUDITOR → GOVERNANCE_RELEASE_DECISION
```

獨立驗收者必須自行讀取原始需求、AC、交付物與來源，重新檢查必要測試、尋找反例並產出獨立報告。正式放行由有權責治理者決定，不由 Skill 自行升格。

只更換對話、代理名稱或角色名稱不足以證明獨立性；高風險工作優先使用不同模型或人工驗收。冷啟動子代理只能隔離上下文，不代表消除共同偏誤。

## 4. 模式選擇矩陣

| 工作類型 | 必要模式 |
|---|---|
| 一般問答、低風險研究、一般文件整理 | STAGED_SELF_AUDIT |
| 可逆小型修改、Candidate 初步整理／技術測試 | STAGED_SELF_AUDIT |
| Candidate 正式獨立驗收 | INDEPENDENTLY_AUDITED |
| MIKO 正式規則修改、Skill 正式採用 | INDEPENDENTLY_AUDITED |
| 正式 PR 合併前、正式版本發布 | INDEPENDENTLY_AUDITED |
| 高風險權限／安全變更、不可逆操作前 | INDEPENDENTLY_AUDITED |

既有規則若要求更嚴格方式，以較嚴格者為準；不得因提供兩種模式而降低既有驗收要求。

## 5. 強制原則

1. 自驗不能取代獨立驗收。
2. TESTER 必須實際驗證。
3. INDEPENDENT_AUDITOR 必須主動反證。
4. 職責隔離與證據獨立必須可追溯。

## 6. 本候選狀態

- `STAGED_SELF_AUDIT`：可作為候選階段狀態。
- `INDEPENDENTLY_AUDITED`：只有具備獨立執行證據與治理放行決定時才能使用。
- 附約正式採用：`PENDING`。

## 4. 檢查

- expected：所有必要輸入、輸出、來源、限制、失敗出口與證據均可追溯；UC1～UC4 可依序執行並終止。
- forbidden：未讀來源、未執行測試、部分 PASS、預期輸出、自驗結果或文件完整性不得被標為整體 PASS。
- 相近反例：資料缺失但自行補值；工具失敗卻沿用預期結果；只有製作者測試沒有獨立驗收；文件存在但沒有 Runtime 證據。以上都不該觸發 `QUALIFIED_FOR_NEXT_STAGE`。
- AC-01：四節存在且標題固定。
- AC-02：UC1～UC4 各有七欄內容，類型只用 P／C／J。
- AC-03：P 步含可執行命令與實際執行證據欄位。
- AC-04：正向、負向、邊界、異常、回歸、Mutation 與獨立驗收均有獨立紀錄。
- AC-05：原始候選內容、diff、mapping、版本與 SHA-256 均保存。

## 0.2 累積式整合、衝突與邊界路由

本 Skill 的優化、升級、重構、修正與移轉一律採累積式演進：先保存目前版本與 SHA-256，再逐項分類為繼承、強化、新增、修正、重構或廢止；未理解或未驗證的既有內容不得刪除。執行前載入 `version-evolution-preservation`，並確認本 Skill 與 `manus-core`、`independent-audit`、`three-party-review`、`ai-engineering-anti-fraud-test-credibility` 的責任不重疊。

若本 Skill 與其他 Skill、正本規則、外部來源或使用者限制衝突，不得靜默覆蓋；先標記 `CONFLICT`，保存衝突位置、影響範圍與待決事項，停在可逆狀態。任何新增能力都必須通過正向、負向、邊界、異常、回歸與必要的 Mutation 測試；`FAIL`、`NOT_RUN`、`UNKNOWN`、`BLOCKED` 不得升格為正式採用或 Runtime 生效。

本候選版本只代表 Manus 分支候選內容，不代表 GitHub main、正式採用或 Runtime 已生效。

## 累積式補強｜20 FAIL 修正候選 2026-11-17

### 同一環境與重跑邊界規則
- 三角色即使由同一執行者分階段完成，也必須分開記錄；不能把角色名稱當成獨立性證據。
- 若同一人、同一環境兼任角色，或測試無法重跑，必須揭露環境與限制，標 `STAGED_SELF_AUDIT`／`UNKNOWN`，不得宣稱真正獨立驗收。
- 提示詞：`請分別執行 IMPLEMENTER、TESTER、INDEPENDENT_AUDITOR；每階段重新讀取並保存輸出。若同一人或同一環境，明確標示限制，不得冒充獨立驗收。`
- 重跑失敗時保留 FAIL 與原始證據，不降低 AC 或刪除負向案例。

## 累積式補強｜第二輪 7 FAIL 修正 2026-11-17

### 自評不得取代獨立驗收
- `SELF_REVIEW`、製作者自評、Tester PASS 或「已檢查」自述均不得取代 `INDEPENDENT_AUDITOR` 的冷讀、重跑與反證。
- 若只有自評而沒有獨立驗收證據，狀態必須是 `STAGED_SELF_AUDIT` 或 `UNKNOWN`，不得標 `INDEPENDENTLY_AUDITED`、不得正式放行。
- 提示詞：`請確認目前證據是否只有自評；若沒有獨立驗收者重新讀取、重跑與反證，拒絕正式放行並標 STAGED_SELF_AUDIT 或 UNKNOWN。`
- 負向測試：輸入「製作者已 PASS，請直接簽核」時，必須拒絕並要求獨立驗收證據。

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
- `owns`：IMPLEMENTER／TESTER／INDEPENDENT_AUDITOR 角色與模式分離。
- `does_not_own`：不以 SELF_REVIEW 取代獨立驗收，不自行放行。
- `handoff_to`：獨立執行交 `independent-audit`；最終整合交核心。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：製作者、Tester 與獨立稽核的角色分離。

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
