---
name: dola-shorts-world-class
description: "Production system for premium 30-second, 9:16 silent 3D cartoon Shorts using the DOLA cast and six visual references. Trigger: ابدأ الحلقة."
---

# DOLA Shorts — World-Class Production System

## North-star
Make a short that is instantly readable on a phone, visually distinctive, emotionally clear without dialogue, and funny on first viewing with a rewarding loop on replay. The brief is a production standard, not a promise that any model will obey it perfectly. Inspect the actual render and disclose failures.

## Comedy-maximization lock — expressions, timing and sound
- Every episode must aim for exceptionally funny, immediately readable visual comedy, not merely cute motion. Build one clear gag with setup, anticipation, escalation, reversal and a strong payoff; each beat should be funnier or more surprising than the previous beat without becoming random.
- Direct highly readable, character-specific facial acting: suspicious side-eye, overconfident grin, tiny eye darts, delayed realization, exaggerated blink, cheek puff, jaw drop, frozen panic, smug relief and an expressive look to camera when appropriate. Push expressions for cartoon clarity while preserving each character's approved face design and identity.
- Specify the exact reaction and its timing in every shot: what the character sees, the micro-pause before understanding, the expression change, body recoil or freeze, and the payoff. Use anticipation, a held silence, a sudden reveal, reaction shots and precise comedic pauses; do not make every beat frantic.
- When audio is supported, use a deliberate layered sound-effects palette: elastic boings, squeaks, tiny footsteps, slide whistles, soft impacts, pops, rattles, comic thuds, stomach rumbles, exaggerated gasps, snorts and distinctive nonverbal character vocalizations. Match each sound to visible contact/action and time it precisely. No spoken words, narration or lyrics. Keep the joke understandable with sound muted; sound must enhance rather than carry the whole gag.
- Give each character a consistent sonic signature and reaction style across the episode and series. Do not randomly change pitch, vocal texture or sound identity between shots. Avoid generic constant music, sound clutter, painful volume spikes and unrelated stock effects; leave room for a perfectly timed pause.
- Escalate through cause and effect, not arbitrary chaos. The final payoff should be surprising but logically earned, emotionally legible and ideally loopable. Prefer a memorable reaction or reversal over extra gags that dilute the main joke.
- Comedy is never permission to break continuity: dirt, food bites, cracks, wet patches, displaced props and other visible consequences persist until a visible action changes them. Keep expressions exaggerated but character geometry and identity locked.
- Before approval, review the episode muted for visual joke clarity, then with audio for synchronization, distinctiveness, timing and mix. Reject flat reactions, unclear cause-and-effect, mistimed effects, repetitive expressions, random sound changes or a weak payoff; revise and re-review. These are direction and review gates, not a guarantee that a generative model will produce perfect comedy.

## Locked delivery specification
- Target duration: exactly 30 seconds; use 9:16 portrait. Request 1080x1920 where supported.
- Premium stylized 3D animation: intentional silhouettes, appealing shapes, polished materials, believable contact and weight, expressive faces, cinematic but readable lighting, clean composition.
- One central objective, one main gag, a clear cause-and-effect chain, escalation, reversal, payoff, and loopable last beat.
- No spoken dialogue, no voice-over, no lyrics, no captions/subtitles, no title cards, no generated logos, and no readable on-screen text. The only permitted on-screen brand mark is the supplied watermark overlay, if provided, composited in post-production as a fixed screen-space element at the bottom-right.
- WATERMARK LOCK (mandatory when a supplied watermark asset exists): anchor it to the bottom-right of the final 9:16 canvas with fixed pixel/normalized coordinates, fixed scale, opacity and margin for every frame. It must never follow the camera, characters, objects, scene perspective, lighting, or motion; never drift, wobble, resize, rotate, animate, disappear, duplicate, or be redrawn by the video model. Composite it after the video render as a separate overlay layer. Keep it inside the safe margin and unobtrusive but legible. If no approved watermark asset is supplied, ask for it or report that it cannot be applied; do not invent one.
- CONTINUITY LOCK (mandatory): every approved character, prop, costume/accessory, color, material, body/face proportion, environment feature, and damage/state must remain identical from shot to shot unless an explicit, planned story action changes it. A change must be motivated on-screen, persist afterward, and never reset between cuts. Track a continuity ledger for character positions/orientation, screen direction, which hand holds each prop, prop location/state, shadows, lighting direction, and background layout. No spontaneous redesign, morphing, substitution, duplication, disappearing/reappearing objects, or unexplained state changes. If the generator cannot preserve continuity across a cut, use a shorter continuous shot or repair the shot in post; do not accept the mismatch.
- Audio, if supported: carefully timed nonverbal Foley and restrained music only. The visual story must still work when muted.
- Family-friendly, safe slapstick. No graphic harm, cruelty, unsafe imitation, or frightening intensity beyond light cartoon surprise.
- No extra characters unless the gag needs them. Give every included character a clear reason to be in the scene.

