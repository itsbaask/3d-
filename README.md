# DOLA Shorts — World-Class Production Bundle

A reference-guided production brief for silent 30-second vertical 3D cartoon Shorts.

## Fixed production standard
- 30 seconds; portrait 9:16; request 1080x1920 where supported.
- Premium stylized 3D with readable acting, coherent physical comedy and a consistent desert world.
- No dialogue, voice-over, subtitles, captions, readable text, logos or watermarks.
- One visual goal, logical escalation, surprising reversal, strong payoff and loop-friendly ending.
- Actual character/world reference images are bundled. Attach them as media inputs when the generation tool supports them.

## Start here
1. Read `SKILL.md` for the production workflow and hard constraints.
2. Read `references/prompt_guide.md` to write the final generation prompt.
3. Read `references/STORY_BIBLE.md` for style, character protection, continuity and silent-comedy rules.
4. Use `EPISODE_TEMPLATE.md` to plan a single gag.
5. Run the static preflight: `python scripts/quality_gate.py`.
6. Build and validate the ZIP: `python scripts/build_bundle.py`.

## Reference assets
- `references/ZUZO_MASTER.png`
- `references/MAKRON_MASTER.png`
- `references/QARQOOSH_MASTER.png`
- `references/SHAQLAB_MASTER.png`
- `references/CHICKEN_FAMILY_MASTER.png`
- `references/DESERT_WORLD_MASTER.png`

The images are included in the ZIP. A filename in a text prompt does not attach the image to a video model; supply the actual media through the supported interface. If the tool cannot accept images, disclose that limitation.

## What the quality gate does
It checks required references and configuration, and optionally checks a finished prompt for required constraints and timecodes. It cannot render video, inspect pixels or certify animation quality. Human/render review is still required.

## Build ZIP
Requires Python 3.8+:
```bash
python scripts/quality_gate.py
python scripts/build_bundle.py
python -m zipfile -t dola-shorts-30s-reference-bundle.zip
```
The builder prints file count, size and SHA-256 after validating the archive.

## Capability honesty
The package prepares prompts and performs static checks. It does not itself generate videos, guarantee model compliance, or turn a prompt into a rendered episode. A real video-generation tool must be available, and the actual output must be reviewed.
