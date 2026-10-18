#!/usr/bin/env python3
"""Build and validate both a portable project ZIP and a skill-installer ZIP."""
from __future__ import annotations
import hashlib
import json
import re
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dola-shorts-world-class-bundle.zip"
SKILL_OUTPUT = ROOT / "dola-shorts-world-class-skill.zip"
SKILL_NAME = "dola-shorts-world-class"
REQUIRED = [
    "README.md", "SKILL.md", "skill.json", "EPISODE_TEMPLATE.md",
    "references/prompt_guide.md", "references/STORY_BIBLE.md",
    "scripts/pipeline_tracker.py", "scripts/quality_gate.py", "scripts/build_bundle.py",
    "references/ZUZO_MASTER.png", "references/MAKRON_MASTER.png",
    "references/QARQOOSH_MASTER.png", "references/SHAQLAB_MASTER.png",
    "references/CHICKEN_FAMILY_MASTER.png", "references/DESERT_WORLD_MASTER.png",
]
SKILL_FILES = [
    "SKILL.md", "EPISODE_TEMPLATE.md",
    "references/prompt_guide.md", "references/STORY_BIBLE.md",
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

def write_zip(output: Path, files: list[str], prefix: str = ""):
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for relative in files:
            zf.write(ROOT / relative, arcname=f"{prefix}{relative}")
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC test failed: {bad}")
        names = set(zf.namelist())
        expected = {f"{prefix}{p}" for p in files}
        if names != expected:
            raise SystemExit(f"ZIP entries mismatch: expected {len(expected)}, got {len(names)}")

def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        print("Missing required files: " + ", ".join(missing), file=sys.stderr)
        return 2
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", skill_text, re.S)
    if not match:
        raise SystemExit("SKILL.md must start with YAML frontmatter delimited by ---")
    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", frontmatter, re.M)
    description_match = re.search(r"^description:\s*.+$", frontmatter, re.M)
    if not name_match or name_match.group(1) != SKILL_NAME or not description_match:
        raise SystemExit("SKILL.md frontmatter must define the matching name and a description")
    cfg = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
    defaults = cfg.get("defaults", {})
    if cfg.get("name") != SKILL_NAME:
        raise SystemExit("skill.json name must match SKILL.md frontmatter")
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
    write_zip(OUTPUT, REQUIRED)
    # Some skill installers expect the skill folder itself at the archive root;
    # others expect a single named directory containing SKILL.md. This archive
    # uses the latter layout and omits project-only metadata/scripts.
    write_zip(SKILL_OUTPUT, SKILL_FILES, prefix=f"{SKILL_NAME}/")
    for path in (OUTPUT, SKILL_OUTPUT):
        print(f"Built: {path.name}")
        print(f"Entries: {len(zipfile.ZipFile(path).namelist())}")
        print(f"Size: {path.stat().st_size} bytes")
        print(f"SHA-256: {hashlib.sha256(path.read_bytes()).hexdigest()}")
    print("ZIP integrity/config/frontmatter/reference checks: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
