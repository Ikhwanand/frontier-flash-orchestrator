# Universal Frontier-to-Flash Orchestrator Protocol

> **Role & Philosophy**:
> "Save Frontier Model tokens (Claude, Gemini, GPT) for architecture, high-stakes decisions, and final review. Delegate high-volume code writing, iterative test runs, and routine debugging to fast, free, or local worker models (such as Xiaomi MiMo-V2.6-Flash Free or DeepSeek Flash via OpenCode / 9Router)."

---

## 1. When This Protocol Activates
- **Skip Trivial Tasks**: Single-line edits, typos, quick explanations stay directly with the active agent.
- **Activate for Substantial Work**: Multi-file features, architectural refactors, test suite additions, and large bug-hunt cycles.

---

## 2. Universal 3-Step Lifecycle

### Step 1: Architect (Frontier Agent)
Before writing voluminous code:
1. Examine existing codebase patterns and dependencies.
2. Formulate a short, strict specification (`docs/agent-work/<task>/spec.md`):
   - Scope boundaries (In-Scope files vs Out-of-Scope files).
   - Clear contracts & interface signatures.
   - Exact verification commands (e.g. `npm test`, `pytest`).
3. Output the executable task brief (`docs/agent-work/<task>/task-brief.md`).

### Step 2: Delegate Implementation (Fast/Free Worker)
Invoke the worker CLI using the cross-tool dispatcher:
```bash
python scripts/dispatch_worker.py --brief docs/agent-work/<task>/task-brief.md --model opencode/mimo-v2.6-flash-free
```
*Or directly via OpenCode:*
```bash
opencode run --model opencode/mimo-v2.6-flash-free "Read and implement docs/agent-work/<task>/task-brief.md, run tests, and report."
```
*The worker handles file discovery, drafting, test-driven debugging, and test validation without eating expensive frontier tokens.*

### Step 3: Acceptance Review (Frontier Agent)
Once the worker concludes:
1. Run `git diff` to inspect every file changed by the worker.
2. Confirm the code adheres strictly to architectural boundaries, security practices, and clean code conventions.
3. Independently execute the verification tests.
4. If clean, accept the patch and summarize the outcome to the user.
