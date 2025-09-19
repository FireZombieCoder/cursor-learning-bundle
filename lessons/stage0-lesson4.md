# Stage 0, Lesson 4: Deploying to Base-Sepolia

## Learning Objectives
- Deploy smart contracts to Base-Sepolia testnet
- Understand the deployment process and verification
- Learn about faucets and testnet ETH
- Configure deployment scripts

## Base-Sepolia Testnet

Base-Sepolia is the testnet for Base, providing a safe environment for testing.

### Network Details
- **Chain ID**: 84532
- **RPC URL**: https://sepolia.base.org
- **Explorer**: https://sepolia.basescan.org
- **Faucet**: https://docs.base.org/docs/tools/network-faucets/

## Getting Testnet ETH

### Option 1: Base Sepolia Faucet
1. Visit the Base faucet
2. Connect your wallet
3. Request testnet ETH

### Option 2: Bridge from Ethereum Sepolia
1. Get ETH on Ethereum Sepolia testnet
2. Use the official bridge: https://bridge.base.org
3. Bridge ETH to Base Sepolia

### Option 3: Alternative Faucets
- Alchemy Faucet
- QuickNode Faucet
- Community faucets

## Deployment Scripts

Create a deployment script in `script/DeployHelloBase.s.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../src/HelloBase.sol";

contract DeployHelloBase is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        address deployer = vm.addr(deployerPrivateKey);
        
        console.log("Deploying contracts with account:", deployer);
        console.log("Account balance:", deployer.balance);
        
        vm.startBroadcast(deployerPrivateKey);
        
        HelloBase helloBase = new HelloBase("Hello Base Sepolia!");
        
        vm.stopBroadcast();
        
        console.log("HelloBase deployed to:", address(helloBase));
    }
}
```

## Deploying to Base-Sepolia

```bash
# Deploy to Base-Sepolia
forge script script/DeployHelloBase.s.sol:DeployHelloBase \
    --rpc-url base_sepolia \
    --broadcast \
    --verify \
    --etherscan-api-key $BASESCAN_API_KEY

# Check deployment
cast call <CONTRACT_ADDRESS> "getMessage()" --rpc-url base_sepolia
```

## Contract Verification

Verification makes your contract source code public and enables interaction through block explorers.

### Automatic Verification
```bash
# During deployment
forge script script/DeployHelloBase.s.sol:DeployHelloBase \
    --rpc-url base_sepolia \
    --broadcast \
    --verify
```

### Manual Verification
1. Go to https://sepolia.basescan.org
2. Find your contract
3. Click "Contract" tab
4. Click "Verify and Publish"
5. Upload source code and constructor arguments

## Interacting with Deployed Contracts

### Using Cast
```bash
# Read contract state
cast call <CONTRACT_ADDRESS> "message()" --rpc-url base_sepolia

# Send transaction
cast send <CONTRACT_ADDRESS> "updateMessage(string)" "New Message" \
    --private-key $PRIVATE_KEY \
    --rpc-url base_sepolia
```

### Using Python (Preview)
```python
from web3 import Web3
from common.rpc import get_rpc
from common.wallet import load_account

# Connect to Base-Sepolia
rpc = get_rpc()
w3 = Web3(Web3.HTTPProvider(rpc.url))

# Load account
account = load_account()

# Contract interaction (we'll cover this in detail later)
contract_address = "0x..."  # Your deployed contract
abi = [...]  # Contract ABI

contract = w3.eth.contract(address=contract_address, abi=abi)
message = contract.functions.getMessage().call()
print(f"Current message: {message}")
```

## Environment Configuration

Ensure your `.env` file is properly configured:

```bash
# Base-Sepolia configuration
BASE_SEPOLIA_RPC=https://sepolia.base.org
PRIVATE_KEY=your_private_key_here
CHAIN_ID=84532

# Optional: For contract verification
BASESCAN_API_KEY=your_basescan_api_key
```

## Common Deployment Issues

### 1. Insufficient Balance
```bash
# Check balance
cast balance <YOUR_ADDRESS> --rpc-url base_sepolia
```

### 2. Gas Estimation Failed
- Check contract constructor parameters
- Ensure all dependencies are available
- Verify network connectivity

### 3. Verification Failed
- Check constructor arguments
- Ensure source code matches deployed bytecode
- Verify compiler version and settings

## Best Practices

1. **Always test locally first**: Use Anvil before deploying
2. **Use deployment scripts**: Automate and document deployments
3. **Verify contracts**: Make source code public
4. **Monitor gas usage**: Optimize before mainnet deployment
5. **Keep private keys secure**: Never commit to version control

## Exercise: Deploy and Verify

1. Deploy the HelloBase contract to Base-Sepolia
2. Verify the contract on Basescan
3. Interact with the contract using Cast
4. Update the message and verify the change

## Next Steps
In the next lesson, we'll create Python scripts to interact with our deployed contract and learn about web3.py integration.

## Key Takeaways
- Base-Sepolia provides a safe testing environment
- Deployment scripts automate the process
- Contract verification is important for transparency
- Always test thoroughly before mainnet deployment
