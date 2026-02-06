# Tooling Strategy (Developer MCP)

Purpose: Improve traceability, reproducibility, and safe automation during development.

---

## Selected MCP Servers

### Tenx MCP Sense
Role: Traceability / black-box recorder
Why: Logs every tool call for audit and debugging

### filesystem-mcp
Role: Structured file editing
Why: Prevents unsafe direct file mutations by agents

### git-mcp
Role: Version control operations
Why: Enables agent-safe commits and diffs

### postgres-mcp (optional)
Role: Local DB inspection
Why: Test schemas without direct credentials

---

## Principle

Developer tools MUST NOT be accessible to runtime agents.
They exist only in the engineering environment.
