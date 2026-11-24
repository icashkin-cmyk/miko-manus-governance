# 三份 MIKO Skill 正式採用紀錄 v0.1.0

## 文件狀態

- 文件狀態：`FORMALLY_ADOPTED_LOCAL`
- 採用軸：`ADOPTED`
- Runtime：`NOT_RUN`；本紀錄不表示 Manus Runtime 已啟用。
- GitHub Merge／Release／正式 Tag：`NOT_RUN`。

## 採用人與範圍

- 批准人：MIKO
- 批准日期：2026-11-17（Asia/Taipei）
- 批准依據：MIKO 明確選擇 B 範圍，要求先完成歷史 C3 清理與三份 Skill 正式採用，再進行 Skill 盤點。
- Repository：`icashkin-cmyk/miko-manus-governance`
- Branch：`manus/governance-acceptance-hardening-v0.1.1`
- 範圍：`miko-flow-optimizer`、`miko-project-note-specialist`、`miko-prompt-optimizer`。

## 正式路徑

| Skill | 正式路徑 | 候選保留 | 原始來源封存 | Runtime |
|---|---|---|---|---|
| `miko-flow-optimizer` | `skills/miko-flow-optimizer/SKILL.md` | `knowledge-cards/proposals/skills/miko-flow-optimizer/SKILL.md` | `source-archive/miko-flow-optimizer/SKILL.md` | `NOT_RUN` |
| `miko-project-note-specialist` | `skills/miko-project-note-specialist/SKILL.md` | `knowledge-cards/proposals/skills/miko-project-note-specialist/SKILL.md` | `source-archive/miko-project-note-specialist/SKILL.md` | `NOT_RUN` |
| `miko-prompt-optimizer` | `skills/miko-prompt-optimizer/SKILL.md` | `knowledge-cards/proposals/skills/miko-prompt-optimizer/SKILL.md` | `source-archive/miko-prompt-optimizer/SKILL.md` | `NOT_RUN` |

## 採用限制

本次採用只建立本 repository 的正式 Skill 檔與可追溯沿革；不代表帳號端偏好、Claude、ChatGPT、Manus Runtime 或其他外部服務已自動載入。任何 Runtime 載入、外部 Connector、Merge、Release、Tag 或正式遠端發布均須另有實測證據。

## 驗收入口

- `tests/three_candidate_skills_validation.py`
- `tests/stage1_inventory_check.py`
- `tests/check_repo.py`
- `tests/history_c3_scan.py`

## 回復方式

刪除本次新增的三個正式 Skill 與採用紀錄，保留候選與來源封存；若涉及 Git 歷史，使用本次保存的原始 bundle 還原，不直接覆蓋目前工作樹。