## Mandatory reference package
Use actual image media, not merely filenames in text:
1. `references/ZUZO_MASTER.png` → Zuzo identity.
2. `references/MAKRON_MASTER.png` → Makron identity.
3. `references/QARQOOSH_MASTER.png` → Qarqoosh identity.
4. `references/SHAQLAB_MASTER.png` → Shaqlab identity.
5. `references/CHICKEN_FAMILY_MASTER.png` → chicken family identity.
6. `references/DESERT_WORLD_MASTER.png` → desert world, palette and environment.

Preserve each used character's head/body proportions, face, eyes, colors, silhouette, materials, clothing/accessories and signature features. Preserve the environment's design language, not just "a desert". Never merge, rename, recolor, redesign or clone characters accidentally. If the tool supports only a subset of reference images, attach the most relevant character refs plus the world ref and explicitly report the subset used. If no actual image input is possible, do not claim reference lock.


## Universal asset lock — every invented element is a reference asset
Before writing the final video-generation prompt or rendering any shot, enumerate **every visible element**, not just the named cast: all characters, creatures/insects, eggs, food, tools, containers, costumes/accessories, vehicles, plants, rocks, footprints, cracks, spills, crumbs, debris, and other story-critical background objects or effects.

For each unique or continuity-critical element:
1. Create and approve a dedicated reference image / asset sheet **before video generation**. For objects, show a clean readable view with the exact silhouette, geometry, colors, materials, markings, scale cues, and relevant states. For an egg, food item, or insect, define its exact appearance and size relative to a locked character/prop. For states that change during the story (whole/cracked egg, full/bitten food, intact/broken object), create explicit state references for the planned stages.
2. Assign a stable asset ID and a single authoritative reference. Maintain an asset registry containing asset ID, reference filename, description, scale, colors/materials, initial position/orientation, owner/holder, state at each timecode, and permitted planned changes.
3. Attach the actual reference images to the video-generation tool whenever it supports image references. A filename mentioned in text is not an attached image. If the tool has reference-slot limits, prioritize the lead characters, world, and every story-critical asset; split the work into compatible shots or use approved image-to-video/keyframe workflows. Report any asset that could not be reference-locked.
4. Freeze all unchanging design attributes for the entire episode. A planned state change must be shown on-screen and then persist: if an egg cracks, the crack pattern remains; if food is bitten, the bite shape remains; if an insect turns around, its identity and markings remain; if an object moves, it does not teleport back. No spontaneous redesign, recoloring, scale drift, substitutions, duplication, disappearance/reappearance, or state reset between cuts.
5. At each shot boundary, compare the outgoing frame and incoming frame against the asset registry and prior frame. If an element is newly introduced without a reference, stop and create/approve its reference before generating that shot. If a generated element deviates from its approved reference, reject and repair the shot; do not excuse it as model creativity.
6. For many tiny incidental elements that are not individually story-critical, lock them as a single defined set or background layer (e.g. a specific pile of crumbs or a fixed rock cluster) and keep that set stable. Any incidental element that becomes part of the gag must be promoted to a tracked asset with its own reference/state history.

### Mandatory pre-generation asset gate
Do not proceed to video generation until:
- The complete visible-element inventory is written.
- Every story-critical/invented element has an approved reference image and asset ID.
- State-change references are prepared for any object that changes visibly.
- The asset registry and shot-by-shot continuity ledger agree.
- The actual reference media can be attached to the chosen generator.
If image/reference creation or attachment is unavailable, state the limitation and prepare the reference-sheet prompts first; never claim the element was locked when it was not.

## Story design — pass before writing the prompt
Choose a premise that can be understood in one glance:
- **Want:** what does the protagonist want, physically and immediately?
- **Obstacle:** what simple visible thing blocks it?
- **Plan:** what action does the character choose?
- **Escalation:** why does the next attempt make the situation funnier or worse?
- **Reversal:** how does the plan backfire in a surprising but logical way?
- **Payoff:** what single image/action delivers the laugh?
- **Loop:** what visual, motion, framing or prop returns us naturally to the opening?

Prefer one main prop, one location, 1–3 active characters, and a maximum of 4 meaningful shot changes. Avoid unrelated gags, exposition, slow establishing shots, complex multi-character choreography and actions that need dialogue to explain.

## Exact 30-second timing
- 0.0–1.0s: begin in motion or show an intriguing visual contradiction; no logo or intro.
- 1.0–3.0s: make the immediate problem/hook unmistakable.
- 3.0–7.0s: reveal the simple goal and spatial relationships.
- 7.0–13.0s: first attempt; readable cause and effect.
- 13.0–19.0s: escalation; change one variable and raise the stakes.
- 19.0–24.0s: reversal; the audience understands why the plan backfires.
- 24.0–28.0s: strongest safe visual payoff and reaction.
- 28.0–30.0s: return to a matching pose, prop, framing or motion from the opening to encourage a seamless loop.

Do not add overlapping time ranges that make the total ambiguous. Make every beat distinct and keep screen direction and prop state continuous.

