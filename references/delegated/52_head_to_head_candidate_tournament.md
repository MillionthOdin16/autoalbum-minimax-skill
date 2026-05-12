# Delegated Stage 52 — Head-to-Head Candidate Tournament

## Goal

Use head-to-head judgment when several concepts, hooks, packets, or renders are plausible. This prevents score inflation and forces concrete tradeoff decisions.

## Inputs

Any candidate set:

- concept candidates
- style/voice trials
- hook/title candidates
- lyric revisions
- MiniMax prompt variants
- render candidates
- album sequence candidates

## Output

```text
reviews/tournaments/<tournament_id>.json
reviews/tournaments/<tournament_id>.md
```

## JSON structure

```json
{
  "tournament_id": "tr_03_hook_tournament_01",
  "candidate_type": "hook|prompt|render|sequence|concept|voice_trial",
  "candidates": [],
  "matches": [
    {
      "a": "A",
      "b": "B",
      "winner": "A",
      "reason": "A has stronger title integration and cleaner vowel shape."
    }
  ],
  "ranked_results": [],
  "selected_candidate": "",
  "no_winner_reason": null,
  "next_action": "SELECT|GENERATE_MORE|REVISE_TOP_TWO|ESCALATE"
}
```

## Judgment rules

Do not select the most polished candidate if it is less memorable, less style-faithful, or less album-specific. Do not select the most unusual candidate if it damages replay value or MiniMax controllability.
