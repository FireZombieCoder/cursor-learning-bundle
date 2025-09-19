#!/usr/bin/env python3
"""
Base Learning Curriculum CLI

Main entry point for the Base Learning Curriculum command-line tools.
This provides access to all stage-specific tools and utilities.

Author: Base Learning Curriculum
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def main():
    """
    Base Learning Curriculum CLI

    A comprehensive toolkit for learning Base L2 development,
    including smart contract interaction, web3 tools, and utilities.
    """
    pass


@main.group()
def stage0():
    """Stage 0: EVM Basics & Tooling commands."""
    pass


@stage0.command()
@click.argument("contract_address")
@click.option("--abi-path", help="Path to contract ABI JSON file")
def info(contract_address, abi_path):
    """Get comprehensive contract information."""
    from python.stage0.hello_base import HelloBaseClient

    try:
        client = HelloBaseClient(contract_address, abi_path)
        info = client.get_contract_info()

        # Create a nice table for contract info
        table = Text()
        table.append("📋 Contract Information\n", style="bold magenta")
        table.append(f"Contract Address: {info['contract_address']}\n", style="cyan")
        table.append(f"Your Account: {info['account']}\n", style="green")
        table.append(f"Balance: {info['balance_eth']:.4f} ETH\n", style="green")
        table.append(f"Current Message: {info['current_message']}\n", style="green")
        table.append(f"Message Length: {info['message_length']} bytes\n", style="green")
        table.append(f"Contract Owner: {info['owner']}\n", style="green")
        table.append(f"You are Owner: {'✅ Yes' if info['is_owner'] else '❌ No'}\n", style="green")
        table.append(f"Chain ID: {info['chain_id']}\n", style="green")

        panel = Panel(table, title="Contract Info", border_style="blue")
        console.print(panel)

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@stage0.command()
@click.argument("contract_address")
@click.argument("new_message")
@click.option("--abi-path", help="Path to contract ABI JSON file")
def update(contract_address, new_message, abi_path):
    """Update the contract message."""
    from python.stage0.hello_base import HelloBaseClient

    try:
        client = HelloBaseClient(contract_address, abi_path)

        if not client.is_owner(client.account.address):
            console.print("[red]❌ Error: You are not the contract owner![/red]")
            return

        console.print(f"[yellow]🔄 Updating message to: {new_message}[/yellow]")
        tx_hash = client.update_message(new_message)
        console.print(f"[green]✅ Transaction sent: {tx_hash}[/green]")

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@main.command()
def setup():
    """Show setup instructions for the curriculum."""
    instructions = """
🔧 Base Learning Curriculum Setup

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
   • poetry run base-cli stage0 info <CONTRACT_ADDRESS>
   • poetry run base-cli stage0 update <CONTRACT_ADDRESS> "New Message"

5. 🔍 Verify on Explorer:
   • Check your contract on: https://sepolia.basescan.org
    """

    console.print(Panel(instructions, title="📚 Setup Guide", border_style="blue"))


@main.command()
def version():
    """Show version information."""
    version_info = """
Base Learning Curriculum v0.1.0

📦 Package: base-learning-curriculum
🐍 Python: 3.10+
🔧 Poetry: Dependency management
🌐 Base: L2 blockchain development
    """

    console.print(Panel(version_info, title="Version Info", border_style="green"))


if __name__ == "__main__":
    main()
