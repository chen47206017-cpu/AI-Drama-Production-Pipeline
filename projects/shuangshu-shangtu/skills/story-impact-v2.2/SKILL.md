---
name: story-impact-adversarial-audit
version: 2.2.0
summary: 兼容PGS30，核查公权竞争公平、交班与封控、交易履约全流程、跨集多事件身份和SSS市场证据隔离；自动测试仅检查结构化断言，不授予正式放行。
---


# v2.0 · Documentary Causality / Cross-Episode Custody Gate（优先于旧版打分）

以“确定有人/钱/道具/承诺”为单位生成结构化追踪，而不是只看同一集有无关键词。

1. **物件单身份追踪**：每个`prop_id`维护`origin / legal_owner / physical_holder / location / seal_state / last_seen_at / next_use / disposal`。物件一旦“销毁、退还、交给他人”，下一次再出现必须有可演的中间动作和正当交接；同名不同物必须给不同ID。
2. **收据原件/抄件区分**：官方/私人账簿原件须说明保管者。抄记只能证明被抄录的内容，不能自动获得原件的授权或可采信等级；禁止为推进谜案，让配角凭空拿走原件。
3. **职务范围与委托范围独立**：公职不替亲近对象商业担保，短工不得自行改已收定钱的主顾订单，未经授权不能代签或代守公共路口。
4. **款项有实体持有人**：`payer / collector / beneficiary / restricted_deposit / wage_earner / refund / liability`分开记录。现金余额≠每张历史收据已审计；禁止“早上赚4文、下午袋空”的失踪。
5. **同一动作不得重复表演**：`opened/inspected/delivered/accepted/paid`的每次状态变化有唯一时点。如戏服箱已本人验收，下集不得改写成“尚未拆验”。镜头重复检查不应成为二次履约。
6. **状态变化不仅在文本成立，还要位置可达**：若搬箱离开车行，不得再次在车行开同一箱；已经离开现场的车夫不能交其手中凭据。
7. **长线情绪目标必须落地为理性行动**：重访穿越地点需要独立消息/许可、真实时间、已交接生存与经商义务；结局可开放，但不得凭“我想回去”视为调查推进或凭空让门生效。
8. **非P0改善不能引入新的P0**：改完需跑逐集差异、前五集冻结、268场/64集、资金与人物知识、时间连贯和演员实测待核；任何自动脚本声称SSS市场评级须失败。

执行测试：`python -m unittest discover -s tests -v`。本轮实际母稿 V23.30→V23.31 的修复属于项目案例，不应把专属剧情写成其他剧本必须具备的设置。

---

# v1.9 新增优先调用顺序

1. 先锁定当前完整母稿与冻结集：不得把仅有片头拍摄注的版本冒充64集整改。
2. 必查公权反事实一致性：执勤人必须对女主、竞争者、陌生顾客执行同一危险处置；私人情感不能成为审批、商业免责或开路依据。
3. 必查每笔服务完整状态：询价、试样、收定钱、正式服务、客户验收、收尾款必须各仅发生一次；E051试看不等于E053已妆造交付。
4. 必查重复事件身份：同一集两起孩子灯笼事件须分别指定地点、伤情和职责，不因道具相同混为同一事故。
5. 爽点依赖具体选择与代价，而非行业报告自称SSS；同比播放窗口、真人/AI/漫剧、热度/播放严格隔离。
6. 执行 `python scripts/v19_symmetry_and_fulfillment.py --cases examples/v19_three_way_cases.json` 后再执行全部继承测试。结构化案例为人工断言，不等同于机器阅读全64集。
7. 变更必须交付**完整正文、SHA256、逐字diff、逐处编辑卡、HOLD门禁**。制作时长须围读/试排；市场级须实际发行验证。

参见 `references/v19_bid_and_public_power.md`。

---

# v1.8：Public-Office Integrity & Romantic Conflict（新增独立门禁）

适用于任何存在执法、行政审批、公共安全监管或权力资源影响商业竞争的影视故事。**剧情选择可以表现现实中的违规腐败，但必须作为有后果的事件被叙事识别；不得把违规特权包装成值得赞美的爱情奖励。** 对架空世界，应使用本项目已建立的职责范围，不能套用现代法律条款。

