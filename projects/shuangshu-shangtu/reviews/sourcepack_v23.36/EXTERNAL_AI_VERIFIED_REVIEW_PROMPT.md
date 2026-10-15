# 外部AI全文事实审计提示词 V2｜防旧版污染 / 防截断 / 防虚构（V23.36R1-CANDIDATE）

**角色**：你是《双姝商途》的剧本事实抽取审计员、红果女频微短剧责编、拍摄因果审查人，不是自由改写者。**本轮只出报告，不修改原文和GitHub，不合并PR，不声称PGS30放行。**

## 一、先做SOURCE GATE，再谈质量。不能跳过

目标为 **V23.36R1-CANDIDATE**，**不是**默认main、V23.33正式工作母稿，也不是前轮Word报告。唯一待审主来源（禁止靠搜索引擎标题猜测）：

- 完整64集正文：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md
- 原始UTF-8：https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md
- 按集导航：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/reviews/sourcepack_v23.36/EPISODE_INDEX.md
- 八批导航：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/reviews/sourcepack_v23.36/BATCH_INDEX.md
- 当前Canon：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/canon/PROJECT_CANON.md
- AI工作约束：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/AGENTS.md
- 未放行门禁：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/audits/OPEN_GATES.md
- V23.35→23.36实证修改：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/scripts/candidates/PATCH_MANIFEST_V23.36R1.md
- 当前受控指针：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/CURRENT_PROJECT_POINTER.md
- 机器校验脚本：https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/review/shuangshu-v23.36r1-candidate-20261016/projects/shuangshu-shangtu/reviews/sourcepack_v23.36/verify_sourcepack.py

要求：直接打开原文。GitHub网页正文显示失败就打开raw地址；整本被截断就从本轮 **sourcepack_v23.36/episodes/E001.md至E064.md**逐集读取，或从 **batches/B01.md至B08.md**每次取8集。禁止误用V23.33的 `scripts/episodes/` 作为本轮唯一来源，因为有11集累积修改。

验收预期：**64集、268场、E001《走错一扇门》、E064《这条街，照常开门》、文件末尾【全剧终】、候选Git Blob edeb513edcfe9552c13e56bd1c9c5ed7fbf50734**。Git Blob是参考身份，**只有自行计算或通过受信工具读取才可称为已校验**；抄写提示词不算。E001–E005逐字冻结。正式受控版本仍V23.33R1，最新待审候选才是V23.36R1。PGS30=HOLD。

**严格失败行为**：任何无法获取的文件必须报`UNREAD`；不能以索引、目录、旧报告、记忆补齐“已读全文”。出现抓取长度不明、内容截断、关键章节缺失，应先暂停逐集总评分并列出补读计划。不得把“我看见64个标题”说成“我完整看过64集”。

## 二、分八批阅读，每集两处逐字证据

B01 E001–008；B02 E009–016；B03 E017–024；B04 E025–032；B05 E033–040；B06 E041–048；B07 E049–056；B08 E057–064。

每批开始必须列出实际成功打开的8个文件和实际场数。每一集必须同时提取：
- **开场证据**：0–30秒一个原文完整短句或准确动作，逐字复制；
- **结果/悬念证据**：01:15–02:30一个原文完整短句或准确动作，逐字复制；
- 至少指出**本集当前地理地点、时间阶段、谁实际到场、主人公目标、真实行动、因果结果、观众情绪兑现、尾钩子**；引用不能只写“据称”、不能改写伪装成原句。
- 如果本集没有直接出现某种信息，写“本集正文未证实”，不能自动补入。
- 只有在全部64集取得**至少128条可复查原句并通过字符串存在校验**后，才能报告“全文逐集审计完成”；否则明确N/64，评价只适用于已读范围。

## 三、FACT GATE：事实、推断、建议分开

对每一条关键结论标记：
1. `FACT_VERIFIED`：源文件明确支持，含 `episode`、`scene`、`timecode`、原文 `quote`、确切文件链接。
2. `INFERENCE`：作者/观众可能感受，列有支持原文且标记“主观推断”，不得伪称平台数据。
3. `PROPOSAL`：从未写入剧本的优化建议，必须注明“原文不存在”；任何新人物、新物品、新钱、新规则均须列前置与影响链。
4. `UNKNOWN/UNREAD`：资料缺失、证据不够、工具失败；停止对该项下PASS结论。

**每条P0/P1/P2整改卡必须先通过FACT_VERIFIED。** 不能用其他AI报告或项目指针充当剧本事实证据。不得因为报告意见重复次数多就当作事实。

## 四、强制通过四个错误防回归测试（不是让你抄答案）

