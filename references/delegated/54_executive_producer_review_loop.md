# Delegated Stage 54 — Executive Producer Review Loop

## Goal

Run a final high-level creative review equivalent to AutoNovel's whole-manuscript senior review loop, but adapted for professional album quality.

## When required

Required for:

- release-package goals
- full albums
- lead-single projects intended as flagship outputs
- any project marked `quality_mode = release_grade`

## Review personas

Run at least two perspectives:

1. **Executive producer / album architect** — cohesion, weak-track replacement, sequencing, sonic identity, market-level quality.
2. **Topliner / songwriter** — hooks, titles, lyric believability, emotional payoff.
3. Optional: **mix/master QC** — technical presentation and transition consistency.
4. Optional: **style purist** — reference fidelity when a strict style or artist lane is requested.

## Inputs

- final selected renders
- timestamped listening notes
- post-audio planning rebuild
- release package draft
- album canon
- final tracklist
- style selection and style cards
- candidate comparison files

## Outputs

```text
reviews/executive_producer_review_cycle_N.json
reviews/executive_producer_review_cycle_N.md
```

## Loop behavior

Repeat until:

- there are no major release-blocking issues, or
- two consecutive cycles identify no new major issues, or
- plateau detection recommends accepting/cutting/replacing rather than revising.

## Required decision

```text
RELEASE_READY
RELEASE_READY_WITH_NOTES
REVISE_TRACKS
RESEQUENCE
REPLACE_WEAK_TRACK
REGENERATE_SELECTED_RENDERS
REOPEN_FOUNDATION
NOT_RELEASE_READY
```

## Quality bar

Do not approve an album because it is complete. Approve only if it feels like a coherent release where the best tracks justify attention and the weakest tracks do not embarrass the record.
