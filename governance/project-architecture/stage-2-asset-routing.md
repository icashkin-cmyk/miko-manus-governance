# Stage 2｜資產分類與路徑架構

- stable_id：`stage-2-asset-classification-and-path-routing`
- 狀態：`PASS`（本 repo 內的分類與路徑結構驗收；不代表 Runtime 生效）
- 輸入 Gate：`G1 / Stage 1 = PASS`
- 驗收角色：`IMPLEMENTER` 產出、`TESTER` 執行、`INDEPENDENT_AUDITOR` 冷讀重驗
- 證據：`evidence/stage-02/asset-classification.tsv`、`stage2-summary.json`、`stage2-self-run.stdout`、`stage2-independent-audit.txt`

## 1. 分類規則

每個目前納入的 Skill 必須有且只能有一個 `primary_asset_type`。本階段 20 筆目前都是 `Skill`；`secondary_role` 只描述治理型、流程型或領域型用途，不得把 secondary role 誤當成第二個主資產。

| secondary_role | 判定範圍 | 主要邊界 |
|---|---|---|
| `governance-skill` | manus-core、make-skill、independent-audit、three-party-review、反造假、版本保護、批次完成制、知識卡格式 | 定義規則、驗收、版本與責任；不得自行宣稱正式採用或 Runtime 生效 |
| `workflow-skill` | dghp-work-handoff、safe-implementation、tw-backtest-workflow | 定義可重複工作流程；不得提高權限，不得繞過停止／暫緩領域 |
| `domain-skill` | 美妝、食物、命理、旅遊、Gmail、外文、照片、臺灣警報、視覺內容 | 只處理各自領域；不得取代 manus-core 治理，不得跨域擴權 |

## 2. 標準路徑

```text
skills/<stable_id>/SKILL.md       # 正在使用的候選 Skill 正文
source-archive/<stable_id>/       # 來源快照、來源 commit、來源 SHA-256
migration-ledger/<stable_id>.md   # 來源→候選→驗收版本沿革
 tests/<scope>/<stable_id>/        # 可重播測試與反例（若有）
evidence/<scope>/<stable_id>/      # stdout、stderr、exit code、時間與 hash
archive/<scope>/<stable_id>/       # 歷史版本、退役版本與 rollback target
adapters/<stable_id>/              # 只有存在介接需求時建立；不等於已啟用
knowledge-cards/<id>.md            # 任務卡；不是 Skill 的替代品
```

路徑選擇器只能依既有 stable ID、資產類型與責任欄位選擇路徑；不能因檔案名稱相近就合併兩個 Skill，也不能藉由改名繞過衝突檢查。

## 3. 任務與責任

- `IMPLEMENTER`：讀取來源與現況，建立分類列、保存來源與候選 hash，提出分類理由。
- `TESTER`：檢查 20 筆是否都有唯一 ID、主分類、canonical path、source path、test path、evidence path、owner，以及是否保留 `runtime_status=UNKNOWN`、`adoption_status=CANDIDATE`。
- `INDEPENDENT_AUDITOR`：不採信摘要中的 PASS，重新讀取 TSV、20 個 Skill 路徑與 20 個來源目錄，確認沒有漏列、重複、越權或 Runtime 成功宣稱。
- `GOVERNANCE_OWNER`：若出現同一能力多個主分類、刪除／取代既有 Skill、權限改變或不可逆路徑搬移，負責裁決；本階段不自行裁決。

## 4. 失敗出口與恢復

| 情況 | 狀態 | 動作 |
|---|---|---|
| Skill 檔不存在 | `FAIL` | 停止 G2，補齊來源或修正 inventory，不進下一 Gate |
| 來源快照不存在 | `NOT_READ`／`FAIL` | 建立來源快照與 hash；不以候選檔代替來源 |
| 主分類重複或分類衝突 | `CONFLICT` | 保留兩案與理由，交 GOVERNANCE_OWNER，不自行改名繞過 |
| Runtime 或採用被過度宣稱 | `FAIL` | 修正文案，保留 `UNKNOWN`／`CANDIDATE`，重跑驗證 |
| 測試未執行 | `NOT_RUN` | 不得升格 PASS，從第一個未完成步驟恢復 |

恢復時採增量修改：保留原始分類檔、失敗輸出與 diff，重建新版本後再次執行 Stage 2 自驗與獨立驗收。

## 5. 本階段限制

本階段只驗證本地資料分類與路徑責任。它沒有驗證 Manus Runtime 是否能載入任何 Skill，也沒有驗證外部工具、MCP、連線、權限或熱插拔。因此下列狀態維持 `UNKNOWN`：`installed`、`callable`、`executable`、`verified`、`adopted`、`runtime_read_back`。
