---
name: batch-task-completion-and-single-report
description: 全量批次任務的範圍凍結、實質 Skill 優化、測試、獨立驗收與單次成果回報。Use when the user requests all Skills, batch migration, full audit, comprehensive upgrade, complete acceptance, or one final report.
---

# 治理-批次任務整體完成與單次回報

## 1. 問問題

啟用前確認：

- 是否為多項目批次任務，而非單一低風險問答？
- 完整範圍、Skill 清單、總數、路徑、版本、來源、相依、排除項與逐項 AC 是否已取得？
- 使用者要求的是實質優化升級，還是僅格式整理？預設視為實質優化升級。
- 是否涉及原始正本、外部寫入、授權、不可逆操作或停止／暫緩領域？

關鍵觸發詞包括：`全部`、`整批`、`逐項完成`、`批次`、`一次回報`、`全部驗收`、`重構後再說`、`不得逐筆回報`、`全部 PASS 才交付`、`全面檢查`、`優化升級`。

範圍未凍結前，不得開始逐項製作，也不得宣稱「全部」。

## 2. 解決

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| B1 | J | 批次任務已觸發 | 載入 `manus-core`，盤點全部候選 Skill，建立 TASK_ID、SCOPE、INVENTORY、TOTAL、AC、DEPENDENCIES、EXCLUSIONS；發現新增相關 Skill 必須記錄並判斷是否納入。 | 不得只處理目前看得到的幾份；不得靜默縮小範圍或刪除未完成項目。 | 完整清單、總數、來源／版本／狀態／相依表、範圍凍結紀錄。 | 清單不完整標 `BLOCKED` 或 `UNKNOWN`，停止依賴清單的步驟並補讀來源。 |
| B2 | P | B1 範圍凍結完成 | 逐份全文讀取 Skill 及必要 references，執行實質審查：定位、觸發、輸入輸出、流程、權限、例外、失敗、恢復、相依、治理相容性與實際可用性；執行 `find <candidate-root>/skills -name SKILL.md -print` 與 `sha256sum <source> <candidate>`；保留 source atom mapping。 | 不得只改七欄、補 ID、改文字或讓 Linter 通過就宣稱升級；不得刪除有效限制、數值、來源或權限。 | 原始版本／內容、問題清單、mapping、優化理由、修改前後 diff、回復方法。 | 發現衝突或缺漏先保留原證據，標 `REWORK_REQUIRED`，只修正通則後重測。 |
| B3 | P | B2 已完成一份實質審查 | 依任務串接 Skill：建立／重構用 `make-skill`；程式或腳本用 `safe-implementation`；領域工作載入對應領域 Skill；保存／交接用 `dghp-work-handoff`；獨立反證用 `independent-audit`。執行 `python3 <MANUS_SKILLS_ROOT>/skill-creator/scripts/quick_validate.py --path <skill-dir>` 與 `python3 <make-skill-root>/scripts/skill_lint.py <skill-dir>/SKILL.md`。 | 不得把角色分工、測試證據或獨立驗收混在同一執行者身上；不得改原始 MIKO 正本。 | Skill 路由表、執行紀錄、角色分工、輸入輸出與保存位置。 | 依賴缺失、權限不足或 Skill 不可用時標 `BLOCKED`，不可假稱已串接。 |
| B4 | C | 每份 Skill 已產生候選結果 | 執行格式／結構、正向、負向、相近反例、邊界、異常、回歸、Mutation、權限／禁止事項、相依／整合及必要端到端測試；逐項記錄 PASS、FAIL、NOT_RUN 或 BLOCKED。 | Linter PASS 不得當成功能合格；不得以局部 PASS 代替整份 Skill；不得將預期輸出當實際輸出。 | 測試 ID、目標檔、完整命令、stdout、stderr、Exit Code、時間、結果與證據檔。 | FAIL 必須保留失敗證據、確認根因、修正通則、重跑失敗案例、回歸並重新獨立驗收。 |
| B5 | C | 全部個別 Skill 已通過必要測試 | 由 `IMPLEMENTER` 交付、`TESTER` 實跑、`INDEPENDENT_AUDITOR` 自行讀取與反證；再檢查 Skill 觸發／路由、相依、共用規則、Writer、輸入輸出與整合流程。 | 製作者不得以自驗取代獨立驗收；測試者不得只複製製作者 PASS；獨立驗收者不得直接接受前兩者結論。 | 三角色證據、獨立冷讀、整合／端到端結果、差異報告。 | 無真正獨立驗收標 `BLOCKED` 或 `NOT_RUN`，不得標合格。 |
| B6 | J | 所有必要 AC 均有實際證據 | 全部必要項目、測試、回歸與獨立驗收通過；必要 UNKNOWN、NOT_RUN、BLOCKED 為零；版本、Hash、diff、來源與保存位置可追溯後，才輸出一次完整總報告。 | 執行期間不得主動逐筆回報局部完成；不得用部分 PASS 宣稱整批 COMPLETE；不得將候選成果宣稱正式採用或 Runtime 生效。 | 最終總表、逐項狀態、FAIL／REWORK 歷史、證據索引、版本／Hash、正式／Runtime 狀態。 | 任一必要條件未達成，輸出 `REWORK_REQUIRED` 或 `BLOCKED`，不得輸出 `COMPLETE`。 |

