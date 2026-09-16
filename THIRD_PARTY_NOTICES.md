# Third-party notices

`lvsea-writing` is an independent synthesis of writing principles found while
reviewing the projects below. It does not copy their complete Skill files,
examples, checker implementations, data, or model weights.

## Existing baseline

### KKKKhazix/human-writing

- Repository: https://github.com/KKKKhazix/human-writing
- Reviewed revision: `4fda173f3fef7fb808f3eba991eeb2528ea4b189`
- License: MIT
- Adapted ideas: material sufficiency, reality/fiction boundaries, source-aware
  writing, paragraph progression, semantic anti-pivot checks, and staged revision.

### weijt606/anti-vibe-writing

- Repository: https://github.com/weijt606/anti-vibe-writing
- Reviewed revision: `3126f86cce5c36904b8d6350edd994e97796ecd3`
- License: MIT
- Adapted ideas: scenario-aware finishing, Chinese translationese checks,
  copy-paste residue cleanup, opt-in texture, sample-based voice calibration,
  and final verification passes.

## Additional reviewed projects

### blader/humanizer

- Repository: https://github.com/blader/humanizer
- Reviewed revision: `523374dee72d67c7b2b5f858ea0094ffda49c3ac`
- License: MIT
- Adapted ideas: pattern-based review, information over mechanical shape,
  no-fabrication boundaries, sample-based voice calibration, and a second final audit.

### Aboudjem/humanizer-skill

- Repository: https://github.com/Aboudjem/humanizer-skill
- Reviewed revision: `9a7f35b7b9ad8c3abd71f10757ec9f91fb8ae165`
- License: MIT
- Adapted ideas: confidence tiers, detect/rewrite/edit routing, voice modes,
  placeholders, citation leakage, style shifts, and iteration checks.

### brandonwise/humanizer

- Repository: https://github.com/brandonwise/humanizer
- Reviewed revision: `4b9b9bee384aea139f599133d2de1e1ceaee71a3`
- License: MIT
- Adapted ideas: burstiness, vocabulary repetition, batch review and baseline
  comparison as auxiliary signals only.

### hardikpandya/stop-slop

- Repository: https://github.com/hardikpandya/stop-slop
- Reviewed revision: `8da1f030185bdfe8471220585162991eaeb970e9`
- License: MIT
- Adapted ideas: concrete subjects and verbs, specificity, reader-in-the-room
  checks, rhythm variation and cutting empty quotables.

### op7418/Humanizer-zh

- Repository: https://github.com/op7418/Humanizer-zh
- Reviewed revision: `91f3d394db8419c20d67ebe22a96cf8fee0a404b`
- License: MIT
- Adapted ideas: Chinese-native pattern review, four-character slogan stacks,
  standard openers, rhetorical Q&A, chatbot residue and positive-ending checks.

### alchaincyf/nuwa-skill

- Repository: https://github.com/alchaincyf/nuwa-skill
- Reviewed revision: `27642f5bfed2dc1bbf8ee59a2c1ee602a626bbd7`
- License: MIT
- Adapted ideas: source hierarchy, evidence labels, cross-source validation,
  expression DNA, anti-patterns and explicit limits.

### leonxlnx/taste-skill

- Repository: https://github.com/leonxlnx/taste-skill
- Reviewed revision: `e988add20dab0fa97d7a76781c48961c8184288e`
- License: MIT
- Adapted ideas: read the brief, audience and quiet constraints first; resist
  default templates. Frontend, CSS, animation and visual dial instructions are
  not included.

### dongbeixiaohuo/writing-agent

- Repository: https://github.com/dongbeixiaohuo/writing-agent
- Reviewed revision: `cd411cfbc44f03dc0513b2f5ec3804f13896f5eb`
- License: MIT
- Adapted ideas: staged long-form workflow, evidence ledger, style modeling,
  fact gate, reader tests and version notes. Claude-specific subagent wiring is
  not included.

### Hello-SimpleAI/chatgpt-comparison-detection

- Repository: https://github.com/Hello-SimpleAI/chatgpt-comparison-detection
- Reviewed revision: `1f8c15c28f87e09a5abfd86ee6e15005dc7d2119`
- License: research/data repository with mixed upstream data licenses
- Adapted ideas: bilingual detector taxonomy and the boundary between a
  statistical signal and an authorship claim. No HC3 data, model weights,
  training code or external detector service is included.

### CommandCodeAI/agent-skills

- Repository: https://github.com/CommandCodeAI/agent-skills
- Reviewed revision: `f490dd9016f2729311e90f317dcb6c98be1a1500`
- License: MIT
- Adapted ideas: research -> outline -> section feedback, citation tracking and
  voice preservation. The external repository and its generated examples are
  not copied.

### mblode/ghostwriter

- Repository: https://github.com/mblode/ghostwriter
- Reviewed revision: `046f1f05906d911277745f1d665cd07203005038`
- License: MIT
- Adapted ideas: a cross-context core voice plus scene-specific voice files,
  separated training/evaluation, and blind-comparison thinking. Private profile
  contents and the external CLI are not included.

### mblode/agent-skills

- Repository: https://github.com/mblode/agent-skills
- Reviewed revision: `e97a3b383f5944f90d41eb92b24b4fb3b917a7f9`
- License: MIT
- Adapted ideas: explicit IS/IS NOT boundaries, brief-first product copy, and
  runnable/link/parameter gates for technical documentation. Unrelated frontend
  and platform-specific routing is not included.

### zhouluobo X article

- Source: https://x.com/zhouluobo/status/2091846529321664695
- Reviewed: 2026-08-25; the X page itself was access-limited, so the article
  content was read through a read-only mirror API and checked against the
  linked article metadata.
- Adapted ideas: role separation, research and structure before style, Humanizer
  as the last editing stage, and author/human judgment as the final gate.
- Boundary: no article text, screenshots, private configuration or original
  prompt bundle is copied into this repository.

### larashero3-dotcom/lieflat-less-ai-tone

- Repository: https://github.com/larashero3-dotcom/lieflat-less-ai-tone
- Reviewed revision: `27d29232f10124db904ca9c0536d0b67cb3b2833`
- License: MIT
- Adapted ideas: whitelist-only late editing, information conservation,
  structure preservation, explicit non-rules and sample auditing before trusting
  a pattern.
- Boundary: the repository remains the authoritative specialist; this package
  does not copy its complete SKILL.md, corpus, scripts or model-specific
  statistics. The specialist is invoked only after a complete draft.

### lhylvsea/lvsea-xiezuo companion Skill

- Repository: https://github.com/lhylvsea/lvsea-xiezuo
- Role: optional local companion for Xiaohongshu material evidence and
  source-backed writing handoff.
- Boundary: it is not a third-party dependency or a second general writing
  entry. `$lvsea-writing` remains the primary user-facing route.

## Adaptation boundary

The rules in this repository are newly organized and rewritten for a
Chinese-first, fact-sensitive workflow that includes manufacturing management,
safety and party-government materials, industry explanation, PPT copy, and
video narration. Upstream examples and private user samples are not included.
