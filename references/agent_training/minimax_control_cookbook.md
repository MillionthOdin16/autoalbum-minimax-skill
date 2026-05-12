# MiniMax Music 2.6 Control Cookbook for AutoAlbum

Use this whenever compiling or evaluating MiniMax packets. MiniMax is controlled primarily through the prompt, lyrics, supported structure tags, provider parameters, and candidate iteration.

## Core principle

The prompt should be a compact creative brief for the renderer. The lyrics field should contain lyrics and supported structure tags. Do not use the lyrics field as a production-instruction dump.

## Prompt architecture

Use this order:

```text
[style lane + tempo/groove feel] + [vocal identity] + [song situation/theme] + [drums/bass/groove] + [2-4 production/mix elements] + [arrangement/tension behavior] + [avoid if critical]
```

## Prompt density target

For direct MiniMax API, the hard limit is 2000 characters. For quality, target roughly 700-1400 characters unless the provider and project require more.

### Too short
```text
Dark emotional rap song with trap drums and catchy hook.
```
Fails because it gives MiniMax almost no style mechanics.

### Too long
A 1900-character prompt listing every motif, every instrument, all album backstory, exact emotional subplot, ten artists, and multiple contradictory mix spaces.

Fails because it overconstrains and dilutes the controls.

### Good
```text
A dark melodic trap song around a slow half-time bounce, with intimate Auto-Tuned sung-rap vocals that turn into a simple chant-like hook. The song is about realizing fame has turned every room into a surveillance camera. Production centers on a sparse minor piano loop, sliding 808 sub bass, crisp trap hats, and dry close vocals with occasional ghostly ad-libs. Keep the verses tense and narrow, then let the chorus widen with stacked vocal doubles without becoming glossy pop.
```

## Field separation

### Put in prompt
- genre/subgenre/style
- vocal delivery
- drums/bass/groove
- instrumentation
- mix space
- arrangement/tension behavior
- mood/scene
- avoid-list

### Put in lyrics
- section tags
- actual sung/rapped words
- short hook repetitions
- structural lyric sections

### Put in metadata/state, not prompt
- full album thesis
- long style analysis
- critic notes
- internal scoring
- provenance
- exact file paths

## Control reliability tiers

### High reliability
- broad genre/subgenre
- vocal gender/type when supported by provider behavior
- lyrics content
- section tags
- mood/energy
- instrument family/palette

### Medium reliability
- exact BPM
- exact key
- exact section duration
- exact mix engineering
- exact vocal similarity

### Low reliability
- precise chord progression
- exact bar counts
- exact mastering settings
- exact ad-lib placement

Use high and medium controls. Avoid making final quality depend on low-reliability controls.

## Lyrics tag discipline

Use provider-specific tags only. Direct MiniMax music generation supports tags including `[Intro]`, `[Verse]`, `[Pre Chorus]`, `[Chorus]`, `[Interlude]`, `[Bridge]`, `[Outro]`, `[Post Chorus]`, `[Transition]`, `[Break]`, `[Hook]`, `[Build Up]`, `[Inst]`, and `[Solo]`.

Never invent tags like:
- `[Verse 2]`
- `[Final Chorus]`
- `[Chorus louder]`
- `[Drop if possible]`
- `[whispered but emotional]`

Put those directions in the prompt.

## Variant strategy

Use variants to search quality space:

- A_on_brief: faithful execution of plan.
- B_hook_forward: stronger replay and clearer chorus/hook.
- C_bold: more distinctive production/arrangement risk.
- Optional D_vocal_intimate: focuses vocal and lyric intelligibility.
- Optional E_production_heavy: stronger sonic identity.

Do not alter lyrics in variants unless the issue is known to be lyrical.

## Common MiniMax packet failures

- prompt is a list of tags, not a creative brief
- prompt has too many reference anchors
- lyrics are too dense for singing
- unsupported tags appear in lyrics
- the prompt asks for one style but lyrics imply another
- no hook described in prompt or lyrics
- exact BPM/key treated as guaranteed
- prompt lacks drums/bass/groove
- prompt lacks vocal identity
- prompt describes mood but not arrangement

## Packet approval checklist

```text
provider profile selected
prompt <= provider limit
lyrics <= provider limit or instrumental mode true
supported tags only
prompt is vivid prose
style lane concrete
vocal delivery specified
groove/drums/bass specified
hook mechanics specified
production/mix space specified
arrangement/tension behavior specified
no contradictions
prompt_budget_report passed
prosody_review passed
```
