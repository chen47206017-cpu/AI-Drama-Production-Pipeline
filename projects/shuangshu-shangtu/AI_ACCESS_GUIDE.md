# 外部 AI 读取指南 / External AI Access Guide

## 0. 最重要：仓库主页不是最新剧本入口

- 仓库：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline
- **当前主分支 main 有较早 V23.5R1 文件；V23.33R1 在独立导入分支，PR #1 尚待人工审核。**
- 最新整本固定快照（commit permalink）：
  https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md
- 最新分集导航（branch link）：
  https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/EPISODE_INDEX.md
- 全部项目协作规则：
  https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/AGENTS.md
- 机器可读入口：
  https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/AI_INDEX.json
- 可复制审查提示词：
  https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/EXTERNAL_AI_REVIEW_PROMPT.md

GitHub 官方文档说明其 Code Search 只索引默认分支。**搜索不到 V23.33R1 并不代表它不存在。** 不要用搜索引擎查询标题替代访问精确文件路径。

## 1. 方法 A — 具有 GitHub 连接器的 AI（推荐）

连接有仓库读取权限的 GitHub 账号，指定仓库名 `chen47206017-cpu/AI-Drama-Production-Pipeline`、精确分支 `ai-import/shuangshu-v23.33r1-20261016`，按 `AI_INDEX.json` 中的源文件路径读取；若支持按 commit 固定，则使用 `3130043f68a85411c8e1e5832296ad4e302178bd`。必须验证母稿 Git blob SHA 为 `c507624f01f56aa2a4c5799ce0dd9fd415926738`。

优先读：`CURRENT_PROJECT_POINTER.md` → `AGENTS.md` → `canon/PROJECT_CANON.md` → `scripts/CURRENT_E001-E064.md` → `skills/story-impact-v2.2/SKILL.md` → `audits/OPEN_GATES.md`。

## 2. 方法 B — 只能浏览网页的 AI

直接打开上方完整母稿的 **blob/commit** 地址，不要先搜索项目名。若 GitHub 网页内容提取失败，可尝试同一快照的原始文本地址：

`https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md`

若页面输出被截断，改为从 [EPISODE_INDEX.md](EPISODE_INDEX.md) 逐集取回，每8集为一批。读取全64集，并记录每集是否确实获得内容。请注意：无法使用某网站的浏览器并不等于 GitHub 文件不存在。

## 3. 方法 C — 不能打开 GitHub 的 AI

要求用户上传 V23.33R1 整本 Markdown / Word 或8批逐集文本；如果无法上传或读取，**如实声明未取得原文，停止基于旧版的“全文审查”**。

## 4. 真实性自查

- 正文版本标题必须包含 `V23.33R1`
- 第一集标题：`E001《走错一扇门》`
- 末集标题：`E064《这条街，照常开门》`
- 末尾标记：`【全剧终】`
- 共 **64 集 / 268 场**，源正文 **210,320 字节**；SHA256 为 `564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935`
- 开场内容：现代国风写真园合影，二人循旧楼侧门误入大晟；不能引用旧版铜镜穿越设定
- E001–E005 原文冻结；PGS30 状态 HOLD

以上是读取真实性的检查点，不代替独立全文读取和审计。

## 5. 仓库可见性警示

2026-10-16 GitHub 查询结果：此仓库 **PUBLIC**；旧 README 中的“保持Private”属于过期说明。公共文件可以下载和复制，无法做到“可阅读不可下载”。外部AI只能通过该平台实际具备的浏览或GitHub读取能力访问；prompt不能替代授权或提升工具权限。

## 6. 审稿文件提交规范

默认只输出审稿报告，不直接修改本剧。若有独立授权，可在独立分支或PR内提交，逐条含：源commit、集号/场次/原句、问题证据、建议改法、涉及的知识/钱物/时序/关系/官权、下游回归测试。不可凭评分宣布 Production Clean，也不可自动合并。
