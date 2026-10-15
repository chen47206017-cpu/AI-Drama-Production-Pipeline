# 外部AI二轮审稿统一提示词｜V23.34R1-CANDIDATE（2026-10-16）

请以**《双姝商途》最新修订候选稿 V23.34R1-CANDIDATE**为审查目标，基线为V23.33R1。你是独立审稿人而非主笔；**只给真实证据和可执行建议，不得自行改GitHub或合并PR。**

## 零：准确网址（必须直接打开，不用搜索引擎推测）

仓库：`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline`

现行受控母稿（保持V23.33R1）：
`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md`

**新候选整本（必须阅读）：**
`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.34r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.34R1_CANDIDATE_E001-E064.md`

原始Markdown（若网页正文提取失败）：
`https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/review/shuangshu-v23.34r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.34R1_CANDIDATE_E001-E064.md`

**审稿资料、采纳与驳回理由：**
`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.34r1-candidate-20261016/projects/shuangshu-shangtu/reviews/EXTERNAL_AI_TRIAGE_V23.33R1_20261016.md`

**候选版本索引与差异：**
`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.34r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/PATCH_MANIFEST.md`

64集入口（同仓库）：
`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.34r1-candidate-20261016/projects/shuangshu-shangtu/EPISODE_INDEX.md`

AI治理文件：`CURRENT_PROJECT_POINTER.md`, `AGENTS.md`, `canon/PROJECT_CANON.md`, `skills/story-impact-v2.2/SKILL.md`, `audits/OPEN_GATES.md`, `reviews/REVIEW_TEMPLATE.md`，均位于 `projects/shuangshu-shangtu/` 下。直接用分支指定路径读取，不要只扫默认main。**仓库PUBLIC，不能把网页解析失败误报“独立分支私有权限”。**

## 一：来源验收先于任何打分

1. 打开以上两份完整母稿/候选稿，说明实际读取字节/行数与每集标题或失败原因。
2. 候选稿必须有64集、268场，首集`E001《走错一扇门》`，末集`E064《这条街，照常开门》`，全文末`【全剧终】`。
3. V23.33R1原文Git Blob `c507624f01f56aa2a4c5799ce0dd9fd415926738`；V23.34候选原文Git Blob请从实际仓库读取；不能靠抄索引来冒称自行算SHA。
4. 预期**只有E011、E018、E019、E050变化**。其他60集，包括逐字冻结的E001–E005，必须和V23.33R1逐字一致。若发现额外差异，先报P0。
5. 如果整本加载被截断，按8批每批8集读取，或逐个打开对应分集文件（候选只在 `scripts/candidates/episodes/` 存放4个修改集；未修改集使用既有 `scripts/episodes/`）。没全部读到不能宣称100%覆盖。

## 二：本轮首要审查四处已发生改动

| 集数 | 变更与预期价值 | 请反证或核验 |
| --- | --- | --- |
| E011 | 六块米糕、4文短工工资条件前3秒可视化 | 与E010茶楼连续性、食物出炉时点、东家钱的状态及150秒拍摄；是否真的更有吸引力 |
| E018 | 裂床旧榫加一段可拍险情 | E017末床已歪，本集再沉是否合理；木匠在场时间、书生安全、E019整铺转场 |
| E019 | 坊书吏处询问韩府侧房进入资格 | 书吏不能代韩府放行，不能新增法律条文；E001/E005/E016知识链；E032/E064回家线是否被提前解决或变得重复 |
| E050 | 阿梅关专属账柜、程实实在在收手 | 阿梅的工钱未动，三百文押钱仍不可得；原文已有边界是否因此重复；动作对白能否在00:00–00:34完成 |

任何建议应以原文逐字引用为主，明确“必修逻辑P0 / 有戏剧价值可选P1 / 主观偏好P2”。不得编剧式旁白、凭空新对手/现代物证、钱物凭空变现。

## 三：对所有外部审稿结论做一次反事实审查

上一轮报告出现真实错误：E001“冰川坠落”、E002“扫码被围观”、E007“挂明妆牌”、E064“互换账本”，这些都不是V23.33R1剧本正文。禁止复制这些虚构场面。

请重新依据**完整候选稿正文**分析：
- E006–E024是否存在可减少的同质商业“问价/核凭/退钱/责任划分”；给出至少3条不用新增反派、且不破坏跨集因果的**具体替换镜头/动作**。
- E025–E048的“查账/履约/赔付”是否构成真正的连续重复。制作逐集商业发动机指纹：顾客需求、主人公动作、反作用/牺牲、视觉结果、关系变化、钩子类型，区分语义相似与镜头体验确实同质。
- 穿越回家线：从E001到E064对每次“想家/询问/行动/失败/下一假设”逐次列证，不要把温寻妹线当成程盛真正回家行动。
- 许曼娘是独立专业对手，不会毫无动机跑去梨市偷窥程，也不得为程排班；江砚舟不能滥用公务。
- 关系和女性选择：程主视角、盛独立事业、阿梅真实决策、温与柳自主。不要为情绪锚点随意制造角色崩溃或添加教训式金句。
- E064：保留韩府正门尚待许可、静默的现代牵挂、见月铺无人监管也能开门；如建议升级末镜，仅能复用已有实物、地点与可观测行动。
- 检查关键货币和人头：E010 480－300－80－60＝40；E032 120＋1288－468＝940，－300－180＝460（120历史来源仍未PASS）；E051/E053定金30+尾款100；夜市在册50→46→41。请逐源检查，不得用新收费凭空增加收入。
- 复核PGS30全部未放行项，任何“SSS/90分/完播率百分比/政策完全合规”只可当待实证的假设，不得作为已测结果。

## 四：完整交付格式（重点是证据而非形容词）

**报告A｜来源证明：** 报告实际读到的所有文件、日期、commit/Blob、64集覆盖范围，无法访问的文件单独列明；不得抄参考文件里的SHA假装重新计算。

**报告B｜四处变更深度裁定：** 原文前/后逐字摘录、镜头价值、演员可拍时间、对前后集连锁影响、PASS/HOLD/FAIL与必要修补。

**报告C｜全64集创作诊断：** 每集开场0–3秒、30秒事件、主要冲突、结果、观众情绪、高光、尾15秒钩子、下一集承接，用64行矩阵呈现；同时给出真正的跨集商业指纹重复证据。

**报告D｜建议修改卡：** 每个问题集号/场次时码、逐字原句、真实问题、最小改法、较高戏剧价值替代改法、损益/钱物/人物知识链/上下游涉及所有集、可拍测试。禁止只有“加冲突/加金句”之类空建议。

**报告E｜生产仓库优化：** 评估当前独立分支/候选PR、根目录管线与专属项目、PR权限、旧版导入、文档版本指针、CI可运行性、变更回归与外部审稿归档。提出可核验的文件级整改，不创建空壳模块。

**报告F｜审核声明：** 本次仅审稿，不直接更新剧本，E001–E005仍冻结；真实质量结论与主观市场预测分开；PGS30一律维持HOLD直至整套Gate Bundle绿灯且经人工放行。

若外部AI无法读取指定GitHub正文，请提供访问报错，提示用户上传文件。不得回退到V23.32R1并宣称分析完成。
