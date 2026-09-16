# Creation Handoff

## Result

- skill / version / owner: lvsea-writing / 0.4.0 / 海洋哥 / lhylvsea
- one-line job: 以 `lvsea-writing` 为唯一入口，按需路由小红书素材专家和终稿后处理专家，串起资料、结构、读者、声音、场景、初稿、最后去 AI 味和人工终审。
- local path: outputs/lvsea-writing
- publication status: published to main through PR #1; GitHub release v0.3.0

## Reference skills studied

- X article by zhouluobo: role separation, last-stage Humanizer, optional composition.
- CommandCodeAI content-research-writer: research, outline, citation and section feedback.
- mblode ghostwriter: core/scene voice profile and blind evaluation boundary.
- mblode agent-skills copywriting/docs-writing: brief-first scope, IS/IS NOT, technical gates.
- local find-skills: leaderboard/search discovery and source verification boundary.
- local lvsea-research: source plan, evidence ledger, fact/inference/assumption distinction.
- local lvsea-zao-skill: governed lifecycle, progressive disclosure, evals and evidence-bound release.
- `larashero3-dotcom/lieflat-less-ai-tone`: late-stage whitelist editing and information conservation; reviewed as a downstream specialist rather than copied wholesale.
- `lhylvsea/lvsea-xiezuo`: Xiaohongshu material radar and source-backed handoff; treated as an optional upstream specialist, not a second writing entry.

## Absorbed and rejected

- keep: evidence before prose; thesis before polish; reader test; scene-aware voice; technical checks; final Humanizer; author gate.
- adapt: external multi-skill roles become one routed entry; private voice files become user-controlled local profiles; English pattern lists become Chinese-first context review.
- reject: forced all-in-one prompt, external runtime dependencies, detector-evasion promises, absolute anti-style rules, private sample publication.
- invent: pipeline stage contracts, late-Humanizer invariant, final-gate feedback classes, single-entry specialist routing and sequencing trigger regression.

## Advantages and evidence

- [design advantage] weak material is exposed before prose polish instead of being hidden by fluent rewriting.
- [design advantage] the same entry supports short edits and deep projects without loading every reference.
- [design advantage] author voice and scene format are separated, reducing generic “natural tone” drift.
- [validated advantage] package-level trigger cases cover positive, negative, near-neighbor and adversarial prompts.
- [hypothesis] the late-Humanizer ordering will improve factual and stylistic stability; provider-backed or human-blind evidence is still missing.

## Verification and limits

- package: validate_package.py PASS; manifest/interface/root entrypoint and local links checked.
- trigger: 16/16 cases pass across should-trigger, should-not-trigger, near-neighbor and adversarial buckets.
- runtime: the standard-library checker remains the only deterministic text checker.
- install: Test-SkillInstall PASS; direct local discovery and validation command both passed.
- provider/human output: missing evidence; no provider A/B or blind human study is claimed here.
- deliberately excluded: remote inline execution, detector APIs, model weights, private voice corpus and automatic external publication beyond the requested repository.
