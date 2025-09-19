# Poetry Dependency Management Guide

## 📚 Understanding Poetry's Dependency Storage and Management

This comprehensive guide explains how Poetry stores, manages, and locates your project's libraries and dependencies.

## 🎯 Overview

Poetry uses a sophisticated system to manage dependencies that ensures:
- **Isolation**: Each project has its own virtual environment
- **Reproducibility**: Lock files ensure consistent installs across environments
- **Efficiency**: Shared cache reduces download times
- **Security**: Dependency resolution prevents conflicts

## 🏗️ Poetry's Architecture

### Core Components

1. **Virtual Environments**: Isolated Python environments per project
2. **Cache System**: Shared package cache across projects
3. **Lock Files**: Deterministic dependency resolution
4. **Configuration**: Project-specific settings and metadata

## 📁 Directory Structure

### Poetry's Global Directories

Poetry stores its data in several key locations:

```bash
# Poetry's main configuration directory
~/.config/pypoetry/

# Virtual environments cache
~/.cache/pypoetry/virtualenvs/

# Package cache (downloaded wheels/sources)
~/.cache/pypoetry/artifacts/

# Poetry configuration
~/.config/pypoetry/config.toml
```

### Project-Specific Files

```bash
your-project/
├── pyproject.toml          # Project configuration and dependencies
├── poetry.lock             # Locked dependency versions
├── .venv/                  # Local virtual environment (if created locally)
└── dist/                   # Built packages (when using poetry build)
```

## 🔍 Finding Your Project's Dependencies

### 1. Virtual Environment Location

```bash
# Show virtual environment information
poetry env info

# Show virtual environment path
poetry env info --path

# List all virtual environments
poetry env list
```

**Example Output:**
```
Virtualenv
Python:         3.10.12
Implementation: CPython
Path:           /home/fireos/.cache/pypoetry/virtualenvs/base-learning-curriculum-gGd5qb8m-py3.10
Executable:     /home/fireos/.cache/pypoetry/virtualenvs/base-learning-curriculum-gGd5qb8m-py3.10/bin/python
Valid:          True
```

### 2. Virtual Environment Naming Convention

Poetry creates virtual environments with this pattern:
```
{project-name}-{hash}-py{python-version}
```

**Example:**
- Project: `base-learning-curriculum`
- Hash: `gGd5qb8m` (unique identifier)
- Python: `3.10`
- Full name: `base-learning-curriculum-gGd5qb8m-py3.10`

### 3. Exploring the Virtual Environment

```bash
# Get the virtual environment path
VENV_PATH=$(poetry env info --path)

# Explore the structure
ls -la $VENV_PATH/

# Check installed packages
ls -la $VENV_PATH/lib/python3.10/site-packages/

# Check scripts/binaries
ls -la $VENV_PATH/bin/
```

**Virtual Environment Structure:**
```
/home/fireos/.cache/pypoetry/virtualenvs/base-learning-curriculum-gGd5qb8m-py3.10/
├── bin/                    # Executables and scripts
│   ├── python             # Python interpreter
│   ├── pip                # Package installer
│   ├── base-cli           # Our custom CLI script
│   └── hello-base         # Our custom CLI script
├── lib/                    # Python libraries
│   └── python3.10/
│       └── site-packages/  # Installed packages
│           ├── web3/       # Web3 library
│           ├── eth_account/ # Ethereum account library
│           ├── rich/       # Rich formatting library
│           └── ...         # Other dependencies
├── include/                # Header files
└── pyvenv.cfg             # Virtual environment configuration
```

## 📦 Package Storage and Caching

### 1. Package Cache Location

```bash
# Poetry's package cache
~/.cache/pypoetry/artifacts/

# Structure
~/.cache/pypoetry/artifacts/
├── 0a/                    # Hash-based organization
│   └── 1b/
│       └── 2c/
│           └── web3-6.20.1-py3-none-any.whl
├── 1d/
│   └── 2e/
│       └── 3f/
│           └── eth_account-0.11.3-py3-none-any.whl
└── ...
```

### 2. Cache Management

```bash
# Show cache information
poetry cache list

# Clear cache
poetry cache clear pypi --all

# Clear specific package cache
poetry cache clear pypi web3

# Show cache size
du -sh ~/.cache/pypoetry/
```

### 3. Package Sources

Poetry can use multiple package sources:

```bash
# Show configured sources
poetry source show

# Add a new source
poetry source add --priority=primary myrepo https://myrepo.com/simple/

# Remove a source
poetry source remove myrepo
```

