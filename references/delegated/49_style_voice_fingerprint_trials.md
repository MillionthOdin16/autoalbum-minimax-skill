# Delegated Stage 49 — Style and Voice Fingerprint Trials

## Goal

Discover the strongest album-specific lyric voice, vocal identity, and MiniMax style-prompt direction before drafting full songs.

This is the music equivalent of AutoNovel's voice-fingerprint process.

## Read

- `references/agent_training/songwriting_lyric_field_guide.md`
- `references/agent_training/hook_chorus_lab.md`
- `references/agent_training/minimax_control_cookbook.md`
- relevant style catalog files
- `references/architecture/option_search_and_tournament_protocol.md`

## Generate 5 trials

Each trial should include:

```text
Trial name:
Lyric voice:
Vocal delivery:
Sonic world:
4-line verse excerpt:
2-line hook excerpt:
MiniMax prompt capsule:
What this trial does better than the others:
What this trial risks:
```

## Evaluate

Score each trial on:

- lyrical specificity
- vocal believability
- hook potential
- style fidelity
- album expandability
- distinctiveness
- MiniMax controllability
- emotional truth

## Outputs

```text
<project_slug>/foundation/style_voice_trials.json
<project_slug>/foundation/style_voice_trials.md
<project_slug>/foundation/lyric_voice.md
<project_slug>/foundation/vocal_identity.md
<project_slug>/foundation/sound_signature.md
```

## Pass criteria

- At least 5 trials exist.
- The selected voice has exemplars and anti-exemplars.
- The final lyric voice explains what to do and what to avoid.
- The final style prompt direction is concrete enough for MiniMax.
