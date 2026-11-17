# 三份候選 Skill 本地人工治理審查報告

> 審查性質：`MANUAL_REVIEW`。本報告不是 Claude API 審查、不是正式獨立稽核、不是採用裁決。
> 審查基線：本地 hardening 分支工作區；僅記錄可由檔案與命令直接支持的判定。

## 1. 審查識別

- Repository：`https://github.com/icashkin-cmyk/miko-manus-governance.git`
- Branch：`manus/governance-acceptance-hardening-v0.1.1`
- Commit：`7e141465cae99079c8f4a64d66649f83879a79d9`
- 審查者：本次 Manus 對話中的人工檢查流程（不可等同 INDEPENDENT_AUDITOR）
- Claude API：`BLOCKED`；既有阻塞紀錄：`evidence/skill-role-alignment-20261117/claude-independent-review-summary-20261117.md`

## 2. 三份候選逐項判定

| 候選 | 角色模型 | 原始內容保留 | 邊界／狀態 | 人工判定 |
|---|---|---|---|---|
| `manus-core` | `PROPOSED` 附錄將 Manus 定義為主手、Claude 審查者、ChatGPT 第二意見；但原正文仍保留 Claude 為總召、Manus 僅能寫入 knowledge-cards 的規則 | 有，且可追溯 | 有 `CONFLICT` 處理文字，但未提供可執行的單一權威優先順序來消除同檔矛盾 | `FAIL`（重大責任衝突） |
| `ai-behavior-emulation` 候選附錄 | Manus 主手、Claude 審查、ChatGPT 第二意見 | 有 | 有 `PROPOSED`、Runtime／正式採用未生效與自驗／獨立驗收分離文字 | `CONDITIONALLY_PASS`（內容邊界可接受；仍需 Claude 審查） |
| `thinking-tools-performance-optimization` 候選附錄 | Manus 主手、Claude 審查、ChatGPT 第二意見 | 有 | 明確保留效能不得犧牲正確性、資安、權限、資料新鮮度與停止／暫緩邊界 | `CONDITIONALLY_PASS`（內容邊界可接受；仍需 Claude 審查） |

## 3. 共同通過項目

- 三份候選均將責任模型放在附錄，並標記為 `PROPOSED`，沒有把候選文字直接宣稱為 Runtime 現行規則。
- 三份候選均保留原始 Skill 內容，符合累積式演進與歷史版本保護方向；本次未執行刪除或覆寫原始來源。
- 候選文字均保留 `UNKNOWN`、`NOT_RUN`、`BLOCKED` 或等價的證據不足處理，不以文件完整性宣稱 Runtime 已啟用。
- 人工檢查未發現三份候選把 ChatGPT 直接授予正式寫入或治理裁決權；其定位為第二意見。

## 4. 重大缺陷與影響

### 4.1 `manus-core`：FAIL

同一份候選檔同時保留兩套不可同時成立的角色模型：原正文仍寫 Claude 為治理總召、Manus 僅能寫入 `knowledge-cards/`；候選附錄則寫 Manus 可編輯專案內所有路徑，Claude 負責審查修訂。附錄另寫「衝突時標記 `CONFLICT`」，但沒有規定遇到這個具體衝突時哪一段具有執行優先權，因此 Runtime 或人工執行者仍可能依讀取順序採用不同權限。

**影響的 AC：** 角色唯一性、權限邊界、責任分離、可執行性與治理一致性。

**必要修正：** 不應只在檔尾追加第三套說法；應建立明確的候選角色模型正文，將舊角色模型保留於歷史／差異區，或逐條標成 `SUPERSEDED_PENDING_ADOPTION`，並明確聲明在正式採用前仍以既有正本為準。修正後必須重新送 Claude 審查與獨立冷讀。

### 4.2 其餘兩份：不得宣稱正式合格

`ai-behavior-emulation` 與 `thinking-tools-performance-optimization` 的候選附錄在責任模型與邊界上未見同等重大矛盾；但三份候選是同一組角色模型變更，`manus-core` 的衝突會影響兩份附錄的上位治理依據。因此這兩份只能記為 `CONDITIONALLY_PASS`，不能升格為正式採用或 Runtime 生效。

## 5. 證據與狀態分離

- 本地候選驗證：`evidence/skill-role-alignment-20261117/local-validation.json`；它只能支持本地自驗結果，不替代本報告的人工判斷。
- Claude API 獨立治理審查：`BLOCKED`；不得寫成 `PASS`。
- 本人工審查：完成，但不具備獨立驗收資格，因執行環境與候選製作工作區相同。
- Runtime 載入：`NOT_RUN`。
- 正式採用：`NOT_RUN`／未授權。
- GitHub Merge／Release／Tag：本次未執行。

## 6. 版本與雜湊

| 檔案 | SHA-256 |
|---|---|
| `knowledge-cards/proposals/skills/ai-behavior-emulation-manus-primary/SKILL.md` | `a34f7186e0a1921be5bc28166197e920666845aba498f69043ea0c4acd4144ae` |
| `knowledge-cards/proposals/skills/manus-core-manus-primary/SKILL.md` | `31f7393740fafe21769496ad72b83f8523c9d1b8e5d7bae3a1cbd0c988fdc8f3` |
| `knowledge-cards/proposals/skills/miko-governance-layer-acceptance/SKILL.md` | `73e5128b4b2bff301ef9cec6cafc03b39cd97465227d44e837d1d46d85a5cead` |
| `knowledge-cards/proposals/skills/thinking-tools-performance-optimization-manus-primary/SKILL.md` | `850caf8ea39c7c4a2ba91598dbeb3aa82aadaa91244aebd19f4617f352d231b3` |

## 7. 建議處理順序

1. 先修正 `manus-core` 的雙重角色模型與權限優先順序，保留原始版本及 diff。
2. 重新執行三份候選的本地格式、反向、負向、邊界、回歸與 Hash 驗證。
3. 在 Claude API 可用後，重新提交三份完整候選供 Claude 治理審查；API 失敗時維持 `BLOCKED`，不可自行改為 PASS。
4. Claude 審查後若有任何字詞變更，整包重新冷讀；再由獨立驗收者於不同執行環境重跑。
5. 在 MIKO 明確採用前，維持候選狀態，不搬入正式 Skill 路徑、不宣稱 Runtime 生效。

## 8. 任務四態

- 狀態：**完成但有疑慮**。人工審查已完成並發現 `manus-core` 重大衝突；Claude 獨立審查仍 `BLOCKED`，三份候選不可宣稱正式採用。
- 困難卡：現象＝Claude API 審查未完成；證據＝既有 Claude review summary；類別＝缺授權／服務阻塞；影響＝無法完成指定獨立治理審查；解除條件＝可用 Claude API 或由 MIKO 提供正式審查結果；負責方＝Claude API／MIKO；首次發現時間＝本輪。

