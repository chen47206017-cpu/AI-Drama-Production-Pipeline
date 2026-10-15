# 剧本/Skill二进制交付资产登记
## 已进库且可逐行审稿
- `scripts/CURRENT_E001-E064.md`（V23.33R1原文件SHA256已锁定）
- `scripts/episodes/E001.md`–`E064.md`
- `scripts/versions/V23.22R1.md`–`V23.33R1.md`（12版，哈希见 `manifests/verified_script_versions.json`）
- `skills/story-impact-v2.2/SKILL.md`（文字执行规则）
- `memory/portable_memory_v2.2.md`
- `audits/`下的审稿报告、台账与索引
## 待导入的二进制归档（非此PR已上传内容）
- V23.33R1完整Word剧本 `.docx`（约54页）
- Story Impact Skill v2.2 `.zip`（含脚本、参考资料、测试）
- V23.33R1研究报告Word `.docx`
- V23.33R1完整交付包 `.zip`
**注意：不能因为目录存在而声称以上二进制资产已上传GitHub。** 此项目先以已认证Markdown原文作为唯一可编辑源，Word/ZIP后续可经校验后存入 `assets/releases/V23.33R1/` 或GitHub Release，不能覆盖脚本。
## 安全与协作
- 不建议把私有源码打包公开发布；Release可保持在私有仓库中。
- 别的AI仅有只读权限时可出Issue；要写改稿须提供PR并经维护者审查。
- 资产哈希、大小和上传者记录应存 `manifests/binary_assets.json`，避免同名二进制覆盖。
