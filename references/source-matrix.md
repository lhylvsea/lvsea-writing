# 新增来源与取舍矩阵

本文件记录本次增量整合的来源、固定 revision、采用内容和明确排除项。来源仓库只作为研究材料，`lvsea-writing` 不把它们的完整 `SKILL.md`、示例、数据集或模型权重复制进来。

| 来源 | 固定 revision | 本次采用 | 不直接采用 |
| --- | --- | --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer) | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | 33 类英文 AI 痕迹、保留信息不保留机械形状、无编造、样本校准、最终二次审校 | 英文中心的绝对破折号规则和完整原文目录 |
| [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) | `9a7f35b7b9ad8c3abd71f10757ec9f91fb8ae165` | 53 模式分层、检测/改写/编辑三模式、5 种声音、代码/引用遮罩、短文本低置信度、迭代复查、统计指标 | 0–100 分数的确定性外观、英文“perplexity”直接迁移到中文 |
| [brandonwise/humanizer](https://github.com/brandonwise/humanizer) | `4b9b9bee384aea139f599133d2de1e1ceaee71a3` | burstiness、词汇重复、批量扫描、版本比较、基线回归和 Unicode 残留的思路 | Node CLI 依赖、英文阈值和“分数等于作者来源”的暗示 |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | `8da1f030185bdfe8471220585162991eaeb970e9` | 主语和动作、具体化、读者在场、少用金句、节奏和快速审校清单 | “所有副词/被动语态/破折号都删”的绝对化规则 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` | 中文四字词堆砌、首先其次最后、套话开头、设问回答、口号结尾、翻译腔提醒 | 译文示例里的虚构数字、未经验证的中文检测结论 |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | `27642f5bfed2dc1bbf8ee59a2c1ee602a626bbd7` | 多源证据、三重验证、观点/表达 DNA、局限、冲突保留、阶段检查点 | 人物蒸馏、并行 Agent 成本承诺和必须联网的流程 |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | `e988add20dab0fa97d7a76781c48961c8184288e` | 先读 brief、反默认、识别受众、不要用一个模板解决所有任务 | 前端栈、视觉 dials、CSS/动效和页面 pre-flight |
| [dongbeixiaohuo/writing-agent](https://github.com/dongbeixiaohuo/writing-agent) | `cd411cfbc44f03dc0513b2f5ec3804f13896f5eb` | 长文分阶段、风格建模证据账本、事实核查、版本记录、读者测试、可选导出 | Claude 专属 Subagent 名称、强制每阶段停机、未必适合短稿的重型项目树 |
| [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection) | `1f8c15c28f87e09a5abfd86ee6e15005dc7d2119` | 中英、单文本/问答/语言学检测的研究背景；检测器作为反馈而非真值 | HC3 数据、模型权重、外部服务调用和数据集衍生内容 |
| [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) | `27d29232f10124db904ca9c0536d0b67cb3b2833`；MIT | 白名单式最后编辑、信息守恒、结构不动、命中样本审计、排除不稳健特征 | 整套上游 Skill、语料、脚本、统计阈值和独立入口触发 |

## 本轮主线升级来源

| 来源 | 固定 revision / 信号 | 本次采用 | 不直接采用 |
| --- | --- | --- | --- |
| [zhouluobo X 文章](https://x.com/zhouluobo/status/2091846529321664695) | 文章发表于 2026-08-24；2026-08-25 通过只读镜像接口提取，X 页面本身受访问限制 | 研究、结构、读者、声音、场景和最后 Humanizer 的角色分工；按需求串联而不是强制全装；技术文档的代码/链接/参数验收；人工终审是最后决定 | 不复制文章全文、截图、原作者私人配置或“所有 Skill 都必须安装”的结论 |
| [CommandCodeAI/agent-skills content-research-writer](https://github.com/CommandCodeAI/agent-skills/tree/main/skills/content-research-writer) | `f490dd9016f2729311e90f317dcb6c98be1a1500`；skills.sh 检索信号 25 installs（2026-08-25） | 研究、提纲、逐段反馈、引用账本和声音保留；改成中文事实账本与按需路由 | 强制问卷、虚构示例数据、把钩子或“准备发布”当成质量证明 |
| [mblode/ghostwriter](https://github.com/mblode/ghostwriter) | `046f1f05906d911277745f1d665cd07203005038`；skills.sh 检索信号 5 installs（2026-08-25）；MIT | 核心声音 + 场景声音、样本训练/评估分离、盲测思路、私人档案不进公开包 | 外部 CLI、私有目录约定、把盲测结果外推成通用质量结论 |
| [mblode/agent-skills](https://github.com/mblode/agent-skills) | `e97a3b383f5944f90d41eb92b24b4fb3b917a7f9`；docs-writing skills.sh 检索信号 770 installs（2026-08-25）；MIT | 用 IS/IS NOT 设边界；产品文案先明确行动/读者/结果；技术文档加可运行代码、链接和参数门 | 外部 Ghostwriter 依赖、前端/品牌专用规则和与本仓库无关的工具路由 |
| [skills.sh content-research-writer 搜索](https://skills.sh/composiohq/awesome-claude-skills/content-research-writer) | 2026-08-25 只用于发现候选；目录安装量不等于质量 | 使用目录作为 prior-art 入口，并保留来源、安装量和实际源文件的区分 | 不把安装量、stars 或搜索排名合并成质量分数，不盲装候选 |
| 本地 `find-skills`、`lvsea-research`、`lvsea-zao-skill` | 当前环境已安装；`lvsea-zao-skill` 0.1.1 | skills.sh -> GitHub 源码 -> keep/adapt/reject/invent 台账；Intent -> Research -> Synthesis -> Package -> Eval -> Review -> Release；研究证据账本和缺失证据标记 | 不把元 Skill 的创建流程复制成写作规则，不用静态评测冒充模型或人工质量证据 |

## 本地专家关系

| 专家 | 在 `lvsea-writing` 中的角色 | 入口策略 |
| --- | --- | --- |
| [lhylvsea/lvsea-xiezuo](https://github.com/lhylvsea/lvsea-xiezuo) | 小红书素材和证据前置专家 | 由单入口按素材意图调用；也支持用户显式调用做素材研究 |
| `lvsea-writing` | 唯一用户侧主入口和通用写作主流程 | 默认调用入口 |
| `lieflat-less-ai-tone` | 完整成稿后的严格后处理专家 | 只在最后阶段调用；缺失时走严格降级合同 |

## 共同安全边界

- 任何来源的“分数”都只能描述文本在某个规则或模型下的可疑信号，不能证明作者身份，也不能保证绕过平台检测。
- 开源项目里的 before/after 只用于理解修订动作；用户没有提供的数字、地点、经历、心理和引语不能从例子借进事实稿。
- 中文的句长、词频、burstiness 和 perplexity 不能直接套用英文阈值。中文检查器默认以字数、分句、四字词密度、结构和语境提示为辅，不把统计信号升级为硬结论。
