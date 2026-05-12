# Non-Rap Style Fidelity Rubric

Use this rubric when the project is pop, R&B, electronic, Latin/global, rock, country, folk, or hybrid. Do not score style fidelity by whether the prompt uses the right genre word. Score whether the musical controls are specific enough to generate that style.

## Scores

```text
9-10: unmistakable lane; rhythm, vocal, harmony, arrangement, and mix all match the requested style.
7-8: generally correct but one dimension is generic or weak.
5-6: broad genre fit but weak stylistic specificity.
3-4: label-level match only; likely generic output.
0-2: wrong style, contradictory controls, or missing core mechanics.
```

## Dimensions

1. **Tempo and groove mechanics** — Does the track use the correct pulse, swing, rhythm, or dance grammar?
2. **Drum/percussion grammar** — Are the drum choices/style-specific rather than generic?
3. **Bass behavior** — Does the low end behave like the requested style?
4. **Harmony/chord color** — Does harmonic language fit the style?
5. **Instrument palette** — Are instruments central to the style present and prioritized?
6. **Vocal delivery** — Does vocal posture, range, phrasing, and layering fit?
7. **Hook mechanics** — Does the hook work the way the style expects?
8. **Arrangement architecture** — Does the structure develop with genre-appropriate energy?
9. **Mix/space** — Does sonic space match the style?
10. **Adjacent-style differentiation** — Could this be confused with a nearby genre? If yes, identify the blur.

## Failure examples

```text
reggaeton without dembow
amapiano without log-drum behavior
neo-soul without harmonic color or live pocket
shoegaze without textural guitar/synth immersion
country without story turn or genre instrumentation
tech house with a pop-ballad verse/chorus architecture
```

## Required output
Write non-rap style fidelity notes into `<project_slug>/tracks/tr_NN/style_fidelity_eval.json` and fail the track if style score is below project threshold.
