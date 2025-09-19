#!/usr/bin/env python3
"""
Number Converter Demo

Demonstrates the NumberConverter functionality with examples
commonly used in blockchain development.

Author: Base Learning Curriculum
"""

from python.tools.number_converter import NumberConverter


def demo_conversions():
    """Demonstrate various number format conversions."""
    print("🔢 Number Format Converter Demo")
    print("=" * 50)

    converter = NumberConverter()

    # Blockchain-specific examples
    print("\n🌐 Blockchain Examples:")
    print("-" * 30)

    # Chain IDs
    base_mainnet_chain_id = 8453
    base_sepolia_chain_id = 84532

    print("Base Mainnet Chain ID:")
    print(f"  Decimal: {base_mainnet_chain_id}")
    print(f"  Hex: {converter.decimal_to_hex(base_mainnet_chain_id)}")
    print(f"  Binary: {converter.decimal_to_binary(base_mainnet_chain_id)}")

    print("\nBase Sepolia Chain ID:")
    print(f"  Decimal: {base_sepolia_chain_id}")
    print(f"  Hex: {converter.decimal_to_hex(base_sepolia_chain_id)}")
    print(f"  Binary: {converter.decimal_to_binary(base_sepolia_chain_id)}")

    # Cryptocurrency conversions
    print("\n💰 Cryptocurrency Conversions:")
    print("-" * 30)

    # ETH to Wei
    eth_amounts = [1.0, 0.5, 0.001, 0.000001]
    for eth in eth_amounts:
        wei = converter.eth_to_wei(eth)
        print(f"  {eth} ETH = {wei:,} Wei")

    # Gwei to Wei
    gwei_amounts = [1, 20, 100, 1000]
    for gwei in gwei_amounts:
        wei = converter.gwei_to_wei(gwei)
        print(f"  {gwei} Gwei = {wei:,} Wei")

    # Common hex values
    print("\n🔢 Common Hex Values:")
    print("-" * 30)

    hex_values = ["0xFF", "0x1A3", "0x14a34", "0x2105"]
    for hex_val in hex_values:
        decimal = converter.hex_to_decimal(hex_val)
        binary = converter.hex_to_binary(hex_val)
        print(f"  {hex_val} = {decimal} = {binary}")

    # Binary examples
    print("\n🔢 Binary Examples:")
    print("-" * 30)

    binary_values = ["0b11010", "0b11111111", "0b10100101000110100"]
    for binary_val in binary_values:
        decimal = converter.binary_to_decimal(binary_val)
        hex_val = converter.binary_to_hex(binary_val)
        print(f"  {binary_val} = {decimal} = {hex_val}")


def demo_gas_calculations():
    """Demonstrate gas price calculations."""
    print("\n⛽ Gas Price Calculations:")
    print("-" * 30)

    converter = NumberConverter()

    # Common gas prices
    gas_prices_gwei = [1, 5, 10, 20, 50, 100]
    gas_limit = 21000  # Standard ETH transfer

    print("Gas Price | Wei Price | Total Cost (Wei) | Total Cost (ETH)")
    print("-" * 60)

    for gwei in gas_prices_gwei:
        wei_price = converter.gwei_to_wei(gwei)
        total_wei = gas_limit * wei_price
        total_eth = converter.wei_to_eth(total_wei)

        print(f"{gwei:8d} | {wei_price:9,} | {total_wei:15,} | {total_eth:.8f}")


def main():
    """Main demo function."""
    try:
        demo_conversions()
        demo_gas_calculations()

        print("\n🎉 Demo completed successfully!")
        print("\nTo use the GUI version, run:")
        print("  poetry run number-converter")
        print("  make number-converter")

    except Exception as e:
        print(f"❌ Demo failed: {e}")


if __name__ == "__main__":
    main()
