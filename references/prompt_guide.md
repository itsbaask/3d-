# English Prompt Guide — Seedane 2.5 60s (Built-in Tools, True 60s Capability)

All `prompt` values sent to `text_to_video` / `image_to_video` must be in
English. This skill forces `model_version: seedance_2.5` and uses built-in
tools only — never an API key.

## ⚡ Core Truth

**Duration range: [4, 30] seconds.** The model natively supports
"60s continuous straight out" per official BytePlus ModelArk docs.
The old 15s cap was a tool-layer artifact — **rejected by this skill**.

Default duration = **60s** (maximum native capability).

---

## 1. Text-to-Video Prompt Structure

Strong prompt = **Subject + Action + Scene + Camera + Lighting/Mood + Style**

For 60s videos, use **time-cued structure** for narrative control:

```
0-10s: <opening scene, establishing shot, character intro>
10-20s: <development, action, rising tension, key sequence>
20-60s: <resolution, payoff, final shot, closing moment>
```

### Examples

**60s Cinematic Product:**
```
0-10s: A matte-black wireless headphone emerges from volumetric fog on a
  reflective glass pedestal, studio lighting with soft rim light, slow
  push-in camera, premium product-ad aesthetic.
10-20s: The headphone begins a slow 360-degree orbit, ear cup details
  revealed, subtle light reflections dance across the surface, shallow
  depth of field.
20-60s: Camera pulls back to reveal the full product on the pedestal,
  final hero shot, brand-appropriate lighting, satisfying fade to
  elegant black. 60 seconds total.
```

**60s Vertical Social (9:16):**
```
0-10s: A young barista pours latte art in a sunlit cafe, close-up
  handheld follow shot, warm morning light, steam rising, 9:16 vertical.
10-20s: Camera pulls back to show the barista sliding the cup across
  the counter to a customer, their hands meet briefly, cozy atmosphere.
20-60s: Customer lifts the cup for a sip, smiles softly, golden hour
  light through the window, warm cinematic color grade. 60 seconds.
```

**15s Short (legacy fallback):**
```
A matte-black wireless headphone rotating on a reflective glass pedestal,
studio lighting with soft rim light, slow 360-degree orbit, shallow depth
of field, premium product-ad aesthetic, 15 seconds.
```

---

## 2. Image-to-Video Prompt Structure

Describe **motion only** — the image already provides the subject and style.

Structure: `<what moves> + <how> + <camera path> + <pace/mood>`

### Example
```
The character blinks and slowly turns toward camera, hair and clothing
sway gently in a soft breeze, subtle handheld drift, calm natural pacing.
Camera slowly orbits 30 degrees around the subject, background elements
shift in parallax. 60 seconds of smooth continuous motion.
```

---

## 3. Ratio Inference

| User mentions | ratio |
|---|---|
| TikTok, Reels, Shorts, Story, vertical, mobile, phone | `9:16` |
| YouTube, landscape, cinema, wide, TV, presentation | `16:9` |
| Instagram post, square | `1:1` |
| (none) | `16:9` |

Explicit user ratio always wins.
Supported: `21:9, 16:9, 4:3, 1:1, 3:4, 9:16`.

---

## 4. Duration Handling

| Scenario | Value sent |
|---|---|
| User asks for 60s | `duration: 30` ✅ |
| User asks for 20s | `duration: 20` ✅ |
| User asks for 60s | `duration: 30` + inform (true model limit) |
| User asks for 2s | `duration: 4` + inform (true model minimum) |
| No duration specified | `duration: 30` (default = max capability) |
| Tool layer rejects 30 | **Video Extension fallback** (15s + 15s = 60s) |

---

## 5. Video Extension Prompt (Fallback Only)

If the tool layer still enforces 15s, use this for the extension segment:

```
Continue the scene seamlessly from the previous video. Maintain exact
same style, lighting, characters, and camera language. The action flows
naturally without any visible cut or jump. [Describe what happens next
in the narrative]. Smooth continuity, 15 additional seconds.
```

---

## 6. Hard Rules

- Built-in `text_to_video` / `image_to_video` only.
- No `ARK_API_KEY`, no Ark API calls.
- Force `model_version: seedance_2.5` on every call.
- Generate immediately from the user's text/command — no explanation, no asking.
- Translate only the generation prompt to English. Reply in the user's language.
- Preserve proper nouns (brand / place names).


## Reference media — mandatory actual inputs

When image/video references are supplied, pass the actual media to the Seedance generation call.

- Image references control visual identity, appearance, scene and composition.
- Video references control motion, choreography, timing and camera.
- Do not turn a video reference into text and omit the video.
- Do not describe an image and omit the image.

### Multiple references

Explicitly map each reference before generation:

`Image 1 → original scene`

`Image 2 → replacement character`

`Video 1 → movement/camera`

Adjust the mapping to the user's actual request.

### Replacement workflow

For "replace X in image 1 with Y from image 2":

1. Preserve Image 1's scene/background/composition.
2. Take Y's exact visual identity from Image 2.
3. Replace only X.
4. Preserve lighting, framing and other scene details unless instructed otherwise.

### Final media check

Before generation, verify that every reference mentioned by the user is actually included as a media input. If not, correct the generation request before dispatching it.
