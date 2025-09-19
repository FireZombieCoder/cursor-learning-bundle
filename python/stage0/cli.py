#!/usr/bin/env python3
"""
HelloBase CLI Tool

A command-line interface for interacting with the HelloBase smart contract.
This tool provides easy-to-use commands for reading and writing to the contract.

Author: Base Learning Curriculum
"""

import click
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from hello_base import HelloBaseClient

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    HelloBase CLI - Interact with your HelloBase contract on Base-Sepolia.
    
    This tool provides commands to read contract state, update messages,
    and view transaction history.
    """
    pass


@cli.command()
@click.argument('contract_address')
@click.option('--abi-path', help='Path to contract ABI JSON file')
def info(contract_address, abi_path):
    """Get comprehensive contract information."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        info = client.get_contract_info()
        
        # Create a nice table for contract info
        table = Table(title="📋 Contract Information", show_header=True, header_style="bold magenta")
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")
        
        table.add_row("Contract Address", info['contract_address'])
        table.add_row("Your Account", info['account'])
        table.add_row("Balance", f"{info['balance_eth']:.4f} ETH")
        table.add_row("Current Message", info['current_message'])
        table.add_row("Message Length", f"{info['message_length']} bytes")
        table.add_row("Contract Owner", info['owner'])
        table.add_row("You are Owner", "✅ Yes" if info['is_owner'] else "❌ No")
        table.add_row("Chain ID", str(info['chain_id']))
        
        console.print(table)
        
        # Show network info
        network_name = "Base-Sepolia" if info['chain_id'] == 84532 else "Base Mainnet" if info['chain_id'] == 8453 else f"Unknown ({info['chain_id']})"
        console.print(f"\n🌐 Network: {network_name}")
        
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        console.print("\n[yellow]💡 Troubleshooting tips:[/yellow]")
        console.print("• Make sure your .env file is configured correctly")
        console.print("• Verify the contract address is correct")
        console.print("• Check that you have sufficient ETH balance")


