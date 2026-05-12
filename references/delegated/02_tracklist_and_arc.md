# Delegated: Tracklist, Album Arc, and Musical Design

## Task
Create the album or track plan in two passes.

Pass 1 creates a skeleton plan from the foundation and album style map. Pass 2 refines it after per-track style cards exist.

Output:
- `planning/tracklist.md`
- `planning/album_arc.md`
- `planning/album_energy_map.md`
- `planning/key_bpm_map.md`
- `planning/transition_map.md`
- `planning/hook_index.md`

## Read
- project_config.json
- foundation/*.md
- style_catalog_outputs/style_selection.json
- style_catalog_outputs/album_style_map.md
- tracks/tr_NN/style_card.json if this is Pass 2
- references/model_profiles/minimax_music_2_6.md
- references/craft/professional_album_craft.md

## Per-track card schema

```markdown
### Track NN: Title
Album function:
Concept:
Emotional role:
Sonic role:
POV/vocal identity:
MiniMax structure plan:
BPM feel:
Key center / harmonic color:
Groove concept:
Energy map by section:
Hook contract:
Hook type:
Memorable moment target:
Verse 1 job:
Verse 2 job:
Bridge/break/interlude job:
Promptable production traits:
Shared album DNA:
Track-specific contrast:
Motifs used or transformed:
Transition in:
Transition out:
Why this track is necessary:
Why it cannot be confused with adjacent tracks:
```

## Album-level rules
- First three tracks must make the promise: sound, voice, stakes.
- Lead single candidates usually belong in tracks 2-4 unless the album concept demands otherwise.
- The closer must be designed as an ending, not a leftover.
- Energy should create intentional runs and releases, not mechanical fast/slow alternation.
- Adjacent tracks may share DNA but must differ in at least two of: BPM feel, key center, groove, vocal intensity, texture, emotional register, section architecture.
- If two tracks serve the same function, merge, cut, or radically differentiate one.


## Two-pass rule

### Pass 1: skeleton plan
Create a tracklist skeleton with provisional title, album function, concept, emotional role, sonic role, rough tempo/energy, and style lane. Do not pretend final per-track style-card detail exists yet.

### Pass 2: refined plan
After `tracks/tr_NN/style_card.json` exists for each track, revise the tracklist, energy map, key/BPM map, transition map, and hook index so they reflect real style-card decisions.

## Single-track mode
If `project_scope` is `single_track` or `lead_single`, create one track card plus a mini arc with:
- opening promise,
- verse tension,
- hook payoff,
- bridge/break contrast,
- final chorus/outro aftertaste.
Do not create fake album-level requirements unless the user asked for an album.
