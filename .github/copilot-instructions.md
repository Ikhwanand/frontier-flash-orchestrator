# GitHub Copilot Orchestrator Instructions

When tackling multi-file builds, refactors, or substantial features:
1. Start with an architectural specification and clear acceptance criteria.
2. Structure implementation into coherent, isolated bundles with designated test commands.
3. If autonomous worker execution is requested, generate an executable task brief in `docs/agent-work/<task>/task-brief.md`.
4. Review all generated code against security standards, edge cases, and unit test pass rates.
