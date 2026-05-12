# Delegated: Generate MiniMax Variants

## Task
Create multiple MiniMax generation variants for Track NN without breaking album continuity.

## Read
- tracks/tr_NN/generation_packet.json
- tracks/tr_NN/minimax_eval.json
- foundation/*.md
- planning/*.md

## Output files
- tracks/tr_NN/variants/A_on_brief.json
- tracks/tr_NN/variants/B_hook_forward.json
- tracks/tr_NN/variants/C_bold.json

## Variant definitions

### A_on_brief
The most faithful version. Preserve prompt, lyrics, BPM/key, vocal, arrangement, and album role.

### B_hook_forward
Same lyrics and album DNA, but prompt emphasizes:
- clearer chorus lift.
- more memorable hook/post-chorus.
- stronger vocal contrast between verse and chorus.
- replay value.

### C_bold
Same track concept and lyrics, but prompt allows a more surprising production angle:
- stronger contrast.
- unusual texture.
- more distinctive groove.
- sharper tension/release.

## Optional variants for singles
- D_vocal_intimate: closer vocal, less production density.
- E_production_heavy: stronger drums/bass/arrangement impact.

## Rule
Do not alter lyrics unless explicitly instructed. If the lyrics are the problem, create a regeneration brief, not a prompt variant.


## V23 renderability requirement

Each variant file must be a complete valid `generation_packet.schema.json` object, not a delta, note, or patch. The agent must be able to send any variant through `export-payloads` without mentally merging it with the base packet.

Required variant IDs:
- `A_on_brief`
- `B_hook_forward`
- `C_bold`

Each variant must include full `model`, `provider`, `prompt`, `lyrics`, `lyrics_optimizer`, `is_instrumental`, `audio_setting`, `provider_profile_path`, `style_card_path`, `prompt_budget_report_path`, `hard_constraints`, `soft_guidance`, `avoid`, `album_continuity`, and `validation` fields.