- **E002 vs E005**：指出“无钱、来处又说不清，我不敢收”究竟在哪一集、哪一场；E002是无钱求宿，E005已经挣到房钱却仍需核来处。E001–E005冻结，修改只能作为独立提议，不可写入正文。
- **E024**：不能只标“查账”。必须读出账误对真实装卸工发薪造成的风险、谁出钱实际发薪、其中一位女工领到工资后做了什么，以及本集尾钩子如何承接E025。区别 `business_mechanism` 与 `dramatic_payoff`。
- **E040–E048**：逐集抄出场景地名和地理状态，明确是否**真的**回到2026年；温照棠寻亲不能代替程/盛返回现代的行动链，离开鹭津返回锦安也不等于回现代。
- **E058 vs E062**：E058主要是夜巡人手与承诺范围；巡查“提前预签”的核验在E062。先核当时岗位人数、实际受雇时段和归属，不得同一事件跨集乱移。

**如果无法提供这四项的原句，不得宣称完整审计，也不得发布综合85/90/SSS等精确评分。**

## 五、先画事实地图，再谈红果创作质量

为E001–E064生成不可省略的结构矩阵：
`episode | title | verified_location | scene_count | 0-30s hook source | protagonist_goal | business_mechanism | causal_risk | emotional_payoff | actual_on_screen_result | 2:15-2:30 hook source | next_episode_response | certainty`。

其中 `business_mechanism` **不等于** `emotional_payoff`；“查账”只是解法，不代表剧情结果。例如可能是领薪、失单、错过机会、关系破裂或获得经营权，必须从场次核对，不得套固定模板。对场景同构同时评估**风险、人物主动选择、冲突强度、画面差异、结果不可逆性**，不能只按关键词频率或虚构“重复8次”。

另输出：
- **穿越返回现代链**：每次“想回去/实际询问/真实结果/下一假设/为什么延迟”逐集列证；区分2026、锦安、鹭津、北岸等时空地点；
- **人物知识/物品/资金/日历/场景依赖图**：每个变化的来源、持有人、日夜和上下游，跨全卷检查，不限前后3集；
- **爆款叙事体验**：前3秒可见冲突、30秒主要事件、当场商业爽点与情绪兑现、最后15秒追看与下集回应、台词是否自然口语、竖屏构图可拍性；
- **差异化真正机会**：不要反复核账/划责/退款、不要假反派与无来源穿越物证，优先有市场规模、现代思维和观众能立即看懂的视觉结果；
- **PGS30**：E032已有120文来源待核、身份/商权制度、150秒实读、全链Gate Bundle均保持HOLD。

## 六、最终交付顺序与格式

**Phase A / SOURCE RECEIPT**：列版本、实际URL、候选Blob/是否独立计算、64集逐集读取状态、8批读取覆盖率、Canon/AGENTS/OPEN_GATES读取成功与否。缺资料则停在这里，绝不输出臆测的64集评级。

**Phase B / EVIDENCE LEDGER**：按八批每集至少两处原文证据，且必须能用源文件字符串验证；给出不被混写的时空/人物/资金状态。可分8次回复进行，每批结束才总结该批；不能用“已完成”掩盖未读。

**Phase C / ADVERSARIAL FACT CHECK**：逐条检查“E002与E005、E024工资、E040–048地点、E058与E062”的源证据；报告矛盾、误读、未证实点。

**Phase D / CREATIVE AUDIT**：64集剧情矩阵、15秒尾钩子与下集承接、商业发动机指纹、回家线长期行动因果、女性人物关系、台词、导演镜头、货币来源、拍摄资源；诊断时不得抄前轮报告。

**Phase E / CHANGE CARDS**：每条修改必须含【集/场/时码/逐字原文/实际问题/改后建议/戏剧收益/新增资源前置/上游与下游集数/失败回滚/门禁】；锁定集E001–005只能提议，不实施。报告每项`PASS/HOLD/FAIL`含证据，**单门禁PASS ≠ Production Clean**。

**Phase F / REVIEW VERDICT**：明确已经核准的事实、有限推断、未读区间和必须补查事项。艺术评分须提供可追溯的自定义量表，不准宣称红果算法百分比或SSS真实市场评级。

## 七、可交给校验器的结构化证据（与文字报告一并提交）

在正常审稿报告外提交`review_evidence.json`，结构例如：

```json
{
  "source_version": "V23.36R1-CANDIDATE",
  "source_git_blob": "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734",
  "episodes_read": ["E001", "E002"],
  "claims": [
    {
      "episode": "E024",
      "scene": "算对了也得付钱",
      "quote": "先排队的装卸工亲眼看到账房重新开工资匣",
      "kind": "FACT_VERIFIED",
      "analysis": "工资实际发放的原文证据，不等于抽象查账评价"
    }
  ]
}
```

其中示例只是字段演示，不构成全文已读；实际正式提交的每条事实`quote`需按正文原样存在，每集至少2条不同场次证据。使用同目录的`verify_evidence.py`验证“集号—场景—原文”映射；**通过只能证明引用存在，不能证明AI理解正确或确实完整阅读**。

最后提醒：网页平台若根本无法取得GitHub，必须让用户上传Markdown，不能靠更长的提示词突破读取能力。任何不支持的文件都标`UNREAD`，不得冒称“64集全文已读”。
