# Stage 0, Lesson 2: Foundry Setup and First Contract

## Learning Objectives
- Install and configure Foundry development environment
- Create your first smart contract
- Understand the basic structure of a Solidity contract
- Deploy and interact with contracts using Anvil

## Installing Foundry

Foundry is a fast, portable, and modular toolkit for Ethereum application development.

### Installation
```bash
# Install Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup

# Verify installation
forge --version
cast --version
anvil --version
```

### Foundry Tools
- **Forge**: Build, test, and deploy smart contracts
- **Cast**: Perform RPC calls and interact with contracts
- **Anvil**: Local blockchain for testing
- **Chisel**: Solidity REPL for quick testing

## Creating Your First Project

```bash
# Initialize a new Foundry project
forge init hello-base
cd hello-base

# Project structure
hello-base/
├── lib/          # Dependencies
├── src/          # Source contracts
├── test/         # Test files
├── script/       # Deployment scripts
└── foundry.toml  # Configuration
```

## Your First Smart Contract

Let's create a simple "Hello Base" contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HelloBase {
    string public message;
    address public owner;

    // Events for logging
    event MessageUpdated(string newMessage, address updater);

    // Custom errors (gas efficient)
    error Unauthorized();

    constructor(string memory _message) {
        message = _message;
        owner = msg.sender;
    }

    function updateMessage(string memory _newMessage) external {
        if (msg.sender != owner) revert Unauthorized();
        message = _newMessage;
        emit MessageUpdated(_newMessage, msg.sender);
    }

    function getMessage() external view returns (string memory) {
        return message;
    }
}
```

### Key Solidity Concepts

1. **Pragma**: Specifies Solidity version
2. **State variables**: Stored on blockchain
3. **Constructor**: Runs once during deployment
4. **Functions**: External (callable from outside), view (read-only)
5. **Events**: Log important state changes
6. **Custom errors**: Gas-efficient error handling

## Testing with Anvil

```bash
# Start local blockchain
anvil

# In another terminal, deploy contract
forge create src/HelloBase.sol:HelloBase --constructor-args "Hello Base!" --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

# Interact with contract
cast call <CONTRACT_ADDRESS> "getMessage()" --rpc-url http://localhost:8545
cast send <CONTRACT_ADDRESS> "updateMessage(string)" "Hello World!" --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --rpc-url http://localhost:8545
```

## Environment Configuration

Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
# Edit .env with your actual values
```

### Key Environment Variables
- `BASE_SEPOLIA_RPC`: RPC endpoint for Base-Sepolia
- `PRIVATE_KEY`: Your wallet's private key
- `CHAIN_ID`: 84532 for Base-Sepolia

## Foundry Configuration

Update `foundry.toml`:
```toml
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
solc = "0.8.20"
optimizer = true
optimizer_runs = 200

[rpc_endpoints]
base_sepolia = "${BASE_SEPOLIA_RPC}"
anvil = "http://localhost:8545"

[etherscan]
base_sepolia = { key = "${BASESCAN_API_KEY}", url = "https://api-sepolia.basescan.org/api" }
```

## Next Steps
In the next lesson, we'll write comprehensive tests for our contract and learn about gas optimization.

## Key Takeaways
- Foundry provides a complete development toolkit
- Smart contracts have state, functions, and events
- Anvil lets you test locally before deploying
- Proper configuration is essential for development
