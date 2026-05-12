# Delegated 43 — Adversarial Song and Prompt Edit

## Purpose
Run a harsh cut/edit pass before a track is allowed to become MiniMax-ready, and optionally after failed renders. The purpose is to expose weak material, not to praise the track.

## Read
- `references/craft/adversarial_song_editing.md`
- `references/schemas/adversarial_edit.schema.json`
- `tracks/tr_NN/style_card.json`
- `tracks/tr_NN/hook_lab.json` if present
- `tracks/tr_NN/lyrics_working.md`
- `tracks/tr_NN/prosody_review.json` if present
- `tracks/tr_NN/preproduction_brief.json` if present
- `tracks/tr_NN/prompt_minimax.txt` and `generation_packet.json` if present
- `foundation/album_canon.json`

## Write

```text
tracks/tr_NN/adversarial_song_edit.json
tracks/tr_NN/adversarial_song_edit.md
```

## Instructions

Attack the track from five angles:

1. Lyric line quality
2. Hook and title memorability
3. Prosody and delivery
4. Style/fingerprint fidelity
5. MiniMax prompt controllability

Classify every issue using the categories in `adversarial_song_editing.md`. For each critical or major issue, propose a precise patch.

## Pass/fail

A track cannot pass this stage with unresolved critical findings. Major findings may pass only with written justification and a logged debt.
