# DOLA Shorts — Premium Prompt & Direction Guide

This guide turns a story idea into one tightly directed, silent 30-second cartoon. Use concrete visual actions and protect character identity above visual complexity.

## Locked brief
- 30 seconds; portrait 9:16; request 1080x1920 where supported.
- Polished stylized 3D, appealing silhouettes, expressive nonverbal acting, desert-world continuity.
- No speech, voice-over, lyrics, captions, subtitles, readable text, generated logos or title cards. If an approved watermark asset is supplied, add it only as a fixed bottom-right screen-space overlay in post-production; never ask the video model to draw it.
- Visual story must be understandable muted. Sound effects/music are optional and only if supported.
- One objective, one main gag, logical escalation, clear payoff, loopable final beat.

## Actual reference media mapping
Attach the image files as media inputs; text names and URLs in a prompt do not by themselves attach images.
1. `ZUZO_MASTER.png` — Zuzo.
2. `MAKRON_MASTER.png` — Makron.
3. `QARQOOSH_MASTER.png` — Qarqoosh.
4. `SHAQLAB_MASTER.png` — Shaqlab.
5. `CHICKEN_FAMILY_MASTER.png` — chicken family.
6. `DESERT_WORLD_MASTER.png` — world design, palette, terrain, props.
Preserve exact identity, proportions, colors, materials, face and signature details. Attach only characters that actually appear plus the world reference if input slots are limited; disclose any omitted reference.

## Non-negotiable continuity and watermark lock
- **Watermark:** use the supplied approved watermark file only. Composite it after rendering as a separate overlay anchored to the bottom-right of the final 9:16 canvas. Lock its x/y position, scale, opacity and edge margin for every frame. It must not track the camera or scene, move, wobble, rotate, pulse, resize, vanish, duplicate or change appearance. Check frames from the beginning, middle and end. If no watermark asset is provided, do not fabricate one; request it or flag it as missing.
- **Element continuity:** maintain a shot-by-shot continuity ledger. Lock character identity, face, proportions, palette, materials, accessories, object count, prop geometry/state, positions, orientation, hand occupancy, screen direction, shadows, light direction and background. Only planned visible actions may change a state; that state must persist across subsequent frames/cuts. No unexplained resets, swaps, morphs, disappearances, new objects or design drift.
- **Prefer continuity over spectacle:** if the model cannot keep an element stable during a complex camera move or cut, simplify the staging, use a longer continuous shot, or repair the segment in post. Do not accept the flawed render.
- **Quality gate:** review the rendered video itself at frame level and across transitions. Reject watermark drift, identity drift, flicker, texture crawl, deformation, prop teleportation, inconsistent lighting, generated text, weak composition or unfinished-looking animation. Fix and re-check; a prompt alone is not proof of quality.

## Story test before prompt
Answer in one short line each:
- Want: what does the lead want right now?
- Obstacle: what blocks it visually?
- Plan: what action do they try?
- Escalation: how does the next attempt make the problem worse?
- Reversal: what logical surprise turns the plan against them?
- Payoff: what image/action delivers the laugh?
- Loop: what framing/prop/motion from the opening returns at the end?
Reject ideas that need dialogue, lore, several locations or more than one main gag.

## Timing: total exactly 30 seconds
| Time | Purpose | Direction |
|---|---|---|
| 0–1s | Cold open | Start with action or a striking visual contradiction |
| 1–3s | Hook | Reveal the funny problem clearly |
| 3–7s | Goal | Establish goal, prop and spatial layout |
| 7–13s | Attempt | One clear plan fails |
| 13–19s | Escalation | Raise stakes by changing one variable |
| 19–24s | Reversal | A surprising but logical backfire |
| 24–28s | Payoff | Strong safe visual gag and readable reaction |
| 28–30s | Loop | Return to a matching visual or movement |

## Production-ready prompt template
```text
Create one coherent 30-second portrait 9:16 premium stylized 3D cartoon short.
Target 1080x1920 if supported. No intro, title, text, logo or watermark.

REFERENCE LOCK:
Use the attached image inputs as the authoritative visual references:
[map each attached image to its named character/world].
Preserve exact face, proportions, silhouette, colors, materials and signature details.
Do not redesign, merge, duplicate or morph characters. Keep the desert world consistent.

STORY:
[One sentence stating the lead's immediate visual goal and obstacle.]
Main prop: [one prop]. Active characters: [only necessary cast].

ACTION / TIMING:
0-1s: [start in motion; striking visual].
1-3s: [hook becomes unmistakable].
3-7s: [goal and geography].
7-13s: [first attempt and visible cause/effect].
13-19s: [escalation; one clear change].
19-24s: [logical reversal/backfire].
24-28s: [safe slapstick payoff and reaction].
28-30s: [pose/prop/motion/framing echoes the opening].

CAMERA & ANIMATION:
Portrait-safe composition; faces, hands and gag remain visible on a phone.
Establish geography before movement; preserve screen direction and prop continuity.
Use purposeful wide/medium/close shots, readable silhouettes, anticipation, contact,
follow-through and settle. Consistent lighting, grounded shadows, believable weight,
polished materials and restrained secondary motion.

NEGATIVE CONSTRAINTS:
No dialogue, voice-over, lyrics, captions, subtitles, readable text, or generated logos.
Do not generate a watermark inside the scene. Composite the supplied approved watermark afterward as a fixed screen-space overlay anchored bottom-right, identical position, scale, opacity and margin on every frame; never track camera or scene motion.
No character identity drift, face/eye changes, extra limbs, duplicate bodies, morphing,
flicker, texture crawl, floating props, foot sliding, teleporting, random camera shake,
unmotivated cuts, excessive blur or unreadable action. Family-friendly harmless slapstick.
The entire story must make sense with audio muted. End on a loop-friendly visual echo.
Total target duration 30 seconds, portrait 9:16.
```

## Mobile-first direction
- Keep the lead's eyes, hands and main prop in a central safe region.
- Ensure the gag still reads when the frame is small.
- Do not use wide empty establishing shots; begin close to the problem.
- Cut only when a new view makes cause/effect clearer.
- Use one main prop and no more than 1–3 active characters where possible.
- Do not let dust, motion blur, depth of field or camera movement obscure the gag.

## Quality review
Score 0–5 each: hook, mute readability, reference identity, physical acting, vertical composition, escalation/payoff, visual consistency, no text/logos, loop ending, audio support (if present). Aim for at least 40/50 and no critical failures. A good prompt is not proof of a good render.

## Delivery honesty
The guide does not generate video by itself. Return an actual rendered file/link only when the video tool provides one. State actual duration/ratio when known and disclose anything that could not be verified.


## Reference-first rule for every invented element
Before generating video, inventory every visible story element, including anything invented during story development: eggs, meals, insects, tools, containers, costume pieces, plants, crumbs, cracks, spills and other props/effects. Give each story-critical element a stable asset ID and create/approve its reference image first. Reference sheets must define exact silhouette, colors, material, markings, relative scale and relevant planned states. Attach the actual reference media to the generator; filenames alone do not count.

Track all assets in an asset registry and continuity ledger at every shot boundary. Freeze design attributes throughout the episode. Only an explicit visible story action may change an element's state, and that change persists (e.g. a cracked egg stays cracked; bitten food keeps the same bite; moved props stay where the action left them). No unexplained morphing, recoloring, size drift, substitutions, duplication, teleporting or state resets. Lock minor background clusters as defined stable layers; any incidental item that becomes part of the gag must become a tracked asset with its own reference. If an element has no approved reference or drifts from it, stop, create/approve the reference or repair the shot, then re-check before delivery.
