# Manus 內建 Skill 授權與平台依賴風險審查

- 審查時間：2026-11-22T03:28:18+00:00
- 實際讀取數量：63
- 使用者前次盤點數量：61（本輪環境更新後重新盤點，實際為 63）
- 審查類型：唯讀靜態掃描，不是法律意見，也不是 Runtime 可移植性證明。
- 來源：`/home/ubuntu/skills`

## 分級規則

| 分級 | 判定 | 可否直接匯入 |
|---|---|---|
| `PLATFORM_DEPENDENT_OR_MANAGED` | 命中 Manus／Runtime／MCP／Connector／平台目錄／平台工具或平台管理詞彙 | 不可直接匯入；需建立 MIKO adapter 或重寫候選，保留平台依賴 |
| `EXTERNAL_SERVICE_DEPENDENT` | 主要依賴 GitHub、Google、Claude、搜尋、外部 API 或其他外部服務 | 不可宣稱獨立可用；需核對服務授權、連線、帳號與失敗出口 |
| `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 靜態掃描未發現上述平台／服務依賴，但授權仍未完整確認 | 只能列為候選研究對象，不可直接再散布 |

## 統計

| 項目 | 數量 |
|---|---:|
| 實際內建 Skill | 63 |
| 平台／管理依賴 | 50 |
| 外部服務依賴 | 4 |
| 可能可移植但授權未確認 | 9 |
| Skill 目錄找到 LICENSE／NOTICE | 3 |
| Skill 目錄未找到 LICENSE／NOTICE | 60 |

## 逐項分級

| # | Skill | 第一個 H1 | 授權檔狀態 | 風險分級 | 命中類別 | SHA-256 |
|---:|---|---|---|---|---|---|
| 1 | `ai-behavior-emulation` | 人工智慧行為研究與程式設計效法 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `d2f35a66de7fe562…` |
| 2 | `automation-and-scheduling` | Automation and Scheduling | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector | `e7f178550696b4f1…` |
| 3 | `builtin-llm-models` | Built-in LLM Models | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api, sensitive_or_auth | `2986d57a278e8066…` |
| 4 | `claude-md-improver` | CLAUDE.md Improver | LICENSE_NOT_FOUND_IN_SKILL_DIR | `EXTERNAL_SERVICE_DEPENDENT` | external_cli_api | `b06c7420be08ca1c…` |
| 5 | `content-gap-analysis` | Content Gap Analysis | LICENSE_NOT_FOUND_IN_SKILL_DIR | `EXTERNAL_SERVICE_DEPENDENT` | external_cli_api, sensitive_or_auth | `c3617335e7012b93…` |
| 6 | `data-analysis` | Data Analysis | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api | `efedd3cc04edd0b6…` |
| 7 | `data-api` | Manus Data API | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `f59c98c040f5a0db…` |
| 8 | `data-backup-restoration` | Data Backup and Restoration | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `90474ee9ed38b6a3…` |
| 9 | `deep-research` | Deep Research | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api | `b69aefe8fab86861…` |
| 10 | `excel-generator` | Excel Generator Skill | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `68cede7c84566524…` |
| 11 | `excel-playbooks` | Excel Playbooks (Manus for Excel) | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `b2c049f20d6eb62e…` |
| 12 | `finance-pro-playbooks` | Finance Pro Playbooks | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `dcba4c099f6da75b…` |
| 13 | `financial-analysis` | Financial Analysis | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding | `1cc6333fd670765f…` |
| 14 | `game-asset-catalog` | Game asset catalog | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector | `1e2e3fce4b25f617…` |
| 15 | `git-attribution` | Git Attribution | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `14096a3a040bade1…` |
| 16 | `github-authentication` | GitHub Authentication v0.1.0-candidate | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, external_cli_api, sensitive_or_auth | `e9856b276bcaf065…` |
| 17 | `github-gem-seeker` | GitHub Gem Seeker | LICENSE_NOT_FOUND_IN_SKILL_DIR | `EXTERNAL_SERVICE_DEPENDENT` | external_cli_api | `05042dca5df6d1af…` |
| 18 | `github-integration` | GitHub Integration | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, external_cli_api | `1490a0b29fdeea4d…` |
| 19 | `google-workspace-integration` | Google Workspace Integration | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, external_cli_api | `eac6329fa929df7e…` |
| 20 | `gws-best-practices` | gws CLI Best Practices | LICENSE_NOT_FOUND_IN_SKILL_DIR | `EXTERNAL_SERVICE_DEPENDENT` | external_cli_api | `9014cd7ba5bce3cd…` |
| 21 | `handoff` | Handoff | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, sensitive_or_auth | `705386611638c16e…` |
| 22 | `image-processing` | Image Processing | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `1ed414ba7bead8a9…` |
| 23 | `imagegen` | ImageGen Manus | LICENSE_FILE_PRESENT | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `bdbf86931215b8e4…` |
| 24 | `internet-skill-finder` | Internet Skill Finder | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | mcp_connector, filesystem_binding, external_cli_api | `aaf9a176a9ff39a1…` |
| 25 | `keyword-research` | Keyword Research | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, external_cli_api | `a90fe02197aaf63b…` |
| 26 | `manus-api` | Manus API Integration Guide | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `4f4f651b3df5c8f3…` |
| 27 | `manus-config` | manus-config | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `5a659a3c043c1103…` |
| 28 | `manus-tasks` | Manus Tasks Addon | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `189c8254984f5329…` |
| 29 | `miko-document-upgrade-audit` | MIKO 文件升級與核對 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `6f4c890b92008086…` |
| 30 | `miko-src-core-rules` | MIKO SRC 核心規則草擬器 v0.2 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `ab029b42ce7ddeeb…` |
| 31 | `miko-universal-skill-contract` | MIKO 統一 Skill 契約與路由治理 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `488bffa96c4414bb…` |
| 32 | `miko-w1-w7-compatibility-audit` | MIKO W1～W7 相容性稽核 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `1854846a15cb27ef…` |
| 33 | `music-prompter` | Music Generation Prompt Guide | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `247d7d71caa168ff…` |
| 34 | `office` | Office files in Manus | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector | `9d4562ad94b6f4f6…` |
| 35 | `office-documents` | Office documents | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | filesystem_binding, external_cli_api | `7e17a2b692a21d7c…` |
| 36 | `payment` | Payment | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `f7bad2306f20ea4a…` |
| 37 | `performance-optimization` | Performance Optimization | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | mcp_connector, external_cli_api | `82af71540457cf85…` |
| 38 | `persistent-computing` | Persistent Computing | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, sensitive_or_auth | `32a9d7878a7d1fe1…` |
| 39 | `read-special-images` | Read Special Images | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `ee8e68e20ec3a687…` |
| 40 | `scrapling` | Scrapling 网页抓取 Skill | LICENSE_FILE_PRESENT | `PLATFORM_DEPENDENT_OR_MANAGED` | mcp_connector, sensitive_or_auth | `5be2707ed7dd50fd…` |
| 41 | `session-self-config` | Session Connector Configuration | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector | `66cdc1b45e2c118c…` |
| 42 | `similarweb-analytics` | SimilarWeb Analytics | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, filesystem_binding, external_cli_api | `81e1c6c8f61d17ad…` |
| 43 | `skill-creator` | Skill Creator | LICENSE_FILE_PRESENT | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, filesystem_binding, sensitive_or_auth | `9396beafe1f61b0e…` |
| 44 | `slack-mcp-guide` | Slack MCP Guide | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `749a3217522e8027…` |
| 45 | `slides` | Slides | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector | `9d6c7d3597a6da13…` |
| 46 | `stock-analysis` | Stock Analysis | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `18901593a0b014c1…` |
| 47 | `support-policy` | Support Policy | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `2d8b449f23704885…` |
| 48 | `system-settings-playbooks` | System Settings Playbooks (Manus for System Settings) | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, sensitive_or_auth | `db9a5cbab5366963…` |
| 49 | `tailscale-network` | Connect a computer to Tailscale | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `19de6b79badd6ee3…` |
| 50 | `thinking-tools-performance-optimization` | 八工具效能最佳化 | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `5bfe2dce504bd51c…` |
| 51 | `touchpoint-contacts` | Touchpoint Contacts | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `594dcbab8cda5210…` |
| 52 | `triggers` | Triggers | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `03821e47d670a79a…` |
| 53 | `trip` | Trip.com deals | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, sensitive_or_auth | `e6b60607e1c26ae9…` |
| 54 | `tts-prompter` | TTS Prompter | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `e4c143aa8d52141e…` |
| 55 | `typst-pdf-maker` | Typst PDF Maker | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `4cb53837ce7835bf…` |
| 56 | `video-generation` | Video Generation | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `a37771e853b000ea…` |
| 57 | `visual-content-intelligence` | Visual Content Intelligence | LICENSE_NOT_FOUND_IN_SKILL_DIR | `POTENTIALLY_PORTABLE_BUT_LICENSE_UNVERIFIED` | 無平台／服務模式命中 | `f3c071ebb89b55c0…` |
| 58 | `webdev` | Webdev | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding, external_cli_api, sensitive_or_auth | `4432383dcd6ce4a1…` |
| 59 | `webdev-seo` | Website SEO | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime | `35312346500ee708…` |
| 60 | `webdev-worklocally` | Webdev Work Locally | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, filesystem_binding, external_cli_api, sensitive_or_auth | `e8bfd082796b6c27…` |
| 61 | `website-traffic-checker` | Website Traffic Checker | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, external_cli_api, sensitive_or_auth | `5f71dbe5d197ca9c…` |
| 62 | `workflow-composer` | Workflow Composer | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, mcp_connector, filesystem_binding | `61b6b1dc44e4fe44…` |
| 63 | `youtube-video-research` | YouTube Video Research | LICENSE_NOT_FOUND_IN_SKILL_DIR | `PLATFORM_DEPENDENT_OR_MANAGED` | platform_runtime, external_cli_api | `95dfb03b78cd5a1e…` |

## 授權判定

- `LICENSE_FILE_PRESENT` 只代表在該 Skill 目錄找到名稱以 LICENSE、NOTICE 或 COPYING 開頭的檔案；不代表已完成條款解讀，也不代表允許改名、再散布或商業使用。
- `LICENSE_NOT_FOUND_IN_SKILL_DIR` 代表本次在各 Skill 目錄內沒有找到這類檔案；不代表著作權不存在，也不代表一定禁止使用。
- 在完成來源提供者、條款、著作權聲明、第三方依賴與再散布條件核對前，一律標示 `LICENSE_UNKNOWN`。

## 平台依賴判定

- 靜態命中 `manus`、`runtime`、`MCP`、`Connector`、`/home/ubuntu`、平台專用 CLI、平台管理目錄等，只能證明文件文字存在相關引用，不能單獨證明每個功能在離線環境一定不可執行。
- 要宣稱可移植，仍須完成工具替代、環境變數、權限、正向、負向、邊界、失敗出口與回歸測試。
- 具有金融、付款、帳號、Token、OAuth、Connector 或外部寫入依賴的 Skill，不應被直接包裝成「MIKO 自有獨立 Skill」；應改成 `MIKO adapter` 或 `MIKO candidate fork`。

## 建議的 MIKO 匯入狀態

- 原始平台副本：`SOURCE_SNAPSHOT_ONLY`。
- 授權未確認：`LICENSE_UNKNOWN`。
- 平台依賴未解除：`PLATFORM_DEPENDENT`。
- 已完成 MIKO 重寫但未正式採用：`MIKO_CANDIDATE`。
- 已經過必要 Gate 且獲 MIKO 決策：才可另行標示正式採用；本次沒有任何內建 Skill 達到此狀態。

## 本次限制

- 未複製 63 個平台 Skill 的正文到 MIKO 專案。
- 未修改 `/home/ubuntu/skills` 平台管理內容。
- 未宣稱取得任何平台 Skill 的著作權或再散布權。
- 未執行每個 Skill 的 Runtime 實測；本報告不能取代可用性驗收。
- 未執行外部 Connector 登入、OAuth 或付費服務授權測試。
