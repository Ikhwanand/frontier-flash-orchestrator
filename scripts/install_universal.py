#!/usr/bin/env python3
"""
Universal AI Coding Agent Orchestrator Installer.
Installs thin-root orchestrator rules and worker dispatchers into any project or AI tool:
- Claude Code (CLAUDE.md)
- Cursor (.cursor/rules/orchestrator.mdc)
- Windsurf (.windsurfrules)
- GitHub Copilot (.github/copilot-instructions.md)
- OpenCode / Kilo Code / Antigravity / Codex (AGENTS.md & .agents/skills/)
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys

SOURCE_ROOT = Path(__file__).resolve().parent.parent

def install_to(target_dir: Path, tools: list[str] | None = None) -> None:
    target_dir = target_dir.resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    all_tools = {"claude", "cursor", "windsurf", "copilot", "universal", "antigravity"}
    selected = set(tools) if tools else all_tools

    print(f"[*] Installing Universal Orchestrator into: {target_dir}")

    # Universal AGENTS.md
    if "universal" in selected:
        agents_src = SOURCE_ROOT / "AGENTS.md"
        if agents_src.exists():
            shutil.copy2(agents_src, target_dir / "AGENTS.md")
            print("  [+] Installed AGENTS.md (Universal: OpenCode, Kilo, Codex, Antigravity)")

    # Claude Code
    if "claude" in selected:
        claude_src = SOURCE_ROOT / "CLAUDE.md"
        if claude_src.exists():
            shutil.copy2(claude_src, target_dir / "CLAUDE.md")
            print("  [+] Installed CLAUDE.md (Claude Code)")

    # Cursor
    if "cursor" in selected:
        cursor_dir = target_dir / ".cursor" / "rules"
        cursor_dir.mkdir(parents=True, exist_ok=True)
        cursor_src = SOURCE_ROOT / ".cursor" / "rules" / "orchestrator.mdc"
        if cursor_src.exists():
            shutil.copy2(cursor_src, cursor_dir / "orchestrator.mdc")
            print("  [+] Installed .cursor/rules/orchestrator.mdc (Cursor)")

    # Windsurf
    if "windsurf" in selected:
        windsurf_src = SOURCE_ROOT / ".windsurfrules"
        if windsurf_src.exists():
            shutil.copy2(windsurf_src, target_dir / ".windsurfrules")
            print("  [+] Installed .windsurfrules (Windsurf)")

    # GitHub Copilot
    if "copilot" in selected:
        github_dir = target_dir / ".github"
        github_dir.mkdir(parents=True, exist_ok=True)
        copilot_src = SOURCE_ROOT / ".github" / "copilot-instructions.md"
        if copilot_src.exists():
            shutil.copy2(copilot_src, github_dir / "copilot-instructions.md")
            print("  [+] Installed .github/copilot-instructions.md (GitHub Copilot)")

    # Antigravity & Agent Skills
    if "antigravity" in selected:
        skill_src = SOURCE_ROOT / ".agents" / "skills" / "frontier-flash-orchestrator"
        if skill_src.exists():
            dest_skill = target_dir / ".agents" / "skills" / "frontier-flash-orchestrator"
            if dest_skill.exists():
                shutil.rmtree(dest_skill)
            shutil.copytree(skill_src, dest_skill)
            print("  [+] Installed .agents/skills/frontier-flash-orchestrator/ (Antigravity & Agent Skills)")

    # Scripts / Dispatcher
    scripts_dest = target_dir / "scripts"
    scripts_dest.mkdir(parents=True, exist_ok=True)
    dispatcher_src = SOURCE_ROOT / "scripts" / "dispatch_worker.py"
    if dispatcher_src.exists():
        shutil.copy2(dispatcher_src, scripts_dest / "dispatch_worker.py")
        print("  [+] Installed scripts/dispatch_worker.py (Execution Engine)")

    print("[SUCCESS] All orchestrator protocols successfully installed!\n")

def main() -> int:
    parser = argparse.ArgumentParser(description="Universal AI Coding Agent Orchestrator Installer")
    parser.add_argument("--target", default=".", help="Target project directory (default: current directory)")
    parser.add_argument("--tools", nargs="+", choices=["claude", "cursor", "windsurf", "copilot", "universal", "antigravity"],
                        help="Specific tools to install for (default: all)")
    args = parser.parse_args()

    install_to(Path(args.target), args.tools)
    return 0

if __name__ == "__main__":
    sys.exit(main())
