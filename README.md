# Cursor Learning Bundle (Base L2 / Python / Foundry)

This bundle gives you:
- `.cursor/rules/00_execution-protocol.mdc` — your always-on entrypoint (Otto)
- Curriculum, Python, Foundry/Security rules under `.cursor/rules/`
- Custom commands under `.cursor/commands/`
- `bootstrap_learning_env.sh` — creates a Task File in `.tasks/` pre-filled with the **Execution Protocol**
- Python scaffolding and `.env.example`

## Install

### Option 1: Poetry (Recommended)
1) Extract this zip at your repo root.
2) Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
3) Run setup: `./scripts/dev-setup.sh` or `poetry install --with dev`
4) Copy `.env.example` → `.env` and set your RPC/keys.

### Option 2: Traditional pip
1) Extract this zip at your repo root.
2) Create a Python venv (optional) and `pip install -r python/requirements.txt`.
3) Copy `.env.example` → `.env` and set your RPC/keys.

## Bootstrap
```bash
./bootstrap_learning_env.sh
git checkout -b task/base-learning_$(date +%Y-%m-%d)_1  # if not already created by protocol
```

Open Cursor, add your goals under **User Input** in `00_execution-protocol.mdc`, and run your commands:
- `/curriculum build stage=0 topic="Tooling on Base-Sepolia"`
- `/exercise topic="storage vs memory" stage=1`
- `/trace-lab contract="Demo" method="queryDouble(address,uint256)"`

## Python Development

This project uses Poetry for dependency management and development tools.

### Quick Start
```bash
# Setup development environment
./scripts/dev-setup.sh

# Use the CLI tools
poetry run base-cli --help
poetry run base-cli stage0 info <CONTRACT_ADDRESS>

# Development commands
make help          # Show all commands
make test          # Run tests
make format        # Format code
make lint          # Run linting

# Learning tools
make number-converter  # Launch number format converter
make tools            # Launch learning tools
```

### Documentation
- [Poetry Setup Guide](POETRY_SETUP.md) - Complete Poetry configuration guide
- [Stage 0 README](STAGE0_README.md) - Stage 0 curriculum documentation
- [Brave Wallet Setup](docs/BRAVE_WALLET_BASE_SEPOLIA_SETUP.md) - Configure Brave wallet for Base-Sepolia
- [Base-Sepolia Quick Reference](docs/BASE_SEPOLIA_QUICK_REFERENCE.md) - Quick reference for network details
- [Number Converter Guide](docs/NUMBER_CONVERTER_GUIDE.md) - Number format conversion tool
