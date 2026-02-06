# Project Chimera

**Autonomous AI Influencer Infrastructure**
*Lead Architect/FDE Trainee: Amare Kassa*

---

## **Overview**

Project Chimera is a **spec-driven, agent-ready system** for building autonomous AI influencers.
It is designed for:

- Multi-agent coordination using the **FastRender Swarm** pattern
- Strict adherence to **Model Context Protocol (MCP)** for all perception and actions
- Platform-agnostic **Skill modules** for agent capabilities
- HITL governance with confidence thresholds and TDD validation
- Horizontal scalability for thousands of agents

---

## **Repository Structure**

```text
chimera/
├─ .github
├─ .venv
├─ .vscode/                # VS Code workspace settings
│  ├─ mcp.json             # MCP configuration
├─ research/               # Research summaries and tooling decisions
├─ specs/                  # Project specifications
│  ├─ _meta.md             # Vision, constraints, and high-level goals
│  ├─ functional.md        # User stories
│  ├─ technical.md         # API contracts, DB schema, and ERD
│  └─ openclaw_integration.md # Optional OpenClaw status integration
├─ skills/                 # Agent capabilities (single README.md covers all skills)
│  ├─ trend_fetcher.py
│  ├─ content_generator.py
│  └─ publisher.py
│  └─ README.md
├─ tests/                  # Failing tests (TDD "empty slots")
│  ├─ test_skills_interface.py
│  └─ test_trend_fetcher.py
├─ main.py                 # Entrypoint for orchestrating Chimera Agents
├─ Dockerfile              # Containerized environment
├─ Makefile                # Standardized commands: setup, test, spec-check
├─ pyproject.toml          # Project metadata and dependencies
└─ coderabbit.yaml         # AI review policy for Spec Alignment and Security
Checks
├─ README.md               # README.md file for the chimera repo
```
---


## **Getting Started**

### 1. Clone the repo

```bash
git clone https://github.com/amare1990/chimera.git
cd chimera
```

### 2. Setup Python environment using `uv`

```bash
uv venv --clear      # Create a clean virtual environment
uv pip install -e .   # Install the project in editable mode
uv pip install pytest # Install testing framework
```

### 3. Running Tests

Project follows **TDD**: all tests start **failing** until a skill is implemented.

```bash
PYTHONPATH=. uv run pytest
```

### 4. Makefile Commands

```bash
make setup       # Install dependencies
make test        # Run tests inside Docker container
make spec-check  # Optional: validate code against specs
```

---

## **Agent & Skill Context**

* **Skills** are modular capabilities:

  * `trend_fetcher`: Fetch trending topics from APIs
  * `content_generator`: Generate post content for influencers
  * `publisher`: Publish generated content to target platforms

* All skill I/O is defined in **`specs/technical.md`**.

* TDD ensures each skill exposes a single `run(input_json)` function that receives JSON-like input.

---

## **CI/CD & Governance**

* `.github/workflows/main.yml` triggers `make test` on every push.
* `coderabbit.yaml` enforces:

  * Spec alignment checks
  * Security and dependency checks
* All code must pass TDD tests before merging.

---

## **VS Code Integration**

* `.vscode/mcp.json` configures **Tenx MCP Sense** for code assistance.
* The `.venv` folder ensures isolated Python environment.
* The workspace is preconfigured to work with Skills, Tests, and Specs.

---

## **Dockerized Environment**

* **Dockerfile** provides a reproducible dev and test environment.
* **Makefile** standardizes commands inside Docker for:

  * setup
  * test
  * spec-check

```bash
# Example Dockerized test run
docker build -t chimera .
docker run --rm chimera
```

---

## **Submission Artifacts**

1. Public GitHub Repository (with the structure above)
2. Loom video (max 5 mins):

   * Spec walkthrough
   * Failing TDD tests demo
   * VS Code Agent context demo
3. MCP telemetry logs (Tenx MCP Sense active)

---

## **License**

MIT License. See `LICENSE.md` for details.
