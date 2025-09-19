#!/usr/bin/env python3
"""
Tool Launcher

A simple launcher for various learning tools and utilities.

Author: Base Learning Curriculum
"""

import sys
import tkinter as tk
from tkinter import messagebox

from number_converter import NumberConverterGUI


def launch_number_converter():
    """Launch the number converter GUI."""
    try:
        root = tk.Tk()
        NumberConverterGUI(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch Number Converter: {e}")


def main():
    """Main launcher function."""
    if len(sys.argv) > 1:
        tool = sys.argv[1].lower()

        if tool == "converter" or tool == "number-converter":
            launch_number_converter()
        else:
            print(f"Unknown tool: {tool}")
            print("Available tools: converter")
            sys.exit(1)
    else:
        # Launch number converter by default
        launch_number_converter()


if __name__ == "__main__":
    main()
