#!/usr/bin/env python3
"""
Number Format Converter GUI

A simple Tkinter application for converting between different number formats
commonly used in blockchain development and learning.

Author: Base Learning Curriculum
"""

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional, Union


class NumberConverter:
    """Number format converter with validation and error handling."""

    @staticmethod
    def hex_to_decimal(hex_value: str) -> Optional[int]:
        """Convert hexadecimal to decimal."""
        try:
            # Remove 0x prefix if present
            hex_value = hex_value.replace("0x", "").replace("0X", "")
            return int(hex_value, 16)
        except ValueError:
            return None

    @staticmethod
    def decimal_to_hex(decimal_value: int, prefix: bool = True) -> str:
        """Convert decimal to hexadecimal."""
        hex_str = hex(decimal_value)
        return hex_str if prefix else hex_str[2:]

    @staticmethod
    def hex_to_binary(hex_value: str) -> Optional[str]:
        """Convert hexadecimal to binary."""
        try:
            # Remove 0x prefix if present
            hex_value = hex_value.replace("0x", "").replace("0X", "")
            decimal = int(hex_value, 16)
            return bin(decimal)
        except ValueError:
            return None

    @staticmethod
    def binary_to_hex(binary_value: str) -> Optional[str]:
        """Convert binary to hexadecimal."""
        try:
            # Remove 0b prefix if present
            binary_value = binary_value.replace("0b", "").replace("0B", "")
            decimal = int(binary_value, 2)
            return hex(decimal)
        except ValueError:
            return None

    @staticmethod
    def decimal_to_binary(decimal_value: int) -> str:
        """Convert decimal to binary."""
        return bin(decimal_value)

    @staticmethod
    def binary_to_decimal(binary_value: str) -> Optional[int]:
        """Convert binary to decimal."""
        try:
            # Remove 0b prefix if present
            binary_value = binary_value.replace("0b", "").replace("0B", "")
            return int(binary_value, 2)
        except ValueError:
            return None

    @staticmethod
    def wei_to_eth(wei_value: int) -> float:
        """Convert Wei to ETH."""
        return wei_value / 10**18

    @staticmethod
    def eth_to_wei(eth_value: float) -> int:
        """Convert ETH to Wei."""
        return int(eth_value * 10**18)

    @staticmethod
    def gwei_to_wei(gwei_value: float) -> int:
        """Convert Gwei to Wei."""
        return int(gwei_value * 10**9)

    @staticmethod
    def wei_to_gwei(wei_value: int) -> float:
        """Convert Wei to Gwei."""
        return wei_value / 10**9


