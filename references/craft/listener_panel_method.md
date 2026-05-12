# Listener Panel Method

The listener panel is the AutoAlbum translation of AutoNovel's reader panel. It exists because technical evaluators can miss listener-facing problems: boredom, weak identity, poor replay value, unclear sequence function, or style mismatch.

## Panel personas

Use at least four for release-grade projects and at least two for risky tracks.

```text
Target fan: knows the requested genre/style and cares about authenticity.
Casual listener: judges immediate appeal, memorability, and skip risk.
Producer/arranger: judges groove, form, energy, and production decisions.
Mix/technical listener: catches vocal intelligibility, harshness, mud, artifacts, loudness inconsistency.
A&R/label listener: judges market position, sequencing, single potential, and weak links.
Lyric critic: judges specificity, emotional truth, prosody, and hook writing.
Style purist: judges whether the named genre/artist/song lane actually lands.
```

## Pre-render panel

Use for lyrics/prompt packets when no audio exists. The panel must mark all conclusions as pre-render hypotheses.

Questions:

```text
Would this song be worth generating?
What is the memorable promise?
What feels generic before audio even exists?
What should MiniMax be told more clearly?
What should be removed from the prompt?
What would likely fail in the render?
```

## Post-render panel

Use after audio candidates exist.

Questions:

```text
Would you replay this?
What moment sticks after one listen?
Where did attention drop? Give timestamp.
Does the hook land emotionally and melodically?
Does the track belong on the album?
Does it sound distinct from adjacent tracks?
Does it satisfy the requested style/fingerprint?
What should be kept, regenerated, revised, or cut?
```

## Panel output discipline

The panel must produce decisions, not just impressions.

```text
KEEP
KEEP_WITH_MINOR_FIX
REGENERATE_SAME_PACKET
REVISE_PROMPT_AND_REGENERATE
REVISE_LYRICS_AND_REGENERATE
CUT_OR_REPLACE
ESCALATE
```

A panel decision must cite evidence: lyric lines, prompt fields, timestamps, or packet artifacts.
