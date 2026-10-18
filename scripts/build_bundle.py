#!/usr/bin/env python3
"""Build and validate a portable DOLA Shorts ZIP with its real reference images."""
from __future__ import annotations
import hashlib
import json
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dola-shorts-world-class-bundle.zip"
REQUIRED = [
    "README.md", "SKILL.md", "skill.json", "EPISODE_TEMPLATE.md",
    "references/prompt_guide.md", "references/STORY_BIBLE.md",
    "scripts/pipeline_tracker.py", "scripts/quality_gate.py", "scripts/build_bundle.py",
    "references/ZUZO_MASTER.png", "references/MAKRON_MASTER.png",
    "references/QARQOOSH_MASTER.png", "references/SHAQLAB_MASTER.png",
    "references/CHICKEN_FAMILY_MASTER.png", "references/DESERT_WORLD_MASTER.png",
]

def png_dimensions(path: Path):
    with path.open("rb") as f:
        header = f.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"Not a valid PNG header: {path}")
    return struct.unpack(">II", header[16:24])

def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        print("Missing required files: " + ", ".join(missing), file=sys.stderr)
        return 2
    cfg = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
    defaults = cfg.get("defaults", {})
    if defaults.get("duration_seconds") != 30 or defaults.get("aspect_ratio") != "9:16":
        raise SystemExit("Config must target 30 seconds and 9:16")
    if defaults.get("dialogue") is not False or defaults.get("on_screen_text") is not False:
        raise SystemExit("Config must disable dialogue and on-screen text")
    print("Reference image dimensions:")
    for name in REQUIRED:
        if name.endswith(".png"):
            path = ROOT / name
            if path.stat().st_size < 1024:
                raise SystemExit(f"Reference unexpectedly small: {name}")
            width, height = png_dimensions(path)
            print(f"  {name}: {width}x{height} ({path.stat().st_size} bytes)")
    # The builder does not include its own generated ZIP; it includes this script as source.
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for relative in REQUIRED:
            zf.write(ROOT / relative, arcname=relative)
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC test failed: {bad}")
        names = set(zf.namelist())
        if len(names) != len(REQUIRED):
            raise SystemExit("ZIP has duplicate or missing entries")
        for relative in REQUIRED:
            if relative not in names:
                raise SystemExit(f"ZIP entry missing: {relative}")
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Built: {OUTPUT.name}")
    print(f"Entries: {len(REQUIRED)}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")
    print(f"SHA-256: {digest}")
    print("ZIP integrity/config/reference checks: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