## 一、五条硬规则
1. **Public Duty / 公权目的**：公务行为必须有明确公共职责（例如封闭危险通道），不能把“喜欢某商户”作为批准营业、给经营牌照、帮拿资源、替人判赔、压制竞争者的原因。公共目的与商业收益若恰好重叠，也须有独立证据。
2. **Equal-Treatment / 一致适用**：相同危险对各商户一视同仁。不得为女主通融、默许她越过封绳，同时强迫竞争者守规矩。反例：官员让女主独走未验区域；正例：女主也被拦下，另寻安全入口。
3. **Hazard–Owner–Action / 处置权限链**：危险发现→暂停通行→查确认物品权属→由货主自主搬移或有可证明的紧急危险处置→专职值守人员控制封绳→实际验通后方开放。商业顾客和女主不得代领巡岗更牌、持守正式封锁绳或替其他商户签字。
4. **Handoff Before Departure / 离岗交接**：如果官员或巡查人因其他事件必须离开正在封控的路口，应有接班人员、交接的具体路段、当面确认仍处封控的事实；新员工“答应来”不等于“到岗”，后者又不等于“实地验过可开”。
5. **Romance Without Favors / 私情隔离**：私下见面应与当值、公服和公职文书清楚分开。爱情的情绪价值来自“职责冲突后仍能理解对方”和平等交流，不能让男人替女人免于交易损失或担保其商业能力。禁止用工具人叙事让公务人员暗中办理经营资格。

## 二、逐事件强制证据字段
`scene_id / public_actor / claimed_scope / hazard_or_rule / independent_evidence / affected_parties / goods_owner / guard_on_duty / orders_issued / handoff_receiver / property_movement / business_beneficiary / private_interest / private_contract_dispute / labor_cost / reopen_verification / downstream_episode / adverse_outcome / state`。

## 三、红队反例
- 官员替恋人批复私人商契→P0；官员因实有堵路停止所有人流→可成立。
- 官员让女主代拉公共封绳→P0；女主在已验安全出口引领自己真正受托客户→可成立。
- 巡夜人尚未到岗，夜市先开→P0；人已到岗但巷口仍有堆货，继续封禁→可成立。
- 官员在诊所安慰受伤者，路口无人接班→P0；有实际交接且之后探望→可成立。
- 官员反对女主擅动他人货物，不构成“妨碍恋爱”；这是两人可正面发生分歧的戏。

## 四、证据与验收
`python scripts/public_authority_gate.py --cases path/to/scene_cases.json --out path/to/findings.json` 审查结构化事实；仅关键词扫描 `--script` 只标人工复核，不自动判罪或给出生产放行；测试 `python -m unittest discover -s tests -v`。所有修改必须保留旧版哈希、全篇diff、冻结集比较与实际集数。市场SSS、艺人表演时长和架空制度法定范围不能由这组机器测试认证。

---

# Story Impact Adversarial Audit v1.7｜跨项目叙事红队与市场证据门禁

> 完整继承 v1.6 全量指令、脚本与测试；新增“新写道具必须证明来源”“已付款与未履约不能混记”“连续集合同状态交接”“文戏/动作/真人时长三轨证明”等可测试要求。v1.7 不覆盖 PGS30 及项目更高要求。

## 本轮新增硬门禁（优先执行）

1. **Object-Origin On Mutation**：对所有**新增**人物、物件、钱袋、券/约帖、临时劳工等做 `[首次出现/上一持有人/转交行为/当前所有权/下一使用]`。如果只在改动末集出现“顾娘子收回急件牌”而此前没有发牌镜头，则属于变更引入的 P0，不准为做爽点临时发明来源。优先复用前集已有“原约帖”。
2. **No One-Transaction-Twice**：事件ID覆盖 `问价→核位置→签单→定钱→履约→尾款→实付成本→已结/退款`。同一客户跨集不可重新“首次到场”，可拍到账不等于利润到账。处于预收状态的现金不能当作可挪用的自由资金。
3. **Competition Proof = Customer Choice × Rival Capacity × Completion**：许家有真实熟手、独立报价和既有客约；客户自带比较证据、真实签约、后日履约、尾款结清。禁止“对手赶来免费展示”或“突然说自己做不好”。此法跨项目通用，但不得把许家专属事实植入其他项目。
4. **Counterfactual Cost Gate**：同一段商业策略需同时回答“顾客若选另一家会怎样”“主角不接这单会怎样”“成本谁付”“错过限期产生哪笔具体损失”。失败必须在下一次机会中延续，而不是赔一笔即洗清信誉。
5. **Stageable Density Review**：列出每场实际人物移动、柜口动作、道具传递、交易、换场及声音；30秒塞进多次签约＋三次妆造+尾款则提示人工复核。**只有围读/试排/剪辑计时能放行**；文本字数和动作数仅作敏感性指标，不会自动证明可拍。
6. **Script vs Reviewer Firewall**：诸如“没有凭空收入”“不得重复付钱”“这不是同一天完成52单”“角色没有给对手帮忙”等**审稿解释**优先写入 ledger，而不是作为演员无从演出的旁白。剧本须改写为看得见的托管钱袋、日期转场、实际受雇动作。
7. **Scope & Ranking Separation**：播放量研究写明发行平台、真人/AI/漫剧类型、口径、统计窗口、发布时间、原始链接。市场标签只能在上线后判断；SSS创作目标≠市场SSS；分账与播放不互换；绝不拿上榜百强样本推算全市场分位数。
8. **Project Memory Isolation & Change-set**：把用户对某一项目的黑发绳、韩府、人物与商路身份规则写入项目专用Canon，不进入跨项目通用知识。导出变更集、冻结集哈希、影响图、风险台账，失败能回滚。

