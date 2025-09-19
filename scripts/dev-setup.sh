#!/bin/bash
# Base Learning Curriculum - Development Setup Script

set -euo pipefail

echo "🚀 Setting up Base Learning Curriculum development environment..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed. Please install Poetry first:"
    echo "   curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

echo "✅ Poetry found: $(poetry --version)"

# Check Python version
PYTHON_VERSION=$(poetry run python --version | cut -d' ' -f2 | cut -d'.' -f1,2)
if [[ "$PYTHON_VERSION" < "3.10" ]]; then
    echo "❌ Python 3.10+ is required. Found: $(poetry run python --version)"
    exit 1
fi

echo "✅ Python version: $(poetry run python --version)"

# Install dependencies
echo "📦 Installing dependencies..."
poetry install --with dev

# Install pre-commit hooks
echo "🔧 Installing pre-commit hooks..."
poetry run pre-commit install

# Check if .env file exists
if [[ ! -f ".env" ]]; then
    echo "⚠️  .env file not found. Creating from template..."
    if [[ -f ".env.example" ]]; then
        cp .env.example .env
        echo "✅ Created .env file from template"
        echo "📝 Please edit .env file with your configuration"
    else
        echo "❌ .env.example not found. Please create .env file manually"
    fi
else
    echo "✅ .env file found"
fi

# Run initial checks
echo "🧪 Running initial checks..."
poetry run python -c "import python.common.rpc; import python.common.wallet; print('✅ Imports working')"

# Show next steps
echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Get testnet ETH from: https://docs.base.org/docs/tools/network-faucets/"
echo "3. Deploy contracts using Foundry"
echo "4. Test the CLI: poetry run base-cli --help"
echo ""
echo "Available commands:"
echo "  make help          - Show all available commands"
echo "  make test          - Run tests"
echo "  make lint          - Run linting"
echo "  make format        - Format code"
echo "  make jupyter       - Start Jupyter notebook"
echo ""
