# Delegated: Full Skill Quality Check

## Task

Run a full AutoAlbum project QA before declaring a track, EP, album, packet set, or release package generation-ready or release-ready.

## Read
- `references/agent_training/final_album_judging_rubric.md`
- `references/agent_training/agent_anti_shortcut_checklists.md`
- `references/architecture/phase_gate_matrix.md`

- SKILL.md
- references/quality/pruning_and_organization_audit.md
- references/quality/user_story_validation.md
- references/quality/fragility_register.md
- intent_intake.json
- project_config.json
- references/quality/style_catalog_qa_checklist.md
- references/api/minimax_prompting_and_style_control_playbook.md
- references/craft/professional_songcraft_and_arrangement_controls.md
- all project artifacts

## Output

Write `reviews/full_skill_quality_check.md`.

## Required sections

```text
1. User story fit
2. Artifact completeness
2. Style catalog resolution quality
3. Album foundation quality
4. Tracklist and sequencing quality
5. Songcraft quality
6. MiniMax packet quality
7. API parameter coverage
8. Variant strategy quality
9. Post-generation review quality
10. Release package quality
11. Missing or weak artifacts
13. Required fixes before proceeding
```

## Pass/fail standard

The album fails if any track lacks:

```text
style card
lyrics
prompt
generation packet
MiniMax eval
variant strategy
render review or approved pending-generation status
```

The album fails if the sequence lacks:

```text
first-three-track promise
energy map
transition map
closer rationale
weakest-track justification
```


## Scope-aware rule
Do not fail a single-track project for missing album-only artifacts. Do fail a full-album project if it lacks sequence, contrast, style-map, or final A&R artifacts appropriate to its output goal.


## Organization checks
- Confirm all active artifacts live under one `<project_slug>/` root.
- Confirm `project_manifest.json` indexes current artifacts.
- Confirm `state.json` validates and has clear next actions.
- Confirm render paths use `raw/`, `selected/`, and `rejected/`.
- Confirm release package includes audio or explicitly declares packet-only status.

## Completion additions
A project cannot be marked complete unless the quality check confirms:

```text
all vocal tracks have prosody_review.json
all generation packets have prompt_budget_report.json
provider profile is recorded for every packet
post-render reviews include timestamped listening notes when audio exists
release goals have final_audio_qc.json
non-rap style requests used non_rap_expansion references where applicable
```