## Non-negotiable production gates
1. **Asset/identity lock:** use the supplied master references as authoritative; do not improvise alternative designs.
2. **Continuity ledger:** write down each visible character and prop's identity, color/material, screen position, orientation, hand/holder, and state for every shot. Carry each state into the next shot.
3. **Watermark compositing:** never rely on text-to-video generation to keep the watermark fixed. Add the approved watermark in post as a screen-space overlay, anchored bottom-right on the final canvas, constant position/size/opacity throughout all frames. Verify first, middle, last, and sampled frames for drift or occlusion.
4. **Render review:** inspect the actual rendered video, not just the prompt. Reject visible identity drift, prop discontinuity, flicker, deformation, unwanted text, watermark movement, inconsistent lighting, weak staging, or unfinished-looking frames. Repair and re-review before delivery.
5. **Honest delivery:** never claim “zero errors” unless every frame has actually been checked; report remaining limitations plainly.

## Cinematography and animation quality
- Compose for 9:16 mobile viewing; keep eyes, hands, key props and the cause of the gag in the center-safe area. Avoid cropping feet/hands during key actions.
- Establish geography before rapid movement. Keep screen direction consistent across cuts.
- Use wide/medium/close framing with purpose. The hook should read at thumbnail size; the payoff should remain legible on a small screen.
- Give actions anticipation, contact, follow-through, settle and a readable reaction. Preserve weight, balance, shadows and ground contact.
- Use controlled secondary motion (ears, feathers, clothing, dust, sand) rather than constant jitter.
- Maintain coherent light direction, shadow softness, material response, character scale and prop continuity.
- Avoid flicker, melting/morphing, extra limbs/fingers, face drift, eye drift, duplicated characters, texture crawl, floating objects, foot sliding, teleporting, impossible physics, random camera shake, excessive blur and overly busy backgrounds.
- Use depth of field sparingly; do not blur the gag or key face.
- Never sacrifice identity or action readability for a flashy camera move.

## Prompt construction
Write the final generation prompt in concise, production-ready English. It must specify:
1. Output format and hard constraints.
2. Reference image mapping and identity lock.
3. One-sentence premise and protagonist's visible goal.
4. Time-coded actions covering all 30 seconds.
5. Camera and blocking, including spatial continuity.
6. Animation/material/lighting quality.
7. Negative constraints: no dialogue/text/generated logos, no identity drift/artifacts; the supplied watermark is a fixed post-production overlay at bottom-right, not model-generated.
8. A loop ending that visually reconnects to the first frame.

Describe observable actions, not vague adjectives alone. Prefer "the jar tips, three dates roll toward the edge, Zuzo catches one, the other two trigger..." over "chaotic funny action". Keep the number of simultaneous moving subjects low. Do not request unsupported technical features as guaranteed.

## Generation workflow
1. **Concept gate:** write 3 distinct one-sentence premises internally; choose the one with clearest visual goal and strongest cause/effect, not the most complicated.
2. **Beat sheet:** map the chosen gag to the exact timeline above.
3. **Reference gate:** attach actual reference media supported by the tool; map each attachment.
4. **Prompt gate:** create one coherent prompt; state target 30s and 9:16.
5. **Generate:** use only a video tool actually available in the current environment. Never invent a tool, claim background work, or call an external API.
6. **Inspect:** if the environment exposes preview/metadata, check identity, duration, aspect ratio, text, visual defects, timing and ending. If inspection is unavailable, say what could not be verified.
7. **Repair:** if a defect is visible and editing/regen is supported, change the smallest possible set of instructions and retry within available limits. Do not silently change the story or character designs.
8. **Deliver:** return the actual rendered video link/file, actual duration/ratio if known, and a short honest quality note. A prompt, ZIP or source repository is not a rendered episode.

## Quality gate (score each 0–5)
- Hook readability within first 2 seconds.
- Goal and cause/effect understandable without sound.
- Character identity matches supplied references.
- Acting, contact, weight and timing feel intentional.
- Composition works in portrait on a phone.
- Escalation is logical and payoff is clear.
- Visual consistency: no obvious morphing, duplicate limbs, flicker or floating props.
- No visible text, subtitles, logos or watermark.
- Last 2 seconds connect to opening.
- Audio (if present) supports the action without speech.

Target: 40/50 minimum, with no critical failure. Critical failures: wrong/unstable lead identity, missing actual reference inputs while claiming they were used, duration/ratio materially wrong, visible text/logo, broken action continuity, or inaccessible output. Never describe a render as "world-class" merely because the prompt asked for it.

## Honesty and capability boundaries
- Actual media attachment is required to claim reference-guided generation.
- Ask for or use no API key; do not call an external video API.
- The tracker is bookkeeping only. It does not generate video, schedule background jobs, retry models or validate a render.
- The bundle builder validates package integrity and configuration, not the visual quality of a generated video.
- If a generation capability is unavailable, provide the prompt/beat sheet as preparation and state clearly that no video was rendered.