## 本轮事实案例（V23.27→V23.28）
- E018–E019两次报价要表示“同一整铺、隔日复询”，不能拍成新房新价；同一笔温的查房工钱只在E018实领一次。
- E040原方案写“收回急件牌”，前文无牌来源；修为已存在的急交原约帖。
- E049“拿印→放印→又拿印”的同一行为重复，在同一场内删重只保留一次授权抉择。
- E051三套妆真实只有程和阿梅两位可动手者：第三位在一席空出后接，定钱30／余100；E053必须穿越真实工时且按顾客认可后收尾款。
- E031点清120文现金不等于已证明全额来源；保留 `P0_HISTORY_PROVENANCE_HOLD`，不捏造早期原始凭据。

## 快速运行
```bash
python scripts/v17_gate.py /path/to/updated.md --baseline /path/to/baseline.md --project 双姝商途 --out /tmp/v17_audit.json
python -m unittest discover -s tests
```

## 红队输出合同
`source_sha256, new_sha256, changed_episodes, frozen_unchanged, scene_count, runtime_density_flags, sales_state_flags, editor_leak_flags, hard_failures, unverifiable_items, evidence_ledger, release=HOLD`。除了明确合同约束，静态规则只报告疑点；不得声称项目已达制作或市场SSS。

---

# Story Impact Adversarial Audit v1.6（跨项目SSS创作目标审稿技能）

> 本版本完整继承v1.5，不删除任何已有效门禁；增加V23.27R1验证出的舞台时码、证据级别、系列利益增长及方案隔离。市场SSS不得预先授予未上映剧本。

## 强制启动合同（每个影视/短剧/网剧/电影/漫剧项目）

0. **唯一母稿**：从用户最新可验证完整正文读取，不拿评审文件当新版正文；备份母稿哈希，并列出确实可用的来源。
1. **建议三分法**：采纳＝在母稿有对应人物/道具/因果；有条件＝须新增真实来源并经过全链检查；否决＝违反Canon、退役设定、人物自主权、知识来源或生产现实。建议文档中的“已升级SSS”不得自动继承。
2. **Market Grade vs Script Grade**：市场评级需平台、统计期、播放还是热度、真人/AI/漫剧、数据发布日期五字段。播放与分账不能写成“或条件”来抬升相同等级；SSS文本仅表示目标而非真实成绩。
3. **15s/30s拍摄预算**：场次写出人物动作、合理走位、工序所占物理时间；镜头内文本密度高是人工复核提示，不可作为机器判定通过/失败；演员围读与分镜计时是唯一真实可拍时长证据。
4. **行动内的商业胜负**：先给对手真实能力/自主经营，再展示客户用脚投票→是否付款→完成→钱归谁→损失、转客、复购、对手应对。只写“我赢了/她输了”属于不成立的情绪钩子。
5. **错法后果延续**：一次赔钱≠信誉恢复。凡角色误车、超售、错荐、代签，需在后续至少一处出现业务条件、风险、人物关系或授权变化；不能用说明性总结替代场面。
6. **跨集账与客户ID**：订单状态由询价→预约→收定钱→履约→尾款→结清/退款，禁止同一客户在两场重复首次介绍或同一笔钱两次入账。身份/道具/知识同样追踪。
7. **记忆点意义生命周期**：道具首次拥有者→特定使用→付出代价/意义转变→最终回收；避免强制口头禅、虚构随身现代设备或角色为对手服务。
8. **项目隔离**：禁止以《双姝商途》的黑发绳、妆镜、大晟、江砚舟、五十摊等设定填充别的项目。通用的是验证流程，不是角色与资产。
9. **PGS复核**：Single Gate PASS ≠ Node PASS ≠ Release PASS；每轮修订必须提交全64集（或当前项目全篇）、diff、改动索引、硬门禁剩余项、可撤回理由。未做演员实测/首看盲审/平台验证时HOLD。

## 重要案例：这轮方案不能直接照搬

