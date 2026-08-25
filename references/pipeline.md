# 写作流水线与阶段交接

## 一条主线

X 文章提出的关键不是把几个提示词叠在一起，而是把写作拆成互相交接的角色：研究解决材料，结构解决主线，读者测试解决理解，声音档案解决“像谁”，场景 Skill 解决“写给谁、拿来做什么”，Humanizer 只在最后清理表达残留。lvsea-writing 把这些角色收进一个入口，按任务需要启用，不要求每篇稿子走满全部阶段。

~~~text
Intent
  -> Research / Evidence
  -> Thesis / Outline
  -> Reader / Context
  -> Voice / Samples
  -> Domain / Format
  -> Draft / Edit
  -> Humanizer final pass
  -> Author final gate
~~~

### 为什么去 AI 味必须靠后

- 结构还没成立时先改“人味”，只会把空洞内容抛光得更顺。
- 来源还没核对时先改写，容易把推测改成肯定、把归属改丢或把数字改错。
- 作者声音还没确定时先套口语，会把所有人写成同一个“自然的人”。
- 初稿已经完成后再做定点清理，才知道哪些重复是为了说明，哪些停顿确实是作者习惯，哪些正式结构不能动。

因此，“去 AI 味”是终稿编辑动作，不是研究、构思或作者声音的替代品。

## 阶段契约

| 阶段 | 要回答的问题 | 最小输入 | 最小交接物 | 通过门 |
| --- | --- | --- | --- | --- |
| brief | 这篇稿子给谁、要做什么、不能动什么 | 任务描述、原稿或题目 | 任务契约 | 体裁、读者、意图和事实边界可说清 |
| evidence | 哪些是真的，哪些还不能写成事实 | 原始材料、来源、用户说明 | 证据账本 | 关键主张有来源或被标为待核验 |
| structure | 主判断是什么，信息如何推进 | 证据账本、读者问题 | 主判断与提纲 | 每段有任务，没有靠小标题填空 |
| reader | 陌生读者会在哪卡住或不信 | 提纲/草稿、读者画像 | 读者测试 | 隐藏前提、术语跳跃和行动缺口已列出 |
| voice | 怎样像作者，而不是像通用好文章 | 3–5 篇同作者样本（可选） | 样本证据与声音规则 | 稳定特征有证据，场景边界明确 |
| domain | 这个场景的格式和验收是什么 | 提纲、读者、交付平台 | 场景约束 | 专业结构、代码、链接、页面或朗读要求明确 |
| draft | 能否把内容写成一版完整稿 | 前置交接物 | draft-v1 / draft-v2 | 事实、主线、格式和信息密度先成立 |
| humanizer | 终稿里还剩哪些模板残留 | 完整草稿、场景、声音规则 | 检测报告与最小修改 | 只改真实问题，事实与结构回查通过 |
| author-gate | 作者真的愿意署名、使用和负责吗 | 终稿、来源、修改说明 | 人工终审记录 | 作者确认或明确保留项/待核验项 |

## 默认路由

### 研究型公众号、行业长文

~~~text
brief -> evidence -> structure -> reader -> voice(可选) -> domain(article) -> draft -> humanizer -> author-gate
~~~

资料不足先研究；材料够但观点散，先搭主线；没有本人样本时不要假装“像本人”。

### 制造管理、安全、党政和政策材料

~~~text
brief -> evidence -> structure -> domain(formal) -> draft -> fact gate -> humanizer(克制) -> author-gate
~~~

“自然”服从准确、庄重、责任边界和正式格式。不要为了去 AI 味删掉编号、引用、政策原文或必要术语。

### 技术教程、README 和产品文档

~~~text
brief -> evidence -> structure -> domain(docs) -> draft -> runnable/link/parameter checks -> humanizer -> author-gate
~~~

Humanizer 不修改代码、参数、命令和链接的语义。代码和链接检查失败时，先修技术内容，不用句子润色遮盖失败。

### 产品页、CTA 和短文案

~~~text
brief(goal/reader/action) -> voice/brand -> domain(copy) -> draft alternatives -> line review -> humanizer -> author-gate
~~~

先明确唯一行动和读者结果，不把长文的研究和段落结构硬套到一句按钮文案上。

### 视频旁白与 PPT

~~~text
brief -> evidence -> structure -> domain(script/slides) -> draft
       -> read-aloud/layout check -> humanizer -> author-gate
~~~

旁白、字幕和页面文字分别适配；页面保留事实、数字和行动，不把制作说明混入正文。

## 可跳过与不可跳过

可以跳过：没有陌生事实的短改稿可不联网；用户没有要求学样本时可不建声音档案；一句 CTA 不需要长文证据账本。

不能跳过：事实边界、主线/交付目的、场景格式和最终事实回查。任何任务都不能把 Humanizer 提前到资料、结构和声音之前。用户明确要求“只检测不改”时，停在检测报告；用户要求只要成稿时，不强制展示全部中间文件。

## 项目文件建议

需要可复核的长文时，再在用户指定的写作目录落盘：

~~~text
brief.md
evidence.md
outline.md
reader-test.md
voice-profile.md
draft-v1.md
draft-v2.md
humanizer-review.md
final-gate.md
final.md
~~~

这些文件是交接面，不是每篇稿子的硬性模板。真实材料、私人样本和凭据留在项目目录，不写进公开 Skill。
