# Stage 0, Lesson 5: Python Web3 Integration

## Learning Objectives
- Set up Python environment for web3 development
- Interact with smart contracts using web3.py
- Handle transactions, events, and errors
- Create a CLI tool for contract interaction

## Python Environment Setup

### Installing Dependencies
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r python/requirements.txt

# Additional useful packages
pip install click rich pyyaml
```

### Project Structure
```
python/
├── common/
│   ├── rpc.py          # RPC connection handling
│   └── wallet.py       # Wallet management
├── stage0/
│   ├── hello_base.py   # Contract interaction
│   └── cli.py          # Command-line interface
└── requirements.txt
```

## Contract Interaction with web3.py

Create `python/stage0/hello_base.py`:

```python
import json
from typing import Dict, Any
from web3 import Web3
from web3.contract import Contract
from common.rpc import get_rpc
from common.wallet import load_account

class HelloBaseClient:
    def __init__(self, contract_address: str, abi_path: str = None):
        self.rpc = get_rpc()
        self.w3 = Web3(Web3.HTTPProvider(self.rpc.url))
        self.account = load_account()
        self.contract_address = contract_address
        
        # Load contract ABI
        if abi_path:
            with open(abi_path, 'r') as f:
                self.abi = json.load(f)
        else:
            # Default ABI for HelloBase contract
            self.abi = [
                {
                    "inputs": [{"internalType": "string", "name": "_message", "type": "string"}],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "anonymous": False,
                    "inputs": [
                        {"indexed": False, "internalType": "string", "name": "newMessage", "type": "string"},
                        {"indexed": True, "internalType": "address", "name": "updater", "type": "address"}
                    ],
                    "name": "MessageUpdated",
                    "type": "event"
                },
                {
                    "inputs": [],
                    "name": "getMessage",
                    "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "message",
                    "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "owner",
                    "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [{"internalType": "string", "name": "_newMessage", "type": "string"}],
                    "name": "updateMessage",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ]
        
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=self.abi
        )
    
    def get_message(self) -> str:
        """Get the current message from the contract."""
        return self.contract.functions.getMessage().call()
    
    def get_owner(self) -> str:
        """Get the contract owner address."""
        return self.contract.functions.owner().call()
    
    def update_message(self, new_message: str) -> str:
        """Update the contract message."""
        # Build transaction
        transaction = self.contract.functions.updateMessage(new_message).build_transaction({
            'from': self.account.address,
            'gas': 100000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
        })
        
        # Sign transaction
        signed_txn = self.w3.eth.account.sign_transaction(transaction, self.account.key)
        
        # Send transaction
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Wait for receipt
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt.transactionHash.hex()
    
    def get_events(self, from_block: int = 0, to_block: str = 'latest') -> list:
        """Get MessageUpdated events from the contract."""
        event_filter = self.contract.events.MessageUpdated.create_filter(
            fromBlock=from_block,
            toBlock=to_block
        )
        return event_filter.get_all_entries()
    
    def get_balance(self) -> int:
        """Get the account balance in wei."""
        return self.w3.eth.get_balance(self.account.address)
    
    def get_balance_eth(self) -> float:
        """Get the account balance in ETH."""
        balance_wei = self.get_balance()
        return self.w3.from_wei(balance_wei, 'ether')

