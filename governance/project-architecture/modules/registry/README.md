# Registry 模組候選契約

- ID：`G06`
- 狀態：`PROPOSED`／`NOT_ADOPTED`
- Runtime：`NOT_RUN`

## 責任

索引 Skill、Knowledge Card、架構模組的 stable ID、版本、來源、commit、SHA-256、依賴、狀態與退役／回復位置。

## 不負責

Registry 不自行決定採用、不修改正本、不以最新日期覆蓋權威、不刪除歷史版本。

## Acceptance Criteria

1. 每筆資產有唯一 stable ID。
2. 版本、來源與 hash 可追溯。
3. `PROPOSED`、`NOT_ADOPTED`、`NOT_RUN`、`UNKNOWN` 不得升格為正式狀態。
4. 缺資料時標 `NOT_READ` 或 `UNKNOWN`。
