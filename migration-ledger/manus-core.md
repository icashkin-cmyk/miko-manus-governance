# Migration Record｜miko-core

- source_path: `skills/miko-core`
- source_commit: `ec80f473695305b35b90f0ebb941431ddde4626e`
- source_version: `1.2.72`
- source_skill_sha256: `80837c78032b2c8ade7d880d5f5ecd0df73c0683c30721eb4c686f4a579eae4d`
- source_baseline_archive: `PASS`
- active_candidate_rewrite: `NOT_RUN`
- reason: `miko-core` is retained as the read-only governance source baseline; no competing active core is created in this candidate package.
- semantic_rewrite: `NOT_RUN`
- independent_acceptance: `NOT_RUN`
- runtime_status: `UNKNOWN`
- candidate_status: `SOURCE_BASELINE_ONLY`

## 2026-11-17｜Manus 現行名稱對齊

- 現行 Skill 路徑由 `skills/miko-core/` 改名為 `skills/manus-core/`。
- 現行 frontmatter 名稱由 `miko-core` 改為 `manus-core`，版本內容沿用 v1.73，未刪除或改寫核心規則語意。
- 原始 MIKO 來源、`archive/`、`source-archive/` 與歷史驗收證據保留原名稱 `miko-core`，作為來源與歷史識別，不作為現行 Runtime 載入路徑。
- 本次改名屬識別與路徑對齊，不宣稱 MIKO 正本、Manus Runtime 或外部平台已自動同步。
