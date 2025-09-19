# Number Format Converter Tool

## 🎯 Overview

The Number Format Converter is a simple Tkinter GUI application designed to help with learning different number formats commonly used in blockchain development. It provides easy conversion between hexadecimal, decimal, binary, and cryptocurrency units.

## 🚀 Quick Start

### Launch the Application

```bash
# Using Poetry
poetry run number-converter

# Using Make
make number-converter

# Using tools launcher
poetry run tools
```

### Basic Usage

1. **Select Conversion Type**: Choose from the dropdown menu
2. **Enter Input Value**: Type your number in the input field
3. **View Result**: The converted value appears automatically
4. **Copy Result**: Click "Copy" to copy the result to clipboard

## 🔧 Available Conversions

### Number System Conversions

| From | To | Description | Example |
|------|----|-----------|---------|
| Hexadecimal | Decimal | Convert hex to decimal | `0x1A3` → `419` |
| Decimal | Hexadecimal | Convert decimal to hex | `419` → `0x1a3` |
| Hexadecimal | Binary | Convert hex to binary | `0x1A` → `0b11010` |
| Binary | Hexadecimal | Convert binary to hex | `0b11010` → `0x1a` |
| Decimal | Binary | Convert decimal to binary | `26` → `0b11010` |
| Binary | Decimal | Convert binary to decimal | `0b11010` → `26` |

### Cryptocurrency Unit Conversions

| From | To | Description | Example |
|------|----|-----------|---------|
| Wei | ETH | Convert Wei to ETH | `1000000000000000000` → `1.0` |
| ETH | Wei | Convert ETH to Wei | `1.0` → `1000000000000000000` |
| Gwei | Wei | Convert Gwei to Wei | `20` → `20000000000` |
| Wei | Gwei | Convert Wei to Gwei | `20000000000` → `20.0` |

## 🎓 Learning Examples

### Blockchain-Specific Examples

**Chain IDs:**
- Base Mainnet: `8453` (decimal) = `0x2105` (hex)
- Base Sepolia: `84532` (decimal) = `0x14a34` (hex)

**Gas Units:**
- 1 ETH = `1000000000000000000` Wei
- 1 Gwei = `1000000000` Wei
- Typical gas price: `20` Gwei = `20000000000` Wei

**Address Formats:**
- Ethereum addresses are 40 hex characters
- Example: `0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6`

### Common Use Cases

1. **Understanding Transaction Data**
   - Convert gas prices from Gwei to Wei
   - Convert ETH amounts to Wei for smart contracts

2. **Working with Chain IDs**
   - Convert between decimal and hex formats
   - Understand network identifiers

3. **Debugging Smart Contracts**
   - Convert between different number formats
   - Understand return values and parameters

4. **Learning Number Systems**
   - Practice binary, hex, and decimal conversions
   - Understand how computers represent numbers

## 🖥️ GUI Features

### Main Interface

- **Conversion Type Dropdown**: Select the type of conversion
- **Input Field**: Enter the value to convert
- **Output Field**: View the converted result (read-only)
- **Copy Button**: Copy result to clipboard
- **Examples Panel**: See examples for the selected conversion type

### Keyboard Shortcuts

- **Enter**: Focus on input field
- **Ctrl+C**: Copy output (when output field is focused)
- **Escape**: Clear all fields

### Error Handling

- Invalid input shows "Invalid input" message
- Supports various input formats (with or without prefixes)
- Handles overflow and underflow gracefully

## 🔧 Technical Details

### Supported Input Formats

**Hexadecimal:**
- With prefix: `0x1A3`, `0X1A3`
- Without prefix: `1A3`, `1a3`

**Binary:**
- With prefix: `0b11010`, `0B11010`
- Without prefix: `11010`

**Decimal:**
- Standard integers: `419`, `-255`
- Floating point: `1.5`, `0.001`

### Precision and Limits

- **Integer conversions**: Limited by Python's int size
- **Floating point**: Standard Python float precision
- **Wei conversions**: 18 decimal places for ETH
- **Gwei conversions**: 9 decimal places for Wei

## 🎯 Educational Value

### Learning Objectives

1. **Number System Understanding**
   - Binary, decimal, and hexadecimal systems
   - How computers represent numbers
   - Base conversion algorithms

2. **Blockchain Concepts**
   - Cryptocurrency units (Wei, Gwei, ETH)
   - Gas pricing and calculations
   - Chain ID formats

3. **Development Skills**
   - Working with different number formats
   - Understanding smart contract data
   - Debugging and troubleshooting

### Best Practices

1. **Always verify conversions** using multiple methods
2. **Understand the context** of each number format
3. **Use appropriate precision** for financial calculations
4. **Be aware of overflow** in large number operations

## 🛠️ Development

### File Structure

```
python/tools/
├── __init__.py
├── number_converter.py    # Main converter logic and GUI
└── launcher.py           # Tool launcher
```

### Key Classes

- **NumberConverter**: Core conversion logic
- **NumberConverterGUI**: Tkinter GUI implementation

### Adding New Conversions

To add new conversion types:

1. Add method to `NumberConverter` class
2. Update conversion type dropdown in GUI
3. Add examples for the new conversion
4. Update `perform_conversion` method

## 🚀 Usage in Learning Curriculum

### Stage 0 Integration

The Number Converter is particularly useful for:

1. **Understanding EVM Basics**
   - Converting between number formats
   - Understanding gas calculations
   - Working with addresses and data

2. **Smart Contract Development**
   - Converting function parameters
   - Understanding return values
   - Debugging contract interactions

3. **Python Integration**
   - Understanding web3.py data types
   - Converting between formats
   - Working with blockchain data

### Example Workflow

1. **Start the converter**: `poetry run number-converter`
2. **Convert gas price**: 20 Gwei → Wei
3. **Use in contract**: Set gas price in transaction
4. **Verify result**: Check transaction on block explorer

## 📚 Additional Resources

- [Base Learning Curriculum](STAGE0_README.md)
- [Poetry Setup Guide](POETRY_SETUP.md)
- [Brave Wallet Setup](BRAVE_WALLET_BASE_SEPOLIA_SETUP.md)
- [Base Documentation](https://docs.base.org/)

## 🎉 Conclusion

The Number Format Converter is a valuable learning tool that helps bridge the gap between theoretical knowledge and practical blockchain development. It provides immediate feedback and examples to reinforce understanding of different number systems and their applications in blockchain technology.

Happy learning and converting! 🚀
