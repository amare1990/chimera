# Agent Rules

## Overview
Explicit rules and constraints governing agent behavior, autonomy, and safety.

---

## General Rules
- Agents must operate within confidence and safety thresholds defined in specs.
- All actions must be logged and auditable.
- Agents may not access or modify memory of other agents.
- Agents must route low-confidence outputs to human reviewers.
- No hardcoded credentials or secrets in agent code.

---

## Skill-Specific Rules
- **Trend Fetcher:**
  - Only fetch trends from approved sources.
  - Respect region and limit parameters.
- **Content Generator:**
  - Content must match persona style and reference topic.
  - Media URLs must be valid and accessible.
- **Publisher:**
  - Only publish content with confidence above threshold.
  - Log all publishing actions.

---

## Safety & Governance
- Agents must not perform actions outside their assigned skill set.
- HITL review is mandatory for flagged outputs.
- All governance events are recorded for audit.

---

## Extensibility
- New skills/tools must be registered via MCP and described in technical spec before use.
- All new rules must be documented and reviewed before deployment.
