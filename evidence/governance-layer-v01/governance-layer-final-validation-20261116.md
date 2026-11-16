# MIKO｜Manus 治理架構逐層驗收報告 v0.1

## 結論

本輪已依使用者提供的 13 頁驗收單，建立並執行 G0–G9 逐層核對。**整體尚未合格，不能標記總體 PASS**。目前 G0、G1、G2、G5 通過；C1–C16 回歸已實際 `16/16 PASS`；獨立冷讀器的證據完整性檢查通過。G3、G6、G7、G8、G9 尚未完成所需實測；G4 發現 K03 穩定識別名的來源衝突，維持 `CONFLICT`。

## 驗收對象

- Repository：`icashkin-cmyk/miko-manus-governance`
- Branch：`manus/initial-architecture-stage1-stage2-20261116`
- Candidate HEAD：`f685fce52a3562d38c76f6bff2f65f44159dbfa1`
- MIKO 正本版本：`1.2.72`
- Manus 候選版本：`0.1.0-manus-candidate`
- 驗收單來源：使用者提供之 DOCX，Hash 保存於 `evidence/governance-layer-v01/checklist-docx.sha256`
- 驗收單原始檔採 `SOURCE_HASH_ONLY` 封存，未將二進位檔寫入 repository。

## G0–G9 結果

| Gate | 結果 | 實際證據 | 目前限制 |
|---|---|---|---|
| G0 | PASS | repository、branch、HEAD、VERSION、MANUS_VERSION、README、CHANGELOG 已讀取 | 僅代表基線身分完整，不代表正式發布 |
| G1 | PASS | `p0-outer-architecture.md`、`module-mapping.md`、Core/Router/Registry/Tools/Lifecycle 模組 README | 屬架構層核對 |
| G2 | PASS | `skills/miko-core/SKILL.md`、`stage-gates.md` | 屬治理契約與邊界核對 |
| G3 | NOT_RUN | Router 候選契約存在 | 尚無實際路由決策測試與 Runtime 讀回 |
| G4 | CONFLICT | K01 正式卡、K02–K50 候選卡索引與逐卡 Hash | K03 有兩個不同語意：任務優先級與資源配置／累積式演進與歷史版本保護；需 MIKO 決定穩定 ID |
| G5 | PASS（範圍限定） | 20 個 Skill、Stage 1 inventory、Stage 2 20 筆分類；兩個檢查器 Exit Code 0 | `RUNTIME_STATUS=UNKNOWN_FOR_ALL`，不宣稱 Runtime 實測 |
| G6 | NOT_RUN | `adapters/README.md`、Tools 模組契約 | 尚未執行外部 connector、授權、讀回與降級測試 |
| G7 | NOT_RUN | 尚無代表性端到端工作流執行器與原始輸出 | 不得以單元／靜態測試代替 E2E |
| G8 | NOT_RUN | 本輪已建立獨立冷讀器，且其證據完整性檢查 PASS | 完整 G8 依賴 G7 通過及真正獨立驗收者；目前只能算候選冷讀 |
| G9 | NOT_RUN | 候選 commit 與生命週期契約存在 | 尚未執行正式 tag、發布、遠端讀回、回復演練 |

## K01–K50 處理

- K01 原檔保留，未覆寫。
- K02 由既有 Manus 候選來源恢復為 `PROPOSED` 候選稿。
- K03–K50 由 `Pasted_content_24.txt` 逐字抽取至 `knowledge-cards/proposals/kcards/`，每張都有來源與 SHA-256。
- 候選來源 Hash 與 48 筆映射見 `evidence/governance-layer-v01/kcards/k03-k50-manifest.json`。
- K03 衝突見 `evidence/governance-layer-v01/kcards/K03-conflict.json`；未裁決前不把任何一方升為唯一正式 K03。
- 因此「50 個識別項已被盤點」不等於「K01–K50 已正式採用」。

## C3 修正與回歸

初次加入驗收證據後，C3 命中 Stage 1 產生的本機絕對路徑。已在最後重跑 Stage 1／Stage 2 後去識別化，再執行原始 `tests/check_repo.py`：

- Stage 1 Exit Code：0
- Stage 2 Exit Code：0
- C1–C16 Exit Code：0
- C3：`PASS`，命中 0
- 總計：`16/16 PASS`
- `git diff --check`：Exit Code 0

C3 去識別化只替換本機路徑表示，不改測試判定、來源語意或卡片正文。

## 獨立冷讀

`tests/governance_layer_independent_audit_v01.py` 直接重讀檔案、重新計算 K 卡數量、確認 K03 衝突紀錄，並重新執行 C1–C16；結果為 `OVERALL=PASS`。此 PASS 僅代表本輪證據完整性與不誤報檢查通過，**不把 G3、G4、G6、G7、G8、G9 的未完成項目改成 PASS**。

## 下一步（不可跳站）

1. 先由 MIKO 裁決 K03 穩定識別名；裁決前維持 `CONFLICT`。
2. 裁決後才重新建立 K03 唯一映射、跑 K01–K50 逐卡格式／來源／反例／回歸驗收。
3. 建立 Router 的正向、負向、邊界及衝突測試，並保存實際 stdout、stderr、Exit Code。
4. 在不需要外部授權的離線範圍先做 Tools contract 與 E2E dry-run；需要 connector 或 Runtime 的部分仍標 `NOT_RUN`，不可繞過授權。
5. 完成 G7 後再做真正獨立驗收 G8；G8 通過後才可規劃 G9 的發布、遠端讀回與回復演練。

## 邊界聲明

本報告與新增卡片均屬候選工作區內容；尚未正式採用、尚未 Runtime 生效、未建立正式 release tag，也未宣稱已合併或已推送 main。原始 MIKO repository 未修改。
