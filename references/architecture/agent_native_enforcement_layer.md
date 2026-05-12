# Agent-Native Enforcement Layer

## Purpose

AutoAlbum is a skill, but it should behave like a disciplined production pipeline. The enforcement layer gives the agent lightweight programmatic guardrails without turning the skill into a rigid standalone application.

The enforcement layer exists to improve output quality by preventing common agent failures:

- skipping required phases;
- forgetting state/manifest updates;
- advancing before artifacts exist;
- losing track of track-level versions;
- overwriting good work with worse revisions;
- claiming completion that does not match the user's requested output goal;
- treating quality gates as optional prose rather than workflow requirements.

## Design decision

Use a lightweight helper script and machine-readable controller files, not a full autonomous app.

### Why not a full orchestrator?

A full orchestrator would need API keys, provider-specific MiniMax execution code, audio handling, retry strategy, storage policy, and potentially custom UI. That is valuable later, but it is not necessary for a Hermes skill to enforce high-quality agent behavior.

### Why a helper script?

Hermes skills can include `scripts/` and reference them from `SKILL.md` using `${HERMES_SKILL_DIR}`. This lets the skill provide concrete operational checks while remaining agent-native. Hermes documentation describes skills as instruction bundles that may include scripts and references, and it exposes the skill directory for script invocation. This makes a helper-script controller appropriate for AutoAlbum.

## Enforcement components

```text
scripts/autoalbum_guard.py
references/controller/phase_order.json
references/controller/gate_requirements.json
references/architecture/controller_command_protocol.md
references/architecture/agent_native_enforcement_layer.md
```

## What the helper enforces

The helper enforces structural reliability:

```text
project initialization
canonical phase IDs
artifact existence by phase
JSON/JSONL syntax sanity
state phase advancement
project_manifest refresh
results.tsv event rows
transaction snapshots
rollback to a prior snapshot
current status reporting
```

It does **not** make creative decisions. It does not decide whether a hook is good, whether a style is authentic, or whether a rendered audio candidate is release-worthy. Those decisions remain with the stage rubrics, evaluator prompts, listener panel, and final A&R review.

## Mandatory usage policy

For high-rigor, release-grade, album, EP, concept-album, style-strict, and autonomous-full-pipeline projects, the agent must use the helper script for:

1. project initialization;
2. validation after creating or editing control files;
3. gate checks before advancing material phases;
4. snapshots before risky revisions;
5. manifest refresh after material artifact changes;
6. status checks before claiming completion.

For quick single-track packet-only work, helper usage is still recommended but can be limited to initialization, packet-stage gate check, and final status.

## Human-readable plus machine-readable

Every major stage should still create human-readable review notes where musically useful. The controller exists to enforce structure; it does not replace the musical analysis references.

## Expected effect on output quality

The helper improves quality indirectly by preserving the integrity of the process:

- good ideas are less likely to be lost;
- failed stages are harder to skip;
- revisions are less likely to create unnoticed regressions;
- MiniMax packets are less likely to be approved without required supporting artifacts;
- final albums are less likely to be incomplete or disjointed.


## Schema validation

The guard validates known JSON artifacts against schemas when the `jsonschema` package is available. Syntax-only validation is not enough for release-grade projects; required root artifacts and canonical track artifacts should match their schemas before phase advancement.


## Applicability routing

`phase_applicability.json` prevents false failures by marking phases that do not apply to a project scope or output goal. The route command should be consulted before gating optional or conditional phases.


## Skip semantics

A skipped phase is not a failed phase. The agent must not fabricate artifacts solely to satisfy a skipped phase. The controller treats skipped phases as pass-through for `status`, `gate`, `advance --require-gate`, and `route`. If a skipped phase becomes relevant because the user changes scope or output goal, update `project_config.json`, run `validate`, then rerun `route`.


## Applicability precedence

Controller applicability is resolved in this order: project scope baseline → quality-mode escalation → output-goal override. Output goal is applied last so packet-only, review-only, or candidate-only projects do not accidentally require release-stage artifacts just because the quality mode is strict.


## Sequential advancement rule

`advance` is sequential by default. The controller refuses non-sequential jumps unless `--allow-jump` is used. Use `--allow-jump` only for documented recovery, replanning, or scope changes; write the reason to `results.tsv` and refresh state/manifest afterward.
