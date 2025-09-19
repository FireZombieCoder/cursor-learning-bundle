"""
Common utilities for Base L2 development.

This module provides shared utilities for RPC connections,
wallet management, and other common blockchain operations.
"""

from .rpc import RPC, get_rpc
from .wallet import load_account

__all__ = ["RPC", "get_rpc", "load_account"]
