# Style Fusion Matrix

Use this when the user requests multiple styles/artists or when album cohesion requires one shared base with different track deltas.

## Default blend ratios

```json
{
  "single_track_two_styles": "70/30",
  "single_track_three_styles": "60/25/15",
  "album_base_plus_track_delta": "60 album DNA / 30 track style / 10 surprise",
  "artist_plus_genre": "55 artist fingerprint / 35 genre mechanics / 10 album DNA",
  "specific_song_plus_album": "60 song fingerprint / 30 album DNA / 10 track function"
}
```

## Compatible blends

| Primary | Compatible secondary | Result |
|---|---|---|
| Memphis crunk-trap | modern trap / horrorcore / phonk | dark chant-heavy club rap |
| Emo rap | pop punk / alt-rock / melodic trap | guitar-driven melodic trap |
| Conscious rap | jazz rap / West Coast / neo-soul | narrative, musical hip-hop |
| Trap | R&B / pop / rage / drill | modern streaming rap variants |
| Alt-R&B | indie pop / trap soul / neo-soul | atmospheric intimate R&B |
| Reggaeton | Latin trap / dancehall / pop | global urbano single |
| Afrobeats | amapiano / R&B / pop | warm syncopated dance-pop |
| House | pop / disco / R&B | club-pop single |
| Techno | industrial / dark pop / synthwave | hypnotic dark electronic track |
| Country | pop / rock / folk | contemporary country-pop |
| Pop punk | emo rap / alt-pop / rock | high-replay angst anthem |

## Risky blends

| Blend | Risk | Repair |
|---|---|---|
| Drill + country | rhythm and vocal posture clash | make one dominant; use the other as texture only |
| Boom bap + hyperpop | mix aesthetic and vocal treatment clash | keep boom-bap drums, use hyperpop synth/processing only |
| Amapiano + metal | groove and guitar density compete | use amapiano log drum as low-end motif under restrained guitars |
| Minimal dark R&B + maximal EDM | emotional intimacy can disappear | put EDM only in final chorus/drop, keep verses intimate |
| Rage rap + singer-songwriter folk | high-energy synths overwhelm storytelling | use rage energy for one climactic section only |

## Fusion prompt recipe

```text
Base the track primarily in {primary_style}. Add {secondary_style} only through {specific elements}. Keep the album DNA in {shared traits}. Do not let {risk} dominate.
```

Example:

```text
Base the track primarily in dark Memphis crunk-trap. Add emo-rap only through a sung melodic chorus and guitar-like minor-key lead, while keeping the drums cowbell-heavy, chantable, and bass-forward.
```
