# Copilot / AI Agent Instructions for chimera

Purpose: give an AI coding assistant the minimum, actionable knowledge
to be productive in this repository.

- **Project snapshot:** very small Python project. Entrypoint: [main.py](main.py).
- **Python version:** >=3.14 (see [pyproject.toml](pyproject.toml)).
- **Dev tools:** `pytest`, `mypy`, `ruff` are in the `dev` group of `pyproject.toml`.

Quick tasks and commands
- Run the app: `python main.py` (single-file script currently prints a message).
- Run tests: `pytest` (no tests present yet; create `tests/` to add tests).
- Type check: `mypy .` (mypy is configured as a dev dependency).
- Lint/format: `ruff .`

Repository structure and conventions
- Root files: [main.py](main.py) is the runtime entrypoint; `README.md` is present but empty.
- Project metadata and dependencies live in [pyproject.toml](pyproject.toml). When adding packages, update `dependencies` and bump `version` there.
- No package layout yet (no `package/` folder). Prefer introducing a package directory (e.g., `chimera/`) before converting to a module-style `python -m` invocation.

Guidance for code changes
- Keep changes minimal and focused; avoid introducing heavy framework code without reason—this repo appears intended as a tiny sample or starter.
- When adding features, update `pyproject.toml` (dependencies) and `README.md` with run instructions and examples.
- Follow the existing dev-toolchain: add tests under `tests/`, and run `pytest`, `mypy .`, and `ruff .` before suggesting merges.

Integration points and external deps
- Currently none declared in `dependencies`. Any external integration must be added to `pyproject.toml`.

Examples to refer to in edits
- To show a runtime example, update [main.py](main.py) or add a new module under a package folder and demonstrate `python -m <pkg>` usage in `README.md`.
- To add CI or formatting checks, modify `pyproject.toml` dev group or add a `.github/workflows/` workflow that runs `ruff`, `mypy`, and `pytest` on push/pull-requests.

What I did not find (so do not assume)
- No existing `.github/copilot-instructions.md` or AGENT.md files to merge—this file is a fresh addition.
- `README.md` is empty; do not assume documented scripts or conventions beyond what's in `pyproject.toml` and `main.py`.

If unclear or incomplete
- Ask which direction you want: keep repo minimal, add a package structure, or scaffold CI/tests. I can then update `pyproject.toml`, add `tests/`, and create a CI workflow.

References
- [main.py](main.py)
- [pyproject.toml](pyproject.toml)
- [README.md](README.md)
