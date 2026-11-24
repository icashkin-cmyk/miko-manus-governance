# Manus-core 角色模型修訂驗收報告

- 狀態：`PROPOSED`／`NOT_ADOPTED`
- 修訂目標：將候選責任模型統一為 Manus 主手、Claude 治理審查與必要修訂、ChatGPT 第二意見。
- 實際執行者：Manus 本地驗證流程。
- Claude API 獨立治理審查：`BLOCKED`；既有紀錄見 `claude-independent-review-summary-20261117.md`。
- Runtime 載入：`NOT_RUN`。
- GitHub Merge／Release／正式 Tag：`NOT_RUN`。

## 修訂內容

1. `knowledge-cards/proposals/skills/manus-core-manus-primary/SKILL.md` 的候選 §6 改為唯一角色模型：Manus／IMPLEMENTER、Claude／REVIEWER、ChatGPT／ADVISOR，並明確分離 `INDEPENDENT_AUDITOR`。
2. §6.1 固定候選建立、Claude 審查修訂、ChatGPT 第二意見、獨立冷讀與 MIKO 採用裁決的順序。
3. 舊版 §6 及相鄰治理條款逐字保存於 `knowledge-cards/proposals/skills/manus-core-manus-primary/references/historical-role-model-v1.73.md`，標記 `SUPERSEDED_PENDING_ADOPTION`。
4. 移除候選正文殘留的「Manus 只能寫入 knowledge-cards」及「程式 repo 由 Claude 單一寫入」矛盾；候選模型改為 Manus 可編輯本專案任何路徑，但不因此取得自動推送、合併、正式採用或 Runtime 權限。
5. `source-manifest.json` 的來源欄位改為相對、去識別化路徑；來源 SHA-256 不變，候選 SHA-256 依修訂後內容更新。

## 實際驗證結果

| 檢查 | 命令／證據 | 結果 |
|---|---|---|
| 三份候選 Skill 格式 | `quick_validate.py --path`，三份各自 Exit 0 | `PASS` |
| manus-core 角色冷讀 | 角色唯一性、責任、獨立驗收、候選狀態與歷史保留逐項檢查，Exit 0 | `PASS` |
| C1–C16 工作樹檢查 | `python3 -I -B tests/check_repo.py`，Exit 0 | `PASS` |
| 目前工作樹本機路徑 | 去識別化後掃描 | `PASS` |
| 完整 Git 歷史 C3 | `tests/history_c3_scan.py`，277 commits、4 hits、Exit 1 | `FAIL`／既有歷史阻塞 |
| Claude API 審查 | 既有多次實際呼叫紀錄 | `BLOCKED` |

## 歷史 C3 困難卡

- 現象：完整歷史 C3 掃描發現 4 筆本機路徑命中。
- 證據：`out/acceptance/history-c3/history-c3.json`；命中均在既有 commit 的 `evidence/skill-role-alignment-20261117/source-manifest.json`。
- 類別：缺資料／歷史清理需另行裁決。
- 影響哪個 AC：公開歷史不得含本機路徑；因此整體 C3 歷史驗收不能標 `PASS`。
- 解除條件：另行確認完整備份、重寫範圍、force-with-lease 目標與遠端回讀，之後重新掃描；本輪不自動重寫共同祖先歷史。
- 負責方：MIKO／Repository 維護者裁決歷史重寫；Manus 可在明確授權後執行。
- 首次發現時間：2026-11-17 15:57（Asia/Taipei）。

## 判定

本次角色模型修訂的現行候選內容與 C1–C16 已通過；完整歷史 C3 與 Claude API 審查仍未通過。因此本包判定為：**局部合格，整體 `BLOCKED`；不可宣稱正式採用、正式上線或 Runtime 生效。**
