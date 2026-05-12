# MiniMax Prompt Budget and Compression Protocol

## Purpose
MiniMax Music 2.6 uses a style/mood/scenario prompt plus a lyrics field. High-quality results depend on giving the model enough concrete musical control without overloading the prompt. This protocol makes prompt compression a mandatory step before packet approval.

## Prompt budget targets

```text
hard API ceiling: provider profile dependent; direct MiniMax prompt max 2000 characters
ideal serious-track range: 650-1400 characters
lead single / complex fusion upper range: 1200-1700 characters
red zone: 1700-2000 characters; allowed only if every sentence controls audible output
fail: above provider limit
```

## Prompt priority order
When the prompt is too long, preserve in this order:

1. genre/subgenre/style lane and raw reference anchors requested by user.
2. vocal identity and delivery.
3. groove/drum/bass behavior.
4. hook mechanics and chorus lift.
5. arrangement/tension curve.
6. 2-4 production/mix-space details.
7. album role and emotional thesis.
8. atmospheric scene/image.
9. secondary instruments and decorative details.

Delete or compress:

```text
backstory that cannot be heard
long lists of adjectives
multiple near-synonyms for the same mood
unverifiable claims like "Grammy-winning"
contradictory tempo/mood/style demands
production minutiae the model cannot reliably control
```

## Required prompt shape
A strong MiniMax prompt should usually be 4-7 sentences:

```text
1. Style lane, tempo feel, and emotional stance.
2. Vocal delivery and persona.
3. Groove, drums, bass, and rhythmic feel.
4. Hook/chorus behavior and arrangement/tension arc.
5. Sonic palette/mix space.
6. Track role or album-continuity detail if useful.
7. Avoid/failure-mode sentence only if the provider supports negative guidance in prompt text.
```

## Hard/soft control distinction
Each generation packet must classify controls as:

```text
hard_constraints: lyrics, valid tags, vocal gender/persona if essential, main style lane, no instrumental when vocal required
soft_guidance: BPM feel, key center, instrumentation, arrangement contour, mix texture
non_controllable_or_low_reliability: exact bar counts, exact mastering numbers, exact vocal likeness, exact plugin chains
```

## Prompt failure modes

```text
style salad: too many genres or references without hierarchy
mood fog: vivid adjectives but no drums, bass, vocal, hook, or arrangement controls
technical cosplay: studio jargon that does not guide generation
reference blur: multiple artist/song references that pull in incompatible directions
album lore overload: story world details with no audible translation
anti-prompt bloat: too many avoid instructions crowd out desired sound
```

## Required output
Write `tracks/tr_NN/prompt_budget_report.json` using `references/schemas/prompt_budget_report.schema.json` and update `minimax_eval.json`.
