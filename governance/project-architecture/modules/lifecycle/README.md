# Lifecycle 模組候選契約

- ID：`G10`
- 現有承接：`archive/`、`migration-ledger/`、`next-step/`
- 狀態：`PROPOSED`／`NOT_ADOPTED`

## 責任

定義建立、候選、測試、獨立驗收、治理採用、發布、退役、回復與歷史保存的狀態轉移。

## 不負責

Lifecycle 不自行合併、推送、正式採用、刪除或改寫歷史；不可逆操作須依授權與確認流程。

## Acceptance Criteria

1. 每次變更保存來源、版本、diff、commit 與 SHA-256。
2. 舊版可追溯、可查閱、可回復。
3. `PASS`、`NOT_ADOPTED`、`NOT_RUN`、`BLOCKED` 等狀態不混用。
4. 任何狀態升格都有直接證據與授權來源。
