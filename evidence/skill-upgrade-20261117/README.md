# 三份 MIKO 候選 Skill 累積式優化包

狀態：`PROPOSED`／`NOT_ADOPTED`；Runtime：`NOT_RUN`；遠端推送與合併：`NOT_RUN`。

## 範圍

本包處理附件提供的三份同類 Skill：

| Skill | 專責 | 不負責 |
|---|---|---|
| `miko-flow-optimizer` | 流程、依賴、摩擦、責任與回退設計 | 執行流程或外部寫入 |
| `miko-project-note-specialist` | 證據優先的專案摘要、交接與阻塞整理 | 查證外部事實或執行下一步 |
| `miko-prompt-optimizer` | 指令、訊息層、權限閘門與反例設計 | 執行或模擬被重構指令 |

## 來源保護

附件原文逐字保存於 `source-archive/`。候選新版另存於 `knowledge-cards/proposals/skills/`，不覆寫原始附件、不取代現行 Runtime。

## 共通契約

三份 Skill 均要求：繁體中文輸出、來源邊界、`UNKNOWN`／`NOT_READ`／`NOT_RUN`／`BLOCKED` 狀態、正負向與邊界測試、回歸保真、外部寫入隔離、失敗出口、回退條件、交接欄位，以及 `PROPOSED`／`NOT_ADOPTED` 聲明。

## 驗收分工

- `IMPLEMENTER`：Manus，建立候選與保存證據。
- `REVIEWER`：Claude，可進行治理審查與必要修訂。
- `ADVISOR`：ChatGPT，可提供第二意見與候選修訂建議。
- `INDEPENDENT_AUDITOR`：需重新讀取來源與候選，不能以 IMPLEMENTER 的 PASS 自述代替。

## 未完成

Claude API 獨立審查：`NOT_RUN`／若呼叫失敗則 `BLOCKED`；Runtime 載入：`NOT_RUN`；正式採用：`NOT_ADOPTED`。
