# MiniMax Music 2.6 Research Notes

## Official/API facts

- Direct API endpoint: `/v1/music_generation` with `model: music-2.6`.
- Prompt describes style, mood, and scenario.
- Prompt limit: 2000 characters.
- Lyrics for non-instrumental songs: required, 1-3500 characters.
- Instrumental mode: `is_instrumental: true`; lyrics not required.
- Lyrics optimizer: auto-generates lyrics from prompt when enabled and lyrics are empty.
- Direct API structure tags: `[Intro]`, `[Verse]`, `[Pre Chorus]`, `[Chorus]`, `[Interlude]`, `[Bridge]`, `[Outro]`, `[Post Chorus]`, `[Transition]`, `[Break]`, `[Hook]`, `[Build Up]`, `[Inst]`, `[Solo]`.
- Default useful output settings: 44.1 kHz, 256 kbps, mp3; some interfaces also support wav/pcm.

## Prompting guidance

- Use vivid English sentences, not comma-separated tag lists.
- Prompt should read like a creative brief for a musician.
- Strong prompt shape: mood + BPM optional + genre/subgenre; vocal description; narrative/theme; scene/atmosphere; key instruments and production elements.
- Describe vocals as a character.
- Include only 2-3 or 2-4 specific instruments/textures rather than an exhaustive list.
- English prompts work best.

## Community/practical cautions

- Some routes expose different tag spellings. Use a provider-specific tag profile and validate before generation.
- Unofficial user reports suggest unsupported tags or parenthetical directions may be sung or ignored; do not put performance directions in the lyrics field.
- Generate multiple candidates because model variance and occasional artifacts are expected.
- Treat the first render as a demo, not a final.

## Skill implications

- AutoAlbum needs a MiniMax packet compiler, not just a production sheet.
- It must validate prompt and lyric lengths.
- It must validate tags against the selected provider profile.
- It must separate lyric quality from generation readiness.
- It must include post-generation review and regeneration briefs.