- 诊断提出E002用手机扫码：现行两女主的手机、钱包已锁在2026写真园，故拒绝。
- 诊断提出E021合伙开店：现行E032才取得独立铺约，故拒绝。
- 诊断提出江违规暗助经商、许查封竞争商户：越权且损坏对手独立人格，故拒绝。
- 诊断提出S/SS/SSS“播放量或分账二选一”：跨量纲，故拒绝。
- 从V23.26到V23.27实际压缩E063最后25秒的551字符场次；场次动作预算仍需真人试排，不宣称已经实际播放150秒。

## 可执行文件

`scripts/v16_audit.py` 提供静态合同、自定义项目账户检查、场景高密度提示。`tests/test_v16.py` 验证结果。原v1.5的所有脚本和测试原样继承。

---

---
name: story-impact-adversarial-audit
version: 1.5.0
summary: 以有来源的爆款研究、叙事因果图、女频情绪兑现、竖屏镜头证据及PGS兼容门禁审计剧本。输出可追溯修改卡与回归测试，不自动授予Production Clean。
trigger: 当任务为短剧/影视剧本结构审计、爆款对标、人物情感、商业事件、多集钩子、剧本重写、镜头节奏或多智能体审稿时加载。
---

# Story Impact Adversarial Audit · v1.5

## 宗旨及边界
执行【市场证据→剧本文本事实→问题定位→最小有力改写→全链回归→独立放行】。本Skill可用于竖屏微短剧、长剧、网剧、电影、漫剧和AI影视；每项目从Canon合约加载参数，不强加固定节奏、角色关系、题材或结局。

**重要：本工具只是PGS30.0（或项目现行更高版本）的叙事扩展层，不提升、覆盖或放宽生产门禁。评分不等于Release Authority。**

## 强制执行顺序
1. `S0 Source Lock`：打开当前完整母稿和Canon；标出已冻结集数、版本、不可回收设定。若没有原文则说明无法正文级裁定；不得用过期版、网页概要或别人的评分代替。
2. `S1 Evidence Ledger`：新近市场信息须记录来源、日期、平台、真人/AI/漫剧、指标名和单位。禁止热度/播放/收藏跨指标比较，禁止把行业经验称为官方节奏标准。提取可迁移机制，**不搬运情节、对白和人物**。
3. `S2 Episode Proof`：分集提取 0–30秒、30–135秒、末15秒；逐场列出触发→动作→对手应对→资源或关系状态变化→支付代价→下一集直接回应。无明确时码则标待验证，不能假造。
4. `S3 State Impact Graph`：每项事件记录演员知识来源、现金/负债、物品保管、地理与时辰、身份资格、经营能力、人际信任、责任权限、后续传播链。使用 `templates/impact_graph_schema.json`。
5. `S4 Adversarial Cross-check`：跑至少八套反例（见 references/attack_suite.md），审查隐藏的免费资源、角色降智、NPC帮助商业对手、跨夜断档、眼神代替商业胜负、重复查账、回家线蒸发、机器评分冒充审核。
6. `S5 Rewrite`：先修P0，再改推进力、胜负、情感、对白、视听；保持未指明角色身份与Canon不变。每个修改都有原文证据、改动位置、前置条件、新增效果、被牵连集数、撤销方案。
7. `S6 Runtime Proof`：比较每场对白长度、演出动作、镜头、转场和整体时码。只有脚本时码不能认证150秒，须围读/粗剪实测。分镜不得代替剧情成因。
8. `S7 Release Assurance`：Machine Flag ≠ Fail；Single Gate PASS ≠ Node PASS；Node PASS ≠ Release PASS。交付候选正文、差异、场次卡、HOLD缺陷清单、证据可追溯表，需独立人工审阅和制作门禁。

## 审稿输出的最少字段
- `claim / evidence / source_type / evidence_date / actual_scene / causal_mechanism / risk / rewrite / touched_episode_ids / regression_check / status`。
- 每一集 `trigger / 1st_decision / adversarial_response / irreversible_change / payoff / hook / immediate_answer_next_ep / time_proof`。
- 每个角色 `goal / power / fear / action / cost / evolving_relations / knowledge_provenance`。
- 每个视觉记忆点 `first_appearance / physical_owner / variation / emotional_meaning / final_payoff`。

## 默认风险优先级
P0：财物流向无来源、身份资格错误、跨日无法兑现、生存交接中断、重大角色知识来源错误、物件空间位移、Canon破坏、误改正文、合同权限越界、时码显然不成立。
P1：重复同一解决机制、无可感知市场胜负、长线目标失踪、重要人物无选择、结尾抛出不回应、反派被降智、情感只靠对视、视频场面无动作。
P2：表述密度、轻喜剧节奏、声画辨识度、台词口癖、精细表演、颜色与光色美感。

