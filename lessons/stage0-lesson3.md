# Stage 0, Lesson 3: Testing and Gas Optimization

## Learning Objectives
- Write comprehensive tests using Foundry
- Understand gas costs and optimization techniques
- Learn about gas snapshots and benchmarking
- Practice debugging failed transactions

## Writing Tests with Foundry

Foundry uses Solidity for testing, making it fast and powerful.

### Basic Test Structure

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../src/HelloBase.sol";

contract HelloBaseTest is Test {
    HelloBase public helloBase;
    address public owner = address(1);
    address public user = address(2);
    
    function setUp() public {
        // Deploy contract with owner as msg.sender
        vm.prank(owner);
        helloBase = new HelloBase("Initial Message");
    }
    
    function testInitialMessage() public {
        assertEq(helloBase.message(), "Initial Message");
        assertEq(helloBase.owner(), owner);
    }
    
    function testUpdateMessage() public {
        vm.prank(owner);
        helloBase.updateMessage("New Message");
        assertEq(helloBase.message(), "New Message");
    }
    
    function testUnauthorizedUpdate() public {
        vm.prank(user);
        vm.expectRevert(HelloBase.Unauthorized.selector);
        helloBase.updateMessage("Hacked Message");
    }
    
    function testEventEmission() public {
        vm.expectEmit(true, true, true, true);
        emit HelloBase.MessageUpdated("Test Message", owner);
        
        vm.prank(owner);
        helloBase.updateMessage("Test Message");
    }
}
```

### Foundry Testing Utilities

1. **vm.prank()**: Sets msg.sender for next call
2. **vm.expectRevert()**: Expects next call to revert
3. **vm.expectEmit()**: Checks event emission
4. **assertEq()**: Asserts equality
5. **vm.deal()**: Gives ETH to an address

## Running Tests

```bash
# Run all tests
forge test

# Run with verbose output
forge test -vvv

# Run specific test
forge test --match-test testUpdateMessage

# Run with gas reporting
forge test --gas-report
```

## Gas Optimization

Understanding gas costs is crucial for efficient contracts.

### Gas Costs by Operation
- **SSTORE**: 20,000 gas (first time), 5,000 gas (subsequent)
- **SLOAD**: 2,100 gas
- **MSTORE**: 3 gas per word
- **MLOAD**: 3 gas per word
- **ADD/SUB**: 3 gas
- **MUL**: 5 gas
- **DIV**: 5 gas

### Optimization Techniques

1. **Pack structs**: Group small variables together
```solidity
struct User {
    uint128 balance;  // 16 bytes
    uint128 timestamp; // 16 bytes
    // Total: 32 bytes (1 storage slot)
}
```

2. **Use events instead of storage**: For data that doesn't need on-chain access
```solidity
event UserAction(address user, uint256 amount, uint256 timestamp);
```

3. **Custom errors**: More gas-efficient than require statements
```solidity
error InsufficientBalance(uint256 available, uint256 required);

function withdraw(uint256 amount) external {
    if (balance[msg.sender] < amount) {
        revert InsufficientBalance(balance[msg.sender], amount);
    }
}
```

4. **Batch operations**: Reduce transaction overhead
```solidity
function batchTransfer(address[] calldata recipients, uint256[] calldata amounts) external {
    // Single transaction for multiple transfers
}
```

## Gas Snapshots

Track gas usage over time:

```bash
# Create gas snapshot
forge snapshot

# Compare snapshots
forge snapshot --diff .gas-snapshot
```

## Debugging Failed Transactions

### Using Cast for Debugging

```bash
# Get transaction trace
cast run <TX_HASH> --rpc-url <RPC_URL>

# Get call trace
cast call <CONTRACT_ADDRESS> <FUNCTION_SIGNATURE> --rpc-url <RPC_URL>

# Decode transaction data
cast tx <TX_HASH> --rpc-url <RPC_URL>
```

### Common Issues and Solutions

1. **Out of gas**: Increase gas limit or optimize code
2. **Revert**: Check error messages and conditions
3. **Invalid opcode**: Ensure contract is deployed correctly
4. **Nonce issues**: Check account nonce

## Exercise: Optimize the HelloBase Contract

Try to optimize this contract for gas efficiency:

```solidity
contract HelloBaseOptimized {
    string public message;
    address public immutable owner; // immutable is cheaper than storage
    
    event MessageUpdated(string indexed newMessage, address indexed updater);
    
    error Unauthorized();
    
    constructor(string memory _message) {
        message = _message;
        owner = msg.sender;
    }
    
    function updateMessage(string calldata _newMessage) external {
        if (msg.sender != owner) revert Unauthorized();
        message = _newMessage;
        emit MessageUpdated(_newMessage, msg.sender);
    }
}
```

### Key Optimizations:
- `immutable` for owner (set once, cheaper than storage)
- `calldata` for string parameter (cheaper than memory)
- `indexed` event parameters (enables filtering)

## Next Steps
In the next lesson, we'll deploy to Base-Sepolia testnet and interact with our contract using Python.

## Key Takeaways
- Foundry tests are fast and powerful
- Gas optimization requires understanding EVM operations
- Gas snapshots help track performance over time
- Proper debugging tools are essential for development
