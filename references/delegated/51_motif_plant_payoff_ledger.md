# Delegated Stage 51 — Motif Plant/Payoff Ledger

## Goal

Track intentional callbacks across the album so repetition creates cohesion rather than accidental sameness.

## Read

- `foundation/album_canon.json`
- `foundation/motif_ledger.md`
- `planning/tracklist.md`
- `planning/album_arc.md`
- all `tracks/tr_NN/style_card.json`

## Motif types

Track these motif types:

- lyrical phrase
- image/symbol
- title callback
- vocal gesture
- rhythmic motif
- drum/bass pattern
- synth/instrument texture
- harmony/key relationship
- structural event
- silence/break/dropout
- transition sound
- cover/re-render relation

## Outputs

```text
foundation/motif_plant_payoff_ledger.json
foundation/motif_plant_payoff_ledger.md
```

## Required fields per motif

```json
{
  "motif_id": "light_as_surveillance",
  "type": "lyrical|sonic|structural|production|vocal",
  "plant_track": "tr_01",
  "payoff_tracks": ["tr_05", "tr_10"],
  "first_form": "fluorescent hallway image",
  "transformed_form": "stage lights as interrogation",
  "purpose": "turn private paranoia into public performance",
  "avoid": "do not repeat the exact phrase accidentally",
  "status": "planned|planted|paid_off|orphaned|overused"
}
```

## Pass criteria

- each intentional repetition is registered
- each major motif has a transformation, not just recurrence
- orphaned motifs are removed or paid off
- overused motifs are flagged for revision
- the album has cohesion without making tracks indistinguishable
