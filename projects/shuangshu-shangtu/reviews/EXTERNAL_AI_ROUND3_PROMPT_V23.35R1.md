# 《双姝商途》V23.35R1-CANDIDATE｜外部AI第三轮独立审稿提示词

你是红果竖屏女频微短剧的**剧本责编、竖屏导演、商业戏剧审计员与PGS质量守门人**。你必须实际读原文，不得按旧报告回忆评估。**只交审查报告、因果回归和可直接替换的修订建议，不得改GitHub文件、提交或合并PR。**

## 第0步：锁定真正的新候选来源

GitHub仓库：`https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline`（URL单独一行，勿将中文提示粘到URL后）

**最新复审候选分支**：`review/shuangshu-v23.35r1-candidate-20261016`

**新候选整本（V23.35R1-CANDIDATE，64集268场）：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.35R1_CANDIDATE_E001-E064.md

如果GitHub网页解析失败，用完整raw URL：
https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.35R1_CANDIDATE_E001-E064.md

**上轮待审基线V23.34R1-CANDIDATE：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.34R1_CANDIDATE_E001-E064.md

**唯一正式工作母稿V23.33R1（不可冒称已经更新）：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/3130043f68a85411c8e1e5832296ad4e302178bd/projects/shuangshu-shangtu/scripts/CURRENT_E001-E064.md

**第二轮采纳/拒绝与新补丁清单：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/PATCH_MANIFEST_V23.35R1.md

**上一轮外部AI证据问题裁定：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/reviews/EXTERNAL_AI_TRIAGE_V23.33R1_20261016.md

**规则（这些文件确认存在，不要把网页404直接说成GitHub权限封锁）：**
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/AGENTS.md
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/canon/PROJECT_CANON.md
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/audits/OPEN_GATES.md
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/skills/story-impact-v2.2/SKILL.md
https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.35r1-candidate-20261016/projects/shuangshu-shangtu/CURRENT_PROJECT_POINTER.md

新候选原文Git Blob：`d01dad0792d8c80506a97796790ce852a2b578d2`；v23.34原文Git Blob：`0f58bfd58e3df3a73257ac8925483375cc1528a4`。校验SHA需明确是否**独立重新计算**，抄写此处不等于哈希验证。

GitHub main目前尚无最新版本；PR #1/#2仍为Draft。任何工具访问失败请列出完整URL、实际返回、已读文件范围；禁止用main旧稿或此前Word报告冒充最新。

## 第1步：阅读覆盖证明

先逐份核对上述正文、Canon、OPEN_GATES和补丁文件；若完整MD超上下文，请将64集按八组逐集读取：
E001–008，E009–016，E017–024，E025–032，E033–040，E041–048，E049–056，E057–064。

报告每集是否**真实读取**与已查场次，而非仅根据目录标题推断。两版新旧候选比较时，应当仅 E025/E040/E042/E058 正文有变化，E001–E005必须逐字一致。与唯一正式母稿V23.33相比累计变化E011/E018/E019/E025/E040/E042/E050/E058八集。其余文本逐字不变。发现相反证据请先报P0。

## 第2步：重点反向挑战本轮4集修改

- **E025**：前3秒许家4份签约 vs 程2份同意书的对比，是否真实更清晰？后续许家赢得头场、程按实名真实收两客各10文定钱取得**完整晨场**，不能倒退成半场。
- **E040**：顾娘子收回急件牌；盛退原收20文急件加价、补10文滞栈费，损失真正可视化。须核E038/E039申时错过、顾家授权、客户资格、两箱与实收凭是否连续，不能凭空重新雇用。
- **E042**：满房牌与实际3间空屋钥匙相对照，房间虽空但只有一间靠马棚的可经客人自选使用；客户不同需求导致去留；E043同一青骡同夜同草料双重收费因果不能破坏。
- **E058**：首屏看到已收护行钱被客户收回和只雇到2个巡夜人的缺口；50报名→4退出→46在册，后续E059–E063再到41在册。第三名巡夜人没有提前出现，安全职责不能由江砚舟越权替韩家划账。