@cli.command()
@click.argument('contract_address')
@click.argument('new_message')
@click.option('--abi-path', help='Path to contract ABI JSON file')
@click.option('--gas-limit', default=100000, help='Gas limit for the transaction')
def update(contract_address, new_message, abi_path, gas_limit):
    """Update the contract message."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        
        # Check if user is owner
        if not client.is_owner(client.account.address):
            console.print("[red]❌ Error: You are not the contract owner![/red]")
            console.print("[yellow]💡 Only the contract owner can update the message.[/yellow]")
            return
        
        # Check balance
        balance = client.get_balance_eth()
        if balance < 0.001:
            console.print(f"[red]❌ Error: Insufficient balance ({balance:.4f} ETH)[/red]")
            console.print("[yellow]💡 You need at least 0.001 ETH for transactions.[/yellow]")
            return
        
        console.print(f"[yellow]🔄 Updating message to: {new_message}[/yellow]")
        console.print(f"[blue]💰 Balance: {balance:.4f} ETH[/blue]")
        console.print(f"[blue]⛽ Gas limit: {gas_limit}[/blue]")
        
        # Update message
        tx_hash = client.update_message(new_message, gas_limit)
        
        console.print(f"[green]✅ Transaction sent successfully![/green]")
        console.print(f"[green]🔗 Transaction hash: {tx_hash}[/green]")
        
        # Wait a moment and verify
        import time
        console.print("[yellow]⏳ Waiting for confirmation...[/yellow]")
        time.sleep(3)
        
        updated_message = client.get_message()
        console.print(f"[green]✅ New message: {updated_message}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        console.print("\n[yellow]💡 Troubleshooting tips:[/yellow]")
        console.print("• Make sure you are the contract owner")
        console.print("• Check that you have sufficient ETH balance")
        console.print("• Verify the message is not empty")
        console.print("• Ensure the new message is different from the current one")


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
            console.print("[yellow]📭 No events found.[/yellow]")
            return
        
        # Create events table
        table = Table(title=f"📜 Recent Events (last {min(count, len(events))})", show_header=True, header_style="bold magenta")
        table.add_column("Block", style="cyan", no_wrap=True)
        table.add_column("Message", style="green")
        table.add_column("Updater", style="blue")
        table.add_column("Transaction", style="dim")
        
        for event in events[-count:]:
            # Truncate long messages
            message = event['args']['newMessage']
            if len(message) > 30:
                message = message[:27] + "..."
            
            # Truncate addresses
            updater = event['args']['updater']
            updater_short = updater[:6] + "..." + updater[-4:]
            
            tx_hash = event['transactionHash'].hex()
            tx_short = tx_hash[:8] + "..." + tx_hash[-6:]
            
            table.add_row(
                str(event['blockNumber']),
                message,
                updater_short,
                tx_short
            )
        
        console.print(table)
        
        # Show total events count
        console.print(f"\n[blue]📊 Total events: {len(events)}[/blue]")
        
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@cli.command()
@click.argument('contract_address')
@click.option('--abi-path', help='Path to contract ABI JSON file')
def balance(contract_address, abi_path):
    """Check your account balance."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        balance_eth = client.get_balance_eth()
        balance_wei = client.get_balance()
        
        # Create balance panel
        balance_text = Text()
        balance_text.append(f"{balance_eth:.6f} ETH\n", style="bold green")
        balance_text.append(f"{balance_wei:,} Wei", style="dim")
        
        panel = Panel(
            balance_text,
            title="💰 Account Balance",
            border_style="green"
        )
        
        console.print(panel)
        
        # Show recommendations
        if balance_eth < 0.001:
            console.print("\n[yellow]⚠️  Low balance warning![/yellow]")
            console.print("[yellow]💡 You may need more ETH for transactions.[/yellow]")
            console.print("[yellow]🔗 Get testnet ETH: https://docs.base.org/docs/tools/network-faucets/[/yellow]")
        elif balance_eth < 0.01:
            console.print("\n[blue]💡 Your balance is sufficient for basic transactions.[/blue]")
        else:
            console.print("\n[green]✅ You have plenty of ETH for transactions![/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@cli.command()
@click.argument('contract_address')
@click.option('--abi-path', help='Path to contract ABI JSON file')
def test(contract_address, abi_path):
    """Run a quick test of contract functionality."""
    try:
        client = HelloBaseClient(contract_address, abi_path)
        
        console.print("[blue]🧪 Running contract tests...[/blue]")
        
        # Test 1: Read current message
        current_message = client.get_message()
        console.print(f"[green]✅ Read message: {current_message}[/green]")
        
        # Test 2: Check owner
        owner = client.get_owner()
        is_owner = client.is_owner(client.account.address)
        console.print(f"[green]✅ Contract owner: {owner}[/green]")
        console.print(f"[green]✅ You are owner: {'Yes' if is_owner else 'No'}[/green]")
        
        # Test 3: Get message length
        length = client.get_message_length()
        console.print(f"[green]✅ Message length: {length} bytes[/green]")
        
        # Test 4: Check balance
        balance = client.get_balance_eth()
        console.print(f"[green]✅ Account balance: {balance:.4f} ETH[/green]")
        
        # Test 5: Get recent events
        events = client.get_events()
        console.print(f"[green]✅ Found {len(events)} events[/green]")
        
        console.print("\n[green]🎉 All tests passed! Contract is working correctly.[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")


@cli.command()
def setup():
    """Show setup instructions for using the CLI."""
    instructions = """
🔧 HelloBase CLI Setup Instructions

1. 📁 Environment Setup:
   • Copy .env.example to .env
   • Set your PRIVATE_KEY (without 0x prefix)
   • Set BASE_SEPOLIA_RPC=https://sepolia.base.org
   • Set CHAIN_ID=84532

2. 💰 Get Testnet ETH:
   • Visit: https://docs.base.org/docs/tools/network-faucets/
   • Connect your wallet and request ETH

3. 📝 Deploy Contract:
   • Use Foundry to deploy HelloBase contract
   • Save the contract address

4. 🚀 Use CLI:
   • python python/stage0/cli.py info <CONTRACT_ADDRESS>
   • python python/stage0/cli.py update <CONTRACT_ADDRESS> "New Message"
   • python python/stage0/cli.py events <CONTRACT_ADDRESS>

5. 🔍 Verify on Explorer:
   • Check your contract on: https://sepolia.basescan.org
    """
    
    console.print(Panel(instructions, title="📚 Setup Guide", border_style="blue"))


if __name__ == "__main__":
    cli()
