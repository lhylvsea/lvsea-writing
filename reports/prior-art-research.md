# Prior-art research

## Scope

- Date: 2026-08-25
- Target: upgrade lvsea-writing into a single-entry writing pipeline
- User-provided primary reference: https://x.com/zhouluobo/status/2091846529321664695
- Discovery path: local find-skills instructions -> skills.sh leaderboard/search -> read-only GitHub source review
- Method reference: local lvsea-zao-skill 0.1.1, using Intent -> Research -> Synthesis -> Package -> Eval -> Review -> Release

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