## 累積式演進與歷史版本保護

本 Skill 的升級預設採累積式演進，不採覆蓋式升級。每次修改前先保存原始版本、來源、日期、Commit、SHA-256 與版本沿革；再逐項分類為繼承、強化、新增、修正、重構、廢止。新版必須建立新候選版本，保留舊版、原始內容、diff、修改理由、測試證據與回復方式。不得因新版較新而刪除、覆寫或自動廢止舊版。

任何刪除、功能移除、廢止或取代，必須保存原內容、理由、證據、影響分析、承接規則、回復方案與核准紀錄；無法確認時保留並標 `UNKNOWN`。新版必須通過原有功能回歸、新增功能測試、來源追溯、舊版可查閱與復原檢查。版本更新與正式採用是不同事件。

## 3. 後設

- 這個 Skill 的核心是「實質功能與規則審查」，不是格式統一。
- `IMPLEMENTER`、`TESTER`、`INDEPENDENT_AUDITOR` 必須保留職責與證據隔離。
- 使用者主動詢問時必須如實提供現況；單次成果回報不代表隱瞞阻塞。
- 授權不足、外部依賴、重大安全風險、不可逆操作、來源缺失或無法繼續時，立即依 manus-core 困難卡回報阻塞。
- 台指期／臺股回測命中停止或暫緩規則時，不執行，維持 `STOPPED_BY_USER`／`PAUSED_BY_USER`。
- 未有遠端讀回或 Runtime 實測證據時，維持 `UNKNOWN`、`NOT_RUN` 或 `BLOCKED`，不得宣稱正式生效。

## 4. 檢查

- expected：完整清單與總數已凍結；每項有實質審查、mapping、diff、測試、回歸、Mutation、獨立驗收與最終狀態。
- forbidden：只看摘要、只改格式、只跑 Linter、只接受自述 PASS、隱藏 FAIL、以局部 PASS 代替整批 PASS、以候選成果冒充正式版本。
- 相近反例：只有一個 Skill 的單一問答；只有格式重排的任務；使用者主動詢問現況；授權或外部依賴造成阻塞。前兩者不必啟用本 Skill，後兩者仍必須即時如實回報。
- AC-01：INVENTORY 完整且 TOTAL 與實際數量一致。
- AC-02：每項保留原始來源、source atom mapping、實質問題、優化理由與 diff。
- AC-03：必要測試與 Mutation 證明測試能識別預期錯誤。
- AC-04：獨立驗收者自行讀取、執行與反證，未接受製作者結論代替證據。
- AC-05：所有必要條件 PASS 前，不得輸出 `OVERALL_STATUS=COMPLETE`。

## 0.2 累積式整合、衝突與邊界路由

本 Skill 的優化、升級、重構、修正與移轉一律採累積式演進：先保存目前版本與 SHA-256，再逐項分類為繼承、強化、新增、修正、重構或廢止；未理解或未驗證的既有內容不得刪除。執行前載入 `version-evolution-preservation`，並確認本 Skill 與 `manus-core`、`independent-audit`、`three-party-review`、`ai-engineering-anti-fraud-test-credibility` 的責任不重疊。

若本 Skill 與其他 Skill、正本規則、外部來源或使用者限制衝突，不得靜默覆蓋；先標記 `CONFLICT`，保存衝突位置、影響範圍與待決事項，停在可逆狀態。任何新增能力都必須通過正向、負向、邊界、異常、回歸與必要的 Mutation 測試；`FAIL`、`NOT_RUN`、`UNKNOWN`、`BLOCKED` 不得升格為正式採用或 Runtime 生效。

本候選版本只代表 Manus 分支候選內容，不代表 GitHub main、正式採用或 Runtime 已生效。

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
- `owns`：批次清單、總數、整批完成判定與單次成果回報。
- `does_not_own`：不壓制授權不足、不可逆風險或 BLOCKED 即時回報。
- `handoff_to`：核心困難卡與任務四態交 `manus-core`。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：批次完成狀態與阻塞回報。

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