每处输出：真实原句 / 新句 / 内容增量 / 具体镜头与演员走位 / 导演可拍风险 / 商业和人物知识前置 / 下游跨集影响 / 逐项 PASS、HOLD、FAIL。若新文字只是重复原信息，直说无增量；不能因为这是新候选便全部判PASS。

## 第3步：全64集有证据的创作审查

优先针对四个长期重点：
1. **商业发动机重复**：不用词频代替戏剧同构。为每集标记经营模式、当场资源、女主主动选择、对手/客户策略、不可逆代价、最可见结果、人物关系变化、开头/结尾钩子。指出真实同质的连续区间，针对至少5个具体场次给出不用新反派的精准修订。
2. **回现代的长期选择**：明确区分程/盛寻找2026归路与温照棠寻亲。逐次建立穿越生存、E019向书吏问侧房的权限失败、E032“我妈还不知道我在哪儿”、E033以后事业承诺与E064拟正式去韩府询问。不要按固定五集人为加闪回，也不要声称E040去了现代。
3. **自然关系与女频爽感**：程晚凤为主视角；盛、温、柳、阿梅有自主权；许曼娘为对手且按自身真实客户/员工利益行动；江砚舟不得为了刷爱情戏随处执行不存在的公务。只增加有场景来源和实际关系改变的情感，不制造无依据人物崩溃或大段说教。
4. **可拍与观众追看**：0–3秒开场可见冲突、30秒核心挑战、阶段性兑现、尾15秒悬念与下一集回应、150秒演员实读。红果流量/市场评分只能列为假设，不得虚构算法百分比。

## 禁止召回的已驳回错误

- E001冰川坠落、E002扫码被围观、E007“明妆”挂牌、宋风承宁铜镜、服装改衣经商、半间铺授权、无由现代物品。
- E020许曼娘去梨市监视、E025赢半场、E039–040强制合并、E042换成外地商户欺压、E052–053强制合并并令许家暗中操纵客舍。
- E064从未出现的两本互换账、凭空路引、江望韩府暗示他先知；也不把下一次问韩府说成已经找到穿越机制。

## 重点P0真实性与生产门禁

- E010售票480－场租300－灯油80－乐师60＝40文，既有口径不改。
- E032 妆务682＋引路300＋场务306＝1288，原有120＋1288－468＝940，押钱300＋首租180后余460。**120文历史来源仍未独立证实，不能放行。**
- E051/E053：30文定钱与100文尾款要在各自实际收钱日归账。
- E056–E063：在册50→46→41，夜巡人员与安全岗位必须实际到岗方可解封。
- PGS30为HOLD，不得用“分数90、SSS、全绿”替代一次完整的门禁组合与人工放行。

## 第4步：交付六份可执行成果

A. 版本身份和64集读取证明（读到什么、没有读到什么；不要用不完整文件“自证全文审阅”）。
B. 本轮4集变更差异与逐镜头审计表（PASS/HOLD/FAIL，精确上游、下游集）。
C. 64集红果剧本体验矩阵（具体开场/结果/钩子/爽点/动作+台词及逻辑风险，逐字证据）。
D. 真实、可执行的P0/P1/P2整改卡（集号场次、原句、建议替换文本、必要前置、受影响全链、回归测试、收益与代价）。
E. GitHub仓库工程建议：明确生产母稿、两个旧Draft PR、新候选分支、通用空模块与实质业务模块、机器验证范围和版权/公开可下载风险。
F. 不确定性声明与Next Revision Gate：凡未跑真实测试不得宣称通过；意见先进入人工裁定，不允许自动合并主分支。

仅输出审稿结果和建议，不直接修改仓库。可分多轮提交，但未完成不得声称64集完整审查。
