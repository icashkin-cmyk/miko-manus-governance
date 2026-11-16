# Project Architecture｜專案架構與路徑責任

- stable_id：`miko-manus-project-architecture`
- 狀態：`CANDIDATE`
- 來源：MIKO 正本 v1.2.72；Manus 專案版本 0.1.0-manus-candidate
- 責任：定義本 repo 的資料夾、規則、任務、邊界、Gate 與證據保存，不宣稱 Runtime 生效。

## 路徑責任矩陣

| 路徑 | 主責 | 內容 | 禁止越界 |
|---|---|---|---|
| `governance/` | `GOVERNANCE_OWNER` | 規則、角色、Gate、權限、衝突處理 | 不執行領域任務、不冒充 Runtime |
| `skills/` | `IMPLEMENTER` | 候選 Skill 正文與資源 | 不直接宣稱正式採用；升級不得覆蓋歷史 |
| `source-archive/` | `IMPLEMENTER` | 來源快照、來源 hash、讀取日期 | 不修改快照內容 |
| `migration-ledger/` | `IMPLEMENTER`／`TESTER` | 逐筆移轉與升級紀錄 | 不刪失敗、不得將舊證據改成 PASS |
| `tests/` | `TESTER` | 驗證器、正反例、邊界、回歸、Mutation | 測試程式不可自行產生通過結論代替輸出 |
| `evidence/` | `TESTER`／`INDEPENDENT_AUDITOR` | 真實執行證據與 hash | 不保存只有宣稱沒有命令的摘要作唯一證據 |
| `archive/` | `IMPLEMENTER` | 歷史版本、退役與回復 | 不因新版而刪除舊版 |
| `adapters/` | `IMPLEMENTER` | 介接候選、資料契約、限制 | 不自行建立外部授權 |
| `knowledge-cards/` | Manus 總召範圍 | 任務卡與提案 | 不取代正本或正式裁決 |

## 階段 Gate

```text
G0 baseline-and-scope
  -> G1 capability-inventory
  -> G2 asset-classification
  -> G3 concept-to-capability
  -> G4 skill-gap-analysis
  -> G5 external-skill-intake
  -> G6 intent-to-execution
  -> G7 quality-and-e2e-acceptance
  -> G8 lifecycle-and-recovery
```

每個 Gate 的完成條件必須包含：輸入、輸出、角色、證據、失敗出口、回復方式、回歸測試與獨立驗收。上一 Gate 未 PASS 時，下一 Gate 最多只能是 `NOT_READY`。

## 三方責任隔離

`IMPLEMENTER` 可以修改候選；`TESTER` 必須重新執行測試；`INDEPENDENT_AUDITOR` 必須自行讀取與驗證。任何一方都不得以另一方的摘要取代自己的證據。若三方由同一執行環境完成，仍要保留三份不同責任的執行紀錄，並明確標示此限制。

## 累積式演進

所有 Skill、規則、架構與測試均採 `原始版本 → 分析版本 → 升級候選 → 驗收版本`。每次修改保存 diff、理由、影響、回復目標與 SHA-256；刪除／廢止／覆寫需明確授權，未知時保留並標記 `UNKNOWN`。
