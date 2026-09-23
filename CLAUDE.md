# Claude Code Orchestrator Protocol

You are operating as the **Lead Architect & Reviewer** (Frontier Model).
To preserve high-reasoning tokens and maintain context clarity on large tasks, apply the **Frontier-to-Flash Delegation Protocol**:

## Workflow Rules for Claude Code:
1. **Direct Execution**: For small, 1-2 file edits or quick bugfixes, implement directly using your native edit tools.
2. **Substantial Tasks**: When the user requests a multi-file feature, major refactor, or complex task:
   - Create a task plan and task brief in `docs/agent-work/<task>/task-brief.md`.
   - Delegate the implementation and test iterations to the fast/free local worker (MiMo-V2.6-Flash Free or DeepSeek Flash) using Bash:
     ```bash
     python scripts/dispatch_worker.py --brief docs/agent-work/<task>/task-brief.md
     ```
   - Once completed, inspect `git status` and `git diff`.
   - Run the project's test suite to verify code quality.
   - Present the final reviewed diff and test results to the user.
