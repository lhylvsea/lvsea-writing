# lvsea-writing

一个中文优先、事实敏感的单入口写作与路由 Skill。

它不是单纯的“AI 味词典”，也不以规避检测为目标。它更关心一篇文字是否有真实材料、明确判断、具体动作和合适的说话位置，再处理自然表达、节奏与格式。

当前版本：<code>0.4.0</code>

## 能做什么

- **轻量改稿**：保留事实、数字、名称和判断，只改表达、推进和格式。
- **检测后改写**：先按意义膨胀、宣传腔、模糊归因、公式句、AI 高频词和风格痕迹出报告，再定点改写。
- **风格校准**：根据 3–5 篇同一作者样本提取稳定的表达特征，不复制原句，不偷渡样本之外的经历和观点。
- **深度长文**：按任务契约、证据账本、立场、提纲、初稿、编辑、去痕、事实核查和终稿推进。
- **写作流水线**：把资料、结构、读者、声音、场景、初稿、最后去 AI 味和人工终审串成一条线；去 AI 味不再抢跑。
- **统计复查**：输出句长变化、词汇多样性、三元组重复、结构和 Unicode 残留等线索，并明确它们不是作者身份结论。
- **中文、英文和中英混写**：中文规则优先，英文规则单独路由，避免把英文阈值直接硬套到中文。

## 单入口使用

日常只调用 `$lvsea-writing`，不需要先判断三个 Skill 谁负责。它会按任务阶段选择下游专家：

| 你要做的事 | 内部路线 |
| --- | --- |
| 普通写作、改稿、长文、教程、制造管理、政策、PPT、口播 | `$lvsea-writing` 主流程 |
| 小红书素材、互动指标、评论区、飞书素材库 | `$lvsea-xiezuo` -> 写作接力包 -> `$lvsea-writing` |
| 已有完整成稿，只做最后去 AI 味 | `$lieflat-less-ai-tone`；未安装时使用严格后处理降级模式 |
| 从小红书素材写成完整文章并交付终稿 | `$lvsea-xiezuo` -> `$lvsea-writing` -> `$lieflat-less-ai-tone` -> 人工终审 |

不要把三套规则一次性叠加。素材专家不负责通用成稿，终稿专家不负责研究和结构，`lvsea-writing` 才是用户侧的总入口。详细判定和降级规则见 [references/specialist-routing.md](references/specialist-routing.md)。

## 核心原则

1. 事实和来源优先于“像真人”。
2. 保留信息，不保留机械形状。
3. 先修主语、动作、证据和顺序，再考虑口语质感。
4. 按成组模式判断，不因为一个词、一个破折号或一个短句就误判。
5. 不凭空添加数字、人物动作、心理、对白、经历、来源或产品能力。
6. 正式报告、技术文档、安全和党政材料优先保证准确、庄重和必要结构。
7. 统计分数只能帮助复查，不能证明文本由谁写成，也不能保证平台检测结果。
8. 去 AI 味是最后的编辑层，不能替代研究、主线、风格、专业核验和作者终审。

## 快速开始

### 安装到 Codex

将仓库目录复制或链接到以下 Skill 目录：

~~~text
C:\Users\rabbit\.codex\skills\lvsea-writing
~~~

确认目录中直接存在 <code>SKILL.md</code>，然后在 Codex 中使用：

~~~text
使用 $lvsea-writing，先判断这份材料适合轻量改稿还是深度流程；保留事实和判断，输出自然终稿，并列出仍需核实的地方。
~~~

也可以使用 Agent Skills 兼容安装器：

~~~powershell
npx skills add https://github.com/lhylvsea/lvsea-writing --skill lvsea-writing -g -y
~~~

`lvsea-xiezuo` 和 `lieflat-less-ai-tone` 是可选下游专家。只有确实要做小红书素材雷达或使用其严格终稿规则时才安装，不影响主入口的普通写作流程。

你可以这样说：

~~~text
用 $lvsea-writing 先研究资料、搭主线和提纲，等初稿完成后最后一步再去 AI 味，保留事实，最后把需要我确认的地方列出来。
~~~

### 常用调用

~~~text
使用 $lvsea-writing，去掉这篇文字的 AI 味，但保留事实和我的判断。

先用 $lvsea-writing 检测这篇稿子的 AI 痕迹，再改写，不要先动原文。

用 $lvsea-writing 学我的写作样本，但不要把我的口头禅机械塞进每一段。

用 $lvsea-writing 按深度长文流程，从选题、证据、提纲、初稿、审稿到事实核查逐步推进。
只调用 `$lvsea-writing`：从小红书素材筛选、证据卡和二创简报开始，写成文章，最后一步再做严格去 AI 味。
~~~

## 推荐主线

资料/证据 -> 主判断/提纲 -> 读者 -> 声音 -> 场景/格式 -> 初稿 -> 最后去 AI 味 -> 人工终审。

短改稿可以合并前几步；研究型长文、教程和正式材料不要跳过资料与结构。完整阶段交接见 [pipeline.md](references/pipeline.md)。

