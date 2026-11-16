# miko-governance-layer-acceptance v0.1.0｜GPT／Claude 共用驗收索引

## 文件狀態

- 文件用途：提供 GPT 與 Claude 進行獨立冷讀、反向驗收與結果比對。
- 文件狀態：`LOCAL_ADOPTION_VALIDATED_PENDING_JOINT_AUDIT`
- 正式採用範圍：本地 Manus repository；不代表 GitHub Push、Merge、Release、正式 Tag 或 Runtime 啟用。
- 驗收原則：GPT／Claude 不直接接受 Manus 自述的 PASS，必須自行讀取檔案、自行確認 commit、自行執行必要測試並保存差異。
- Repository 根目錄：`<REPO_ROOT>`

## 核心驗收對象

| 類別 | 相對路徑 | 驗收用途 |
|---|---|---|
| 正式 Skill | `skills/miko-governance-layer-acceptance/SKILL.md` | 驗證 v0.1.0、ADOPTED、內容與 Runtime 邊界 |
| 候選原檔 | `knowledge-cards/proposals/skills/miko-governance-layer-acceptance/SKILL.md` | 驗證原候選仍保留且未被覆寫 |
| 來源封存 | `source-archive/miko-governance-layer-acceptance/SKILL.md` | 驗證來源快照與候選內容可追溯 |
| 採用紀錄 | `governance/formal-adoptions/miko-governance-layer-acceptance-v0.1.0.md` | 驗證採用範圍、回復方式與未啟用邊界 |
| Stage 1 inventory | `evidence/stage-01/skill-inventory-current.json` | 驗證 active Skill 總數 21、唯一名稱與 Hash |
| Stage 1 驗收器 | `tests/stage1_inventory_check.py` | 驗證 21 筆正式 Skill inventory |
| G0–G9 主驗收器 | `tests/governance_layer_acceptance_v01.py` | 驗證架構 Gate |
| G0–G9 獨立驗收器 | `tests/governance_layer_independent_audit_v01.py` | 由獨立驗收者重新判定 |
| G6 | `tests/g6_tools_acceptance.py` | Tools Contract 驗收 |
| G7 | `tests/g7_e2e_acceptance.py` | 端到端 Dry-run 驗收 |
| G8 | `tests/g8_independent_acceptance.py` | 獨立全體架構驗收 |
| G9 | `tests/g9_lifecycle_acceptance.py` | 本地候選生命週期與回復演練 |
| 原始 CI | `tests/check_repo.py` | C1–C16；C3 私密路徑命中必須為零 |
| 驗收前證據 | `evidence/governance-layer-v01/formal-adoption-audit-20261116/` | 保存採用前各項實際 stdout、stderr 與 scope |

## 建議獨立驗收命令

在 `<REPO_ROOT>` 執行：

```bash
python3 -I -B tests/stage1_inventory_check.py
python3 -I -B tests/g6_tools_acceptance.py
python3 -I -B tests/g7_e2e_acceptance.py
python3 -I -B tests/g8_independent_acceptance.py
python3 -I -B tests/g9_lifecycle_acceptance.py
python3 -I -B tests/governance_layer_acceptance_v01.py
python3 -I -B tests/governance_layer_independent_audit_v01.py
python3 -I -B tests/check_repo.py

git diff --check
git status --short
git rev-parse HEAD
sha256sum skills/miko-governance-layer-acceptance/SKILL.md \
  knowledge-cards/proposals/skills/miko-governance-layer-acceptance/SKILL.md \
  source-archive/miko-governance-layer-acceptance/SKILL.md
```

## 必須判定

1. `skills/miko-governance-layer-acceptance/SKILL.md` 的 frontmatter 必須含 `version: 0.1.0` 與 `status: ADOPTED`。
2. 候選原檔必須仍為 `PROPOSED`，不得被正式檔案反向覆寫。
3. 來源封存必須存在；其 Hash 應可與候選原檔比對。
4. Stage 1 active Skill 總數必須為 21，frontmatter name 必須唯一且與資料夾名稱一致。
5. `G0–G9`、`G6`、`G7`、`G8`、`G9` 與 `C1–C16` 必須以實際 Exit Code 0 判定；輸出中的 `PASS` 文字不能單獨作為證據。
6. C3 必須為零命中；若驗收證據重新產生本機路徑，應先去識別化再重跑，不得刪除原始 FAIL 證據。
7. Runtime、Push、Merge、Release、正式 Tag 必須維持 `NOT_RUN`，不得從本地驗收 PASS 推論已生效。
8. 任何 GPT／Claude 與 Manus 結論不一致時，保留雙方輸出，狀態降為 `CONFLICT`，不得自行裁決或覆寫。

## 角色分離

- `IMPLEMENTER`：Manus，負責本地升格與修正。
- `TESTER`：可由 GPT 或 Claude 依本索引自行執行測試。
- `INDEPENDENT_AUDITOR`：另一個未產生該測試結果的 GPT／Claude 工作串，必須冷讀並保存自己的命令、stdout、stderr、Exit Code、時間與 Hash。

## 證據回報欄位

每個驗收項目至少回報：`Test ID`、目的、對象路徑、repository、branch、commit SHA、環境、完整命令、stdout 路徑、stderr 路徑、Exit Code、執行時間、結果、與 Manus 結果差異。

`PASS` 只在實際 Exit Code 0 且 Acceptance Criteria 全部符合時使用；`UNKNOWN`、`NOT_RUN`、`BLOCKED` 不得轉換成 `PASS`。