## 🔒 Lock File Management

### 1. Understanding poetry.lock

The `poetry.lock` file contains:
- Exact versions of all dependencies
- Dependency resolution tree
- Package hashes for security
- Metadata for reproducible builds

```bash
# Show lock file information
poetry show --tree

# Show specific package details
poetry show web3

# Show outdated packages
poetry show --outdated
```

### 2. Lock File Operations

```bash
# Update lock file without changing dependencies
poetry lock --no-update

# Update lock file and dependencies
poetry lock

# Update specific package
poetry update web3

# Update all packages
poetry update
```

## 🛠️ Dependency Resolution

### 1. How Poetry Resolves Dependencies

Poetry uses a sophisticated resolver that:

1. **Reads pyproject.toml**: Gets dependency specifications
2. **Checks poetry.lock**: Uses locked versions if available
3. **Resolves conflicts**: Finds compatible versions
4. **Downloads packages**: From configured sources
5. **Installs to venv**: Creates isolated environment

### 2. Dependency Tree Visualization

```bash
# Show dependency tree
poetry show --tree

# Show only top-level dependencies
poetry show --only=main

# Show development dependencies
poetry show --only=dev

# Show specific package tree
poetry show --tree web3
```

**Example Output:**
```
web3 6.20.1 Web3.py
├── aiohttp >=3.7.4.post0,<4.0.0
├── eth-abi >=4.0.0,<5.0.0
├── eth-account >=0.8.0,<1.0.0
├── eth-hash >=0.4.0,<1.0.0
├── eth-typing >=3.0.0,<4.0.0
├── eth-utils >=2.0.0,<3.0.0
├── hexbytes >=0.1.0,<1.0.0
├── jsonschema >=4.0.0,<5.0.0
├── lru-dict >=1.1.6,<2.0.0
├── protobuf >=3.10.0,<5.0.0
├── pywin32 >=304; sys_platform == "win32"
├── requests >=2.16.0,<3.0.0
├── typing-extensions >=4.0.0,<5.0.0
└── websockets >=10.0.0,<12.0.0
```

## 🔧 Configuration and Customization

### 1. Poetry Configuration

```bash
# Show current configuration
poetry config --list

# Set configuration values
poetry config virtualenvs.in-project true
poetry config virtualenvs.path /custom/path
poetry config cache-dir /custom/cache

# Reset to defaults
poetry config --unset virtualenvs.in-project
```

### 2. Virtual Environment Options

```bash
# Create virtual environment in project directory
poetry config virtualenvs.in-project true

# Use system Python (not recommended)
poetry config virtualenvs.create false

# Set custom virtual environment path
poetry config virtualenvs.path /path/to/venvs
```

### 3. Cache Configuration

```bash
# Set custom cache directory
poetry config cache-dir /custom/cache/path

# Disable cache (not recommended)
poetry config cache-dir false
```

## 📊 Monitoring and Maintenance

### 1. Disk Usage Analysis

```bash
# Check virtual environment size
du -sh $(poetry env info --path)

# Check cache size
du -sh ~/.cache/pypoetry/

# Check specific package sizes
poetry show --tree | grep -E "^\w" | while read pkg; do
    echo "$pkg: $(du -sh $(poetry env info --path)/lib/python3.10/site-packages/$pkg 2>/dev/null | cut -f1)"
done
```

### 2. Cleanup Operations

```bash
# Remove unused virtual environments
poetry env remove --all

# Clear package cache
poetry cache clear --all

# Remove build artifacts
poetry build --clean
```

### 3. Health Checks

```bash
# Check for broken dependencies
poetry check

# Verify lock file consistency
poetry lock --check

# Test dependency resolution
poetry install --dry-run
```

## 🚀 Best Practices

### 1. Virtual Environment Management

```bash
# Always use poetry run for commands
poetry run python script.py

# Activate environment for interactive work
poetry shell

# Deactivate when done
exit
```

### 2. Dependency Management

```bash
# Pin major versions in pyproject.toml
web3 = "^6.15.1"  # Allows 6.15.1 to 6.x.x

# Use exact versions for critical dependencies
eth-account = "0.11.3"  # Exact version

# Regular updates
poetry update  # Update all dependencies
poetry update web3  # Update specific package
```

### 3. Cache Management

```bash
# Regular cache cleanup
poetry cache clear --all

# Monitor cache size
du -sh ~/.cache/pypoetry/

# Use local cache for CI/CD
poetry config cache-dir ./cache
```

