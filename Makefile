# Base Learning Curriculum - Development Makefile

.PHONY: help install dev-install test lint format clean build docs

help: ## Show this help message
	@echo "Base Learning Curriculum - Development Commands"
	@echo "=============================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

dev-install: ## Install development dependencies
	poetry install --with dev

test: ## Run tests
	poetry run pytest

test-cov: ## Run tests with coverage
	poetry run pytest --cov=python --cov-report=html --cov-report=term

lint: ## Run linting (black, isort, flake8)
	poetry run black --check python/
	poetry run isort --check-only python/
	poetry run flake8 python/ --max-line-length=100 --extend-ignore=E203,W503,F401

mypy: ## Run mypy type checking
	poetry run mypy python/ --ignore-missing-imports --no-strict-optional

lint-all: lint mypy ## Run all linting including mypy

format: ## Format code
	poetry run black python/
	poetry run isort python/

format-check: ## Check code formatting
	poetry run black --check python/
	poetry run isort --check-only python/

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	poetry build

docs: ## Generate documentation
	@echo "Documentation generation not yet implemented"

pre-commit: ## Install pre-commit hooks
	poetry run pre-commit install

pre-commit-run: ## Run pre-commit on all files
	poetry run pre-commit run --all-files

jupyter: ## Start Jupyter notebook
	poetry run jupyter notebook

cli-help: ## Show CLI help
	poetry run base-cli --help

stage0-help: ## Show Stage 0 CLI help
	poetry run base-cli stage0 --help

tools: ## Launch learning tools
	poetry run tools

number-converter: ## Launch number format converter
	poetry run number-converter

demo-converter: ## Run number converter demo
	poetry run python scripts/demo-converter.py

check-env: ## Check environment setup
	@echo "Checking environment setup..."
	@poetry --version
	@poetry run python --version
	@echo "Virtual environment: $$(poetry env info --path)"
	@echo "Dependencies installed: $$(poetry show --only=main | wc -l) packages"

check-wallet: ## Check wallet setup for Base-Sepolia
	poetry run python scripts/verify-wallet-setup.py

setup-dev: dev-install pre-commit ## Complete development setup
	@echo "Development environment setup complete!"
	@echo "Run 'make check-env' to verify installation"
