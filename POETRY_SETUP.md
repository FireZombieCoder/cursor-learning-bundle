# Poetry Setup Guide

This guide explains how to use Poetry for dependency management and development in the Base Learning Curriculum project.

## 🎯 What is Poetry?

Poetry is a modern dependency management and packaging tool for Python. It provides:

- **Dependency Resolution**: Automatically resolves and installs compatible package versions
- **Virtual Environment Management**: Creates and manages isolated Python environments
- **Package Building**: Builds and publishes Python packages
- **Lock File**: Ensures reproducible builds across different environments
- **Script Management**: Manages command-line scripts and entry points

## 🚀 Quick Start

### 1. Install Poetry

If Poetry is not already installed:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Verify installation
poetry --version
```

### 2. Setup Development Environment

```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd cursor-learning-bundle

# Run the automated setup script
./scripts/dev-setup.sh

# Or manually:
poetry install --with dev
poetry run pre-commit install
```

### 3. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

## 📦 Project Structure

```
cursor-learning-bundle/
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Locked dependencies
├── python/                 # Main Python package
│   ├── __init__.py
│   ├── cli.py             # Main CLI entry point
│   ├── common/            # Shared utilities
│   │   ├── __init__.py
│   │   ├── rpc.py
│   │   └── wallet.py
│   ├── stage0/            # Stage 0 tools
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   └── hello_base.py
│   └── examples/          # Example scripts
│       ├── __init__.py
│       └── sign_message.py
├── scripts/               # Development scripts
│   └── dev-setup.sh
├── Makefile              # Development commands
└── .pre-commit-config.yaml # Code quality hooks
```

## 🛠️ Development Commands

### Using Make (Recommended)

```bash
# Show all available commands
make help

# Install dependencies
make install

# Install with development dependencies
make dev-install

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Check code formatting
make format-check

# Run linting
make lint

# Clean build artifacts
make clean

# Start Jupyter notebook
make jupyter

# Show CLI help
make cli-help
```

### Using Poetry Directly

```bash
# Install dependencies
poetry install

# Install with development dependencies
poetry install --with dev

# Run commands in virtual environment
poetry run python python/examples/sign_message.py
poetry run base-cli --help
poetry run pytest

# Activate virtual environment
poetry shell

# Add new dependency
poetry add requests

# Add development dependency
poetry add --group dev pytest

# Update dependencies
poetry update

# Show dependency tree
poetry show --tree
```

## 🎮 Using the CLI Tools

### Main CLI

```bash
# Show help
poetry run base-cli --help

# Show version
poetry run base-cli version

# Show setup instructions
poetry run base-cli setup

# Stage 0 commands
poetry run base-cli stage0 --help
poetry run base-cli stage0 info <CONTRACT_ADDRESS>
poetry run base-cli stage0 update <CONTRACT_ADDRESS> "New Message"
```

### Stage 0 CLI (Legacy)

```bash
# Direct access to Stage 0 CLI
poetry run hello-base --help
poetry run hello-base info <CONTRACT_ADDRESS>
poetry run hello-base update <CONTRACT_ADDRESS> "New Message"
```

## 🔧 Configuration Files

### pyproject.toml

The main configuration file containing:

- **Project metadata**: Name, version, description, authors
- **Dependencies**: Runtime and development dependencies
- **Scripts**: Command-line entry points
- **Tool configurations**: Black, isort, mypy, pytest settings

### Key Sections:

```toml
[tool.poetry.dependencies]
python = "^3.10"
web3 = "^6.15.1"
eth-account = "^0.11.3"
# ... other dependencies

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
black = "^23.11.0"
# ... other dev dependencies

[tool.poetry.scripts]
base-cli = "python.cli:main"
hello-base = "python.stage0.cli:cli"
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=python --cov-report=html

# Run specific test file
poetry run pytest python/tests/test_hello_base.py

# Run with verbose output
poetry run pytest -v
```

### Test Structure

```
python/
├── tests/              # Test files (to be created)
│   ├── __init__.py
│   ├── test_common/
│   └── test_stage0/
```

## 🎨 Code Quality

### Pre-commit Hooks

Pre-commit hooks automatically run code quality checks:

```bash
# Install hooks
poetry run pre-commit install

# Run on all files
poetry run pre-commit run --all-files

# Run on staged files (automatic on commit)
git add .
git commit -m "Your commit message"
```

### Manual Code Quality

```bash
# Format code
poetry run black python/
poetry run isort python/

# Check formatting
poetry run black --check python/
poetry run isort --check-only python/

# Lint code
poetry run flake8 python/
poetry run mypy python/
```

## 📊 Virtual Environment

### Poetry Virtual Environment

Poetry automatically manages virtual environments:

```bash
# Show virtual environment info
poetry env info

# Show virtual environment path
poetry env info --path

# Activate virtual environment
poetry shell

# Deactivate (if using poetry shell)
exit
```

### Manual Virtual Environment (Alternative)

If you prefer manual virtual environment management:

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r python/requirements.txt
```

## 🚀 Deployment

### Building the Package

```bash
# Build package
poetry build

# This creates:
# - dist/base_learning_curriculum-0.1.0-py3-none-any.whl
# - dist/base-learning-curriculum-0.1.0.tar.gz
```

### Publishing (Future)

```bash
# Configure PyPI credentials
poetry config pypi-token.pypi your-token

# Publish to PyPI
poetry publish
```

## 🔍 Troubleshooting

### Common Issues

**1. Poetry not found**
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH (if needed)
export PATH="$HOME/.local/bin:$PATH"
```

**2. Virtual environment issues**
```bash
# Remove and recreate virtual environment
poetry env remove python
poetry install
```

**3. Dependency conflicts**
```bash
# Update lock file
poetry lock --no-update

# Or update all dependencies
poetry update
```

**4. Import errors**
```bash
# Ensure you're in the virtual environment
poetry shell

# Or run with poetry run
poetry run python your_script.py
```

### Getting Help

```bash
# Poetry help
poetry --help
poetry install --help

# Show dependency information
poetry show
poetry show --tree

# Show environment information
poetry env info
```

## 📚 Best Practices

1. **Always use Poetry commands** instead of pip when possible
2. **Commit poetry.lock** to ensure reproducible builds
3. **Use poetry run** for one-off commands
4. **Use poetry shell** for interactive development
5. **Keep pyproject.toml updated** with new dependencies
6. **Run pre-commit hooks** before committing
7. **Use make commands** for common development tasks

## 🎯 Next Steps

1. **Explore the CLI**: `poetry run base-cli --help`
2. **Run examples**: `poetry run python python/examples/sign_message.py`
3. **Start development**: `make dev-install` and begin coding
4. **Add tests**: Create test files in `python/tests/`
5. **Contribute**: Follow the development workflow with pre-commit hooks

Happy coding! 🚀