## 不可硬编码的经验阈值
“3秒”“30秒”“末15秒”“每3/8集”“各类钩子比例”“女主出场率”可作为**项目内部参数**；不应声称为红果、抖音、广电总局公开认证的统一标准。任何指标的基准样本、验证方法和目标受众必须写在审计单中。

## 工具和测试
`python scripts/audit_script.py input.md --output-dir out` 提取每集汉字量、对白汉字量、场次、时码覆盖及风险**提示**；脚本不判断演技、钩子优劣或合规放行。运行 `python -m unittest discover -s tests` 做基础自测。

## 导航
- `references/evidence_matrix.md` 行业样本与可迁移DNA
- `references/attack_suite.md` 红队问题与叙事反例
- `references/craft_modules.md` 八项叙事子能力
- `templates/episode_audit_card.md` 分集审稿执行卡
- `templates/impact_graph_schema.json` 多层影响图协议
- `memory/portable_memory.md` 跨项目记忆（通用）；项目专属Canon禁止误传播


## v1.1 强制新增门禁（2026-10-15）
**SSS目标不是SSS获证**：请运行 `scripts/calibrate_rank.py` 对每一条播放量输入同时核验平台、真人/AI/漫剧形态、指标、起止窗口；只有已上映且达到内部阈值的作品才能标注对应的“市场表现等级”。未上映剧本只可标 `CREATIVE_TARGET=SSS` / `MARKET_GRADE=UNVERIFIED`；绝对禁止把人工脚本评分转成真实播放量、官方热度或Production Clean。

**竞争胜负的三张证明**：同场至少给出(1)独立来源的重叠潜在买客；(2)对手有合理的竞争力与报价；(3)顾客自主比选并真实付费/交付；在未交付前，预约定钱只能作为负有后续履约责任的现金，不得当成全部利润。失败方应能解释自己的经营选择，不能突然变蠢。

**Runtime Compression Trap**：对0–30/30–135/末15秒逐段列出现有动作总量，时间码只是宣称；把“方案讲解+竞价+三人试妆+盖印+收钱”压在36秒，或把“完整三次妆造+结账”压在26秒必须标记 `PERFORMANCE_PROOF_REQUIRED`。无法取得围读实测只能HOLD，允许通过缩放跨日蒙太奇表达但须真实说明时间轴。

**近因记忆点**：每个镜头级母题登记 `(origin, current_owner, first_cost, next_use, power_shift, final_payoff)`；新增改变必须让观众通过动作而不是概念台词认出。禁用强制口头禅、半边对比、没有来源的随身道具、没获得权限就拿钱或雇人。

**结构动作多样性**：同一种“核凭—协商—分责”作为主解决手段累计多次时，必须主动检索其他可拍发动器：定价、市场分层、流量识别、产能上限、库存风险、客户选择、人才授权、场地占有、流转损失、拒单、货路、真实复购。不要把“换了行业但仍用同一个查凭办法”误算创新。

**全链回归**：每次改编前对接前置集/后续集/资金账/人证/地点/道具状态/人物立场/顾客是否有合法来源。保持冻结集字节一致；自证市场SSS与解除HOLD均须独立Release Assurance Case。

## v1.1 测试运行
```bash
python scripts/calibrate_rank.py --metric monthly_increment_views --platform douyin --format ai_drama --period 2026-09 --value 2370000000
python scripts/release_guard.py /path/to/64_episodes.md --expected-episodes 64 --expected-scenes 268 --freeze-reference /path/to/previous_version.md --frozen E001,E002,E003,E004,E005
python -m unittest discover -s tests -v
```

详见 `references/market_20261015.md` 与 `references/shot_proof_protocol.md`，二者记录已核实数据和可播放时长不能仅凭字数认证的限制。


## v1.2 强制红队协议：同一事件证据、现金负债与播放样本（2026-10-15）
**Causal Scene Identity Gate**：跨集钩子的下一集开头，对每个`actor_id/order_id/scene_date/location/handheld_prop`做连续性检查；“上一集抱婴妇人，下一集又一位抱婴妇人”不能不经来源把一个人变两个。同一客户询价→定钱→交付→尾款分别记录独立`transaction_id`，不能重复收定金。

**Survival↔Enterprise Liability Gate**：三类钱绝对隔离：①已收且已履约的营业收入；②已收但待履约的定钱（附交付义务）；③第三方款/受雇人的工钱。任何将“到账”“成交”“营收”“可自由支配现金”“毛贡献”混写的场次自动列为待核。早期历史结转有实钱不等于历史凭证齐全。

**Counterparty Logic Gate**：对手必须自带真实客户、产能、工资、报价与替代方案；不能出现在直接竞争者的铺里替对方演示产品。竞争失利后对手仍可保留稳定客户；也可能真实退费或承担商户信誉代价。

