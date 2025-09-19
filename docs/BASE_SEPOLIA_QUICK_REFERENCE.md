# Base-Sepolia Quick Reference

## 🔧 Network Configuration

```
Network Name: Base Sepolia
RPC URL: https://sepolia.base.org
Chain ID: 84532 (0x14a34)
Currency Symbol: ETH
Block Explorer: https://sepolia.basescan.org
```

## 💰 Faucets

### Primary Faucets
- **Base Official**: https://docs.base.org/docs/tools/network-faucets/
- **Alchemy**: https://sepoliafaucet.com/
- **QuickNode**: https://faucet.quicknode.com/base/sepolia

### Bridge from Ethereum Sepolia
- **Base Bridge**: https://bridge.base.org/

## 🔍 Block Explorers

- **Base Sepolia**: https://sepolia.basescan.org/
- **Ethereum Sepolia**: https://sepolia.etherscan.io/

## 🛠️ Development Tools

### CLI Commands
```bash
# Check setup
poetry run base-cli version

# Contract interaction
poetry run base-cli stage0 info <CONTRACT_ADDRESS>
poetry run base-cli stage0 update <CONTRACT_ADDRESS> "Message"

# Deploy contract
forge script script/DeployHelloBase.s.sol:DeployHelloBase \
    --rpc-url base_sepolia \
    --broadcast \
    --verify
```

### Environment Variables
```bash
BASE_SEPOLIA_RPC=https://sepolia.base.org
CHAIN_ID=84532
PRIVATE_KEY=your_private_key_here
```

## 🔗 Useful Links

- **Base Documentation**: https://docs.base.org/
- **Base Discord**: https://discord.gg/buildonbase
- **Chainlist**: https://chainlist.org/ (for easy network addition)
- **Base Bridge**: https://bridge.base.org/

## ⚠️ Important Notes

- Base-Sepolia is a **testnet** - use only for testing
- Never use real ETH on testnets
- Keep your private keys secure
- Always verify transactions on block explorers
