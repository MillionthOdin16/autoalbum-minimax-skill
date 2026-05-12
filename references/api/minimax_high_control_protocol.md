# MiniMax Music 2.6 High-Control Protocol

## Control hierarchy
MiniMax responds best when the packet separates what the model can hear from what the project internally knows.

### Put in `prompt`
- genre/subgenre/style lane,
- mood and scene,
- vocal delivery,
- groove/drums/bass,
- harmonic color,
- instrumentation/texture,
- hook behavior,
- energy/tension architecture,
- one or two album-continuity cues.

### Put in `lyrics`
- words to be sung/rapped,
- supported structure tags,
- hook/refrain repetition,
- short parenthetical performance cues only when absolutely necessary.

### Keep out of MiniMax prompt
- long worldbuilding lore,
- biography that does not affect sound,
- too many references,
- exact plugin/mix settings,
- exact chord voicings,
- unsupported bracket tags,
- separate contradictory style lanes.

## Prompt length target
- 700-1200 characters: ideal for one clear style.
- 1200-1600 characters: acceptable for fusion or strict artist/song references.
- 1600-2000 characters: use only when necessary; require prompt-priority ordering.

## Prompt-priority ordering
Use this order:
1. style lane and tempo feel,
2. vocal identity,
3. groove/drums/808/bass,
4. harmonic and instrumental palette,
5. hook mechanics,
6. arrangement/tension behavior,
7. track scene/theme,
8. album continuity or adjacent-track distinction.

## MiniMax style levers that matter most
1. Groove and drum pattern.
2. Bass/808 behavior.
3. Vocal tone, delivery, and density.
4. Hook type.
5. Instrument palette.
6. Arrangement shape.
7. Mix/space adjectives.
8. Specific emotional scene.

## Structure-tag discipline
Use the selected provider tag profile exactly. For direct MiniMax API, the documented tags are:

```text
[Intro], [Verse], [Pre Chorus], [Chorus], [Interlude], [Bridge], [Outro],
[Post Chorus], [Transition], [Break], [Hook], [Build Up], [Inst], [Solo]
```

Some wrappers mention `[Drop]` or alternate hyphenated tags. Treat those as provider-specific, not universal.

## Instrumental-first scouting
When style is uncertain, generate a short instrumental or instrumental-leaning packet first to validate:
- tempo feel,
- drum/bass language,
- harmonic palette,
- arrangement energy.

Then add final lyrics after the sonic lane proves viable.

## Variant principle
Each variant should change one primary control dimension.

- A_on_brief: most faithful to the style card.
- B_hook_forward: stronger chorus/hook/replay salience.
- C_bold: more distinct arrangement or texture.
- D_vocal_focus: stronger voice/delivery/ad-lib control.
- E_groove_focus: stronger drums/bass/pocket control.

Never create variants that change genre, voice, lyrics, groove, and arrangement all at once.

## Common failure corrections
- Generic render: add drum/bass/hook/vocal specificity, not more adjectives.
- Wrong style: add adjacent-style differentiators and failure-mode avoid list.
- Weak hook: create a B_hook_forward variant and simplify the chorus lyric.
- Overcrowded render: shorten prompt, remove secondary instruments, make vocal primary.
- Ignored structure: simplify tags and remove unsupported stage directions.
- Flat arrangement: add tension architecture and section energy map.
