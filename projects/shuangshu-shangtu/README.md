# 《双姝商途》｜64集竖屏短剧协作项目

> **唯一工作母稿：V23.33R1（E001–E064）；状态：PGS30 HOLD / NOT PRODUCTION CLEAN；Skill：Story Impact Adversarial Audit v2.2。**
>
> 此目录是独立项目空间，不覆盖仓库已有影视制作工程。所有批改先在独立分支/Issue/PR进行，**不得绕过审批改写主线**。

## 一键入口

- [外部AI访问指南](AI_ACCESS_GUIDE.md) — 固定commit、默认分支陷阱与访问失败退路
- [机器可读索引](AI_INDEX.json) — 当前源哈希、64集路径和8批阅读顺序
- [逐集阅读目录](EPISODE_INDEX.md) — E001–E064直接链接
- [外部AI审稿完整提示词](EXTERNAL_AI_REVIEW_PROMPT.md) — 版本锁定、逐集证据、因果回归与仓库评估

## 阅读顺序

1. [版本指针](CURRENT_PROJECT_POINTER.md)
2. [AI约束](AGENTS.md)、[项目Canon](canon/PROJECT_CANON.md)
3. [最新整本](scripts/CURRENT_E001-E064.md) 或 [逐集正文](scripts/episodes/)
4. [Skill执行规则](skills/README.md) 与 [记忆协议](memory/portable_memory_v2.2.md)
5. [待核问题](audits/OPEN_GATES.md)、[审稿卡](reviews/REVIEW_TEMPLATE.md)

## 多AI协作

- AI只提意见 → Issue / `reviews/incoming`，需含集号、原句/场次、证据、改法及上下游影响。
- AI实际修稿 → 以当前母稿为基础开独立分支 → 提PR → 核验逐字diff、64集与前5集冻结、钱物/身份/时序/公务权力等PGS门禁。
- 主审完成裁定后，才由获授权人员合并PR并修改版本指针。**模型分数和单项测试通过不等于Production Clean。**

## 注意

2026-10-16实际仓库可见性为 **PUBLIC**（而不是Private）：公开文件可被下载和复制；若仓库后来设为Private，外部AI须获得被授权的读取方式。**项目最新V23.33R1在 `ai-import/shuangshu-v23.33r1-20261016` 分支的Draft PR #1，默认 `main` 尚为V23.5R1。** GitHub代码搜索只索引默认分支，因此查不到不等于没有上传。详见 [访问指南](AI_ACCESS_GUIDE.md)。
