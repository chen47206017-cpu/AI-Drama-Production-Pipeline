# 最新：更可靠的外部AI阅读/审稿入口

**优先看这一版**：[防误判全文审查母提示词](reviews/sourcepack_v23.36/EXTERNAL_AI_VERIFIED_REVIEW_PROMPT.md) · [64集逐集阅读](reviews/sourcepack_v23.36/EPISODE_INDEX.md) · [8批阅读](reviews/sourcepack_v23.36/BATCH_INDEX.md) · [源文件清单](reviews/sourcepack_v23.36/SOURCE_MANIFEST.json) · [全文数据一致性校验](reviews/sourcepack_v23.36/verify_sourcepack.py) · [报告逐字引证校验](reviews/sourcepack_v23.36/verify_evidence.py)。

外部AI先报告实际读取覆盖率、逐集两个不同场次的**精确原文**，并将剧本中的**事实**、对观众体验的**主观推断**与尚未写进正文的**创作建议**明确分开。若源文件未读取，必须回答UNREAD并终止对应结论。此前AI常把E024“二十名工人领薪”只说成查账，把E040–E048误报为回现代，必须先完成对应事实对抗测试。

以上所有资料位于V23.36候选分支，未改正式V23.33指针；PGS30 HOLD。

---

# 第四轮AI协作唯一入口 — V23.36R1-CANDIDATE

**重要：这是审核中的最新候选，不是正式CURRENT。** 正式工作稿仍V23.33R1、PGS30 HOLD；分支在 `review/shuangshu-v23.36r1-candidate-20261016`，未合并main。仓库为Public，公开文件可下载。

## 直接打开

- [候选完整64集剧本正文](scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md) — V23.36R1，64集268场，Git blob `edeb513edcfe9552c13e56bd1c9c5ed7fbf50734`
- [V23.35候选全文](scripts/candidates/V23.35R1_CANDIDATE_E001-E064.md) — 对比基线
- [V23.33正式工作母稿](scripts/CURRENT_E001-E064.md) — 官方受控指针所指版本
- [第三轮AI报告裁定与E002冻结草案](reviews/ROUND3_EXTERNAL_AUDIT_V23.35_TO_V23.36.md)
- [外部AI第四轮完整审稿提示词](reviews/EXTERNAL_AI_ROUND4_PROMPT_V23.36R1.md)
- [结构/版本校验脚本](scripts/candidates/verify_v23_36.py)
- [Canon](canon/PROJECT_CANON.md)
- [AGENTS多AI约束](AGENTS.md)
- [PGS30未放行风险](audits/OPEN_GATES.md)
- [审核规则Skill v2.2](skills/story-impact-v2.2/SKILL.md)
- [唯一正式版本指针](CURRENT_PROJECT_POINTER.md)

### 版本核对

- V23.35→V23.36实际变化仅**E010、E024、E045**。
- V23.33→V23.36累计变化**E010/E011/E018/E019/E024/E025/E040/E042/E045/E050/E058**，其他53集逐字未动。
- E001–E005**逐字冻结不变**；E002新对白只作审稿草案。
- 账目、身份制度、150秒演员实读、归途线的长线行动、商业发动机同构仍需独立审计；**结构PASS不等于Release PASS**。

## 访问问题

如网页抓取失败请直接访问原始文件：
`https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md`

GitHub搜索默认分支不能检出尚在评审分支的内容。无法访问时应请用户上传原始Markdown，禁止以旧版的概览或报告代替完整剧本。
