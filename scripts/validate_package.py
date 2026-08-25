#!/usr/bin/env python3
"""Validate the lvsea-writing package without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "USAGE.zh-CN.md",
    "VERSION",
    "manifest.json",
    "agents/interface.yaml",
    "evals/trigger_cases.json",
    "reports/skill-ir.json",
    "reports/trigger-eval.json",
    "reports/prior-art-research.md",
    "reports/creation-handoff.md",
)


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected an object")
    return value


def local_links(text: str) -> list[str]:
    links = re.findall(r"\]\(([^)]+)\)", text)
    return [
        link.split("#", 1)[0].strip()
        for link in links
        if link.endswith(".md") and not link.startswith(("http://", "https://"))
    ]


def validate(root: Path) -> dict:
    root = root.resolve()
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            failures.append(f"missing file: {relative}")

    skill_path = root / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8") if skill_path.is_file() else ""
    if not re.search(r"(?m)^name:\s*lvsea-writing\s*$", skill_text):
        failures.append("SKILL.md frontmatter name is not lvsea-writing")
    if not re.search(r"(?m)^description:\s*.+$", skill_text):
        failures.append("SKILL.md has no single-line description")
    if len([p for p in root.rglob("SKILL.md") if ".git" not in p.parts]) != 1:
        failures.append("package must have exactly one discoverable SKILL.md")

    for link in local_links(skill_text):
        if not (root / link).exists():
            failures.append(f"SKILL.md links to missing file: {link}")

    try:
        manifest = load_json(root / "manifest.json")
        if manifest.get("name") != "lvsea-writing":
            failures.append("manifest name does not match lvsea-writing")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
            failures.append("manifest version is not semantic")
        if manifest.get("maturity_tier") == "governed":
            for field in ("review_due", "review_cadence", "release_gates"):
                if not manifest.get(field):
                    failures.append(f"manifest missing governed field: {field}")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        failures.append(f"manifest.json invalid: {exc}")

    try:
        trigger = load_json(root / "reports/trigger-eval.json")
        summary = trigger.get("summary", {})
        if trigger.get("ok") is not True or summary.get("passed") != summary.get("total"):
            failures.append("trigger-eval report is not fully passing")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        failures.append(f"trigger-eval report invalid: {exc}")

    if "Humanizer" not in skill_text or "人工终审" not in skill_text:
        failures.append("SKILL.md is missing the late Humanizer or author gate invariant")
    if "最后一步" not in skill_text:
        warnings.append("SKILL.md does not state the final-step wording")
    if "missing evidence" not in skill_text:
        warnings.append("SKILL.md does not label missing provider/human evidence")

    return {
        "ok": not failures,
        "root": str(root),
        "failures": failures,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the lvsea-writing package.")
    parser.add_argument("skill_dir", nargs="?", default=".")
    args = parser.parse_args()
    result = validate(Path(args.skill_dir))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["ok"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
