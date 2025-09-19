#!/usr/bin/env python3
"""
Wallet Setup Verification Script

This script helps verify that your wallet is properly configured
for Base-Sepolia testnet development.

Author: Base Learning Curriculum
"""

import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from web3 import Web3

console = Console()


def check_environment():
    """Check if environment variables are set."""
    console.print("\n[blue]🔍 Checking Environment Configuration...[/blue]")

    required_vars = ["BASE_SEPOLIA_RPC", "PRIVATE_KEY"]
    missing_vars = []

    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        console.print(f"[red]❌ Missing environment variables: {', '.join(missing_vars)}[/red]")
        console.print("[yellow]💡 Make sure your .env file is configured correctly[/yellow]")
        return False
    else:
        console.print("[green]✅ Environment variables configured[/green]")
        return True


def check_network_connection():
    """Check connection to Base-Sepolia network."""
    console.print("\n[blue]🌐 Checking Network Connection...[/blue]")

    try:
        rpc_url = os.getenv("BASE_SEPOLIA_RPC", "https://sepolia.base.org")
        w3 = Web3(Web3.HTTPProvider(rpc_url))

        if w3.is_connected():
            chain_id = w3.eth.chain_id
            console.print(f"[green]✅ Connected to network (Chain ID: {chain_id})[/green]")

            if chain_id == 84532:
                console.print("[green]✅ Connected to Base-Sepolia testnet[/green]")
                return True
            else:
                console.print(
                    f"[yellow]⚠️  Connected to different network (Chain ID: {chain_id})[/yellow]"
                )
                console.print("[yellow]💡 Expected Chain ID: 84532 (Base-Sepolia)[/yellow]")
                return False
        else:
            console.print("[red]❌ Failed to connect to network[/red]")
            return False

    except Exception as e:
        console.print(f"[red]❌ Network connection error: {e}[/red]")
        return False


def check_wallet_balance():
    """Check wallet balance on Base-Sepolia."""
    console.print("\n[blue]💰 Checking Wallet Balance...[/blue]")

    try:
        from python.common.rpc import get_rpc
        from python.common.wallet import load_account

        rpc = get_rpc()
        w3 = Web3(Web3.HTTPProvider(rpc.url))
        account = load_account()

        balance_wei = w3.eth.get_balance(account.address)
        balance_eth = w3.from_wei(balance_wei, "ether")

        console.print(f"[green]✅ Wallet Address: {account.address}[/green]")
        console.print(f"[green]✅ Balance: {balance_eth:.6f} ETH[/green]")

        if balance_eth < 0.001:
            console.print("[yellow]⚠️  Low balance warning![/yellow]")
            console.print("[yellow]💡 You may need more ETH for transactions[/yellow]")
            console.print(
                "[yellow]🔗 Get testnet ETH: "
                "https://docs.base.org/docs/tools/network-faucets/[/yellow]"
            )
            return False
        else:
            console.print("[green]✅ Sufficient balance for transactions[/green]")
            return True

    except Exception as e:
        console.print(f"[red]❌ Wallet check error: {e}[/red]")
        return False


def show_network_info():
    """Show network information table."""
    console.print("\n[blue]📊 Network Information[/blue]")

    table = Table(title="Base-Sepolia Network Details")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Network Name", "Base Sepolia")
    table.add_row("Chain ID", "84532 (0x14a34)")
    table.add_row("RPC URL", "https://sepolia.base.org")
    table.add_row("Block Explorer", "https://sepolia.basescan.org")
    table.add_row("Currency", "ETH")
    table.add_row("Type", "Testnet")

    console.print(table)


def show_faucet_info():
    """Show faucet information."""
    console.print("\n[blue]🚰 Testnet Faucets[/blue]")

    faucets = [
        ("Base Official", "https://docs.base.org/docs/tools/network-faucets/"),
        ("Alchemy", "https://sepoliafaucet.com/"),
        ("QuickNode", "https://faucet.quicknode.com/base/sepolia"),
        ("Base Bridge", "https://bridge.base.org/"),
    ]

    table = Table(title="Available Faucets")
    table.add_column("Name", style="cyan")
    table.add_column("URL", style="green")

    for name, url in faucets:
        table.add_row(name, url)

    console.print(table)


def main():
    """Main verification function."""
    console.print(
        Panel(
            "Base-Sepolia Wallet Setup Verification",
            title="🔍 Wallet Setup Check",
            border_style="blue",
        )
    )

    # Run checks
    env_ok = check_environment()
    network_ok = check_network_connection()
    balance_ok = check_wallet_balance()

    # Show information
    show_network_info()
    show_faucet_info()

    # Summary
    console.print("\n[blue]📋 Summary[/blue]")

    if env_ok and network_ok and balance_ok:
        console.print("[green]🎉 All checks passed! Your wallet is ready for development.[/green]")
        console.print("\n[blue]Next steps:[/blue]")
        console.print("1. Deploy a test contract")
        console.print("2. Try the CLI tools: poetry run base-cli --help")
        console.print("3. Follow the Stage 0 curriculum")
        return 0
    else:
        console.print("[red]❌ Some checks failed. Please fix the issues above.[/red]")
        console.print("\n[blue]Common solutions:[/blue]")
        console.print("1. Check your .env file configuration")
        console.print("2. Get testnet ETH from a faucet")
        console.print("3. Verify you're connected to Base-Sepolia")
        return 1


if __name__ == "__main__":
    sys.exit(main())
