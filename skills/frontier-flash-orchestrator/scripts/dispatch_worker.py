#!/usr/bin/env python3
"""
Worker Dispatcher for Frontier Flash Orchestrator in Antigravity.
Dispatches implementation task briefs to fast/free worker models via OpenCode or 9Router.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

DEFAULT_MODEL = "opencode/mimo-v2.6-flash-free"

def run_cmd(cmd: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout, proc.stderr

def main() -> int:
    parser = argparse.ArgumentParser(description="Dispatch task brief to OpenCode worker model")
    parser.add_argument("--brief", required=True, help="Path to the task-brief.md file")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Worker model slug (default: {DEFAULT_MODEL})")
    parser.add_argument("--cwd", default=".", help="Working directory for worker")
    parser.add_argument("--dry-run", action="store_true", help="Print dispatch plan without calling worker")
    args = parser.parse_args()

    repo_root = Path(args.cwd).resolve()
    brief_path = Path(args.brief).resolve()

    if not brief_path.exists():
        print(json.dumps({"status": "error", "message": f"Task brief file not found: {brief_path}"}, indent=2))
        return 1

    brief_content = brief_path.read_text(encoding="utf-8", errors="replace")

    # Check for opencode CLI
    opencode_bin = shutil.which("opencode") or shutil.which("opencode.cmd")
    if not opencode_bin:
        print(json.dumps({
            "status": "error",
            "message": "OpenCode CLI ('opencode') was not found in PATH. Please ensure it is installed globally."
        }, indent=2))
        return 1

    prompt = (
        f"You are the implementation worker for this project. "
        f"Please read the following task brief carefully and implement all requirements, "
        f"create/modify the required files, and run the specified verification command.\n\n"
        f"--- TASK BRIEF START ---\n{brief_content}\n--- TASK BRIEF END ---\n\n"
        f"Execute all code changes and run verification tests now. Report your final status when done."
    )

    if args.dry_run:
        print(json.dumps({
            "status": "dry-run",
            "model": args.model,
            "brief": str(brief_path),
            "opencode_bin": opencode_bin,
            "repo_root": str(repo_root)
        }, indent=2))
        return 0

    print(f"[*] Dispatching task to worker model: {args.model} via OpenCode...")
    start_time = time.time()

    # Call opencode run
    cmd = [opencode_bin, "run", "--model", args.model, prompt]
    code, stdout, stderr = run_cmd(cmd, cwd=repo_root)
    elapsed = round(time.time() - start_time, 2)

    # Check git status for changed files
    _, git_status, _ = run_cmd(["git", "status", "--short"], cwd=repo_root)
    changed_files = [line.strip() for line in git_status.splitlines() if line.strip()]

    result = {
        "status": "completed" if code == 0 else "failed",
        "return_code": code,
        "model": args.model,
        "elapsed_seconds": elapsed,
        "changed_files": changed_files,
        "stdout_tail": stdout[-2000:] if len(stdout) > 2000 else stdout,
        "stderr_tail": stderr[-1000:] if len(stderr) > 1000 else stderr
    }

    print(json.dumps(result, indent=2))
    return code

if __name__ == "__main__":
    sys.exit(main())
