# GitHub导入核验状态｜2026-10-16

## 已确认写入独立分支（尚未合并main）
- 活跃完整母稿：`scripts/CURRENT_E001-E064.md` 与 `scripts/versions/V23.33R1.md`。
- 母稿原始SHA256：`564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935`；Git blob SHA：`c507624f01f56aa2a4c5799ce0dd9fd415926738`；完整64集。
- 逐集：`scripts/episodes/E001.md`–`E064.md`，均由同一完整母稿直接拆分，不重新创作。
- 历史全稿：`scripts/versions/V23.22R1.md`–`V23.32R1.md`，以已校验Git对象SHA存档；V23.33R1另有全稿版本快照。
- 协作约束：`AGENTS.md`、`canon/PROJECT_CANON.md`、`CURRENT_PROJECT_POINTER.md`、`reviews/REVIEW_TEMPLATE.md`、`reviews/README.md`。
- 审稿辅助：Skill v2.2 核心说明（`skills/story-impact-v2.2/SKILL.md`）、通用记忆协议、研究报告、变更索引、PGS未放行台账、真实diff。
- 主仓库原有项目文件未覆盖；新文件仅在 `projects/shuangshu-shangtu/` 下。

## 尚未作为GitHub二进制文件导入
- 最新Word成稿、原始Skill v2.2 ZIP完整压缩包（含脚本/测试/参考文件）、整套交付ZIP与历史Word/ZIP资产。
- 如需要所有原始二进制文件进入GitHub，必须另外通过Git LFS、Release asset、或具有二进制权限的上传方式导入。不能把单一SKILL.md视为已保存完整Skill ZIP。
- 更早的V23.21R1及以前历史正文尚未包含在已声明的22–33版本范围；另行按来源/哈希核验后可继续归档。

## 未完成生产验收
PGS30 HOLD；初始120文历史来源、大晟经营与身份制度、演员实测时长/用户观看留存仍未通过独立Release Assurance。

## 合并纪律
本次为审查PR，不自动合并main；缺失二进制/更早版本不得误写为“全部完成”。
