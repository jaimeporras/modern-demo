# Use official slim Python image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed by Poetry & requests
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# --- IMPORTANT FIX ---
# Tell Poetry not to create virtualenvs (install into system Python instead)
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1

# Copy dependency files first (to leverage Docker cache)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies into system Python
RUN poetry install --no-root

# Copy the rest of the project
COPY . /app

# Default command: run your package
CMD ["python", "-m", "modern_demo"]
