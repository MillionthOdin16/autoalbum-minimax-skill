# Delegated Task: Musical Knowledge Bootstrap Check

## Objective
Before executing a creative or evaluative phase, identify the exact musical knowledge the agent needs and confirm the relevant training references were read.

## Read
- `references/agent_training/README.md`
- `references/agent_training/musical_expertise_bootcamp.md`
- `references/agent_training/stage_operator_manual.md`
- stage-specific training references listed in the README
- the delegated prompt for the current phase

## Process
1. Name the current phase.
2. List the musical decisions required in this phase.
3. List the reference files that supply the missing knowledge.
4. Extract the non-negotiable checklist for this phase.
5. Identify the top three likely non-expert failure modes.
6. State the pass/fail criteria.

## Output
Write to:

```text
<project_slug>/reviews/knowledge_checks/phase_XX_<phase_slug>.json
<project_slug>/reviews/knowledge_checks/phase_XX_<phase_slug>.md
```

JSON must follow `references/schemas/knowledge_dependency_check.schema.json`.

## Rule
If the agent cannot identify the musical mechanisms required for the phase, it must not proceed. It must read the relevant training reference and rerun the check.
