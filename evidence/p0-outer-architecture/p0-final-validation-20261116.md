# P0 外圈架構與 G01–G10 映射驗收

- 日期：2026-11-16
- IMPLEMENTER／TESTER：Manus
- 冷讀驗收：同一執行環境建立的獨立 Git clone；不是外部人員角色分離
- 範圍：GitHub `manus/initial-architecture-stage1-stage2-20261116` 的乾淨 clone；只驗收外圈與 G01–G10 路徑映射
- 來源附件：`source-archive/p0/Pasted_content_27.txt`
- 候選 commit：`dc3dd7281944e23346bc488e845c3a5b9df11d82`
- 採用軸：`PROPOSED`
- 正式採用：`NOT_ADOPTED`
- Runtime：`NOT_RUN`
- 原始 MIKO repository：未修改
- 遠端推送：本輪未執行

## 建立內容

- `governance/project-architecture/p0-outer-architecture.md`
- `governance/project-architecture/module-mapping.md`
- `governance/project-architecture/modules/core/README.md`
- `governance/project-architecture/modules/router/README.md`
- `governance/project-architecture/modules/registry/README.md`
- `governance/project-architecture/modules/tools/README.md`
- `governance/project-architecture/modules/lifecycle/README.md`
- `tests/p0_outer_architecture_check.py`
- `source-archive/p0/Pasted_content_27.txt`

## IMPLEMENTER／TESTER 實際命令

```bash
python3 -I -B tests/p0_outer_architecture_check.py
python3 -I -B tests/check_repo.py
git diff --check
```

結果：

```text
P0_SELF_CHECK_EXIT_CODE=0
POSITIVE=PASS
NEGATIVE_MAPPING_REMOVAL=PASS
NEGATIVE_STATUS_REMOVAL=PASS
BOUNDARY=PASS
REVERSE_MAPPING=PASS
OVERALL=PASS

CHECK_REPO_EXIT_CODE=0
C1-C16：16/16 PASS
C3 命中：[]

DIFF_CHECK_EXIT_CODE=0
```

## 冷讀驗收

冷讀副本重新建立於 `/tmp/miko-manus-governance-p0-cold-20261116`，讀取候選 commit `dc3dd7281944e23346bc488e845c3a5b9df11d82`，不接受原工作樹的輸出作為判定。

```text
COLD_P0_EXIT_CODE=0
POSITIVE=PASS
NEGATIVE_MAPPING_REMOVAL=PASS
NEGATIVE_STATUS_REMOVAL=PASS
BOUNDARY=PASS
REVERSE_MAPPING=PASS
OVERALL=PASS

COLD_CHECK_REPO_EXIT_CODE=0
C1-C16：16/16 PASS
C3 命中：[]

COLD_DIFF_CHECK_EXIT_CODE=0
```

## 判定

P0 外圈架構與 G01–G10 映射：`PASS_WITH_EVIDENCE`。

本判定包含「沒有的模組已建立候選承接」：Core、Router、Registry、Tools、Lifecycle 均已在 `governance/project-architecture/modules/` 建立契約。它們不是第二套治理核心；Router 不取代現行路由表，Registry 不取代 VERSION，Tools 不代表已連線，Lifecycle 不自行採用或合併。

本判定不代表：正式採用、Runtime 載入、工具已連線、Manus 已具備完整端到端能力、已推送遠端、已合併 `main`，或 Claude／其他角色已完成外部獨立治理裁決。

## 未完成與邊界

1. 真正外部角色分離的 `INDEPENDENT_AUDITOR` 尚未執行；本次冷讀只是獨立 Git clone 驗證。
2. 本輪候選尚未推送遠端。
3. 正式採用：`NOT_ADOPTED`。
4. Runtime：`NOT_RUN`。
5. 下一階段可進入 P1，但仍須另立 P1 驗收條件，不得把 P0 PASS 延伸成 P1 PASS。
