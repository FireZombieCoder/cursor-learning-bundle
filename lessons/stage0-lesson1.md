# Stage 0, Lesson 1: Introduction to Base and EVM Basics

## Learning Objectives
- Understand what Base is and why it matters for Ethereum scaling
- Learn the fundamentals of the Ethereum Virtual Machine (EVM)
- Set up your development environment for Base development

## What is Base?

Base is a Layer 2 (L2) blockchain built on top of Ethereum using Optimism's OP Stack. It provides:

- **Low fees**: Transactions cost pennies instead of dollars
- **Fast finality**: Quick transaction confirmation times
- **Ethereum security**: Inherits security from Ethereum mainnet
- **Developer-friendly**: Full EVM compatibility

### Key Facts about Base
- **Chain ID**: 8453 (mainnet), 84532 (testnet - Base-Sepolia)
- **Block time**: ~2 seconds
- **Gas token**: ETH (same as Ethereum)
- **Built by**: Coinbase

## EVM Fundamentals

The Ethereum Virtual Machine (EVM) is the runtime environment for smart contracts. Key concepts:

### 1. Accounts
- **Externally Owned Accounts (EOAs)**: Controlled by private keys
- **Contract Accounts**: Controlled by code, have no private key

### 2. Transactions
- **Value transfers**: Sending ETH between accounts
- **Contract calls**: Interacting with smart contracts
- **Contract creation**: Deploying new smart contracts

### 3. Gas
- **Purpose**: Prevents infinite loops and spam
- **Units**: Gas limit (max gas) × Gas price = Transaction cost
- **Base units**: Wei (1 ETH = 10^18 Wei)

### 4. Storage
- **Storage**: Persistent data on blockchain (expensive)
- **Memory**: Temporary data during execution (cheaper)
- **Stack**: Temporary data for computations (cheapest)

## Development Environment Setup

### Prerequisites
- Node.js (v16 or later)
- Git
- A code editor (VS Code recommended)

### Tools We'll Use
1. **Foundry**: Smart contract development framework
2. **Anvil**: Local blockchain for testing
3. **Python + web3.py**: For blockchain interactions
4. **Base-Sepolia**: Testnet for deployment

## Next Steps
In the next lesson, we'll install and configure Foundry, then create our first smart contract.

## Key Takeaways
- Base is a fast, cheap L2 built on Ethereum
- EVM provides a consistent environment for smart contracts
- Gas is the mechanism that prevents abuse and pays for computation
- We'll use Foundry for development and Base-Sepolia for testing