def main():
    """Example usage of HelloBaseClient."""
    # Replace with your deployed contract address
    contract_address = "0x..."  # Your contract address here
    
    try:
        client = HelloBaseClient(contract_address)
        
        print(f"Connected to contract at: {contract_address}")
        print(f"Account: {client.account.address}")
        print(f"Balance: {client.get_balance_eth():.4f} ETH")
        print(f"Current message: {client.get_message()}")
        print(f"Contract owner: {client.get_owner()}")
        
        # Update message
        new_message = "Hello from Python!"
        print(f"\nUpdating message to: {new_message}")
        tx_hash = client.update_message(new_message)
        print(f"Transaction hash: {tx_hash}")
        
        # Verify update
        print(f"New message: {client.get_message()}")
        
        # Get recent events
        events = client.get_events()
        print(f"\nRecent events: {len(events)}")
        for event in events[-3:]:  # Show last 3 events
            print(f"  - {event['args']['newMessage']} by {event['args']['updater']}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

## Command-Line Interface

Create `python/stage0/cli.py`:

```python
import click
from rich.console import Console
from rich.table import Table
from hello_base import HelloBaseClient

console = Console()

@click.group()
def cli():
    """HelloBase CLI - Interact with your HelloBase contract."""
    pass

@cli.command()
@click.argument('contract_address')
@click.option('--abi-path', help='Path to contract ABI JSON file')
def info(contract_address, abi_path):
    """Get contract information."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        
        table = Table(title="Contract Information")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Contract Address", contract_address)
        table.add_row("Account", client.account.address)
        table.add_row("Balance", f"{client.get_balance_eth():.4f} ETH")
        table.add_row("Current Message", client.get_message())
        table.add_row("Owner", client.get_owner())
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@cli.command()
@click.argument('contract_address')
@click.argument('new_message')
@click.option('--abi-path', help='Path to contract ABI JSON file')
def update(contract_address, new_message, abi_path):
    """Update the contract message."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        
        console.print(f"[yellow]Updating message to: {new_message}[/yellow]")
        tx_hash = client.update_message(new_message)
        console.print(f"[green]Transaction sent: {tx_hash}[/green]")
        
        # Wait a moment and verify
        import time
        time.sleep(2)
        console.print(f"[green]New message: {client.get_message()}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@cli.command()
@click.argument('contract_address')
@click.option('--abi-path', help='Path to contract ABI JSON file')
@click.option('--count', default=5, help='Number of recent events to show')
def events(contract_address, abi_path, count):
    """Show recent contract events."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        events = client.get_events()
        
        if not events:
            console.print("[yellow]No events found.[/yellow]")
            return
        
        table = Table(title=f"Recent Events (last {min(count, len(events))})")
        table.add_column("Block", style="cyan")
        table.add_column("Message", style="green")
        table.add_column("Updater", style="blue")
        
        for event in events[-count:]:
            table.add_row(
                str(event['blockNumber']),
                event['args']['newMessage'],
                event['args']['updater']
            )
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    cli()
```

## Error Handling and Best Practices

### Common Errors and Solutions

1. **Insufficient Balance**
```python
if client.get_balance_eth() < 0.001:
    raise Exception("Insufficient balance for transaction")
```

2. **Transaction Reverted**
```python
try:
    tx_hash = client.update_message("test")
except Exception as e:
    if "revert" in str(e).lower():
        print("Transaction reverted - check contract state")
```

3. **Network Issues**
```python
try:
    message = client.get_message()
except Exception as e:
    print(f"Network error: {e}")
    # Implement retry logic
```

### Best Practices

1. **Always check balance before transactions**
2. **Handle network timeouts gracefully**
3. **Use proper gas estimation**
4. **Validate inputs before sending transactions**
5. **Log important operations**

## Exercise: Create Your CLI Tool

1. Deploy the HelloBase contract to Base-Sepolia
2. Update the contract address in the Python code
3. Test the CLI commands:
   ```bash
   python python/stage0/cli.py info <CONTRACT_ADDRESS>
   python python/stage0/cli.py update <CONTRACT_ADDRESS> "Hello from CLI!"
   python python/stage0/cli.py events <CONTRACT_ADDRESS>
   ```

## Next Steps
You've completed Stage 0! In the next stage, we'll dive deeper into Solidity fundamentals and build more complex contracts.

## Key Takeaways
- web3.py provides powerful tools for contract interaction
- CLI tools make contract interaction user-friendly
- Proper error handling is essential for production code
- Always validate inputs and check balances before transactions
