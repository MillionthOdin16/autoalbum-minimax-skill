# Delegated 45 — Listener Panel Review

## Purpose
Use listener personas to catch replay, appeal, authenticity, pacing, and emotional-impact issues that specialized technical evaluators may miss.

## Read
- `references/craft/listener_panel_method.md`
- `references/schemas/listener_panel.schema.json`
- current track or album artifacts
- selected audio or candidate renders if available
- `foundation/album_canon.json`
- relevant style profile/fingerprint

## Write

Track:
```text
tracks/tr_NN/listener_panel.json
tracks/tr_NN/listener_panel.md
```

Album:
```text
reviews/listener_panel_album.json
reviews/listener_panel_album.md
```

## When required

Required for:

- release-grade albums
- lead singles
- style-strict artist/song requests
- tracks with borderline candidate comparison
- albums with unclear sequencing
- any stage where technical scores pass but the result feels dull

## Output
Return valid `listener_panel.schema.json` and include a decision:

```text
KEEP
KEEP_WITH_MINOR_FIX
REGENERATE_SAME_PACKET
REVISE_PROMPT_AND_REGENERATE
REVISE_LYRICS_AND_REGENERATE
CUT_OR_REPLACE
ESCALATE
```
