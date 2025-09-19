"""
Stage 0: EVM Basics & Tooling

This module contains tools and utilities for Stage 0 of the Base Learning Curriculum,
including smart contract interaction clients and CLI tools.
"""

from .cli import cli
from .hello_base import HelloBaseClient

__all__ = ["HelloBaseClient", "cli"]