## 适用场景

仓库内置了四个可直接改写的示例：

1. [制造管理与生产运营](examples/01-manufacturing-management.md)
2. [安全管理、党建党政与政策解读](examples/02-safety-and-policy.md)
3. [公众号、知乎与行业解读](examples/03-industry-article.md)
4. [视频口播与 PPT 页面文字](examples/04-video-and-slide-copy.md)

更多中文触发词、输入要求、模式说明和调用示例见 [USAGE.zh-CN.md](USAGE.zh-CN.md)。

## 文稿检查器

检查器只报告问题，不自动改写文章。它使用 Python 标准库，建议 Python 3.10+。

~~~powershell
python scripts/check_writing.py path\to\draft.md --scenario general
python scripts/check_writing.py path\to\draft.md --scenario professional
python scripts/check_writing.py path\to\draft.md --scenario social --texture
python scripts/check_writing.py path\to\draft.md --json
~~~

高置信复制残留和助手式框架会返回失败；语境词、句式、统计指标、占位符、隐藏字符和格式问题会作为人工复查提醒。脚本通过不代表事实已经核实，出现提醒也不代表某个词在当前语境一定错误。

## 深层参考

- [写作流水线](references/pipeline.md)：把研究、结构、读者、声音、场景、初稿、最后去 AI 味和人工终审串起来。
- [写作工作流](references/workflow.md)：轻量改稿、深度长文、检测评分和风格学习的路由。
- [作者人工终审](references/human-final-gate.md)：事实回看、读出声、署名决定和反馈回写。
- [事实与证据](references/evidence.md)：来源分层、虚构边界和事实核对。
- [风格建模](references/style-modeling.md)：样本门、表达 DNA、验证短文和盲测。
- [读者测试](references/reader-test.md)：目标读者、怀疑读者和行动读者检查。
- [中文 AI 痕迹规则](references/patterns-zh.md)：中文套话、翻译腔、成组信号和例外。
- [英文 AI 痕迹规则](references/patterns-en.md)：英文结构模式和误判防护。
- [检测信号边界](references/detector-evidence.md)：统计指标、检测器和作者判断的边界。
- [新增来源取舍矩阵](references/source-matrix.md)：整合来源、固定 revision 和排除项。
- [单入口专家路由](references/specialist-routing.md)：三个 Skill 的职责、顺序、交接和降级。
- [最后编辑适配说明](references/late-humanizer-adapter.md)：`lieflat-less-ai-tone` 的白名单式终稿边界。

## 来源与许可证

本项目为独立整理和改写，不复制上游 Skill 的完整文件、示例、检查器实现、数据集或模型权重。详细 revision、许可证和取舍记录见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [source-matrix.md](references/source-matrix.md)。

项目代码以 MIT License 发布，见 [LICENSE](LICENSE)。

## 验证

仓库维护时可运行：

~~~powershell
$env:PYTHONUTF8='1'
python -m py_compile scripts/check_writing.py
python -m unittest discover -s tests -v
~~~

完整的中文使用说明、限制和四个真实应用场景见 [USAGE.zh-CN.md](USAGE.zh-CN.md)。

## 维护者检查

发布前清单：

- [ ] SKILL.md 只有根入口，且描述包含中文触发词
- [ ] 资料、结构、声音、场景和最后 Humanizer 的顺序没有被改乱
- [ ] 触发评测、包校验、单元测试和安装发现均通过
- [ ] provider/人工证据缺失时已明确标注，不把静态结果写成质量结论

~~~powershell
$env:PYTHONUTF8='1'
python scripts/validate_package.py .
python -m unittest discover -s tests -v
~~~

本包的治理方法参考 qiaomu-meta-skill、yao-meta-skill 和本地 lvsea-zao-skill；在治理环境中还可以运行对应的 validate_skill.py、trigger_eval.py、Skill IR 和上下文预算检查。由于上游 validate_skill.py 默认校验的是 lvsea-zao-skill，本仓库的可直接运行入口是 validate_package.py。

## Troubleshooting

- Skill 未被发现：确认安装目录下直接存在 SKILL.md，不要只把仓库套在多层目录里。
- Skill 过早去 AI 味：在调用中明确“先资料、结构和场景，最后一步再去 AI 味”，并要求保留中间产物。
- 不知道该用哪个 Skill：只调用 `$lvsea-writing`；出现小红书素材指标时让它路由到 `lvsea-xiezuo`，已有完整成稿时才进入 `lieflat-less-ai-tone`。
- 风格不像本人：补充 3–5 篇同作者、同场景样本，先建声音证据，不要只追加禁用词。
- 事实不稳：停在证据账本，补来源或把主张降级为推断，不要继续抛光句子。

## 重要边界

去 AI 味不是规避检测，也不是凭空伪造真人经历。统计信号不能证明作者身份；没有 provider 或人工盲评时，仓库只声明完成了静态、触发、结构和安装验证。
