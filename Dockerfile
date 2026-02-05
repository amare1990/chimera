FROM python:3.11-slim

WORKDIR /app

# install uv
RUN pip install uv

COPY pyproject.toml .
RUN uv pip install -e . || true

COPY . .

CMD ["pytest", "-q"]
