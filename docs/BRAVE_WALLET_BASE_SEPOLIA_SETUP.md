# Brave Wallet Setup for Base-Sepolia Testnet

## 🎯 Overview

This guide will help you configure your Brave wallet to work with Base-Sepolia testnet for the Base Learning Curriculum. You'll learn how to add the network, get testnet ETH, and use it for smart contract development.

## 🔧 Step 1: Add Base-Sepolia Network to Brave Wallet

### Method 1: Manual Network Addition

1. **Open Brave Wallet**
   - Click the Brave wallet icon in your browser toolbar
   - Or go to `brave://wallet/`

2. **Access Network Settings**
   - Click the network dropdown (usually shows "Ethereum Mainnet")
   - Click "Add network" or "Custom network"

3. **Add Base-Sepolia Network**
   - Click "Add a network manually"
   - Fill in the following details:

```
Network Name: Base Sepolia
RPC URL: https://sepolia.base.org
Chain ID: 84532
Currency Symbol: ETH
Block Explorer URL: https://sepolia.basescan.org
```

4. **Save the Network**
   - Click "Save" to add the network
   - Switch to "Base Sepolia" network

### Method 2: Using Chainlist (Recommended)

1. **Visit Chainlist**
   - Go to https://chainlist.org/
   - Search for "Base Sepolia"
   - Click "Connect Wallet"
   - Select your Brave wallet
   - Click "Add to Brave Wallet"

2. **Confirm Addition**
   - Brave wallet will prompt you to add the network
   - Click "Approve" to add Base-Sepolia

## 💰 Step 2: Get Base-Sepolia Testnet ETH

### Option 1: Base Official Faucet (Recommended)

1. **Visit Base Faucet**
   - Go to https://docs.base.org/docs/tools/network-faucets/
   - Click on "Base Sepolia Faucet"

2. **Connect Your Wallet**
   - Click "Connect Wallet"
   - Select Brave wallet
   - Approve the connection

3. **Request Testnet ETH**
   - Your wallet address should appear
   - Click "Request Sepolia ETH"
   - Wait for the transaction to complete

### Option 2: Alchemy Faucet

1. **Visit Alchemy Faucet**
   - Go to https://sepoliafaucet.com/
   - Enter your wallet address
   - Complete any required verification
   - Click "Send Me ETH"

### Option 3: QuickNode Faucet

1. **Visit QuickNode Faucet**
   - Go to https://faucet.quicknode.com/base/sepolia
   - Connect your wallet
   - Request testnet ETH

### Option 4: Bridge from Ethereum Sepolia

If you have ETH on Ethereum Sepolia testnet:

1. **Visit Base Bridge**
   - Go to https://bridge.base.org/
   - Connect your wallet
   - Select "Ethereum Sepolia" to "Base Sepolia"
   - Enter the amount to bridge
   - Complete the bridge transaction

## 🔍 Step 3: Verify Your Setup

### Check Your Balance

1. **Switch to Base Sepolia**
   - In Brave wallet, select "Base Sepolia" network
   - Check your ETH balance

2. **View on Block Explorer**
   - Go to https://sepolia.basescan.org/
   - Enter your wallet address
   - Verify your balance and transactions

### Test a Transaction

1. **Send a Small Amount**
   - Send 0.001 ETH to another address (or back to yourself)
   - Verify the transaction appears on Basescan

## 🛠️ Step 4: Configure for Development

### Update Your .env File

Make sure your `.env` file is configured correctly:

```bash
# Base-Sepolia Configuration
BASE_SEPOLIA_RPC=https://sepolia.base.org
CHAIN_ID=84532

# Your wallet private key (without 0x prefix)
PRIVATE_KEY=your_private_key_here

# Optional: Gas settings
GAS_LIMIT=300000
GAS_PRICE=1000000000  # 1 gwei
```

### Get Your Private Key

⚠️ **Security Warning**: Never share your private key or commit it to version control!

1. **Export Private Key from Brave Wallet**
   - Open Brave wallet
   - Click the three dots menu
   - Go to "Account details"
   - Click "Show private key"
   - Enter your password
   - Copy the private key (remove the 0x prefix)

2. **Add to .env File**
   ```bash
   PRIVATE_KEY=your_private_key_without_0x_prefix
   ```

## 🧪 Step 5: Test with the Learning Curriculum

### Test CLI Tools

```bash
# Check your setup
poetry run base-cli version

# Test contract interaction (after deploying)
poetry run base-cli stage0 info <CONTRACT_ADDRESS>
```

### Deploy a Test Contract

1. **Deploy HelloBase Contract**
   ```bash
   # Deploy to Base-Sepolia
   forge script script/DeployHelloBase.s.sol:DeployHelloBase \
       --rpc-url base_sepolia \
       --broadcast \
       --verify
   ```

2. **Interact with Contract**
   ```bash
   # Update the contract message
   poetry run base-cli stage0 update <CONTRACT_ADDRESS> "Hello Base Sepolia!"
   ```

## 🔧 Troubleshooting

### Common Issues

**1. Network Not Found**
- Ensure you're using the correct Chain ID: 84532
- Double-check the RPC URL: https://sepolia.base.org
- Try refreshing the page and reconnecting

**2. No ETH Balance**
- Check if the faucet transaction completed
- Verify you're on the correct network (Base Sepolia)
- Try a different faucet if one isn't working

**3. Transaction Failures**
- Ensure you have sufficient ETH for gas
- Check the gas limit and price settings
- Verify the contract address is correct

**4. Connection Issues**
- Clear browser cache and cookies
- Restart Brave browser
- Check if Brave wallet is up to date

### Getting Help

**Base Documentation:**
- https://docs.base.org/
- https://docs.base.org/docs/tools/network-faucets/

**Block Explorers:**
- Base Sepolia: https://sepolia.basescan.org/
- Ethereum Sepolia: https://sepolia.etherscan.io/

**Community:**
- Base Discord: https://discord.gg/buildonbase
- Base Twitter: @base

## 🎯 Next Steps

Once you have Base-Sepolia ETH:

1. **Complete Stage 0 Lessons**
   - Follow the curriculum lessons
   - Deploy your first smart contract
   - Test contract interactions

2. **Explore the CLI Tools**
   - Use `poetry run base-cli --help`
   - Try the Stage 0 commands
   - Experiment with contract interactions

3. **Build Your Skills**
   - Practice with different contract types
   - Learn gas optimization
   - Explore advanced features

## 🔒 Security Best Practices

1. **Never Share Private Keys**
   - Keep your private key secure
   - Use environment variables
   - Never commit keys to version control

2. **Use Testnet Only**
   - Base-Sepolia is for testing only
   - Don't use real ETH on testnets
   - Be careful when switching networks

3. **Verify Transactions**
   - Always check block explorers
   - Verify contract addresses
   - Double-check transaction details

## 📚 Additional Resources

- [Base Learning Curriculum](STAGE0_README.md)
- [Poetry Setup Guide](POETRY_SETUP.md)
- [Base Documentation](https://docs.base.org/)
- [Ethereum Development Tools](https://ethereum.org/developers/)

Happy learning and building on Base! 🚀
