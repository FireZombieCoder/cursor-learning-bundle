# Stage 0: EVM Basics & Tooling on Base-Sepolia

Welcome to Stage 0 of the Base Learning Curriculum! This stage introduces you to the fundamentals of Ethereum Virtual Machine (EVM) development and the tools needed to build on Base.

## 🎯 Learning Objectives

By the end of this stage, you will be able to:
- Understand what Base is and why it matters for Ethereum scaling
- Set up a complete development environment with Foundry
- Write, test, and deploy smart contracts to Base-Sepolia
- Interact with contracts using Python and web3.py
- Optimize gas usage and handle errors properly

## 📚 Lessons

### [Lesson 1: Introduction to Base and EVM Basics](./lessons/stage0-lesson1.md)
- What is Base and why it matters
- EVM fundamentals (accounts, transactions, gas, storage)
- Development environment overview

### [Lesson 2: Foundry Setup and First Contract](./lessons/stage0-lesson2.md)
- Installing and configuring Foundry
- Creating your first smart contract
- Understanding Solidity basics
- Testing with Anvil

### [Lesson 3: Testing and Gas Optimization](./lessons/stage0-lesson3.md)
- Writing comprehensive tests with Foundry
- Understanding gas costs and optimization
- Debugging failed transactions
- Gas snapshots and benchmarking

### [Lesson 4: Deploying to Base-Sepolia](./lessons/stage0-lesson4.md)
- Getting testnet ETH from faucets
- Deploying contracts to Base-Sepolia
- Contract verification on Basescan
- Best practices for deployment

### [Lesson 5: Python Web3 Integration](./lessons/stage0-lesson5.md)
- Setting up Python environment
- Interacting with contracts using web3.py
- Creating CLI tools for contract interaction
- Error handling and best practices

## 🏗️ Smart Contracts

### [HelloBase.sol](./contracts/stage0/HelloBase.sol)
A simple contract demonstrating:
- Basic Solidity syntax
- State variables and functions
- Events and custom errors
- Access control with owner pattern

### [SimpleStorage.sol](./contracts/stage0/SimpleStorage.sol)
A more complex contract showing:
- Storage vs memory vs calldata
- Structs and mappings
- Modifiers and access control
- Complex data types

## 🧪 Tests

### [HelloBase.t.sol](./test/stage0/HelloBase.t.sol)
Comprehensive tests covering:
- Initial state verification
- Function behavior testing
- Error condition testing
- Event emission verification
- Gas usage analysis
- Fuzz testing

### [SimpleStorage.t.sol](./test/stage0/SimpleStorage.t.sol)
Advanced tests including:
- Complex state management
- Access control testing
- Event verification
- Gas optimization validation

## 🐍 Python Tools

### [hello_base.py](./python/stage0/hello_base.py)
A complete Python client for interacting with the HelloBase contract:
- Contract state reading
- Transaction sending
- Event monitoring
- Error handling

### [cli.py](./python/stage0/cli.py)
A user-friendly command-line interface:
- Contract information display
- Message updating
- Event history viewing
- Balance checking

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Install Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup

# Install Python dependencies
pip install -r python/requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your private key and RPC URL
```

### 2. Get Testnet ETH
Visit the [Base faucet](https://docs.base.org/docs/tools/network-faucets/) to get testnet ETH.

### 3. Deploy Contracts
```bash
# Deploy HelloBase contract
forge script script/DeployHelloBase.s.sol:DeployHelloBase \
    --rpc-url base_sepolia \
    --broadcast \
    --verify

# Deploy SimpleStorage contract
forge script script/DeploySimpleStorage.s.sol:DeploySimpleStorage \
    --rpc-url base_sepolia \
    --broadcast \
    --verify
```

### 4. Run Tests
```bash
# Run all tests
forge test

# Run with gas report
forge test --gas-report

# Run specific test
forge test --match-test testUpdateMessage
```

### 5. Use Python CLI
```bash
# Get contract info
python python/stage0/cli.py info <CONTRACT_ADDRESS>

# Update message (if you're the owner)
python python/stage0/cli.py update <CONTRACT_ADDRESS> "New Message"

# View events
python python/stage0/cli.py events <CONTRACT_ADDRESS>
```

## 📊 Exercises

### Exercise 1: Basic Contract Interaction
1. Deploy the HelloBase contract
2. Read the initial message
3. Update the message (if you're the owner)
4. Verify the change

### Exercise 2: Python Integration
1. Use the Python CLI to interact with your contract
2. Monitor events using the events command
3. Check your account balance

### Exercise 3: Gas Optimization
1. Analyze gas usage in the test output
2. Try to optimize the SimpleStorage contract
3. Compare gas usage before and after optimization

## 🧠 Quiz

Take the [Stage 0 Quiz](./quizzes/stage0.md) to test your understanding:
- 8 multiple choice questions
- Passing score: 6/8 (75%)
- Covers all lesson topics

## ✅ Done Criteria

Before moving to Stage 1, ensure you can:
- [ ] Deploy a contract to Base-Sepolia
- [ ] Write and run Foundry tests
- [ ] Interact with contracts using Python
- [ ] Understand gas costs and optimization
- [ ] Handle errors and edge cases
- [ ] Pass the Stage 0 quiz

## 🔗 Useful Links

- [Base Documentation](https://docs.base.org/)
- [Foundry Book](https://book.getfoundry.sh/)
- [web3.py Documentation](https://web3py.readthedocs.io/)
- [Base-Sepolia Explorer](https://sepolia.basescan.org/)
- [Base Faucet](https://docs.base.org/docs/tools/network-faucets/)

## 🆘 Troubleshooting

### Common Issues

**"Insufficient balance"**
- Get testnet ETH from the faucet
- Check your account balance

**"Transaction reverted"**
- Verify you're the contract owner
- Check function parameters
- Review contract logic

**"Network connection failed"**
- Verify your RPC URL
- Check your internet connection
- Try a different RPC endpoint

**"Contract not verified"**
- Ensure you have the correct ABI
- Check contract address
- Verify the contract is deployed

## 🎉 Congratulations!

You've completed Stage 0! You now have a solid foundation in:
- EVM basics and Base network
- Foundry development workflow
- Smart contract testing
- Python web3 integration
- Gas optimization techniques

Ready for [Stage 1: Solidity Core](../stage1/README.md)? 🚀
