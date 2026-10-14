# Creation Handoff

## Result

- skill / version / owner: lvsea-writing / 0.6.0 / 海洋哥 / lhylvsea
- one-line job: 以 `lvsea-writing` 为唯一入口，按需路由小红书素材专家和终稿后处理专家，串起资料、结构、读者、声音、场景、完整初稿后复查、最后去 AI 味和人工终审。
- local path: outputs/lvsea-writing
- publication status: PR #8 merged into `main`; public release [v0.6.0](https://github.com/lhylvsea/lvsea-writing/releases/tag/v0.6.0) published at commit `7184be8d667b47c043c664034e4484c1b611ab53`

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
- `seyedehsanhadi/sloptrim` v0.9.4 at `38dbb7cb4e97de0b9bf157903c95bdcab016dda2`: complete-draft-first review, pattern-family triage, confidence labels and critical-content preservation; adapted semantically, without copying its code or hooks.
- `docwriter-org/plain-writing-skill` at `f0d3630983ac7a82aa580f1c1509d72df739ee12`: plain words, explicit subjects and actions, conclusion-first explanation, `deslopify` and optional revision view; adapted as a mode, without copying its Skill, evals or result claims.

## Absorbed and rejected

- keep: evidence before prose; thesis before polish; reader test; scene-aware voice; technical checks; final Humanizer; author gate.
- adapt: external multi-skill roles become one routed entry; private voice files become user-controlled local profiles; English pattern lists become Chinese-first context review.
- reject: forced all-in-one prompt, external runtime dependencies, detector-evasion promises, absolute anti-style rules, private sample publication.
- invent: pipeline stage contracts, late-Humanizer invariant, final-gate feedback classes, single-entry specialist routing, sequencing trigger regression, the Chinese-first `review_score` triage layer and the optional `plain/deslopify` revision-view contract.

## Advantages and evidence

- [design advantage] weak material is exposed before prose polish instead of being hidden by fluent rewriting.
- [design advantage] the same entry supports short edits and deep projects without loading every reference.
- [design advantage] author voice and scene format are separated, reducing generic “natural tone” drift.
- [validated advantage] package-level trigger cases cover positive, negative, near-neighbor and adversarial prompts.
- [hypothesis] the late-Humanizer ordering will improve factual and stylistic stability; provider-backed or human-blind evidence is still missing.

## Verification and limits

- package: validate_package.py PASS; manifest/interface/root entrypoint and local links checked.
- trigger: 25/25 v0.6.0 cases pass across should-trigger, should-not-trigger, near-neighbor and adversarial buckets, including plain/deslopify positives and plain-writing explanation-only negatives.
- runtime: the standard-library checker remains the only deterministic text checker; it now returns bounded `review_score`, `review_band` and `review_confidence` fields.
- install: v0.6.0 synchronized to `C:\Users\rabbit\.codex\skills\lvsea-writing` and `C:\Users\rabbit\.agents\skills\lvsea-writing`; both `Test-SkillInstall.ps1` gates passed, with no source-file SHA-256 mismatches. The previous local trees were backed up before synchronization.
- provider/human output: missing evidence; no provider A/B or blind human study is claimed here.
- deliberately excluded: remote inline execution, detector APIs, model weights, private voice corpus and automatic external publication beyond the requested repository.
