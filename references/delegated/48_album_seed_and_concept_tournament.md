# Delegated Stage 48 — Album Seed and Concept Tournament

## Goal

Before locking the album or single concept, generate and evaluate multiple concept directions. Do not accept the first coherent idea.

## Read

- user request
- `references/architecture/option_search_and_tournament_protocol.md`
- `references/agent_training/final_album_judging_rubric.md`
- relevant style catalog files if the user gave genre/artist/song references

## Inputs

- raw user concept
- requested scope
- requested style references
- any supplied lyrics/audio/material

## Process

1. Generate 5–10 candidate project concepts.
2. Each candidate must include:
   - working title
   - one-sentence thesis
   - emotional engine
   - style lane
   - audience promise
   - sonic DNA
   - track/album arc potential
   - biggest risk
3. Score candidates against:
   - originality
   - listener appeal
   - album depth
   - style compatibility
   - MiniMax controllability
   - hook potential
   - expansion potential across multiple tracks
4. Run pairwise comparisons for the top 3.
5. Select a winner or generate another round if all are weak.

## Outputs

```text
<project_slug>/foundation/concept_tournament.json
<project_slug>/foundation/concept_tournament.md
<project_slug>/seed.txt
```

## Pass criteria

- At least 5 candidates were considered.
- The winner has a clear reason to exist.
- The concept can support the requested scope.
- The concept has concrete musical implications, not just a story idea.
- The decision is logged in `results.tsv`.
