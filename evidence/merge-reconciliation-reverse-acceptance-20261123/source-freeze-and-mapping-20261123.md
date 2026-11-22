# Source Freeze and Bidirectional Mapping

## Task freeze

- MERGE_TASK_ID：`merge-reconciliation-reverse-acceptance-20261123`
- 目標：建立並驗收合併／彙整風險與反向驗收 Skill。
- 目標候選：`skills/governance-merge-reconciliation-reverse-acceptance/SKILL.md`
- 非範圍：Project Settings 寫入、Manus Runtime 啟用、正式 Merge、Release、Connector 寫入。
- EXPECTED：1 個候選 Skill、1 個離線行為驗收器、1 組驗收證據與 1 份正式採用前 mapping。
- ACTUAL：候選 Skill 1、驗收器 1、證據目錄 1、mapping 1。
- UNIQUE：候選 Skill 1、驗收器 1。
- 缺件：Runtime 載入／觸發／讀回證據；維持 `NOT_RUN`。
- 多件：無。

## Source inventory and authority order

| ID | 來源 | 用途 | 權威層級 | 讀取狀態 |
|---|---|---|---|---|
| S01 | 使用者本輪要求：將主要風險、防範措施與反向測試整合成 Skill | 定義目標與範圍 | 使用者當次要求 | READ |
| S02 | `skills/skill-creator/SKILL.md` | Skill frontmatter、建立、驗證與交付規則 | 平台 Skill 建置規範 | READ |
| S03 | `skills/independent-audit/SKILL.md` | 冷讀、重跑、反證與獨立性限制 | 專案治理 Skill | READ |
| S04 | `skills/three-party-review/SKILL.md` | IMPLEMENTER／TESTER／INDEPENDENT_AUDITOR 分離 | 專案治理 Skill | READ |
| S05 | `skills/batch-task-completion-and-single-report/SKILL.md` | 範圍凍結、完整清單與整批判定 | 專案治理 Skill | READ |
| S06 | `skills/manus-core/SKILL.md` | 權限、狀態、停止、採用與 Runtime 邊界 | 核心治理候選 | READ |
| S07 | `tests/governance_merge_reconciliation_reverse_acceptance.py` | 可重播離線行為驗收 | 本次候選測試器 | READ／UPDATED |
| S08 | G9 本地生命週期輸出 | archive、回復、候選 tag 與遠端身分證據 | 本次執行證據 | READ |

權威衝突處理：S01 定義本輪目標；S06 管理權限與正式狀態；S02 管理 Skill 格式；S03～S05 管理驗收責任。若同層來源衝突，維持 `CONFLICT`，不得靜默覆蓋。

## Source-to-candidate mapping

| Source ID | 原始要求／規則原子 | 候選位置 | 分類 | 覆蓋狀態 |
|---|---|---|---|---|
| S01 | 主要風險與防範措施做成 Skill | SKILL.md §2、§7 | ADD | PASS |
| S01 | 與反向測試整合 | SKILL.md §8、RT-01～RT-12 | ADD | PASS |
| S01 | 特別處理合併／彙整衝突 | SKILL.md §5～§7 | ADD | PASS |
| S01 | 規則遺漏、語意衝突、責任重疊 | SKILL.md §7、RT-01～RT-02 | ADD | PASS |
| S01 | 舊版／新版覆蓋與歷史保留 | SKILL.md §6、§7、RT-04、§11 | ADD | PASS |
| S01 | 權限邊界放寬與候選誤升格 | SKILL.md §7、RT-03、RT-05、RT-06 | ADD | PASS |
| S01 | 路由、Settings、Runtime 不一致 | SKILL.md §3、§7、RT-07、RT-08 | ADD | PASS_WITH_RUNTIME_GAP |
| S01 | 部分成功、回復、重複執行與無限重試 | SKILL.md §7、§10、RT-09～RT-12 | ADD | PASS |
| S02 | frontmatter 必須有 name／description | SKILL.md frontmatter | INHERIT | PASS |
| S02 | 使用 quick_validate.py | evidence/quick_validate-final.txt | INHERIT | PASS |
| S03 | 冷讀、重跑、不得把自評當獨立驗收 | SKILL.md §4、§14；本次 independent audit | INHERIT | PASS |
| S04 | 角色分離與獨立性揭露 | SKILL.md §4、§14 | INHERIT | PASS |
| S05 | 範圍凍結、總數與完整報告 | 本文件 Task freeze；acceptance-report.md | INHERIT | PASS |
| S06 | UNKNOWN／NOT_RUN／BLOCKED 不得升格 PASS | SKILL.md §10、§12；離線測試 | INHERIT | PASS |
| S06 | 下單／交易／Broker／LIVE 硬禁止 | SKILL.md §3；RT-03、RT-05、RT-06 | INHERIT | PASS_WITH_RUNTIME_GAP |
| S06 | 台指期 STOPPED_BY_USER、回測 PAUSED_BY_USER | SKILL.md §3 | INHERIT | PASS_WITH_RUNTIME_GAP |

## Candidate-to-source reverse mapping

候選正文的核心章節均可回指來源：§1～§4 回指 S01、S02、S03、S04、S05、S06；§5～§8 回指 S01、S05、S06；§9～§14 回指 S02～S06。新增的 RT-01～RT-12、風險矩陣與固定輸出格式是 S01 的新增實作，不宣稱來自未讀取來源。

## Mapping conclusion

- 來源→候選：完整覆蓋；Runtime 相關項目保留 `NOT_RUN` 缺口。
- 候選→來源：完整可回指或標明 `ADD`。
- 未裁決衝突：無。
- 可回復：原始初始化模板、候選 Skill、Diff、Hash 與測試證據均保留。
