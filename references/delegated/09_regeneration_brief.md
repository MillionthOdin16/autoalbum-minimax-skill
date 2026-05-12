# Delegated: Regeneration Brief

## Task
Create a precise regeneration brief when a MiniMax render is not good enough.

## Read
- tracks/tr_NN/post_generation_eval.json
- tracks/tr_NN/generation_packet.json
- tracks/tr_NN/prompt_minimax.txt
- tracks/tr_NN/lyrics_minimax.txt

## Output
Write `tracks/tr_NN/regeneration_brief.md` and, if needed, a revised packet.

## Action types

- SAME_PACKET_NEW_TAKE: prompt/lyrics are good; model variance was the issue.
- PROMPT_SIMPLIFY: model averaged or ignored instructions.
- PROMPT_MORE_SPECIFIC: output was generic or undercontrolled.
- HOOK_FORWARD: chorus failed to lift or stick.
- STRUCTURE_REPAIR: tags or form failed.
- VOCAL_RETARGET: vocal identity wrong.
- GENRE_REBALANCE: model leaned into wrong genre.
- BASS_OR_GROOVE_REPAIR: low end, drums, or movement wrong.
- LYRIC_REWRITE: lyric cannot be sung or hook is weak.
- CUT_OR_REPLACE: track does not earn its album slot.

## Brief format

```markdown
# Regeneration Brief: Track NN

Decision:
Root cause:
Keep:
Change:
Do not change:
Prompt edit:
Lyrics edit if any:
Variant to generate next:
Success criteria:
```
