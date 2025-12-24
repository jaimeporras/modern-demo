# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python demo project showcasing modern Python tooling with Poetry as the package manager. The package is published to TestPyPI via GitHub Actions on tagged releases.

## Development Commands

### Environment Setup
```bash
# Install Poetry if not already installed
pip install poetry

# Install all dependencies (including dev dependencies)
poetry install
```

### Testing
```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run a specific test file
poetry run pytest tests/test_core.py

# Run a specific test function
poetry run pytest tests/test_core.py::test_process_numbers
```

### Linting and Formatting
```bash
# Format code with Black
poetry run black .

# Check formatting without making changes
poetry run black --check .

# Sort imports with isort
poetry run isort .

# Check import sorting
poetry run isort --check-only .

# Run Ruff linter
poetry run ruff check .
```

### Running the Application
```bash
# Run the package as a module
python -m modern_demo

# Or using Poetry
poetry run python -m modern_demo
```

### Building and Publishing
```bash
# Build the package
poetry build

# Publish to TestPyPI (happens automatically on tagged releases via CI)
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi --username __token__ --password $POETRY_PYPI_TOKEN_TESTPYPI
```

### Docker
```bash
# Build Docker image
docker build -t modern-demo .

# Run Docker container
docker run modern-demo
```

## Code Architecture

### Package Structure
```
modern_demo/
├── __init__.py       # Package marker
├── __main__.py       # Entry point with fetch_data() and main()
└── core.py           # Core utilities (process_numbers)

tests/
├── test_core.py      # Tests for core.py utilities
└── test_demo.py      # Tests for __main__.py functions
```

### Key Components

**modern_demo/__main__.py**: Main entry point that demonstrates HTTP requests with fallback behavior. The `fetch_data()` function attempts to fetch data from httpbin.org and falls back to synthetic data if the request fails. This is the executable module when running `python -m modern_demo`.

**modern_demo/core.py**: Contains utility functions like `process_numbers()` which filters and transforms numeric data.

### Testing Approach

The project uses pytest with parametrized tests. See `tests/test_core.py` for examples of both basic assertions and `@pytest.mark.parametrize` for running multiple test cases automatically.

## Tool Configuration

### Python Version
- Minimum: Python 3.11
- Target version for Black: py311

### Code Style
- Line length: 88 characters (Black default)
- Import sorting: Black-compatible profile (via isort)
- Linter: Ruff with pyflakes (F) and pycodestyle (E) checks

### Dependencies
- Runtime: `requests` (>=2.32.5,<3.0.0)
- Dev: `pytest`, `black`, `isort`, `ruff`

## CI/CD Pipeline

The GitHub Actions workflow (.github/workflows/ci.yml) runs on pushes to main and on version tags:

1. **Build job**: Installs dependencies, runs linters (black, isort, ruff), and runs tests
2. **Release job**: Triggers on tags starting with 'v*', builds the package, and publishes to TestPyPI using the `TEST_PYPI_API_TOKEN` secret

### Creating a Release
1. Update version in `pyproject.toml`
2. Commit the change
3. Create and push a tag: `git tag v0.1.x && git push origin v0.1.x`
4. CI will automatically publish to TestPyPI
