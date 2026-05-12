# Current Active Skill Map

Active build: **v24 verification hardened**.

Read this after `SKILL.md`. It gives the minimum active navigation set and prevents loading historical or unrelated references.

## Start set

1. `references/architecture/stage_reference_map.md`
2. `references/architecture/phase_gate_matrix.md`
3. `references/architecture/gate_applicability_matrix.md`
4. `references/architecture/agent_native_enforcement_layer.md`
5. `references/architecture/controller_command_protocol.md`

## Controller files

```text
scripts/autoalbum_guard.py
references/controller/phase_order.json
references/controller/gate_requirements.json
references/controller/phase_applicability.json
```

## Principle

Use the smallest adequate reference set for the current phase. Use `autoalbum_guard.py route <project_slug>` before gating optional or conditional phases; do not manufacture artifacts for phases marked `skip`. Escalate only when scope, quality mode, style request, MiniMax provider, gate failure, or musical failure requires deeper references.

## Historical material

Historical audit and superseded version files have been removed from the active package. Design rationale is preserved in `CHANGELOG.md` and `references/quality/pruning_and_organization_audit.md`.


## Verification hardening commands

Use these when a phase claims readiness or completion:

```text
hash-artifacts, verify-freshness, verify-quotes, verify-style, verify-tournaments,
lint-prompt, verify-variants, export-payloads, verify-payloads, verify-state, reconcile-state, preflight
```

These commands exist to prevent the common failure mode where a project has all required files but the files are stale, invalid, ungrounded, or not actually renderable.
