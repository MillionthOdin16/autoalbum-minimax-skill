# Progressive Disclosure Operating Model

## Purpose

This skill is large because it contains musical training, MiniMax API guidance, style catalogs, schemas, and quality gates. Progressive disclosure keeps execution reliable by loading only the information needed at the current decision point.

## Disclosure tiers

### Tier 0 — Activation context

Read at skill start:

- `SKILL.md`
- `references/active/CURRENT.md`
- `references/architecture/active_reference_index.md`
- `references/architecture/stage_reference_map.md`
- `references/architecture/phase_gate_matrix.md`

Goal: understand the project workflow without loading detailed training, catalogs, or provider docs prematurely.

### Tier 1 — Project operating context

Read after intent intake starts:

- `references/architecture/project_root_organization.md`
- `references/architecture/artifact_path_standard.md`
- `references/architecture/state_and_provenance.md`
- `references/architecture/project_scope_modes.md`
- `references/architecture/user_story_operating_flows.md`
- `references/delegated/28_user_intent_intake.md`
- `references/delegated/00_project_config.md`

Goal: create the project root, config, state, manifest, and scope-specific plan.

### Tier 2 — Phase-specific execution

For each phase, read only the delegated stage file plus the small set of phase references named in `stage_reference_map.md`.

Examples:

- Lyric drafting reads lyric/songcraft references, not cover-workflow docs.
- MiniMax packet compilation reads provider profile and prompt-control references, not the full style catalog.
- Final audio QC reads mastering/sequencing references, not seed-generation docs.

### Tier 3 — Conditional style/provider specialization

Open these only when triggered:

- Rap catalog: rap style, rap artist, rap song, current rap taste.
- Non-rap expansion: pop/R&B/electronic/Latin/rock/country/etc.
- Cover workflow: source audio, re-render, alternate version, or cover mode.
- Currentness refresh: user asks for current chart taste or contemporary artist style.
- Provider profile: selected provider route requires route-specific payload behavior.

### Tier 4 — Quality escalation

Open these when a stage is high-rigor/release-grade, borderline, failed, or user specifically requests maximum quality:

- `references/delegated/36_musical_knowledge_bootstrap_check.md`
- `references/delegated/40_quality_counterexample_review.md`
- `references/delegated/32_critical_musical_stage_review.md`
- `references/quality/style_catalog_qa_checklist.md`
- `references/quality/pruning_and_organization_audit.md`
- `references/critics/critical_musical_analyst_protocol.md`

## Anti-patterns

Do not:

- Read the whole style catalog before knowing the requested style.
- Read every agent-training file for every simple stage.
- Treat historical versioned audits as active instructions.
- Let checklists replace actual artifacts and decisions.
- Advance a phase without updating state, manifest, and results.
- Use a broad genre label when a concrete style lane is needed.

## Required output discipline

Each phase should produce:

1. Required artifact(s).
2. Required machine-readable JSON where a schema exists.
3. Required human-readable markdown where judgment matters.
4. State update.
5. Manifest update.
6. Results row.
7. Explicit blockers or next action.
