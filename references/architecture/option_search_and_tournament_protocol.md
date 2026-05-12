# Option Search and Tournament Protocol

## Purpose

High-quality albums rarely emerge from the first idea, first hook, first prompt, or first render. This protocol makes option search explicit and prevents the agent from accepting the first coherent artifact.

Use it when the decision has high leverage:

- album concept
- album title
- sound signature
- lyric voice
- artist/vocal persona
- lead single hook
- track title
- chorus
- MiniMax prompt
- generation variant
- selected render
- final track order

## Candidate minimums

| Decision | Minimum candidates |
|---|---:|
| Album concept/title/style thesis | 5 |
| Lyric voice / vocal identity | 5 trial snippets |
| Lead single hook | 8 |
| Ordinary track hook | 4 |
| MiniMax prompt for important track | 3 |
| Lead single render | 5 |
| Ordinary render | 3 |
| Track order | 3 sequences |

## Tournament styles

### Scorecard tournament

Use when artifacts are structurally different and can be scored against a rubric.

### Pairwise tournament

Use when several artifacts are good but hard to rank. Compare A vs B and record the winner and reason. Optional Elo scores can be used for 5+ candidates.

### Blind contrast tournament

Use when style bias or overattachment may distort judgment. Hide candidate names and compare only musical function, impact, memorability, and fit.

## Required outputs

```text
<project_slug>/reviews/tournaments/<tournament_id>.json
<project_slug>/reviews/tournaments/<tournament_id>.md
```

## Winning rule

The winner must not simply be the safest option. Select the candidate that best balances:

- memorability
- emotional specificity
- style fidelity
- album fit
- distinctiveness
- MiniMax controllability
- listener appeal
- professional plausibility

If no candidate is strong, generate a new set instead of crowning a weak winner.
