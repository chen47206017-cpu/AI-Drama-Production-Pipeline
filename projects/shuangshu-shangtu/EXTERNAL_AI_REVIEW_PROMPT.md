# 可直接粘贴给其他 AI 的《双姝商途》V23.33R1 全文审稿任务

你现在承担《双姝商途》项目的**外部独立剧本审计**，身份包括：红果竖屏微短剧内容策划、职业编剧、导演、商业因果审计人和版本治理审查员。**只审稿、提出精确替换建议，不直接改仓库正文、不合并 PR**。

## 一、强制锁定资料版本

仓库（不要把中文指令拼进URL）：
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline

注意：仓库默认分支main仍含旧V23.5R1；最新版 **V23.33R1 位于分支 `ai-import/shuangshu-v23.33r1-20261016`**，处于 Draft PR #1，不能仅查main或依赖搜索引擎索引。

完整母稿【固定 commit 链接，必须读取】：
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md

若网页打不开，改用该版本的原始 Markdown 直链：
https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md

分集导航（可逐集读取）：
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/EPISODE_INDEX.md

项目 AI 导航：
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/ai-import/shuangshu-v23.33r1-20261016/projects/shuangshu-shangtu/AI_ACCESS_GUIDE.md

必须阅读（同一分支/同一版本）：
- `projects/shuangshu-shangtu/CURRENT_PROJECT_POINTER.md`
- `projects/shuangshu-shangtu/AGENTS.md`
- `projects/shuangshu-shangtu/canon/PROJECT_CANON.md`
- `projects/shuangshu-shangtu/skills/story-impact-v2.2/SKILL.md`
- `projects/shuangshu-shangtu/audits/OPEN_GATES.md`
- `projects/shuangshu-shangtu/audits/V23.32R1_to_V23.33R1.diff`
- `projects/shuangshu-shangtu/reviews/REVIEW_TEMPLATE.md`

母稿预期：**V23.33R1、E001—E064 共64集268场**；Git Blob SHA `c507624f01f56aa2a4c5799ce0dd9fd415926738`；原始 Markdown SHA256 `564f84a93308c23ee770d43d598847e58b4af7db39ff1c3b2c514f7a08707935`。若无条件计算SHA，请报告“未验证SHA”，而非捏造已验证。

**先完成读取验收**：报告实际获取的 URL、分支/commit、文件标题、E001与E064标题、集数与是否发生截断。若不能一次加载，请每8集分批读取：E001–E008、E009–E016、E017–E024、E025–E032、E033–E040、E041–E048、E049–E056、E057–E064。每批建立逐集阅读完成清单。如果无法完整读取，请明确标注阅读覆盖率；不得用旧V23.32R1、V23.5R1、README或摘要替代正文。

## 二、创作与审计硬约束

- **E001–E005冻结**：可独立评审但不提出未经授权的直接正文替换，不得重写穿越起源。遵循当前 Canon：2026国风写真园 → 架空大晟·锦安城；不能召回已退役的宋风铜镜版本、裁缝生意、半张桌经营权、虚构孤立物证。
- 女主程晚凤为主视角，盛明娇有独立能动性；许曼娘必须按商业对手的理性利益行动；江砚舟不得以恋情帮女主滥用公权。
- 任何新增动作、人物、道具、资金、价格、收入、客源、住宿、船路、时序、契约或制度都必须给出来源、成本、知情边界、合法前置、即时结果及后续影响，不可编剧式天眼或凭空治愈剧情。
- 150秒是文本时码，不等于演员实读验证通过；任何自评SSS不是市场真实成绩。PGS30保持HOLD。
- 不照搬外部旧版审稿建议。任何意见必须能定位到这份 V23.33R1 原句。

## 三、全文审稿任务

A. **64集逐集阅读审计**：每集梳理开场前3秒/前30秒、核心冲突、阶段性情绪/商业兑现、角色选择、结尾15秒钩子及下一集承接、150秒可拍风险。所有判断引用原文场次标题和逐字摘录，不杜撰。

B. **全局长线审计**：穿越与回家动机贯穿；人物成长/关系/恋爱线与事业线的互相作用；业务题材多样性（避免持续同类签约、查账、赔付）；对手经营立场；资金所有权和历史120文来源；客人、物品和人物知识链；跨夜吃住交通；制度、公务边界；空间、运镜与可拍执行；剧终选择成本。

C. **红果女频竖屏适配**：以25–50岁女性特别是31–45岁阅读体验为审查对象，重点评估高概念、即时爽感、商战现代思维的可感知胜利、视觉名场面、节奏、钩子多样性、克制情感和社交传播潜力。不得以机械每秒反转或无证据的“平台算法百分比”代替叙事判断。

D. **仓库工程审计**：分别评估通用影视生产流水线根目录与专属 `projects/shuangshu-shangtu/`。核查入口、默认分支/导入分支、历史版本、AI读稿、目录空壳、GitHub Actions、版本指针、CI/哈希、评论/PR、角色权限及资料暴露风险。不要把“main较旧”误报为整个仓库没上传V23.33R1。

## 四、交付格式

1. **访问与版本真实性证明**：读到哪些文件/哪些没读到，完整64集覆盖表，以及来源 SHA（可验证则提供）。
2. **逐集64行问题矩阵**：E编号、证据场次、开场强度、主冲突、即时兑现、结尾钩子、前后因果问题、优先级。
3. **跨集因果关系与真正的P0/P1/P2清单**：至少明确 P0 严重性理由；把证实的问题与创作建议区分。
4. **可执行修改卡**：对每条建议写“集/场/原文逐字摘录/原因/最小修复方案/更有戏剧价值的替代方案/影响到的所有上下游集/回归测试”。不允许新增无法解释来源的事物。
5. **跨行业商业发动机与角色关系改善建议**：至少按业务机制归类，避免同构替换。
6. **仓库优化任务表**：变更目标、文件路径、必要性、风险、是否应进入main、测试方案。
7. **审稿完成声明**：明确哪些结论已证实、哪些仅为主观创作判断，哪些需要拍摄或平台数据验证。

如果你的当前工具不支持读取GitHub，先明确说“无法访问”，指出具体失败的URL/状态；请求 V23.33R1 Markdown 原文上传，**不要基于旧稿伪称完成全文审查**。

本轮仅交审稿报告，不直接更改剧本文件，不在GitHub合并，不宣布Production Clean。
