# Propagation and Debt Rules

AutoAlbum changes are not local. A change to one layer can invalidate downstream artifacts. This file defines when the agent must create propagation debts and what must be rechecked.

## Debt object

A propagation debt is a machine-readable reminder that an upstream decision changed and downstream artifacts may now be stale.

Required fields:

```json
{
  "debt_id": "debt_0001",
  "created_at": "ISO-8601 timestamp",
  "source_change": "sound_signature_changed",
  "source_artifact": "foundation/sound_signature.md",
  "affected_artifacts": ["tracks/tr_03/prompt_minimax.txt"],
  "severity": "critical|major|minor",
  "required_action": "re-evaluate affected MiniMax prompts for style alignment",
  "status": "open|in_progress|resolved|accepted",
  "resolution_notes": ""
}
```

## Propagation map

| If this changes | Recheck these | Why |
|---|---|---|
| `project_config.json` provider/profile | all generation packets, audio settings, prompts, payloads | API limits and tag rules may change. |
| style selection or style profile | album style map, track style cards, lyrics, prompts, style-fidelity evals | Style drift is a primary quality failure. |
| `foundation/album_thesis.md` | tracklist, hook labs, motif ledger, lyrics | The reason for the album changed. |
| `foundation/sound_signature.md` | style cards, preproduction briefs, prompts, selected renders | Sonic DNA must remain coherent. |
| `foundation/lyric_voice.md` | lyrics, prosody, vocal prompts | Words and performance posture must align. |
| `foundation/vocal_identity.md` | vocal delivery prompts, prosody, render reviews | MiniMax may render the wrong performer identity. |
| `foundation/album_canon.json` | any artifact that references changed canon entries | Canon is the truth ledger. |
| track order | transitions, adjacent-track contrast, key/BPM map, album arc | Sequencing changes meaning and flow. |
| selected render | post-audio planning, final sequence, release package metadata | Actual audio supersedes paper plan. |
| lyrics | prosody, prompt, packet, render variants | Lyrics are core generation input. |
| prompt | packet eval, payloads, render logs | New prompt creates a new render lineage. |
| MiniMax output | candidate comparison, album assembly, final QC | Actual audio must update planning reality. |

## Debt rules

1. Do not silently update one artifact when another artifact depends on it.
2. Record a debt whenever downstream validity is uncertain.
3. Critical debts block release-package completion.
4. Major debts block packet-ready or render-ready status unless explicitly accepted.
5. Minor debts may remain open only if they do not affect style, lyrics, prompt validity, sequence, or final output quality.
6. Every resolved debt must cite the artifact and evaluation that resolved it.

## Debt severity

```text
critical: could make the final track/album incoherent, invalid, or low quality
major: could reduce style fidelity, sequencing, prompt control, or songcraft
minor: documentation or low-impact consistency issue
```