**Evidence-Graded Market Grade**：作品播放分级必须先通过 `metric/platform/format/period_start/period_end/aggregation/source_date` 七元数据一致性；同市场窗口有≥30条可核样本才可使用项目暂定分位数（S P90 / SS P97 / SSS P99）；不足30条只能列为案例，不授等级。平台官方称谓、内部等级与作品播放数据不可互换。未上映作品永远是 `MARKET_GRADE=UNVERIFIED`。

**Runtime-State Coupling**：`150s`仅是标注。若实际施妆/修缮/搬箱/绕场所需时间高于镜头段时长，必须标 `montage with visible passage of time`，仍须演员围读及粗剪检验；不得通过旁白的一句“做完了”代替履约证明。

**Mechanism Half-Life Gate**：连续三次同类发动机（核单、划责、退款）须证明每次在`能力/市场份额/成本/权利/关系`至少一维发生与前次不同的不可逆变化；只有换场景不算升级。优先采用客户流失、产能约束、渠道竞争、人才授权、市场真实选择、供应可得性、连锁资金压力。不要强制每集同一种反转模板。

**记忆点回收规则**：每个角色/道具记忆点必须可定位`出场/归属/动机/初代价/意义变化/可见回收`，禁止为刷存在感创造无来源道具或口头禅；已冻结前几集只能通过无事实变更的摄影机语法辅助，不擅自篡改剧本正文。

**Top-list Selection Bias Gate**：即便同质数据有30条，也必须披露入样母体和采样规则；只收录“热播百强”“热门十强”产生左截断/幸存者偏差，其P90只是榜内分位数，不是全平台S/SS/SSS标准。没有可推及目标母体的完整数据时，只报告“榜单内相对位置”，不得评为市场SSS。

**本版附带**：`scripts/market_cohort.py`用于同质样本分位数等级、`scripts/transaction_guard.py`用于结构化交易状态回归、`references/v12_real_cases.md`用于2026-10-15证据、`references/v12_redteam_tests.md`用于修订前后的正反样例。程序只验证结构化输入，不读取自然语言给出PGS放行。


## v1.3 叙事复利与回归硬门禁（2026-10-15）
在v1.2基础上新增下列**不可跳过**的审稿环节。v1.3是跨项目可移植文本工具，不修改PGS的Floor或Production Clean权力。

**1. Causal Return Gate（上一集承诺→下一集兑现）**：每个集尾必须填 `promise_or_question -> immediate_next_episode_evidence`。如E010提早晨六块米糕，E011须明确店主已蒸六块且仍要重新谈用工价；如果是隔天、跨城或跨月，必须有实际时间转场。不能用“又来了新委托”装作之前的问题已解决。

**2. Market Flywheel Gate（复利而非每次重新打工）**：每3–6集检查事业状态实际变化：已完成现金收入、客户复购、独立产品/店面/渠道、劳动者自主授权、对手应对、已丧失市场份额与责任成本。若前后状态无差，仅行业名换了，触发 `P1_REPEAT_ENGINE`。不强制所有故事经商；非商战替换成职业技能、人物关系、世界地位或叙事权变化。

**3. Cinematic Proof Gate（取舍可被观众看到）**：主角“比竞争者强”必须让买客亲眼对比服务时辰、质量/体验与价格并自主付钱；不必迫使对手现场认输。赌错须有可见流失、真赔付或后续权限损失。抽象抒情不得代替实际动作。

**4. Beat Budget Gate（可拍动作容量）**：逐段估算人物走位、对白、付款动作、妆造/货物运输真实工时，并区分屏幕剪辑时长与故事世界经过时长；跨时蒙太奇须有至少一个时光变化证据（天气、灯芯、日影、日期牌等）。原稿自称150秒只算名义时码；没有围读粗剪只可标`RUNTIME_HOLD`。

**5. Count and Denominator Gate（数术与口径）**：31笔+12笔+9班=52个业务单位，不能写54；收入、收入净额、可用现金与利润四种概念分开。原始交易凭缺失的现金保留`SOURCE_PENDING`，不得凭空补一张古代账证让事情通过。

**6. Memory Character Arc Gate（记忆点即状态变化）**：将母题当成真实道具/业务权力/不可逆选择管理；一次出现须满足`owner -> new meaning -> measurable consequence`至少其一，终局重复初始物件必须伴有已改变的选择。禁靠所谓高频口头禅刷存在感。

**7. Anti-Score Laundering Gate**：先标注 `CREATIVE_TARGET=SSS` 再做书面创作检查；`MARKET_GRADE`只有上线作品且来源、周期、类型、播放量均可信才可填，完整母体不足时不得从百强榜中推断总体P99。不得声称“达到90=官方SSS”或“模型都打高分=制作绿灯”。

