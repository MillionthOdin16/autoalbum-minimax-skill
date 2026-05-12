# Quality Loop Controller

The quality loop controller is an AutoNovel-inspired operating pattern for AutoAlbum. It is a behavioral controller for agents; it can later be implemented as a script. Its purpose is to make the pipeline score-gated, rollback-aware, and resistant to quality drift.

## Loop types

### Foundation loop

Run until the album foundation is strong enough to support generation.

```text
create/revise foundation artifact
→ run unified evaluation scope=foundation
→ identify weakest dimension
→ revise only that dimension
→ update album canon if new hard facts appear
→ re-evaluate
→ keep if improved; otherwise restore previous artifact or log rejection
→ update results.tsv and state.json
```

Exit when:

```text
foundation_overall >= 8.0
album_concept_score >= 8.0
sound_signature_score >= 8.0
style_map_score >= 8.0
album_canon_integrity_score >= 8.0
blocking_issues == []
```

### Track loop

Run per track until the track is ready for MiniMax packet generation.

```text
style_card + hook_lab + arrangement plan
→ lyrics draft
→ songcraft/prosody/adversarial edit
→ patch/revise
→ unified evaluation scope=track_pre_packet
→ keep if improved
→ update canon/debts/results/state
```

Exit when:

```text
songcraft_score >= 7.5
prosody_score >= 8.0
hook_score >= 8.0
style_fidelity_score >= 8.0 when style requested
adversarial_critical_findings == 0
```

### Packet loop

Run until the generation packet is concise, valid, and controllable.

```text
compile packet
→ prompt budget review
→ MiniMax packet evaluation
→ adversarial prompt edit
→ patch packet/prompt/lyrics only if needed
→ re-evaluate
→ keep if improved
```

Exit when:

```text
minimax_packet_score >= 8.0
prompt_budget_pass == true
provider_profile_valid == true
style_fidelity_score >= required threshold
no critical prompt contradictions
```

### Render loop

Run after MiniMax returns candidates.

```text
render variants
→ timestamped listening notes
→ candidate comparison
→ listener panel when high-risk or release-grade
→ select / regenerate / revise packet / cut track
→ update post-audio album facts
→ update canon/state/results
```

Exit when:

```text
selected_candidate exists OR approved_pending_generation exists for packet-only goals
post_generation_decision in [KEEP, CUT_WITH_JUSTIFICATION, REGENERATE_WITH_BRIEF]
```

### Album revision loop

Run after enough actual audio exists to judge the album.

```text
post-audio planning rebuild
→ unified evaluation scope=album_post_audio
→ identify weakest track/sequence/transition/style-cohesion issue
→ revise/cut/regenerate/resequence one targeted issue
→ re-evaluate
→ keep if improved; otherwise revert and log
```

Exit when:

```text
album_sequence_score >= 8.0
weakest_track_score >= 7.5 or track is cut/replaced
final_audio_qc_pass == true for release packages
no unresolved critical blockers
```

## Keep/discard rule

A revision is kept only if it improves the target dimension without causing new critical regressions. If a revision improves one dimension but damages another, classify it:

```text
KEEP_WITH_DEBT        improvement is important and debt is logged
REVISE_AGAIN          promising but incomplete
DISCARD               net regression
ESCALATE_TO_HUMAN     subjective tradeoff cannot be resolved autonomously
```

## Plateau detection

Stop repeating the same fix when the same score remains within +/- 0.2 for three attempts or when the same reviewer complaint appears three times. Then choose one:

```text
CUT_TRACK
REPLACE_TRACK
CHANGE_STYLE_LANE
SIMPLIFY_PROMPT
CHANGE_HOOK
CHANGE_STRUCTURE
ACCEPT_WITH_JUSTIFICATION
ESCALATE_TO_HUMAN
```
