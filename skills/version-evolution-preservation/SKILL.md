---
name: version-evolution-preservation
description: Skill、規則、文件或架構升級時的累積式演進與歷史版本保護。Use when upgrading, refactoring, correcting, migrating, replacing, deprecating, or versioning an existing artifact.
---

# 版本-累積式演進與歷史保護

## 1. 問問題

確認目標是累積式升級、修正、重構或經授權取代；確認原始路徑、來源版本、目前使用版本、相依者、授權與不可逆操作。未確認是否可刪除時，預設保留並標 `UNKNOWN`。新版較新不等於舊版失效。

## 2. 解決

| ID | 類型 | 觸發條件 | 操作要求 | 禁止事項 | 驗收證據 | 失敗處理 |
|---|---|---|---|---|---|---|
| VEP1 | P | 已確認既有 Skill 或文件需升級 | 執行 `cp <artifact> <archive>/pre-upgrade/<version>/` 與 `sha256sum <artifact>`；記錄來源、日期、Commit、版本與目前使用狀態。 | 不得直接覆寫或刪除原始版本。 | 舊版快照、Hash、來源與版本基線。 | 基線缺失標 `BLOCKED`，停止修改。 |
| VEP2 | C | 舊版基線已保存 | 逐項分類：繼承、強化、新增、修正、重構、廢止；建立 source／feature mapping 與影響清單。 | 不得因未理解、未驗證或不熟悉而刪除內容。 | 分類表、原文位置、修改理由與相依影響。 | 無法分類時保留原內容並標 `UNKNOWN`。 |
| VEP3 | P | 分類與影響清單完成 | 以新版本檔案追加改善，執行 `diff -u <old> <new>`；保存新增、修改、刪除與回復方案。 | 不得把覆蓋、無理由功能移除或格式重排宣稱為升級。 | 新版、diff、版本沿革、回復目標與 Hash。 | 發現未授權刪除，回復候選版本並重做。 |
| VEP4 | C | 新候選版本產生 | 執行原有功能回歸、新功能測試、來源追溯、舊版可查閱、復原與相依整合檢查。 | 不得只以 Linter 或新版存在代表升級合格。 | 測試命令、stdout、stderr、Exit Code、回歸與復原證據。 | 任一 FAIL 保留證據、修正新版本並重測；不得改舊版。 |
| VEP5 | J | 所有升級 AC 有實際證據 | 分開記錄最新版本、目前使用版本、候選版本、歷史版本與已廢止版本；版本更新與正式採用分開判定。 | 不得自動把新版標為正式採用、把舊版標為失效或宣稱 Runtime 生效。 | 版本沿革、採用裁決、狀態、Hash 與保存位置。 | 證據不足標 `UNKNOWN`、`NOT_RUN` 或 `BLOCKED`，不得放行。 |

## 3. 後設

最高原則：升級是累積，不是抹除；重構是改善，不是遺失；新版是演進，不是歷史的替代品。任何刪除或廢止都必須有原內容、理由、證據、影響、承接、回復與核准紀錄。內容保護與版本保護都必須驗證。

## 4. 檢查

- expected：原始版本完整存在；有效內容已繼承或有明確處理依據；新增功能有測試；原有功能回歸通過；diff、來源、Hash、版本沿革與復原方式完整。
- forbidden：直接覆寫歷史版本、只改格式宣稱升級、未理解即刪除、以新版存在代表正式採用、以文件完整代表 Runtime 生效。
- 相近反例：只建立新檔但未保存舊版；刪除舊功能但沒有影響分析；只改標題或欄位；只跑 Linter。
- AC-01：升級前基線、舊版快照與 Hash 已保存。
- AC-02：每項修改均分類為繼承／強化／新增／修正／重構／廢止。
- AC-03：原有功能回歸、新功能測試、復原與相依檢查均有證據。
- AC-04：刪除／廢止／取代有授權與完整理由；未確認內容保留並標記。
- AC-05：版本更新、正式採用、Runtime 生效分開記錄。

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
- `owns`：原始版本、diff、Hash、沿革、回復與功能繼承。
- `does_not_own`：未確認舊功能不得刪除、廢止或覆寫。
- `handoff_to`：Skill 製作交 `make-skill`；正式採用仍交核心／治理者。


## 第五套高難度邊界與回復補強（候選升級 2026-11-18）

本節是累積式升級，不取代或刪除既有規則；本 Skill 的本次職責為：版本沿革、內容繼承與復原。

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
