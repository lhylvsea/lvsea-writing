#!/usr/bin/env python3
"""Check high-confidence AI residue and human-judgment writing risks.

The checker reports. It never rewrites the draft and it does not claim to
measure whether a text was written by a human.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path


HARD_RESIDUE = (
    "contentReference",
    "oaicite",
    "turn0search",
    "turn1news",
    "turn0view",
    "filecite",
    "[cite:",
    "[cite_start]",
    "[span_",
    "grok_card",
    "ppl-ai-file-upload",
    "Here is the revised version",
    "好的，下面是",
    "以下是修改后的",
    "以下是改写后的",
    "很好的问题",
    "你完全正确",
    "希望这对你有帮助",
)

HARD_STOPS = (
    "说白了",
    "说穿了",
    "简单来说",
    "换句话说",
    "先说结论",
    "值得一提的是",
    "不得不说",
    "引人入胜的观点",
    "这是一个很有趣的视角",
)

CONTEXT_TERMS = (
    "赋能",
    "生态",
    "抓手",
    "闭环",
    "破局",
    "颠覆式",
    "认知升级",
    "长期主义",
    "关键抓手",
    "底层逻辑",
    "全链路",
    "颗粒度",
    "对齐",
    "协同",
    "方法论",
    "心智",
    "打法",
    "落地",
)

ROAD_SIGNS = (
    "让我们来看看",
    "接下来",
    "值得注意的是",
    "需要指出的是",
    "从某种意义上说",
    "更重要的是",
    "更微妙的是",
    "还有一层",
    "总之",
    "综上所述",
    "归根结底",
)

CONJUNCTIONS = (
    "因为",
    "所以",
    "但是",
    "然而",
    "同时",
    "此外",
    "而且",
    "并且",
    "因此",
    "不仅",
)

PIVOT_PATTERNS = (
    re.compile(r"(?:并)?不是[^。！？\n]{0,90}?而是"),
    re.compile(r"并非[^。！？\n]{0,90}?而是"),
    re.compile(r"不在于[^。！？\n]{0,90}?而在于"),
    re.compile(r"与其说[^。！？\n]{0,90}?(?:不如|毋宁|倒不如)"),
    re.compile(r"看似[^。！？\n]{0,90}?(?:其实|实际|实则)"),
    re.compile(r"表面(?:上)?[^。！？\n]{0,90}?(?:其实|实际|实则)"),
    re.compile(r"回头(?:看|一看)?才(?:发现|明白|知道)"),
    re.compile(r"你以为[^。！？\n]{0,60}?(?:其实|才发现|才知道)"),
)

NOMINALIZATION_PATTERNS = (
    re.compile(r"进行(?:了|一次|一场|着)?[^。，！？\n]{0,12}(?:调整|优化|升级|分析|讨论|沟通|梳理|复盘|迭代|探索|尝试|思考|规划)"),
    re.compile(r"实现了?[^。，！？\n]{0,14}的?[^。，！？\n]{0,6}(?:提升|增长|突破|转变|跃升|落地)"),
    re.compile(r"完成了?对[^。，！？\n]{0,16}的"),
    re.compile(r"具有[^。，！？\n]{0,10}(?:意义|价值)"),
    re.compile(r"通过[^，。！？\n]{1,20}从而"),
)

UNSOURCED_AUTHORITY = (
    "研究表明",
    "数据显示",
    "业内普遍认为",
    "专家指出",
    "众所周知",
)

REPEATED_OPENERS = (
    "其实",
    "不过",
    "当然",
    "所以",
    "但是",
    "后来",
    "当时",
    "很多人",
    "问题是",
    "更重要的是",
)

PLACEHOLDER_PATTERNS = (
    re.compile(r"\b(?:TODO|TBD|FIXME|INSERT\s+(?:SOURCE|DETAILS?)|YOUR\s+(?:NAME|TOPIC|TEXT))\b", re.IGNORECASE),
    re.compile(r"\b20\d{2}-(?:XX|MM|DD)(?:-(?:XX|MM|DD))?\b", re.IGNORECASE),
    re.compile(r"\[[^\]\n]{1,36}(?:your|insert|placeholder|fill|name|date|source)[^\]\n]{0,36}\]", re.IGNORECASE),
    re.compile(r"(?:待补充|待填写|待核实|占位符)", re.IGNORECASE),
)

REASONING_ARTIFACT_PATTERNS = (
    re.compile(r"\b(?:let me think|i(?:'ll| will) start by|breaking this down|step\s+\d+|first,?\s+i(?:'ll| will))\b", re.IGNORECASE),
    re.compile(r"(?:下面是修改后的|以下是改写后的|接下来我(?:们)?(?:将|来)|让我(?:们)?先(?:看|梳理))"),
)

FALSE_AGENCY_TERMS = (
    "数据告诉我们",
    "市场奖励",
    "算法决定",
    "数字说明",
    "the data tells us",
    "the market rewards",
    "the numbers prove",
    "the algorithm decided",
)

HOOK_TERMS = (
    "你可能会问",
    "答案是",
    "你是否也",
    "听起来很熟悉",
    "the catch?",
    "here's the thing",
    "the brutal truth",
    "sound familiar?",
)

LATIN_WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
METRIC_TOKEN_PATTERN = re.compile(r"[\u4e00-\u9fff]|[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?")
SUSPICIOUS_CODEPOINTS = {0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF}


@dataclass
class Finding:
    category: str
    line: int
    message: str
    excerpt: str


@dataclass
class ScanResult:
    han_count: int
    scenario: str
    failures: list[Finding]
    warnings: list[Finding]
    metrics: dict[str, int | float | None]

    @property
    def exit_code(self) -> int:
        return 1 if self.failures else 0


def han_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def content_unit_count(text: str) -> int:
    """Count Chinese characters plus Latin words so English can be reviewed too."""

    return han_count(text) + len(LATIN_WORD_PATTERN.findall(text))


def tokenize_for_metrics(text: str) -> list[str]:
    return METRIC_TOKEN_PATTERN.findall(text)


def coefficient_of_variation(values: list[int]) -> float | None:
    if len(values) < 2:
        return None
    mean = sum(values) / len(values)
    if not mean:
        return None
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return math.sqrt(variance) / mean


def compute_metrics(text: str) -> dict[str, int | float | None]:
    """Return review signals, never an authorship verdict."""

    tokens = tokenize_for_metrics(text)
    trigrams = [tuple(tokens[index : index + 3]) for index in range(len(tokens) - 2)]
    sentence_values = [
        content_unit_count(match.group())
        for match in sentences(text)
        if content_unit_count(match.group()) >= 4
    ]
    unique_tokens = len(set(token.casefold() for token in tokens))
    repeated_trigram_ratio = 0.0
    if trigrams:
        repeated_trigram_ratio = 1 - (len(set(trigrams)) / len(trigrams))
    return {
        "content_units": content_unit_count(text),
        "token_count": len(tokens),
        "sentence_count": len(sentences(text)),
        "sentence_cv": coefficient_of_variation(sentence_values),
        "type_token_ratio": unique_tokens / len(tokens) if tokens else 0.0,
        "repeated_trigram_ratio": repeated_trigram_ratio,
        "paragraph_count": len(paragraph_blocks(text)),
        "four_char_run_count": len(re.findall(r"[\u4e00-\u9fff]{4,}", text)),
    }


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def excerpt(value: str, width: int = 72) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value if len(value) <= width else value[: width - 1] + "…"


def mask_non_prose(text: str) -> str:
    """Mask frontmatter, code and links without changing line positions."""

    def mask(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group())

    patterns = (
        re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL),
        re.compile(r"```.*?```", re.DOTALL),
        re.compile(r"`[^`\n]*`"),
        re.compile(r"\]\([^\n)]*\)"),
        re.compile(r"https?://[^\s)>]+"),
        re.compile(r"<[^>\n]+>"),
    )
    masked = text
    for pattern in patterns:
        masked = pattern.sub(mask, masked)
    return masked


def term_matches(text: str, terms: tuple[str, ...]) -> list[tuple[int, str]]:
    matches: list[tuple[int, str]] = []
    occupied: list[tuple[int, int]] = []
    for term in sorted(terms, key=len, reverse=True):
        for match in re.finditer(re.escape(term), text, re.IGNORECASE):
            start, end = match.span()
            if any(start < old_end and end > old_start for old_start, old_end in occupied):
                continue
            matches.append((start, term))
            occupied.append((start, end))
    return sorted(matches)


def pattern_matches(text: str, patterns: tuple[re.Pattern[str], ...]) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for pattern in patterns:
        matches.extend(pattern.finditer(text))
    return sorted(matches, key=lambda match: match.start())


def add_pattern_findings(
    findings: list[Finding],
    source_text: str,
    prose: str,
    patterns: tuple[re.Pattern[str], ...],
    category: str,
    message: str,
) -> None:
    for match in pattern_matches(prose, patterns):
        findings.append(
            Finding(
                category,
                line_number(source_text, match.start()),
                message,
                excerpt(match.group()),
            )
        )


def add_unicode_findings(findings: list[Finding], source_text: str, prose: str) -> None:
    for position, char in enumerate(prose):
        codepoint = ord(char)
        category = unicodedata.category(char)
        if codepoint in SUSPICIOUS_CODEPOINTS or (category == "Cf" and char not in "\n\r\t"):
            name = unicodedata.name(char, f"U+{codepoint:04X}")
            findings.append(
                Finding(
                    "隐藏字符",
                    line_number(source_text, position),
                    f"发现不可见或格式控制字符 {name}，检查是否为复制残留或 Unicode 混淆",
                    f"U+{codepoint:04X}",
                )
            )


def sentences(text: str) -> list[re.Match[str]]:
    return list(re.finditer(r"[^。！？!?\n]+[。！？!?]", text))


def paragraph_blocks(text: str) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    cursor = 0
    for block in re.split(r"\n\s*\n", text):
        position = text.find(block, cursor)
        cursor = max(position + len(block), cursor)
        clean = re.sub(r"[>*_`]", "", block).strip()
        if not clean or clean.startswith(("#", "http", "![", "```")):
            continue
        if re.match(r"^(?:[-+*]|\d+[.、])\s", clean):
            continue
        if content_unit_count(clean) >= 4:
            blocks.append((position, clean))
    return blocks


def add_term_findings(
    findings: list[Finding],
    text: str,
    terms: tuple[str, ...],
    category: str,
    message: str,
) -> None:
    for position, term in term_matches(text, terms):
        findings.append(Finding(category, line_number(text, position), f"{message}：{term}", excerpt(text[position : position + 80])))


def scan_text(text: str, scenario: str = "general", texture: bool = False) -> ScanResult:
    prose = mask_non_prose(text)
    total_han = han_count(prose)
    failures: list[Finding] = []
    warnings: list[Finding] = []
    metrics = compute_metrics(prose)

    add_term_findings(failures, prose, HARD_RESIDUE, "机器残留", "删除复制自聊天或搜索模型的框架")
    add_term_findings(failures, prose, HARD_STOPS, "套话", "改成直接陈述")

    pivots = pattern_matches(prose, PIVOT_PATTERNS)
    for index, match in enumerate(pivots):
        target = warnings if index == 0 else failures
        target.append(
            Finding(
                "翻案句",
                line_number(text, match.start()),
                "只有真实存在的误解到修正过程才保留，重复使用时改成正面判断",
                excerpt(match.group()),
            )
        )

    for position, term in term_matches(prose, CONTEXT_TERMS):
        warnings.append(
            Finding(
                "语境词",
                line_number(text, position),
                f"检查是否能换成具体动作，准确描述机制时可以保留：{term}",
                excerpt(prose[position : position + 80]),
            )
        )

    add_term_findings(
        warnings,
        prose,
        ROAD_SIGNS,
        "路标词",
        "检查是否能直接进入事实或判断，避免用教程式连接词推进每一段",
    )

    for position, term in term_matches(prose, UNSOURCED_AUTHORITY):
        warnings.append(
            Finding(
                "模糊归因",
                line_number(text, position),
                f"后面应有明确来源，否则删掉权威铺垫：{term}",
                excerpt(prose[position : position + 80]),
            )
        )

    for match in pattern_matches(prose, NOMINALIZATION_PATTERNS):
        warnings.append(
            Finding(
                "空转句式",
                line_number(text, match.start()),
                "把名词化或空转结构还原成直接动作",
                excerpt(match.group()),
            )
        )

    add_pattern_findings(
        warnings,
        text,
        prose,
        PLACEHOLDER_PATTERNS,
        "占位符",
        "补齐或删除占位内容，不要把内部草稿标记交付给读者",
    )
    add_pattern_findings(
        warnings,
        text,
        prose,
        REASONING_ARTIFACT_PATTERNS,
        "推理脚手架",
        "删除面向模型的过程说明，只保留面向读者的正文",
    )
    add_term_findings(
        warnings,
        prose,
        FALSE_AGENCY_TERMS,
        "拟人化归因",
        "给数据、市场或算法补上真实主体和证据，避免把结果写成主动意志",
    )
    add_term_findings(
        warnings,
        prose,
        HOOK_TERMS,
        "公式化钩子",
        "检查是否真的需要设问或悬念，不要用标准钩子替代具体事实",
    )
    add_unicode_findings(warnings, text, prose)

    if scenario == "social":
        for match in re.finditer(r"(?m)^\s{0,3}(?:#{1,6}\s|[-*+]\s|\d+[.)、]\s)", prose):
            warnings.append(
                Finding(
                    "格式痕迹",
                    line_number(text, match.start()),
                    "社交短帖中检查 Markdown 或列表是否服务于扫描，避免把提示词排版原样交付",
                    excerpt(match.group()),
                )
            )

    if metrics["token_count"] < 40 and metrics["content_units"]:
        warnings.append(
            Finding(
                "样本长度",
                1,
                "文本过短，统计信号和 AI 痕迹判断置信度有限，优先人工核对语境",
                f"内容单元 {metrics['content_units']}",
            )
        )

    if metrics["token_count"] >= 80:
        repeated_ratio = float(metrics["repeated_trigram_ratio"] or 0)
        type_token_ratio = float(metrics["type_token_ratio"] or 0)
        if repeated_ratio >= 0.08:
            warnings.append(
                Finding(
                    "重复度信号",
                    1,
                    f"三元组重复比例约 {repeated_ratio:.1%}，检查是否存在模板化句群或反复措辞",
                    "统计信号，不是作者身份结论",
                )
            )
        if type_token_ratio <= 0.40:
            warnings.append(
                Finding(
                    "词汇多样性信号",
                    1,
                    f"类型词占比约 {type_token_ratio:.1%}，检查是否过度重复同一批词",
                    "统计信号，不是作者身份结论",
                )
            )

    if not texture:
        for symbol in ("—", "–", "…"):
            for match in re.finditer(re.escape(symbol), prose):
                warnings.append(
                    Finding(
                        "标点痕迹",
                        line_number(text, match.start()),
                        f"检查是否为装饰性 AI 标点，必要时改用句号、逗号或普通停顿：{symbol}",
                        excerpt(prose[max(0, match.start() - 24) : match.start() + 48]),
                    )
                )

    if total_han >= 600:
        conjunction_hits = term_matches(prose, CONJUNCTIONS)
        density = len(conjunction_hits) * 1000 / total_han
        if density > 7:
            warnings.append(
                Finding(
                    "连词密度",
                    1,
                    f"每千字约 {density:.1f} 个连接词，检查是否可以让事实关系直接连接",
                    "删掉一半连接词后朗读比较",
                )
            )

    sentence_lengths = [content_unit_count(match.group()) for match in sentences(prose) if content_unit_count(match.group()) >= 4]
    if len(sentence_lengths) >= 12:
        mean = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((value - mean) ** 2 for value in sentence_lengths) / len(sentence_lengths)
        cv = math.sqrt(variance) / mean if mean else 0
        if cv < 0.42:
            warnings.append(
                Finding(
                    "句长节奏",
                    1,
                    f"{len(sentence_lengths)} 个句子长度过于接近，变异系数为 {cv:.2f}",
                    "让少数句子更短或更长，但不要机械切句",
                )
            )

    blocks = paragraph_blocks(prose)
    if len(blocks) >= 10:
        one_sentence = sum(len(re.findall(r"[。！？!?]", block)) <= 1 for _, block in blocks)
        ratio = one_sentence / len(blocks)
        if ratio >= 0.75:
            warnings.append(
                Finding(
                    "短段鼓点",
                    line_number(text, blocks[0][0]),
                    f"可识别段落中 {ratio:.0%} 只有一句，检查是否为了制造节奏而切碎",
                    blocks[0][1],
                )
            )

    opener_counts: collections.Counter[str] = collections.Counter()
    opener_positions: dict[str, int] = {}
    for position, block in blocks:
        value = block.lstrip("“‘\"（(")
        for opener in REPEATED_OPENERS:
            if value.startswith(opener):
                opener_counts[opener] += 1
                opener_positions.setdefault(opener, position)
                break
    for opener, count in opener_counts.items():
        if count >= 4:
            warnings.append(
                Finding(
                    "重复开头",
                    line_number(text, opener_positions[opener]),
                    f"段落反复以“{opener}”开头，共 {count} 次",
                    opener,
                )
            )

    return ScanResult(total_han, scenario, failures, warnings, metrics)


def load_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def print_report(result: ScanResult, as_json: bool) -> None:
    if as_json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return

    print(f"汉字数：{result.han_count}")
    print(f"内容单元：{result.metrics['content_units']}；句子：{result.metrics['sentence_count']}；段落：{result.metrics['paragraph_count']}")
    print(f"场景：{result.scenario}")
    print(f"必须修改：{len(result.failures)} 项；需要人工判断：{len(result.warnings)} 项")
    if result.failures:
        print("\n需要修改")
        for item in result.failures:
            print(f"- [{item.category}] 第 {item.line} 行，{item.message}。{item.excerpt}")
    if result.warnings:
        print("\n需要人工判断")
        for item in result.warnings:
            print(f"- [{item.category}] 第 {item.line} 行，{item.message}。{item.excerpt}")
    if not result.failures and not result.warnings:
        print("\n未发现检查器覆盖的高置信问题。仍需人工核对事实、读者和语气。")


def main() -> int:
    parser = argparse.ArgumentParser(description="检查中英文写作中的高置信 AI 残留和需要人工判断的表达风险")
    parser.add_argument("path", help="Markdown 或文本文件路径，使用 - 从标准输入读取")
    parser.add_argument("--scenario", choices=("general", "professional", "social", "script"), default="general")
    parser.add_argument("--texture", action="store_true", help="允许温暖质感模式，减少标点痕迹提醒")
    parser.add_argument("--json", action="store_true", help="输出 JSON 报告")
    args = parser.parse_args()

    try:
        text = load_text(args.path)
    except (OSError, UnicodeError) as error:
        print(f"无法读取稿件：{error}", file=sys.stderr)
        return 2

    if content_unit_count(mask_non_prose(text)) == 0:
        print("没有检测到可分析正文。", file=sys.stderr)
        return 2

    result = scan_text(text, args.scenario, args.texture)
    print_report(result, args.json)
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
