# Delegated: Validate User Story Fit

## Task
Confirm that the current project artifacts satisfy the original user story.

## Read
- intent_intake.json
- project_config.json
- references/quality/user_story_validation.md
- references/quality/fragility_register.md
- all relevant project artifacts

## Output
Write `reviews/user_story_fit_report.md`.

## Required sections
1. Original user story
2. Inferred scope and output goal
3. Assumptions made
4. Artifacts created
5. Missing artifacts
6. Quality gates passed
7. User-story-specific risks
8. Required fixes
9. Next action

## Pass/fail
Fail if the project delivers a different scope than the user requested, hides assumptions, loses style references, or marks a project complete before its output_goal is actually satisfied.


## V23 mandatory verification

Before writing a pass decision, run or verify results from:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py validate <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-freshness <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-quotes <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-style <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-tournaments <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py lint-prompt <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-variants <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py reconcile-state <project_slug>
```

Also write:
- `reviews/completion_adversarial_audit.md`
- `reviews/completion_verifier_review.json`

Fail if any required verifier or controller check fails. Do not summarize completion positively around unresolved blockers.
