# Stage 2｜資產分類人讀表

- 輸入 Gate：`G1 PASS`
- 記錄總數：20
- 主分類：全部為 `Skill`
- Runtime：全部 `UNKNOWN`
- 正式採用：全部 `CANDIDATE`
- 機讀原表：[`asset-classification.tsv`](asset-classification.tsv)
- 驗收：自驗 `PASS`；獨立驗收 `PASS`

| stable_id | secondary_role | canonical_path | source_path | owner | runtime_status | adoption_status |
|---|---|---|---|---|---|---|
| ai-engineering-anti-fraud-test-credibility | governance-skill | `skills/ai-engineering-anti-fraud-test-credibility/SKILL.md` | `source-archive/ai-engineering-anti-fraud-test-credibility/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| batch-task-completion-and-single-report | governance-skill | `skills/batch-task-completion-and-single-report/SKILL.md` | `source-archive/batch-task-completion-and-single-report/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| dghp-beauty | domain-skill | `skills/dghp-beauty/SKILL.md` | `source-archive/dghp-beauty/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| dghp-food | domain-skill | `skills/dghp-food/SKILL.md` | `source-archive/dghp-food/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| dghp-metaphysical-integrated-analysis | domain-skill | `skills/dghp-metaphysical-integrated-analysis/SKILL.md` | `source-archive/dghp-metaphysical-integrated-analysis/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| dghp-travel | domain-skill | `skills/dghp-travel/SKILL.md` | `source-archive/dghp-travel/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| dghp-work-handoff | workflow-skill | `skills/dghp-work-handoff/SKILL.md` | `source-archive/dghp-work-handoff/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| gmail-cleanup | domain-skill | `skills/gmail-cleanup/SKILL.md` | `source-archive/gmail-cleanup/` | IMPLEMENTER／領域邊界 | UNKNOWN | CANDIDATE |
| independent-audit | governance-skill | `skills/independent-audit/SKILL.md` | `source-archive/independent-audit/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| knowledge-card-format | governance-skill | `skills/knowledge-card-format/SKILL.md` | `source-archive/knowledge-card-format/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| label-foreign-text | domain-skill | `skills/label-foreign-text/SKILL.md` | `source-archive/label-foreign-text/` | IMPLEMENTER／領域邊界 | UNKNOWN | CANDIDATE |
| make-skill | governance-skill | `skills/make-skill/SKILL.md` | `source-archive/make-skill/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| miko-core | governance-skill | `skills/miko-core/SKILL.md` | `source-archive/miko-core/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| photo-inspection-log | domain-skill | `skills/photo-inspection-log/SKILL.md` | `source-archive/photo-inspection-log/` | IMPLEMENTER／領域邊界 | UNKNOWN | CANDIDATE |
| safe-implementation | workflow-skill | `skills/safe-implementation/SKILL.md` | `source-archive/safe-implementation/` | IMPLEMENTER／miko-core 邊界 | UNKNOWN | CANDIDATE |
| three-party-review | governance-skill | `skills/three-party-review/SKILL.md` | `source-archive/three-party-review/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| tw-alert-check | domain-skill | `skills/tw-alert-check/SKILL.md` | `source-archive/tw-alert-check/` | IMPLEMENTER／領域邊界 | UNKNOWN | CANDIDATE |
| tw-backtest-workflow | workflow-skill | `skills/tw-backtest-workflow/SKILL.md` | `source-archive/tw-backtest-workflow/` | IMPLEMENTER／停止領域邊界 | UNKNOWN | CANDIDATE |
| version-evolution-preservation | governance-skill | `skills/version-evolution-preservation/SKILL.md` | `source-archive/version-evolution-preservation/` | GOVERNANCE_OWNER＋三方證據隔離 | UNKNOWN | CANDIDATE |
| visual-content-intelligence | domain-skill | `skills/visual-content-intelligence/SKILL.md` | `source-archive/visual-content-intelligence/` | IMPLEMENTER／領域邊界 | UNKNOWN | CANDIDATE |

> TSV 的 tab 是機器欄位分隔符，不是內容縮排；提交時以 CSV/TSV parser、欄位數與上表交叉核對，不能用一般 whitespace linter 直接判定 TSV 內容錯誤。
