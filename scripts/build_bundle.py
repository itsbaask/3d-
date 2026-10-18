#!/usr/bin/env python3
"""Build a portable DOLA Shorts ZIP with reference images and validate it."""
from __future__ import annotations
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dola-shorts-30s-reference-bundle.zip"
REQUIRED = [
    "README.md", "SKILL.md", "skill.json", "EPISODE_TEMPLATE.md",
    "references/prompt_guide.md", "scripts/pipeline_tracker.py",
    "references/ZUZO_MASTER.png", "references/MAKRON_MASTER.png",
    "references/QARQOOSH_MASTER.png", "references/SHAQLAB_MASTER.png",
    "references/CHICKEN_FAMILY_MASTER.png", "references/DESERT_WORLD_MASTER.png",
]

def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()
    ]
    if missing:
        print("Missing required bundle files: " + ", ".join(missing), file=sys.stderr)
        return 2
    config = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
    defaults = config.get("defaults", {})
    if defaults.get("duration_seconds") != 30 or defaults.get("aspect_ratio") != "9:16":
        raise SystemExit("Config validation failed: expected 30 seconds and 9:16")
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for relative in REQUIRED:
            zf.write(ROOT / relative, arcname="dola-shorts-30s/" + relative)
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC validation failed: {bad}")
        names = set(zf.namelist())
        if len(names) != len(REQUIRED):
            raise SystemExit("ZIP contains duplicate or missing paths")
        for path in REQUIRED:
            if "dola-shorts-30s/" + path not in names:
                raise SystemExit(f"ZIP entry missing: {path}")
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Built: {OUTPUT.name}")
    print(f"Entries: {len(REQUIRED)} (including six reference images)")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    print(f"SHA-256: {digest}")
    print("Validation: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
