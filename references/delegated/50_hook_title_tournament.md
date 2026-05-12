# Delegated Stage 50 — Hook and Title Tournament

## Goal

Prevent weak hooks from reaching MiniMax. Generate multiple hook/title options and select the strongest through structured comparison.

## When required

Required for:

- lead singles
- opening tracks
- closers
- tracks with `hook_lab_score < 8.0`
- any style lane where hook identity drives appeal

Recommended for every vocal track when quality mode is `release_grade`.

## Read

- `references/agent_training/hook_chorus_lab.md`
- `references/craft/prosody_scansion_and_topline_gate.md`
- track style card
- album canon
- relevant style profile

## Process

1. Generate 4–8 hook/title candidates.
2. Each candidate must include:
   - title phrase
   - chorus anchor line
   - optional post-chorus phrase
   - melodic/rhythmic shape description
   - vowel/breath analysis
   - why it would be remembered
   - failure risk
3. Run scorecard and pairwise comparison.
4. Select, revise, or generate another round.

## Outputs

```text
tracks/tr_NN/hook_title_tournament.json
tracks/tr_NN/hook_title_tournament.md
```

## Pass criteria

- winner has a clear title/hook relationship
- hook is singable/rappable in the target style
- chorus payoff is stronger than verse energy
- hook is not generic, overwritten, or detached from album thesis