**8. Cross Project Isolation Gate**：加载项目自身Canon/禁用池；禁止把程晚凤、盛明娇、许曼娘、黑发绳、架空大晟、特定30/15秒规范自动传播到无关电影/网剧。短剧的时间设定是项目合同，不是通用定律。项目档案和通用原则必须分别存放。

### 最小输出合同
`references/v13_episode_state_contract.md`为每集状态卡；`scripts/v13_regression.py`可机器验证章节完整、冻结集字节一致、简单跨月业务数、留白与需要人工审查标记。机器只能给出FLAG，不能推断人物动机/演技/市场爆款质量；新改动必须提供真实diff与回滚来源。

### v1.3回归命令
```bash
python scripts/v13_regression.py --base /path/to/V23.23.md --candidate /path/to/V23.24.md --out /tmp/result.json
python -m unittest discover -s tests -v
```


## v1.4 · Narrative Compounding & Editorial Contamination (2026-10-15)

在v1.3基础上新增**先逆向检验再放入母稿**的七项强制测试：

1. **Editorial Leakage Firewall / 审稿痕迹防火墙**：扫描“没有重复入账”“这一处以后在E0xx回收”“不是49秒做完”等给审稿人的解释语；若出现在表演动作中，改成观众能看到的动作。制作级字幕、画面调度说明可保留，但审计断言不能冒充剧情。运行 `scripts/editorial_leakage_gate.py`；扫描结果是待审核提示，不能逐字替换否定词。
2. **Capacity Experiment Gate / 产能试验**：商战胜负不能仅靠客户读一张价目表，要看到工位、人手、原材料、队列或进出路径的实际试验；客户的付款是对此次可证能力的独立选择。反例：凭空加一个没领工钱的帮手。
3. **Commercial Asset Accumulation / 商业资产积累**：在3–6集窗中跟踪从租场→获得特定客户→建立可信技能→服务可履约→授权雇员→形成复购，不得把别人的成交或单次雇工算成自己客资。每条链必须具备可查的首次来源。
4. **Cost Spillover / 损失跨集传导**：错误在本集赔款后，后续是否改变商业资格、雇佣条件、客户选择或同事的信任？短剧的失败不是一笔结清就自动重置。不能为展示损失临时制造无来源资金、顾客或资格禁令。
5. **No New-Bug Editing / 改写防新BUG**：每项补戏都跑`actor_origin / payment_state / prior_booking / object_owner / scene_date / space_transfer / employer_authority`。绝不能无故新增雇员、赠送关键道具、让同一位租客在相邻集两次交押钱或改变已经冻结的集数。
6. **Visible Choice vs Commentary / 可拍取舍**：比胜负结果更重要的是取舍过程：对手仍有正当生意、客人看得到差异、女主放弃过哪些真机会。删掉“第一次意识到”“她的成长在于”等旁白式作者解释的部分，可换成实际动作；非全部解释句一律删除，避免矫枉过正。
7. **Calibration Cohort / 播放量母体**：基于DataEye 2026年上半年真人剧的10亿+真实数据只能建立内部头部目标区间；60天5亿、10亿、20亿门槛均为**暂拟观察指标**，未由完整同质母体百分位证明。不得将红果热力、抖音月增量、跨半年累计、AI漫剧混为一谈。未上映项目只能目标`CREATIVE_TARGET=SSS`，`MARKET_GRADE=UNVERIFIED`。

### v1.4 审稿流程要求
修改前生成**双向依赖卡**：本集前置资源、人物知识、付钱事实，以及未来受本次修改影响的集数和结果；修改后必须保留`old/new/reason/affected_ids/recheck_result`证据链。对表演时长，提供逐镜动作预算和音乐蒙太奇的实际故事时间；150秒时码仍非围读或剪辑验收。

### 运行
```bash
python scripts/editorial_leakage_gate.py screenplay.md --out redteam_editorial.json
python scripts/v14_regression.py --base v2324.md --candidate v2325.md --out redteam_regression.json
python scripts/audit_script.py screenplay.md --output-dir audit_out
python -m unittest discover -s tests -v
```


## v1.5 · Evidence-to-Action, Opponent Autonomy, Continuity (2026-10-15)

**升级基准**：继承v1.4全部测试；PGS-Floor以项目最新合约为准，v1.5绝不自授SSS或Production Clean。

