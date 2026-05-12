# Adversarial Song and Prompt Editing

Adversarial editing is the AutoAlbum equivalent of AutoNovel's cut pass. The editor is not trying to be encouraging. The editor tries to remove the weakest material and expose what is hurting quality.

## What to attack

For lyrics:

```text
GENERIC_LINE       line could appear in hundreds of songs
ABSTRACT_FILLER    emotion named but not dramatized
TWIN_VERSE         second verse repeats first verse's information
WEAK_HOOK          chorus lacks title/memory/payoff
BAD_PROSODY        line fights the implied rhythm or breath
CLICHE_IMAGE       overused image with no transformation
UNSINGABLE_DENSITY too many words or stresses for style
FALSE_DEPTH        sounds profound but says little
STYLE_DRIFT        lyric posture does not match target style
BAD_SECTION_JOB    section does not do its required musical/narrative work
```

For arrangements/preproduction:

```text
FLAT_ENERGY        no change between sections
NO_CONTRAST        bridge/break does not reveal anything new
WRONG_GROOVE       drum/bass grammar mismatches style
OVERARRANGED       too many ideas for one track
UNDERARRANGED      no memorable sonic event
MISSING_LIFT       chorus does not open, drop, or intensify
```

For MiniMax prompts:

```text
TAG_PILE           comma list rather than vivid creative brief
OVERSTUFFED        too many instructions; core controls diluted
UNAUDIBLE_LORE     backstory that MiniMax cannot render
CONTRADICTION      e.g. intimate acoustic + maximal EDM drop without rationale
VAGUE_STYLE        style words without drums/bass/vocal/hook mechanics
REFERENCE_COLLAPSE named style request becomes generic genre
BAD_NEGATIVE       avoid list is absent, vague, or excessive
```

## Required adversarial output

For every material track before packet approval, create:

```text
tracks/tr_NN/adversarial_song_edit.json
tracks/tr_NN/adversarial_song_edit.md
```

The JSON must identify exact target text or artifact sections, classify the issue, explain why it hurts the final generated track, and propose a patch.

## Severity levels

```text
critical: must fix before proceeding
major: should fix unless there is a strong artistic reason
minor: fix if easy or if repeated elsewhere
watch: possible issue; monitor after render
```

## Cut discipline

A serious adversarial pass should propose at least one cut, compression, or replacement even when the track is promising. If nothing can be cut, explain why the track is already lean.

## Patch rule

Never rewrite a whole song when the problem is local. Prefer the smallest patch that improves the target dimension and avoids new regression.
