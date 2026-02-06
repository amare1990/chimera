# Project Chimera — Meta Spec

## Mission
Build autonomous AI Influencers that research trends, generate content, and engage without human intervention.

## Constraints
- Spec-first development (no implementation before specs)
- MCP-only external integrations
- Skills modularity (no direct SDK calls)
- Human oversight for low-confidence outputs
- Dockerized + CI/CD reproducibility

## MCP/Tooling Governance & Autonomy
- **MCP Enforcement:** All agent perception and actions are mediated by the Model Context Protocol (MCP), ensuring traceability and auditability.
- **Tooling Extensibility:** New skills/tools must be registered via MCP and described in the technical spec before use.
- **Autonomous Operation:** Agents operate independently within defined confidence and safety thresholds; all actions are logged.
- **Governance:** Human-in-the-loop (HITL) review is enforced for low-confidence or novel actions. All governance events are auditable.
- **CI/CD Integration:** Spec alignment and security checks are automated in the pipeline (see coderabbit.yaml).

## Non-Goals
- Manual workflows
- Prompt-only prototypes
- Hardcoded integrations
