# Agent Execution Playbook

## Operating principle
A user should be able to say “make an album about X in Y style” and the agent should know what to do without exposing the internal machinery.

## Execution loop

```text
1. Intake: identify scope, output goal, style/reference request, supplied materials, and assumptions.
2. Configure: write project_config.json.
3. Resolve style: use catalog and refresh if currentness matters.
4. Build foundation: thesis, sound, voice, motifs, constraints.
5. Plan: skeleton tracklist or single-track architecture.
6. Style cards: one per track.
7. Refine plan: use style cards to revise arc, energy, transitions, hook index.
8. Write lyrics: song-first, singable, tagged for MiniMax.
9. Evaluate songcraft.
10. Compile MiniMax packet.
11. Audit API parameters.
12. Generate variants.
13. Export payloads/commands.
14. Render or prepare for render depending on environment.
15. Review candidates.
16. Regenerate, cut, or resequence.
17. Final A&R and release package.
```

## Efficiency rules
- Do not run full album-only checks for single-track projects.
- Do not generate final release materials before selected audio exists unless the output goal is release planning.
- Do not make every track a lead single; assign roles.
- Do not create more variants than the decision warrants; lead singles need more, interludes need fewer.
- Do not refresh current catalogs for evergreen references unless the user asks for current trends.

## Quality escalation
Escalate when:
- style card score < 8,
- style request is strict and fingerprint lacks differentiators,
- lyrics are good poetry but poor song lyrics,
- prompt is under-specific or overstuffed,
- adjacent tracks blur together,
- MiniMax render follows style but loses songcraft,
- MiniMax render has a great hook but fails album role.
