# 三個 Skill 角色對齊候選包

狀態：`PROPOSED`／`NOT_ADOPTED`／Runtime `NOT_RUN`。

本候選包依 MIKO 指示採用「Manus 主手、Claude 治理審查與必要修訂、ChatGPT 第二意見」模型。原始 Skill 不刪除、不覆寫；候選副本只供審查與測試，不自動取代現行 Runtime。

## 候選檔案

- `knowledge-cards/proposals/skills/manus-core-manus-primary/SKILL.md`
- `knowledge-cards/proposals/skills/ai-behavior-emulation-manus-primary/SKILL.md`
- `knowledge-cards/proposals/skills/thinking-tools-performance-optimization-manus-primary/SKILL.md`
- `source-manifest.json`

## 角色邊界

- `IMPLEMENTER`：Manus。
- `REVIEWER`：Claude，負責治理審查與必要修訂建議。
- `ADVISOR`：ChatGPT，提供第二意見與候選修訂建議。
- `INDEPENDENT_AUDITOR`：不得由產生被驗收結果的同一執行者兼任；同一者兼任時只能標 `SELF_REVIEW`。

## 未授予權限

本包不授予 Merge、正式採用、Release、正式 Tag、Runtime 啟用、外部服務寫入或永久權限。這些狀態維持 `NOT_RUN`／`NOT_ADOPTED`，直到完成獨立審查與 MIKO 明確裁決。
