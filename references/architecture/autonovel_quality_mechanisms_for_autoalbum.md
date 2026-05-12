# AutoNovel Quality Mechanisms Translated for AutoAlbum

This reference captures the AutoNovel mechanisms that improve output quality and reliability when translated into AutoAlbum. The goal is not architectural imitation. The goal is to import mechanisms that produce better intermediate artifacts, reduce drift, and improve final tracks and albums.

## Imported mechanisms

| AutoNovel mechanism | AutoAlbum translation | Why it improves music output |
|---|---|---|
| Foundation score gate | Foundation + album canon + style map gate | Prevents weak concepts from becoming many weak tracks. |
| Layered creative state | Album thesis, sound signature, lyric voice, style map, album canon, per-track briefs | Keeps style, lyrics, sequencing, and MiniMax packets aligned. |
| Canon grows during drafting | `foundation/album_canon.json` grows during lyrics, prompt compilation, render review | Keeps motifs, persona facts, sonic rules, and accepted render facts consistent. |
| Keep/discard after evaluation | Score-gated revision cycles with rollback decisions | Prevents revisions that sound plausible but reduce song quality. |
| Results log | `results.tsv` plus state history | Makes improvement measurable rather than vibes-based. |
| Propagation rules | Propagation debts whenever upstream decisions change | Prevents a style or lyric voice change from leaving stale prompts/tracks behind. |
| Adversarial editing | Adversarial song/prompt edit + patch plan | Finds weak lines, bloated sections, generic hooks, and unhelpful prompt language. |
| Reader panel | Listener panel with fans, casual listeners, producer, engineer, A&R, style purist | Catches problems that a technical evaluator misses. |
| Revision brief | Regeneration/revision brief from concrete evidence | Converts criticism into controlled changes. |
| Plateau detection | Revision cycle manager | Stops endless churn and forces cut/replace/escalate decisions. |
| Rebuild docs after draft | Post-audio planning rebuild | Updates tracklist, arc, transitions, and album story after hearing actual renders. |

## Quality principle

Every imported mechanism must answer at least one of these questions:

1. Does it make weak material easier to detect?
2. Does it make revisions safer and less likely to drift?
3. Does it preserve coherence across the album?
4. Does it improve MiniMax prompt controllability?
5. Does it improve the final listener experience?

If a mechanism adds paperwork without improving one of those outcomes, do not apply it.
