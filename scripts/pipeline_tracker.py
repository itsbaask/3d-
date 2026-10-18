#!/usr/bin/env python3
"""Local bookkeeping for DOLA Shorts jobs; this script does not generate videos."""
from __future__ import annotations
import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path.home() / ".dola_shorts_pipeline.json"
LOG_FILE = Path.home() / ".dola_shorts_pipeline.log"
STATUSES = {"pending", "dispatched", "done", "failed", "retry", "needs_review"}
MIN_SECONDS, MAX_SECONDS = 4, 30

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def log(message):
    line = f"[{now_iso()}] {message}"
    print(line, flush=True)
    try:
        with LOG_FILE.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError:
        pass

def load_state():
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

def init_state():
    state = {"pipeline_id": f"dola_{int(time.time())}", "skill": "dola-shorts-world-class",
             "duration_range_seconds": [MIN_SECONDS, MAX_SECONDS], "created_at": now_iso(), "jobs": {}}
    save_state(state)
    log(f"initialized bookkeeping state at {STATE_FILE}")
    return 0

def enqueue(args):
    state = load_state()
    if not state:
        state = {"pipeline_id": f"dola_{int(time.time())}", "skill": "dola-shorts-world-class",
                 "duration_range_seconds": [MIN_SECONDS, MAX_SECONDS], "created_at": now_iso(), "jobs": {}}
    requested = int(args.duration)
    duration = min(MAX_SECONDS, max(MIN_SECONDS, requested))
    jid = f"job_{len(state['jobs']) + 1:03d}"
    state["jobs"][jid] = {
        "status": "pending", "created_at": now_iso(), "mode": args.mode,
        "duration_requested": requested, "duration_target": duration,
        "aspect_ratio": args.ratio, "prompt": args.prompt,
        "reference_files": args.reference or [], "attempts": 0,
        "render_url": None, "error": None
    }
    save_state(state)
    log(f"enqueued {jid}; requested={requested}s target={duration}s ratio={args.ratio}")
    print(f"Enqueued {jid}; target {duration}s, {args.ratio}.")
    print("Bookkeeping only: dispatch and render must be performed by an actual available video tool.")
    return 0

def update_job(args):
    state = load_state()
    job = state.get("jobs", {}).get(args.job_id)
    if not job:
        print(f"Job not found: {args.job_id}")
        return 1
    if args.status not in STATUSES:
        print("Invalid status. Choose: " + ", ".join(sorted(STATUSES)))
        return 2
    job["status"] = args.status
    job["updated_at"] = now_iso()
    if args.url is not None:
        job["render_url"] = args.url
    if args.error is not None:
        job["error"] = args.error
    if args.attempts is not None:
        job["attempts"] = args.attempts
    save_state(state)
    log(f"{args.job_id} -> {args.status}")
    return 0

def show_status():
    state = load_state()
    if not state:
        print("No pipeline state. Run: python scripts/pipeline_tracker.py init")
        return 0
    jobs = state.get("jobs", {})
    print(f"Pipeline: {state.get('pipeline_id')} | skill: {state.get('skill')}")
    print(f"Jobs: {len(jobs)}")
    for jid, job in jobs.items():
        print(f"- {jid}: {job.get('status')} | {job.get('duration_target')}s | {job.get('aspect_ratio')} | render={job.get('render_url') or 'not set'}")
    return 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="create a local bookkeeping state")
    add = sub.add_parser("enqueue", help="record a planned render")
    add.add_argument("--mode", choices=["text-to-video", "image-to-video"], default="image-to-video")
    add.add_argument("--prompt", required=True)
    add.add_argument("--ratio", choices=["9:16", "16:9", "1:1"], default="9:16")
    add.add_argument("--duration", type=int, default=30)
    add.add_argument("--reference", action="append", help="reference file path; repeat as needed")
    mark = sub.add_parser("mark", help="update bookkeeping status after external action")
    mark.add_argument("job_id")
    mark.add_argument("status", choices=sorted(STATUSES))
    mark.add_argument("--url")
    mark.add_argument("--error")
    mark.add_argument("--attempts", type=int)
    sub.add_parser("status", help="show local jobs")
    args = parser.parse_args()
    if args.command == "init":
        return init_state()
    if args.command == "enqueue":
        return enqueue(args)
    if args.command == "mark":
        return update_job(args)
    return show_status()

if __name__ == "__main__":
    raise SystemExit(main())
