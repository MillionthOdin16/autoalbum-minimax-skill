# Delegated: Style Catalog QA and Refresh

## Task
Review and refresh the style catalog for the active project before strict style generation.

## Read
- `references/style_catalog/style_catalog_governance.md`
- `references/quality/style_catalog_qa_checklist.md`
- relevant genre templates
- relevant artist profiles
- relevant song fingerprints
- current source index for the genre, e.g. `references/style_catalog/rap_current/current_rap_source_index.md`
- web/current research notes if available

## Procedure
1. Identify which profiles will be used by the project.
2. Check each profile for required fields.
3. Check whether the profile has currentness metadata.
4. Check adjacent-style differentiators.
5. Check MiniMax prompt capsule usefulness.
6. Check whether the profile contains enough drum/bass/vocal/hook controls.
7. Add refresh notes when current chart or release signals have changed.
8. Produce missing profile addendum if needed.

## Output
Write `style_catalog_outputs/catalog_qa_report.md`.

Return:

```json
{
  "profiles_reviewed": [],
  "profiles_passed": [],
  "profiles_needing_refinement": [],
  "new_profiles_recommended": [],
  "style_catalog_ready": false
}
```

Do not proceed with strictness 4-5 requests if the required profile lacks non-confusion controls.
