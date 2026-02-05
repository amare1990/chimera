FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv venv && uv pip install pytest

COPY . .

CMD ["uv", "run", "bash", "-c", "PYTHONPATH=. pytest -q"]