## 🔍 Troubleshooting

### 1. Common Issues

**Virtual Environment Not Found:**
```bash
# Recreate virtual environment
poetry env remove python
poetry install
```

**Package Not Found:**
```bash
# Clear cache and reinstall
poetry cache clear --all
poetry install
```

**Lock File Conflicts:**
```bash
# Regenerate lock file
rm poetry.lock
poetry lock
poetry install
```

### 2. Debugging Commands

```bash
# Verbose installation
poetry install -vvv

# Show dependency resolution
poetry show --tree

# Check environment
poetry env info

# Validate configuration
poetry check
```

### 3. Recovery Procedures

```bash
# Complete reset
rm -rf .venv poetry.lock
poetry install

# Reset to specific state
git checkout poetry.lock
poetry install

# Clean reinstall
poetry cache clear --all
rm -rf $(poetry env info --path)
poetry install
```

## 📈 Performance Optimization

### 1. Cache Optimization

```bash
# Use local cache for CI/CD
poetry config cache-dir ./cache

# Pre-populate cache
poetry install --no-dev

# Use parallel downloads
poetry config installer.parallel true
```

### 2. Virtual Environment Optimization

```bash
# Use in-project virtual environments
poetry config virtualenvs.in-project true

# Reuse virtual environments
poetry config virtualenvs.reuse true
```

### 3. Dependency Optimization

```bash
# Use only necessary dependencies
poetry install --only=main

# Skip optional dependencies
poetry install --no-optional
```

## 🎯 Summary

Poetry's dependency management system provides:

1. **Isolation**: Each project has its own virtual environment
2. **Reproducibility**: Lock files ensure consistent installs
3. **Efficiency**: Shared cache reduces download times
4. **Security**: Dependency resolution prevents conflicts
5. **Flexibility**: Configurable storage locations and behaviors

### Key Locations:
- **Virtual Environments**: `~/.cache/pypoetry/virtualenvs/`
- **Package Cache**: `~/.cache/pypoetry/artifacts/`
- **Configuration**: `~/.config/pypoetry/config.toml`
- **Project Files**: `pyproject.toml`, `poetry.lock`

### Key Commands:
- `poetry env info` - Show virtual environment information
- `poetry show --tree` - Show dependency tree
- `poetry cache list` - List cached packages
- `poetry config --list` - Show configuration

This system ensures reliable, reproducible, and efficient Python dependency management for your Base Learning Curriculum project! 🚀

## 🎯 Real-World Example: Base Learning Curriculum Project

Let's examine the actual Poetry setup for this project:

### Current Project Information

**Virtual Environment:**
```
Path: /home/fireos/.cache/pypoetry/virtualenvs/base-learning-curriculum-gGd5qb8m-py3.10
Size: 347M
Python: 3.10.12
```

**Cache Information:**
```
Cache Location: ~/.cache/pypoetry/
Cache Size: 572M
Source: PyPI (_default_cache)
```

**Installed Packages (Sample):**
```
- web3 6.20.1 (Web3.py library)
- eth-account 0.11.3 (Ethereum account management)
- rich 13.9.4 (Rich text formatting)
- click 8.3.0 (CLI framework)
- black 23.12.1 (Code formatter)
- pytest 7.4.4 (Testing framework)
```

**Custom CLI Scripts:**
```
- base-cli (Main CLI entry point)
- hello-base (Stage 0 CLI tool)
```

### Practical Commands for This Project

```bash
# Check project status
poetry env info
poetry show --tree

# Run our custom CLI tools
poetry run base-cli --help
poetry run hello-base --help

# Development workflow
make format    # Format code
make lint      # Check code quality
make test      # Run tests

# Package management
poetry add requests          # Add new dependency
poetry remove package-name   # Remove dependency
poetry update               # Update all dependencies
```

### Project-Specific Locations

**Configuration Files:**
- `pyproject.toml` - Project configuration and dependencies
- `poetry.lock` - Locked dependency versions
- `.pre-commit-config.yaml` - Code quality hooks

**Development Tools:**
- `Makefile` - Development commands
- `scripts/dev-setup.sh` - Automated setup script
- `.gitignore` - Git ignore patterns

**Documentation:**
- `POETRY_SETUP.md` - Poetry setup guide
- `POETRY_DEPENDENCY_MANAGEMENT.md` - This guide
- `STAGE0_README.md` - Stage 0 curriculum

This real-world example demonstrates how Poetry manages a complex Python project with multiple dependencies, custom CLI tools, and development workflows! 🎯
