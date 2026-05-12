# Project Root Organization

## Purpose
Every AutoAlbum run must be contained in a single top-level project folder named for the specific work being created. This keeps multiple albums, singles, EPs, cover projects, and revision projects isolated, auditable, resumable, and easy for the user to locate.

## Rule
Never write project artifacts into the skill reference folder. Never use a generic project root such as `autoalbum-full/` for active work. Use:

```text
<project_slug>/
```

Examples:

```text
midnight-paranoia/
velvet-afterparty-ep/
cartier-tears-single/
```

## Naming
`project_slug` must be stable for the lifetime of the project.

Slug rules:
- lowercase
- words separated by hyphens
- no spaces
- no punctuation except hyphens
- avoid dates unless needed for disambiguation
- do not rename after renders have been created unless all paths are migrated and state is updated

## Benefits
- Prevents unrelated project artifacts from mixing.
- Makes state recovery possible.
- Lets the user zip or share one folder.
- Keeps generated audio, prompts, reviews, and release files together.
- Makes final release provenance auditable.

## Minimum project root
At project creation, create:

```text
<project_slug>/
  project_manifest.json
  state.json
  intent_intake.json
  project_config.json
  seed.txt
  source_notes.md
```

Do not begin foundation, style, track planning, lyrics, or MiniMax packet compilation until the project root and initial state exist.
