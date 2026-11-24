# GPT 十模組 × GitHub Manus 路徑映射

- 狀態：`PROPOSED`／`NOT_ADOPTED`
- 用途：將 GPT 建議的 G01–G10 映射至現有路徑或新建候選邏輯模組。
- 原則：映射不是 Runtime 啟用，不是正式採用，也不代表遠端已寫入。

| ID | GPT 模組 | GitHub 承接路徑 | 類型 | 唯一責任 | 驗收狀態 |
|---|---|---|---|---|---|
| G01 | Governance | `governance/` | 現有 | 治理規則、權限、Gate 與邊界 | PASS_WITH_EVIDENCE |
| G02 | Core | `skills/manus-core/`；契約 `governance/project-architecture/modules/core/` | 現有＋候選契約 | 核心規則與核心 Skill 的邊界 | PASS_WITH_EVIDENCE |
| G03 | Router | `governance/project-architecture/modules/router/`；實際調用仍依 `skills/manus-core/` 路由表 | 新建候選契約 | 定義選擇與路由，不執行工作 | PASS_WITH_EVIDENCE |
| G04 | Knowledge Cards | `knowledge-cards/` | 現有 | 知識卡、索引與候選提案 | PASS_WITH_EVIDENCE |
| G05 | Skills | `skills/` | 現有 | 可載入候選 Skill | PASS_WITH_EVIDENCE |
| G06 | Registry | `migration-ledger/`、`VERSION`、`MANUS_VERSION`；契約 `modules/registry/` | 現有＋候選契約 | 版本、來源、依賴與狀態索引 | PASS_WITH_EVIDENCE |
| G07 | Tools Specifications | `adapters/`；契約 `modules/tools/` | 現有＋候選契約 | 工具能力、權限與介接規格 | PASS_WITH_EVIDENCE |
| G08 | Tests | `tests/` | 現有 | 測試器、反向測試與回歸測試 | PASS_WITH_EVIDENCE |
| G09 | Evidence | `evidence/` | 現有 | 保存可重現命令、輸出、Exit Code 與 Hash | PASS_WITH_EVIDENCE |
| G10 | Lifecycle | `archive/`、`migration-ledger/`、`next-step/`；契約 `modules/lifecycle/` | 現有＋候選契約 | 建立、升級、候選、採用、退役、回復 | PASS_WITH_EVIDENCE |

## 不重複責任規則

- `modules/router/` 只定義路由契約，不取代 `skills/manus-core/` 的現行路由表。
- `modules/registry/` 只定義索引契約，不取代 `VERSION` 或正式來源。
- `modules/tools/` 只定義介接契約，不宣稱工具已連線或已授權。
- `modules/lifecycle/` 只定義生命週期契約，不自行採用、合併或發布。
- 五個新目錄都是候選架構層；存在不等於 Runtime 生效。
