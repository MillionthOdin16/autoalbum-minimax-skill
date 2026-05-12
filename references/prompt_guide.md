# MiniMax Prompt Guide Shim

This skill keeps its operative MiniMax prompt guidance in:

```text
references/api/minimax_prompting_and_style_control_playbook.md
references/model_profiles/minimax_music_2_6.md
references/api/minimax_music_2_6_full_api_reference.md
```

Core rules used throughout the skill:

1. Prompts should be vivid English creative briefs, not comma-separated tag piles.
2. Preserve the requested style reference, then translate it into audible controls: groove, drums, bass, vocal delivery, hook mechanics, arrangement, and mix space.
3. Keep `prompt_minimax.txt` within the selected provider limit, usually 2000 characters for direct Music 2.6.
4. Put sung content only in `lyrics_minimax.txt`; put production and performance instructions in `prompt_minimax.txt`.
5. Validate all structure tags against the active provider profile before exporting payloads.
