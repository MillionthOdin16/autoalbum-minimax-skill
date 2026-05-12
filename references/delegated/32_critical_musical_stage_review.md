# Delegated: Critical Musical Stage Review

## Task
At the end of the current pipeline stage, run the critical musical analyst review before moving to the next stage.

## Read
- `references/critics/critical_musical_analyst_protocol.md`
- `references/schemas/critic_stage_review.schema.json`
- current project `state.json`
- current project `project_manifest.json`
- artifacts produced in the current stage
- relevant style, MiniMax, songcraft, and architecture references for the stage

## Output
Write:

```text
<project_slug>/reviews/critic_comments/phase_XX_<stage_slug>.md
```

If machine-readable output is useful, also write:

```text
<project_slug>/reviews/critic_comments/phase_XX_<stage_slug>.json
```

and validate the JSON against `references/schemas/critic_stage_review.schema.json`.

Append or update:

```text
<project_slug>/reviews/critic_comments/index.md
<project_slug>/state.json
<project_slug>/project_manifest.json
```

## Required review sections
1. Stage under review
2. Artifacts inspected
3. What the stage is trying to accomplish
4. Musical value of the stage
5. Main strengths
6. Harsh criticism / likely quality failures
7. Technical/API risks
8. Songwriting/production/music-theory risks
9. Style-fidelity risks
10. Album-cohesion risks
11. Required fixes before advancing
12. Optional improvements
13. Decision: PASS, PASS_WITH_RECORDED_RISKS, REPAIR_BEFORE_ADVANCING, or FAIL
14. State update required

## Critic rules
- Be blunt. Do not protect the current artifacts from criticism.
- Do not allow a stage to pass because it is elaborate; only pass if it improves the record.
- Identify whether each weakness is a concept problem, song problem, style problem, prompt problem, API problem, render problem, or sequence problem.
- If a BLOCKER exists, write it as a blocking issue in `state.json`.
- If a stage passes with risks, record the risks and revisit them in later phases.

## Common failure modes to hunt
- Generic style language
- Artist/style blending into indistinguishable mush
- Lyrics that read well but do not sing well
- Hooks without repeat value
- Overwritten verses
- Paper tracklists that will collapse after audio exists
- Prompt overload
- Valid JSON but weak musical direction
- Clean-but-boring renders
- Weak closers
- Mid-album sag
- Unjustified interludes
- Unchecked render artifacts
- Final package without selected-audio provenance
