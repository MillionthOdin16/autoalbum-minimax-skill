# Delegated: Refine Style Profile

## Task

Given a genre, artist, song, scene, or fusion request, refine or create a high-fidelity style profile that can be used for MiniMax Music 2.6 generation.

## Read

- references/quality/style_catalog_qa_checklist.md
- references/style_catalog/rap_current/profile_quality_standards.md when rap-related
- references/style_catalog/style_profile.schema.json
- references/style_catalog/minimax_style_compiler.md
- references/api/minimax_prompting_and_style_control_playbook.md
- relevant existing style catalog files

## Output

Write or update the relevant style profile and produce a QA summary:

```text
style_id:
status: approved | needs_refinement
missing_fields:
adjacent_blur_risks:
minimax_prompt_capsule:
recommended_style_strictness:
currentness_metadata:
```

## Requirements

- Do not approve broad labels such as "trap" or "pop rap" for strictness 4-5 without concrete rhythmic, vocal, production, hook, and mix details.
- Always identify adjacent artists/styles that the profile must not collapse into.
- Always include a MiniMax prompt capsule between 500 and 1200 characters.
- Always include currentness metadata for current-pop/current-rap profiles.
