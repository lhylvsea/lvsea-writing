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

## 共同安全边界

- 任何来源的“分数”都只能描述文本在某个规则或模型下的可疑信号，不能证明作者身份，也不能保证绕过平台检测。
- 开源项目里的 before/after 只用于理解修订动作；用户没有提供的数字、地点、经历、心理和引语不能从例子借进事实稿。
- 中文的句长、词频、burstiness 和 perplexity 不能直接套用英文阈值。中文检查器默认以字数、分句、四字词密度、结构和语境提示为辅，不把统计信号升级为硬结论。
