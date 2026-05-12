# Delegated: Post-Generation Review

## Task
Review a generated MiniMax render against its packet and the album plan.

## Read
- `references/agent_training/final_album_judging_rubric.md`
- `references/agent_training/production_mix_mastering_primer.md`
- `references/agent_training/agent_anti_shortcut_checklists.md`
- tracks/tr_NN/generation_packet.json
- tracks/tr_NN/variants/*.json
- selected audio path or listening notes
- foundation/*.md
- planning/*.md
- adjacent generated tracks if available

## Output
Write `tracks/tr_NN/post_generation_review.md` and `tracks/tr_NN/post_generation_eval.json`.

## Evaluation dimensions
Use timestamped listening evidence when audio is available. Do not accept the first render by default.
- Lyric adherence: were words followed closely enough?
- Section adherence: did structure tags produce useful form?
- Hook impact: is there a memorable chorus/hook/post-chorus?
- Vocal identity: does the voice match the planned persona?
- Production fit: does the sound match the prompt and album DNA?
- Distinction: does it avoid sounding like adjacent tracks?
- Energy map: does the song build/release as intended?
- Creative value: does it contain a non-obvious musical or lyrical moment?
- Appeal: would the target listener replay/save it?
- Artifact risk: hiss, warble, bad transitions, unnatural phrasing, awkward lyric setting, mushy low end, harsh high end.

## JSON schema

```json
{
  "track_number": 1,
  "candidate_id": "A_on_brief",
  "keep_decision": "KEEP|REGENERATE|REVISE_PROMPT|REVISE_LYRICS|CUT_TRACK",
  "lyric_adherence": 0,
  "section_adherence": 0,
  "hook_impact": 0,
  "vocal_identity": 0,
  "production_fit": 0,
  "album_fit": 0,
  "adjacent_contrast": 0,
  "appeal_score": 0,
  "creative_value_score": 0,
  "artifact_risk": "low|medium|high",
  "specific_failures": [],
  "best_moments": [],
  "recommended_action": "..."
}
```
