# Project Scope Modes

## single_track
A complete song workflow: concept, style card, lyrics, MiniMax prompt, variants, parameter audit, and render review when possible.

Required artifacts:
```text
project_config.json
foundation/track_thesis.md or compact album_thesis.md
tracks/tr_01/style_card.json
tracks/tr_01/lyrics_minimax.txt
tracks/tr_01/prompt_minimax.txt
tracks/tr_01/generation_packet.json
tracks/tr_01/variants/*.json
ops/parameter_audit.md
```

## lead_single
Like single_track, but with stronger hook, first-30-second, replay, and style-identity gates. Must create at least five variants if feasible.

## EP
3-6 tracks. Requires compact sequence arc, contrast map, opener/closer logic, and no filler.

## mixtape
Looser than an album. Prioritize identity, momentum, variety, quotable moments, and standout track run. Narrative cohesion is optional.

## album
A full authored sequence. Requires first-three-track promise, midpoint development, late payoff, closer aftertaste, and weakest-track justification.

## concept_album
Requires thesis, narrative/emotional architecture, motifs, callbacks, transformations, and sequence logic.

## beat_tape
Producer-led. Lyrics optional. Requires instrumental identity, texture/groove variety, loop fatigue checks, and transition flow.

## instrumental_score
Mood/scene-driven. Requires motif development, cue function, dynamics, instrumentation map, and narrative pacing.

## cover_or_rerender
Source-audio workflow. Requires cover packet, source audio registry, source compliance, and render review.

## revision_of_existing_work
User supplies lyrics, packets, demos, or renders. Preserve user material unless asked to rewrite. Identify what stage the project is already in and resume from there.
