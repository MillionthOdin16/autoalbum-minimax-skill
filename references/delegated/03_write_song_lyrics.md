# Delegated: Write Song Lyrics

## Task
Write a complete song lyric for Track NN using the approved track card.

## Read
- `references/agent_training/songwriting_lyric_field_guide.md`
- `references/agent_training/hook_chorus_lab.md`
- `references/agent_training/prosody_scansion_worked_examples.md`
- `tracks/tr_NN/hook_lab.json`
- `tracks/tr_NN/arrangement_energy_review.json`
- intent_intake.json
- project_config.json
- foundation/*.md
- planning/tracklist.md track NN card
- tracks/tr_NN/style_card.json
- planning/hook_index.md
- planning/transition_map.md
- references/model_profiles/minimax_music_2_6.md
- references/craft/professional_album_craft.md
- previous track brief/lyrics if it exists
- next track brief only, not future lyrics

## Output files
- tracks/tr_NN/lyrics_working.md
- tracks/tr_NN/lyrics_minimax.txt

## Requirements
- Do not write from general lyrical intuition. Apply the lyric field guide, hook lab output, and arrangement review.
- The selected hook phrase and delivery strategy from `hook_lab.json` must shape the chorus/hook.

### Structure
Use only the chosen tag profile. For direct MiniMax API, use tags like:

```text
[Intro]
[Verse]
[Pre Chorus]
[Chorus]
[Post Chorus]
[Bridge]
[Break]
[Build Up]
[Inst]
[Solo]
[Outro]
```

Do not use `[Verse 2]`, `[Final Chorus]`, `[Refrain]`, `[Chorus louder]`, or parenthetical directions that might be sung.

### Songwriting
- Open with scene, motion, or a striking sensory image.
- Verse 1 establishes tension.
- Pre-chorus, if present, narrows pressure into the hook.
- Chorus/hook states the emotional thesis in simpler, more repeatable language.
- Verse 2 must add new information, not paraphrase verse 1.
- Bridge/break/interlude must change meaning, perspective, harmonic color, or energy.
- Final return must feel changed by what came before.

### Singability
- Keep most chorus lines shorter than verse lines.
- Use open vowels for title/hook phrase where possible.
- Avoid overpacked lines unless the vocal style is rap/spoken/rhythmic.
- Do not write purely literary lines that cannot be sung naturally.
- Use repetition deliberately, especially hook/post-chorus, but register it in motif_ledger if it recurs across songs.

### Anti-generic rules
- No vague uplift phrases: rise above, through the fire, heart of gold, never gonna break, find my way, etc.
- No interchangeable chorus. The hook must require this song's verses and album position.
- No generic dramatic weather unless the album has earned it as a motif.
- Every track must have at least one image, turn, or line that could not belong to any other track on the album.

## Output format
Write `lyrics_working.md` with short craft notes and write `lyrics_minimax.txt` as the exact MiniMax input. Include character counts.

## Mandatory songwriting additions
Before treating lyrics as complete, draft toward the prosody/topline gate:

- Write hooks with open vowels and repeatable cadence where the style requires singability.
- For rap, mark where flow switches, ad-libs, internal rhymes, and breath resets are expected.
- For melodic genres, keep chorus lines shorter and more singable than dense verses unless the style profile says otherwise.
- Do not create final `lyrics_minimax.txt` until `33_prosody_scansion_topline_review.md` passes.
- If a line is clever but unsingable, revise it.
