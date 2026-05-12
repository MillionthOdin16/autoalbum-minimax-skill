# Album Style Map Template

Use this after project configuration and before tracklist generation. The goal is to avoid disjoint AI albums by establishing shared sonic DNA and track-specific variation.

## Output: `style_catalog_outputs/album_style_map.md`

```markdown
# Album Style Map

## Raw user style request
...

## Reference anchors
- Artist / producer / song / album / scene / era references.

## Primary style lane
...

## Secondary style lanes
...

## Style strictness
1-5 with explanation.

## Shared sonic DNA
- Drums:
- Bass:
- Harmony:
- Instruments:
- Vocal identity:
- Ad-lib philosophy:
- Mix space:
- Recurring textures:
- Recurring rhythmic cells:
- Recurring lyrical image fields:

## Controlled variation plan
| Track | Function | Style lane | Tempo feel | Groove | Vocal mode | Production delta | Why it belongs | Why it is distinct |
|---|---|---|---|---|---|---|---|---|

## Album-level do-not-list
- Traits that would make the album generic.
- Traits that would break the chosen style lane.
- Overused prompt words to avoid.

## Reference translation
For each named reference, convert name into musical controls:

| Reference | Keep | Translate into | Use on tracks | Avoid |
|---|---|---|---|---|

## Sequencing implications
- Opener should establish:
- Track 2 should prove:
- Lead single should maximize:
- Mid-album contrast should come from:
- Closer should resolve:

## MiniMax compilation rules
- Max prompt density:
- Tags allowed:
- Common prompt fragment:
- Per-track prompt field to vary:
```

## Album cohesion rules

Each track must carry at least three shared DNA traits. Each track must also have at least two strong distinguishing traits. If a track cannot satisfy both, revise it or cut it.

## Track contrast matrix

Before generation, build a matrix comparing adjacent tracks:

```text
Track N vs Track N+1:
- tempo contrast
- drum contrast
- vocal contrast
- lyrical perspective contrast
- harmonic/mode contrast
- energy contrast
- hook contrast
- production texture contrast
```

No adjacent pair may share more than 70% of the same style fingerprint unless one is an intentional reprise/interlude.
