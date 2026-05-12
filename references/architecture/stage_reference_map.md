# Stage Reference Map

This map preserves the canonical stage order and adds controller enforcement. Use progressive disclosure: read only the minimum references for the current stage, plus conditional references triggered by style, provider, scope, or failure.

## Universal controller step

For every material stage:

1. Check status:
   ```bash
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py status <project_slug>
   ```
2. If unsure which phases apply, run `autoalbum_guard.py route <project_slug>` and follow the reported applicability. Do not gate skipped phases unless explicitly debugging with `--force`.
3. Read the stage-specific delegated file.
4. Create or update required artifacts.
5. Refresh manifest:
   ```bash
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py manifest <project_slug>
   ```
6. Validate JSON/JSONL syntax, known schemas, hashes, quote grounding, prompt linting, style catalog use, and variant renderability when applicable:
   ```bash
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py validate <project_slug>
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-freshness <project_slug>
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-quotes <project_slug>
   ```
7. Run the phase gate when the stage is required or conditional and active for the project:
   ```bash
   python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py gate <project_slug> --phase <phase_id> --write-report
   ```
8. Only advance after required quality rubrics and controller gate pass.

## Phase map

| Phase ID | Stage | Minimum references | Required controller action |
|---|---|---|---|
| `intake` | Intent/project setup | `references/delegated/28_user_intent_intake.md`, `references/delegated/00_project_config.md`, `references/architecture/project_root_organization.md` | `init`, then `validate`, `gate --phase intake` |
| `concept_option_search` | Concept tournament | `references/delegated/48_album_seed_and_concept_tournament.md`, `references/architecture/option_search_and_tournament_protocol.md` | `snapshot` before replacing seed; `gate --phase concept_option_search` |
| `style_resolution` | Style catalog resolution | `references/delegated/16_select_style_from_catalog.md`, `references/style_catalog/README.md`, conditional style files | `gate --phase style_resolution` |
| `style_voice_trials` | Style/voice trials | `references/delegated/49_style_voice_fingerprint_trials.md` | `snapshot` before locking style voice; `gate --phase style_voice_trials` |
| `foundation` | Album foundation | `references/delegated/01_foundation.md`, `references/agent_training/musical_expertise_bootcamp.md` | `gate --phase foundation` |
| `canon_setup` | Album canon/debts | `references/delegated/41_build_album_canon.md`, `references/architecture/propagation_and_debt_rules.md` | `gate --phase canon_setup` |
| `planning_style_cards` | Tracklist/style cards | `references/delegated/02_tracklist_and_arc.md`, `references/delegated/23_build_track_style_card.md` | `gate --phase planning_style_cards` |
| `motif_plant_payoff` | Motif ledger | `references/delegated/51_motif_plant_payoff_ledger.md` | `gate --phase motif_plant_payoff` when applicable |
| `hook_title_tournament` | Hook/title tournament | `references/delegated/50_hook_title_tournament.md`, `references/agent_training/hook_chorus_lab.md` | `gate --phase hook_title_tournament` when applicable |
| `arrangement_energy_design` | Form/energy design | `references/delegated/38_arrangement_energy_form_review.md`, `references/agent_training/arrangement_form_energy_manual.md` | `gate --phase arrangement_energy_design` |
| `lyrics_songcraft` | Lyrics/songcraft | `references/delegated/03_write_song_lyrics.md`, `references/agent_training/songwriting_lyric_field_guide.md` | `snapshot` before major lyric rewrites; `gate --phase lyrics_songcraft` |
| `prosody_topline` | Prosody/topline | `references/delegated/33_prosody_scansion_topline_review.md`, `references/agent_training/prosody_scansion_worked_examples.md` | `gate --phase prosody_topline` |
| `line_polish` | Line polish / independent lyric verifier | `references/delegated/55_line_polish_review.md`, `references/delegated/56_independent_verifier_review.md` | `gate --phase line_polish`; fail if quoted issues are not grounded in current lyrics |
| `preproduction_brief` | Preproduction | `references/delegated/39_track_preproduction_brief.md`, `references/agent_training/harmony_melody_groove_primer.md` | `gate --phase preproduction_brief` |
| `adversarial_song_edit` | Adversarial song/preproduction edit | `references/delegated/43_adversarial_song_prompt_edit.md`, `references/craft/adversarial_song_editing.md` | `snapshot` before applying patches; `gate --phase adversarial_song_edit` |
| `packet_compilation` | MiniMax packet | `references/delegated/05_compile_minimax_packet.md`, `references/api/minimax_prompting_and_style_control_playbook.md` | `gate --phase packet_compilation` |
| `prompt_budget` | Prompt compression | `references/delegated/34_prompt_budget_and_compression.md`, `references/api/prompt_budget_and_compression_protocol.md` | `gate --phase prompt_budget` |
| `adversarial_packet_edit` | Prompt/packet adversarial review | `references/delegated/43_adversarial_song_prompt_edit.md` | `snapshot` before packet rewrites; `gate --phase adversarial_packet_edit` |
| `packet_evaluation` | Packet/style/API eval | `references/delegated/06_evaluate_minimax_packet.md`, `references/delegated/19_evaluate_style_fidelity.md`, `references/delegated/26_minimax_parameter_audit.md` | `gate --phase packet_evaluation` |
| `unified_quality_decision` | Unified quality decision | `references/delegated/42_unified_quality_evaluation.md`, `references/delegated/47_revision_cycle_manager.md` | `gate --phase unified_quality_decision` |
| `variant_strategy` | Variant packets | `references/delegated/07_generate_variants.md`, `references/delegated/52_head_to_head_candidate_tournament.md` | `gate --phase variant_strategy` |
| `payload_export` | Payload/render logistics | `references/delegated/13_api_payload_export.md`, `references/delegated/14_render_logging_and_download.md` | `gate --phase payload_export` |
| `cover_workflow` | Cover/re-render | `references/delegated/11_compile_cover_packet.md`, `references/delegated/12_cover_preprocess_and_rerender.md` | `gate --phase cover_workflow` when applicable |
| `render_candidates` | Generate/download renders | `references/delegated/14_render_logging_and_download.md`, provider docs | `gate --phase render_candidates` |
| `post_render_review` | Candidate review/listener panel | `references/delegated/24_compare_render_candidates.md`, `references/delegated/45_listener_panel_review.md`, `references/delegated/09_regeneration_brief.md` | `gate --phase post_render_review` |
| `post_audio_rebuild` | Rebuild album plan from audio | `references/delegated/46_post_audio_planning_rebuild.md` | `gate --phase post_audio_rebuild` |
| `final_qc_release` | Final QC/release | `references/delegated/35_final_audio_mastering_and_transition_qc.md`, `references/delegated/31_build_release_package.md` | `gate --phase final_qc_release` |
| `executive_producer_review` | Final whole-work review | `references/delegated/54_executive_producer_review_loop.md` | `gate --phase executive_producer_review` |
| `completion_fit` | Completion claim check | `references/delegated/29_validate_user_story_fit.md`, `references/delegated/22_full_skill_quality_check.md` | `gate --phase completion_fit`, then `status` |

## Advancement rule

After a gate passes and the stage quality criteria pass, advance with:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py advance <project_slug> --to <next_phase_id> --require-gate
```

Do not use controller pass status as proof of artistic quality. Controller pass means required artifacts exist, validate against schemas where available, are current, and satisfy the controller-level content checks for that phase. Musical rubrics and verifier reviews still decide whether they are good enough artistically.


## Sequential advancement rule

`advance` is sequential by default. The controller refuses non-sequential jumps unless `--allow-jump` is used. Use `--allow-jump` only for documented recovery, replanning, or scope changes; write the reason to `results.tsv` and refresh state/manifest afterward.


## Verification commands

Use these before completion and whenever a gate depends on external truth rather than file presence:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py hash-artifacts <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py validate <project_slug> --deep  # use only near completion or when diagnosing readiness
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-freshness <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-quotes <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-style <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-tournaments <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py lint-prompt <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-variants <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py export-payloads <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-payloads <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py reconcile-state <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py preflight <project_slug> --reconcile
```

A controller pass only counts if the artifact under review is current. Any review with a stale hash or quoted line that cannot be found in the current source artifact is invalid and cannot support advancement.
