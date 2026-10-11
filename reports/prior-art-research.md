# Prior-art research

## Scope

- Date: 2026-08-25
- Target: upgrade lvsea-writing into a single-entry writing pipeline
- User-provided primary reference: https://x.com/zhouluobo/status/2091846529321664695
- Discovery path: local find-skills instructions -> skills.sh leaderboard/search -> read-only GitHub source review
- Method reference: local lvsea-zao-skill 0.1.1, using Intent -> Research -> Synthesis -> Package -> Eval -> Review -> Release

## 2026-10-11 incremental review: sloptrim

The requested source was reviewed read-only at [seyedehsanhadi/sloptrim](https://github.com/seyedehsanhadi/sloptrim), tag `v0.9.4`, commit `38dbb7cb4e97de0b9bf157903c95bdcab016dda2`, under Apache-2.0. The source describes a local, deterministic prose-pattern linter with pattern-family scoring, confidence notes, code/format protection, critical-content preservation and a two-loop rewrite cap. Its ethics boundary explicitly rejects authorship claims and detector-evasion use.

| Decision | Result |
| --- | --- |
| `keep` | complete-draft-first ordering, pattern-family triage, bounded score bands, short-text confidence warning, preservation of numbers/names/attribution/hedges/placeholders, character-layer review and anti-sterility recheck |
| `adapt` | use the existing Chinese-first `check_writing.py`; expose `review_score`, `review_band`, `review_confidence` and scored categories; use the signal only to choose editorial depth |
| `reject` | Claude-specific hooks and commands, automatic file rewriting, English vocabulary thresholds as Chinese rules, rich-document rebuild, external detector calls and silent-output requirements that hide a requested report |
| `invent` | a single-entry route that places local review between complete drafting and the final Humanizer, with a separate author gate and explicit format boundary |

The upstream detector was not executed as a dependency and its code was not copied. The local score is intentionally not comparable to `sloptrim`'s `ai_tell_score`; both remain review heuristics rather than authorship evidence.

## Article findings

The referenced article divides writing into research, structure, reader collaboration,
voice/profile, scene-specific writing, technical validation and final Humanizer
review. Its central sequencing decision adopted here is:

~~~text
research/material -> structure -> reader/context -> voice -> domain/format
-> draft/edit -> Humanizer final pass -> author final gate
~~~

The article is used as a design reference, not copied as a prompt or text corpus.
The X page was access-limited in the current environment; the linked article was
read through a read-only mirror API and checked against its metadata. This is
source-retrieval evidence, not independent evidence that the article's workflow
improves every writing task.

## Incremental specialist routing decision

On 2026-09-16, the local reviewed source of [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) was checked at commit `27d29232f10124db904ca9c0536d0b67cb3b2833`. Its design is intentionally narrower than `lvsea-writing`: it accepts a complete draft, applies only explicit whitelist rules, preserves structure and information, and leaves semantic style judgments to the author. The repository reports a 629-article comparison corpus and 11 retained signals, but also documents model variation, denominator errors and rejected features; those numbers are not imported as universal thresholds.

The current [lvsea-xiezuo](https://github.com/lhylvsea/lvsea-xiezuo) package is a platform-specific material radar with a source-backed handoff. It is useful before prose, but it should not become a second general writing entry or own the final Humanizer stage.

| Decision | Result |
| --- | --- |
| `keep` | one user-facing `$lvsea-writing` entry; xiezuo for Xiaohongshu evidence; lieflat for complete-draft final editing |
| `adapt` | explicit route table, specialist availability fallback, handoff fields and route regression cases |
| `reject` | a fourth mega-Skill that pastes all three prompts, automatic loading of every specialist, and broad anti-AI rules before structure exists |
| `invent` | `references/specialist-routing.md` and `references/late-humanizer-adapter.md` as the stable orchestration contract |

## Discovery signals

| Candidate | Discovery signal | Source review | Decision |
| --- | --- | --- | --- |
| composiohq/awesome-claude-skills content-research-writer | 6.9K installs on skills.sh | candidate directory and related source pattern | adapt research/outline/feedback mechanism; do not install |
| mblode/agent-skills docs-writing | 770 installs on skills.sh | read source at revision in source matrix | adapt technical documentation gates |
| mblode/ghostwriter | 5 installs on skills.sh | read source and README at revision in source matrix | adapt core/scene profiles and blind evaluation boundary |
| CommandCodeAI/agent-skills content-research-writer | 25 installs on skills.sh | read source at revision in source matrix | adapt evidence and section feedback |
| local lvsea-research | installed local skill | read routing and evidence contract | adapt research/source ledger |
| local lvsea-zao-skill | installed local skill | read package and release method | adapt governed package/eval/release structure |

Install counts are discovery metadata and may drift. They were not combined into
a quality score, and no unreviewed remote code was executed.

## Keep / adapt / reject / invent ledger

### Keep

- Research and evidence precede drafting when the topic is unfamiliar, changing or contested.
- A thesis/outline is an intermediate contract instead of a decorative outline.
- Reader testing catches hidden assumptions that a fluent model may miss.
- Voice is evidence from samples, not a generic “warm” switch.
- Technical writing has runnable/link/parameter gates.
- Humanizer is a late-stage, minimal-diff editor.

### Adapt

- Convert external multi-skill routing into one lvsea-writing entry with optional stage reads.
- Convert private profile files into a local, user-controlled core voice and scene voice model.
- Convert English-heavy AI pattern lists into Chinese-first, context-sensitive review.
- Convert blind evaluation into a manual author gate unless real held-out human review exists.
- Use the existing standard-library checker as a signal layer, not a detector truth layer.

### Reject

- Forced installation of every upstream Skill.
- External CLIs, model weights, detector services, telemetry or private profile content in
  the public package.
- Absolute rules such as deleting every passive voice, adverb, dash, four-character phrase
  or imperfect sentence.
- Any promise to bypass an AI detector or to prove authorship from a score.

### Invent

- The explicit late-Humanizer ordering and stage contracts in references/pipeline.md.
- The author final gate and feedback classification in references/human-final-gate.md.
- A single Chinese-first route that covers manufacturing, policy, industry writing,
  technical docs, copy, slides and narration without forcing one style.
- Trigger cases that test both “last step” sequencing and false positives for explanation-only
  or one-off copy requests.

## Evidence boundary

Static source review, trigger fixtures, package checks and local script results can prove
that the package is structured and its stated routing is regression-tested. They cannot
prove that every model will follow the sequence, that a provider will produce a strong
article, or that a human author will approve the final voice. Those claims remain
missing evidence until provider-backed or human-blind output evidence is collected.