class NumberConverterGUI:
    """Tkinter GUI for number format conversion."""

    def __init__(self, root):
        self.root = root
        self.root.title("Number Format Converter - Base Learning Curriculum")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        # Configure style
        style = ttk.Style()
        style.theme_use("clam")

        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame, text="Number Format Converter", font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Conversion type selection
        ttk.Label(main_frame, text="Conversion Type:").grid(row=1, column=0, sticky=tk.W, pady=5)

        self.conversion_var = tk.StringVar(value="hex_to_decimal")
        conversion_combo = ttk.Combobox(
            main_frame, textvariable=self.conversion_var, state="readonly", width=30
        )
        conversion_combo["values"] = (
            "Hexadecimal to Decimal",
            "Decimal to Hexadecimal",
            "Hexadecimal to Binary",
            "Binary to Hexadecimal",
            "Decimal to Binary",
            "Binary to Decimal",
            "Wei to ETH",
            "ETH to Wei",
            "Gwei to Wei",
            "Wei to Gwei",
        )
        conversion_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        conversion_combo.bind("<<ComboboxSelected>>", self.on_conversion_change)

        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        input_frame.columnconfigure(1, weight=1)

        ttk.Label(input_frame, text="Value:").grid(row=0, column=0, sticky=tk.W, pady=5)

        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var, font=("Courier", 10))
        self.input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.input_entry.bind("<KeyRelease>", self.on_input_change)

        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        output_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        output_frame.columnconfigure(1, weight=1)

        ttk.Label(output_frame, text="Result:").grid(row=0, column=0, sticky=tk.W, pady=5)

        self.output_var = tk.StringVar()
        self.output_entry = ttk.Entry(
            output_frame, textvariable=self.output_var, state="readonly", font=("Courier", 10)
        )
        self.output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        # Copy button
        copy_button = ttk.Button(output_frame, text="Copy", command=self.copy_output)
        copy_button.grid(row=0, column=2, padx=(10, 0), pady=5)

        # Examples section
        examples_frame = ttk.LabelFrame(main_frame, text="Examples", padding="10")
        examples_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        examples_frame.columnconfigure(0, weight=1)

        self.examples_text = tk.Text(examples_frame, height=8, wrap=tk.WORD, font=("Courier", 9))
        self.examples_text.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Scrollbar for examples
        scrollbar = ttk.Scrollbar(
            examples_frame, orient="vertical", command=self.examples_text.yview
        )
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.examples_text.configure(yscrollcommand=scrollbar.set)

        # Clear button
        clear_button = ttk.Button(main_frame, text="Clear All", command=self.clear_all)
        clear_button.grid(row=5, column=0, pady=20)

        # About button
        about_button = ttk.Button(main_frame, text="About", command=self.show_about)
        about_button.grid(row=5, column=2, pady=20)

        # Initialize examples
        self.update_examples()

        # Focus on input entry
        self.input_entry.focus()

    def on_conversion_change(self, event=None):
        """Handle conversion type change."""
        self.update_examples()
        self.on_input_change()

    def on_input_change(self, event=None):
        """Handle input change and perform conversion."""
        input_value = self.input_var.get().strip()

        if not input_value:
            self.output_var.set("")
            return

        conversion_type = self.conversion_var.get()
        result = self.perform_conversion(input_value, conversion_type)

        if result is not None:
            self.output_var.set(str(result))
        else:
            self.output_var.set("Invalid input")

    def perform_conversion(
        self, input_value: str, conversion_type: str
    ) -> Optional[Union[str, int, float]]:
        """Perform the actual conversion."""
        converter = NumberConverter()

        try:
            if conversion_type == "Hexadecimal to Decimal":
                return converter.hex_to_decimal(input_value)
            elif conversion_type == "Decimal to Hexadecimal":
                return converter.decimal_to_hex(int(input_value))
            elif conversion_type == "Hexadecimal to Binary":
                return converter.hex_to_binary(input_value)
            elif conversion_type == "Binary to Hexadecimal":
                return converter.binary_to_hex(input_value)
            elif conversion_type == "Decimal to Binary":
                return converter.decimal_to_binary(int(input_value))
            elif conversion_type == "Binary to Decimal":
                return converter.binary_to_decimal(input_value)
            elif conversion_type == "Wei to ETH":
                return converter.wei_to_eth(int(input_value))
            elif conversion_type == "ETH to Wei":
                return converter.eth_to_wei(float(input_value))
            elif conversion_type == "Gwei to Wei":
                return converter.gwei_to_wei(float(input_value))
            elif conversion_type == "Wei to Gwei":
                return converter.wei_to_gwei(int(input_value))
        except (ValueError, OverflowError):
            return None

        return None

    def copy_output(self):
        """Copy output to clipboard."""
        output_value = self.output_var.get()
        if output_value:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_value)
            messagebox.showinfo("Copied", "Output copied to clipboard!")

    def clear_all(self):
        """Clear all fields."""
        self.input_var.set("")
        self.output_var.set("")
        self.input_entry.focus()

    def update_examples(self):
        """Update examples based on current conversion type."""
        conversion_type = self.conversion_var.get()

        examples = {
            "Hexadecimal to Decimal": [
                "0x1A3 → 419",
                "0xFF → 255",
                "0x14a34 → 84532 (Base Sepolia Chain ID)",
                "0x2105 → 8453 (Base Mainnet Chain ID)",
            ],
            "Decimal to Hexadecimal": [
                "419 → 0x1a3",
                "255 → 0xff",
                "84532 → 0x14a34 (Base Sepolia Chain ID)",
                "8453 → 0x2105 (Base Mainnet Chain ID)",
            ],
            "Hexadecimal to Binary": [
                "0x1A → 0b11010",
                "0xFF → 0b11111111",
                "0x14a34 → 0b10100101000110100",
            ],
            "Binary to Hexadecimal": [
                "0b11010 → 0x1a",
                "0b11111111 → 0xff",
                "0b10100101000110100 → 0x14a34",
            ],
            "Decimal to Binary": [
                "26 → 0b11010",
                "255 → 0b11111111",
                "84532 → 0b10100101000110100",
            ],
            "Binary to Decimal": [
                "0b11010 → 26",
                "0b11111111 → 255",
                "0b10100101000110100 → 84532",
            ],
            "Wei to ETH": [
                "1000000000000000000 → 1.0 ETH",
                "500000000000000000 → 0.5 ETH",
                "1000000000000000 → 0.001 ETH",
            ],
            "ETH to Wei": [
                "1.0 → 1000000000000000000",
                "0.5 → 500000000000000000",
                "0.001 → 1000000000000000",
            ],
            "Gwei to Wei": ["1 → 1000000000", "20 → 20000000000", "100 → 100000000000"],
            "Wei to Gwei": ["1000000000 → 1.0", "20000000000 → 20.0", "100000000000 → 100.0"],
        }

        self.examples_text.delete(1.0, tk.END)
        for example in examples.get(conversion_type, []):
            self.examples_text.insert(tk.END, f"• {example}\n")

    def show_about(self):
        """Show about dialog."""
        about_text = """
Number Format Converter
Base Learning Curriculum

A simple tool for converting between different number formats
commonly used in blockchain development:

• Hexadecimal ↔ Decimal
• Binary ↔ Hexadecimal
• Binary ↔ Decimal
• Wei ↔ ETH
• Gwei ↔ Wei

Useful for:
• Understanding blockchain addresses
• Working with transaction data
• Learning number systems
• Debugging smart contracts

Author: Base Learning Curriculum
Version: 1.0.0
        """
        messagebox.showinfo("About", about_text)


def main():
    """Main function to run the application."""
    root = tk.Tk()
    NumberConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
