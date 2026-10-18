#!/usr/bin/env python3
"""Static preflight checks for a DOLA Shorts prompt and its local reference bundle.

This is not a video renderer and cannot judge actual animation quality. It checks
that required files/configuration exist and that a supplied prompt includes key
production constraints and all timeline anchors.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_REFERENCES = [
    "references/ZUZO_MASTER.png",
    "references/MAKRON_MASTER.png",
    "references/QARQOOSH_MASTER.png",
    "references/SHAQLAB_MASTER.png",
    "references/CHICKEN_FAMILY_MASTER.png",
    "references/DESERT_WORLD_MASTER.png",
]
REQUIRED_TIMECODES = ["0-1", "1-3", "3-7", "7-13", "13-19", "19-24", "24-28", "28-30"]
REQUIRED_TERMS = ["9:16", "30-second", "no dialogue", "no", "loop"]

def check_bundle():
    errors = []
    for path in REQUIRED_REFERENCES:
        p = ROOT / path
        if not p.is_file():
            errors.append(f"Missing reference: {path}")
        elif p.stat().st_size < 1024:
            errors.append(f"Reference unexpectedly small: {path}")
    config_path = ROOT / "skill.json"
    if not config_path.is_file():
        errors.append("Missing skill.json")
    else:
        try:
            cfg = json.loads(config_path.read_text(encoding="utf-8"))
            defaults = cfg["defaults"]
            if defaults.get("duration_seconds") != 30:
                errors.append("Config duration_seconds must equal 30")
            if defaults.get("aspect_ratio") != "9:16":
                errors.append("Config aspect_ratio must equal 9:16")
            if defaults.get("dialogue") is not False or defaults.get("on_screen_text") is not False:
                errors.append("Dialogue and on-screen text must both be disabled")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"Invalid skill.json: {exc}")
    return errors

def check_prompt(path: Path):
    text = path.read_text(encoding="utf-8").lower()
    errors = []
    for token in REQUIRED_TERMS:
        if token not in text:
            errors.append(f"Prompt is missing required constraint/term: {token}")
    for code in REQUIRED_TIMECODES:
        if code not in text:
            errors.append(f"Prompt is missing timeline anchor {code}")
    for phrase in ("voice-over", "captions", "subtitles", "watermark", "reference"):
        if phrase not in text:
            errors.append(f"Prompt is missing constraint/topic: {phrase}")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", type=Path, help="Optional text file containing a finished generation prompt")
    args = parser.parse_args()
    errors = check_bundle()
    if args.prompt:
        if not args.prompt.is_file():
            errors.append(f"Prompt file not found: {args.prompt}")
        else:
            errors.extend(check_prompt(args.prompt))
    if errors:
        print("PREFLIGHT: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PREFLIGHT: PASS")
    print("Verified: config and six reference files.")
    if args.prompt:
        print("Verified: required prompt constraints and time-coded beats.")
    print("Note: this is a static preflight, not a visual render-quality assessment.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
