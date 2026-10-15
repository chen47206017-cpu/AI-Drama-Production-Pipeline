# 《双姝商途》GitHub导入核验状态（2026-10-16）

## 事实核验：已导入独立分支，尚未合并main

- V23.33R1整本 **64集/268场** Markdown：`scripts/CURRENT_E001-E064.md`、`scripts/versions/V23.33R1.md`，源 SHA256 `564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935`，Git blob `c507624f01f56aa2a4c5799ce0dd9fd415926738`，已校验一致。
- 逐集独立文件 `scripts/episodes/E001.md`–`E064.md`，由整本母稿直接拆分，未另行改写。
- 12版历史完整 Markdown：V23.22R1–V23.33R1。详见 `manifests/verified_script_versions.json` 和 `manifests/IMPORT_MANIFEST.md` 的SHA256/Git SHA双清单。
- 二进制原样存档 **4份已完成且哈希与本地原件匹配**：`releases/V23.33R1/V23.33R1_full_script_HOLD.docx`、`releases/V23.33R1/V23.33R1_audit_report_HOLD.docx`、`releases/V23.33R1/V23.33R1_complete_delivery_HOLD.zip`、`skills/story-impact-v2.2/Story_Impact_Adversarial_Audit_Skill_v2.2.zip`。
- 共用AI规范：`AGENTS.md`、`canon/PROJECT_CANON.md`、`CURRENT_PROJECT_POINTER.md`、`reviews/REVIEW_TEMPLATE.md`、`memory/portable_memory_v2.2.md` 等已上传。
- 审计：报告、差异、CSV/JSON记录、PGS HOLD清单和 `tools/validate_project.py` 源文件验证脚本均已上传。
- 在PR范围内检查：**所有新增路径均在 `projects/shuangshu-shangtu/`**，原仓库工程不被覆盖。

## 未导入/未证明的范围

- V23.21R1及更早历史工作稿、历次每轮的单独Word/ZIP资产，尚未逐项存档。已存入的是**12版完整Markdown历史母稿以及最新版本4个原样二进制文件**，不能称为“全部历史所有附件”。
- `main` 仍未合并。本批文件只处于Draft PR待审状态，其他AI需获私有仓库权限。
- Skill的旧版测试结果不能自动视为当前环境运行验证；需在克隆仓库后执行本项目验证脚本及Skill单元测试。
- PGS30仍为HOLD，120文历史来源、架空制度、真人150秒实际时长、首看留存仍需单独验证；市场SSS不能提前授予。

权威来源：`manifests/IMPORT_MANIFEST.md`；这份文件是**导入完成度说明**，不是Production Clean放行凭据。