### 新增不可跳过的流程
1. **Competitive Delta Without Stage Theft / 对手独立场域**：对手拿真实报价、熟手、成本与信誉服务自己的顾客，不准为让主角胜出，把对手员工安排到主角铺内示范、免费代排或擅自把约客转移。客户应亲见两家不同体验及期限，不以旁白说“选择更好”。
2. **Earned Flywheel / 获得性复利**：每个商业单元记录 `inquiry → quote → deposit → delivered → final_paid → review/referral`，无签名或未交付的意向不得升级为商誉/利润；`repeat_customer`与`referred_lead`必须分开；一场赚过钱不自动获得经营场所。
3. **Choice Has Opportunity Cost / 可见放弃**：主角放弃单/客户/高工价时至少一次让该资源被现实对手接走或过期，不新增凭空奖励。每个3–6集阶段有赢有输；禁止“服软→奇迹客户突然出现”的公式。
4. **What Changed After Compensation / 长期负面后果**：赔付只了结特定债务，可能仍丧失急件资格、客户信任或机会；后续恢复须有新的按时履约，绝不凭一句“我懂了”当日恢复。
5. **Static Pass Is Not Filmability / 负担预算**：分场记录屏幕时间、剧情经过时间、必要转场、人/物走位、实际工序。跨月52项不能在50秒中逐单表演；明确蒙太奇与日期、天气、状态变动。超过窗口列 `HOLD_RUNTIME` 不靠加快台词解除。
6. **Production Notes Firewall / 制作注释隔离**：正文可以写可拍镜头和明确字幕，却不准写“不让演员演五十二单”“今后第X集回收”“这代表人物成长”等审稿说明。所有未证事实放审计台账。
7. **Market Cohort Ontology / 播放分级标准**：每条成绩保留 `title,platform,format,metric,period_start,period_end,observed_on,units,source`；有选择偏差的榜单只做对标案例。同平台、真人、同60日且可核数据才可讨论用户预设S/SS/SSS暂拟档。无同质发行数据库不能说“P99”或官方等级；未上映用 `CREATIVE_TARGET=SSS,MARKET_GRADE=UNVERIFIED`。
8. **Baseline Is Law / 版本与锁定**：修改前/后完整章节、场次、每处真实差异；封存集逐字不变；无明确授权不得写回旧穿越设定、金融丑闻、性格互撕、男主官面代办或退役商业业态。新剧加载自己的禁用表，不继承本剧角色。
9. **Money Versus Proof / 现钱≠来源凭据**：E031可见120文只能证明拿得出来，缺旧零工原凭仍列`SOURCE_PENDING`；E032现账公式与52业务单位必须分别通过，缺证不可假补。E053三妆的30定钱和100尾钱只计一次。
10. **Editorial Diff Reverse Gate / 修复负面样本**：任何新增的人、画押、客钱、镜具、场位或改时辰都要做前驱检查和后效回归；如果新增问题多于解决问题，撤销该改动，不能凭“更爽”免除。

### 交付须包括的证据
`完整剧本 + 文本差异 + 变更集索引 + 改动前后前提/结果 + 未放行项 + 行业证据与口径 + 首看和粗剪测试协议 + Skill测试结果`。另附一份与项目Canon分开的通用记忆文件；写出可由用户或其他Agent导入的步骤，不宣称已更新账户记忆。

### v1.5新增运行程序
`python scripts/v15_evidence_gate.py --base base.md --candidate candidate.md --ledger change_ledger.json --out evidence.json`
`python -m unittest discover -s tests -v`


## v2.1 新增硬门禁：Source Trace & Canon Isolation & Pacing Proof
1. 首先识别项目当前64集或其他目标全集的真实母稿；报告或评分不替代母稿。
2. 对诊断中所有“原剧如此”“某集原句是...”进行Source Quote Anchor测试；unverified不得据此修改。
3. 将旧版本/禁用手段/竞品复用分类为PROJECT-CONFLICT、UNSUPPORTED、APPLICABLE，不强行三集一反派。
4. 可操作的修改应输出具体文本、集数、角色知识、物件/钱的来源及下一集后果，进行全局diff与回归。
5. 0-150秒覆盖是静态结构检查；密度和试排独立HOLD。
6. 发布/内部创作等级拆分，市场同源同窗口，未上映不得预评级。
参见 references/v21_evidence_contamination_and_runtime.md 与 scripts/v21_source_and_pacing_gate.py。

## v2.2 Emotional Cost & Evidence-Grounded Retention Gate
先做诊断证据锁，后做中段选择四证：选择、放弃机会、可见后果、后续改用。自动程序可以验证结构化事件的字段是否存在，但不能宣称人类观众一定共鸣。详见 `references/v22_emotional_cost_and_fact_lock.md`，执行 `python -m unittest discover -s tests -v`。严禁将未播稿自评为SSS市场等级、将AI榜单月增量冒充真人或把编剧修复建议写进演员台词。任何生产级放行仍遵守PGS30 Gate Bundle。