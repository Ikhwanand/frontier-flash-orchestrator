# Frontier Flash Orchestrator ⚡

> **Save Frontier tokens for decisions that matter. Let fast/free worker models do the heavy writing.**

An open, universal AI Agent Skill and protocol compatible with **Antigravity, Claude Code, Cursor, Windsurf, OpenCode, Kilo Code, and GitHub Copilot**.

Published for the **[skills.sh](https://skills.sh)** ecosystem.

---

## 💡 The Philosophy: Thin-Root Orchestration

When working on substantial features, large refactors, or test suite generation, having an expensive **Frontier Model** (Claude 3.7 Sonnet, Gemini 3.8 Flash High, GPT-5) write hundreds of lines of boilerplate and loop through iterative debugging burns massive token budgets and bloats context.

**Frontier Flash Orchestrator** separates concerns into two distinct roles:

```text
┌────────────────────────────────────────────────────────┐
│             Frontier Model (Orchestrator)              │
│       "The Architect & High-Level Reviewer"            │
│  - Understands repository patterns & architecture      │
│  - Produces strict, bounded task briefs & contracts    │
│  - Runs security, design, and acceptance review        │
└──────────────────────────┬─────────────────────────────┘
                           │ Dispatches brief via CLI
                           ▼
┌────────────────────────────────────────────────────────┐
│            Fast/Free Worker (OpenCode / 9Router)       │
│          "The High-Volume Implementation Builder"      │
│  - Uses: Xiaomi MiMo-V2.6-Flash Free / DeepSeek Flash  │
│  - Writes implementation code and runs automated tests │
│  - Self-corrects edge cases and returns patch evidence │
└────────────────────────────────────────────────────────┘
```

---

## 📦 Installation via skills.sh

Install directly into any new project using the `skills.sh` CLI:

### Option 1: Install to Current Project
```bash
npx skills add ikhwanand/frontier-flash-orchestrator
```

### Option 2: Install Globally (Available in all projects)
```bash
npx skills add ikhwanand/frontier-flash-orchestrator -g
```

---

## 🚀 Supported AI Coding Agents

This repository provides zero-config native rule files for all major AI coding tools:

| Agent | Config / Integration File | How It Activates |
| :--- | :--- | :--- |
| **Antigravity** | `skills/frontier-flash-orchestrator/SKILL.md` | In chat: `$frontier-flash-orchestrator` |
| **Claude Code** | `CLAUDE.md` | Automatically active when running `claude` |
| **Cursor** | `.cursor/rules/orchestrator.mdc` | Native Cursor Rules in Composer / Agent |
| **Windsurf** | `.windsurfrules` | Native rules for Cascade agent |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Copilot Chat & Workspace instructions |
| **OpenCode / Kilo** | `AGENTS.md` | Universal multi-agent protocol |

---

## 🛠️ How It Works (The 3-Step Lifecycle)

### Step 1: Architect (Frontier Agent)
When assigned a substantial feature or refactor, the Frontier model creates a task brief:
- In-scope files to create/edit.
- Out-of-scope boundaries.
- Mandatory verification command (e.g. `npm test`, `pytest`).

### Step 2: Implementation (Fast/Free Worker)
The agent executes the worker dispatcher via terminal:
```bash
python scripts/dispatch_worker.py --brief docs/agent-work/<task>/task-brief.md --model opencode/mimo-v2.6-flash-free
```
The worker (MiMo-V2.6-Flash Free or DeepSeek Flash via OpenCode / 9Router) writes the code and runs test loops autonomously.

### Step 3: Acceptance Review (Frontier Agent)
The Frontier model reviews the `git diff`, ensures architectural integrity and security, runs tests independently, and presents the final reviewed result.

---

## 💻 Manual Setup in Existing Projects

To copy this orchestrator into any existing project manually, run:

```powershell
python scripts/install_universal.py --target "C:\Path\To\YourProject"
```

---

## 📄 License
MIT License. Free to use, adapt, and share.
