---
name: dola-shorts-30s
description: "DOLA Shorts: reference-guided 30-second silent 3D cartoon Shorts. Trigger: ابدأ الحلقة."
---

# DOLA Shorts — 30-second reference-locked episode

## Output requirements
- Target exactly 30 seconds, portrait 9:16 (1080x1920 when supported).
- Polished original 3D cartoon, expressive physical comedy, consistent desert world.
- No spoken dialogue, voice-over, subtitles, captions, title cards, logos, watermarks, or readable text.
- Nonverbal sound effects only if audio is supported.
- One clear visual gag with cause-and-effect, escalating reversal, payoff, and a final image that echoes the opening for a loop.
- Never claim a video exists unless the generation tool returns a usable result.

## Mandatory visual references
Pass the actual images as media inputs when the video tool supports them. Text filenames alone are not image inputs.
- `references/ZUZO_MASTER.png` — Zuzo identity.
- `references/MAKRON_MASTER.png` — Makron identity.
- `references/QARQOOSH_MASTER.png` — Qarqoosh identity.
- `references/SHAQLAB_MASTER.png` — Shaqlab identity.
- `references/CHICKEN_FAMILY_MASTER.png` — chicken family identity.
- `references/DESERT_WORLD_MASTER.png` — desert environment and visual style.

Preserve reference identity, proportions, colors, materials, clothing/accessories and distinctive details. Do not invent replacement designs. If actual media cannot be attached, disclose that limitation rather than claiming reference fidelity.

## Episode timeline — 30 seconds total
- 0–3s: immediate visual hook.
- 3–8s: establish one simple silent goal and readable staging.
- 8–16s: first physical-comedy attempt fails.
- 16–23s: escalation or surprising reversal.
- 23–28s: strong, harmless slapstick payoff.
- 28–30s: reaction/composition echoes the opening for a loop.
Use clean English in the generation prompt, mobile-friendly 9:16 framing, readable silhouettes, consistent props and screen direction, and no unnecessary montage.

## Tool use and delivery
Use only a video-generation tool actually available in the current environment. Prefer reference-guided/image-to-video when actual media can be passed. Request duration 30 and ratio 9:16 when supported. If rejected, report the real tool limit; use segment/extension only if the capability actually exists. Do not invent tools, request an API key, or call an external video API. Retry transient failures only when supported.

Before delivery, verify the output link, actual duration, aspect ratio, and whether reference images were passed. The pipeline tracker is bookkeeping only; it does not generate or validate videos.
