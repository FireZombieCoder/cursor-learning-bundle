#!/usr/bin/env python3
"""
HelloBase Contract Interaction Module

This module provides a Python interface to interact with the HelloBase smart contract
deployed on Base-Sepolia testnet. It demonstrates basic web3.py usage patterns.

Author: Base Learning Curriculum
"""

import json
import os
from typing import Dict, Any, List, Optional
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError, TransactionNotFound
from common.rpc import get_rpc
from common.wallet import load_account


class HelloBaseClient:
    """
    A client for interacting with the HelloBase smart contract.
    
    This class provides methods to read from and write to the HelloBase contract,
    handle events, and manage transactions.
    """
    
    def __init__(self, contract_address: str, abi_path: Optional[str] = None):
        """
        Initialize the HelloBase client.
        
        Args:
            contract_address: The address of the deployed HelloBase contract
            abi_path: Optional path to the contract ABI JSON file
        """
        self.rpc = get_rpc()
        self.w3 = Web3(Web3.HTTPProvider(self.rpc.url))
        self.account = load_account()
        self.contract_address = contract_address
        
        # Load contract ABI
        if abi_path and os.path.exists(abi_path):
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
                    "name": "getMessageLength",
                    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getOwner",
                    "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "isOwner",
                    "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
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
        """
        Get the current message from the contract.
        
        Returns:
            The current message stored in the contract
        """
        return self.contract.functions.getMessage().call()
    
    def get_owner(self) -> str:
        """
        Get the contract owner address.
        
        Returns:
            The address of the contract owner
        """
        return self.contract.functions.getOwner().call()
    
    def get_message_length(self) -> int:
        """
        Get the length of the current message.
        
        Returns:
            The length of the message in bytes
        """
        return self.contract.functions.getMessageLength().call()
    
    def is_owner(self, address: str) -> bool:
        """
        Check if an address is the contract owner.
        
        Args:
            address: The address to check
            
        Returns:
            True if the address is the owner, False otherwise
        """
        return self.contract.functions.isOwner(address).call()
    
    def update_message(self, new_message: str, gas_limit: int = 100000) -> str:
        """
        Update the contract message.
        
        Args:
            new_message: The new message to store
            gas_limit: Gas limit for the transaction
            
        Returns:
            The transaction hash
            
        Raises:
            ValueError: If the message is empty
            ContractLogicError: If the transaction reverts
        """
        if not new_message.strip():
            raise ValueError("Message cannot be empty")
        
        # Build transaction
        transaction = self.contract.functions.updateMessage(new_message).build_transaction({
            'from': self.account.address,
            'gas': gas_limit,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
        })
        
        # Sign transaction
        signed_txn = self.w3.eth.account.sign_transaction(transaction, self.account.key)
        
        # Send transaction
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Wait for receipt
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status == 0:
            raise ContractLogicError("Transaction reverted")
        
        return receipt.transactionHash.hex()
    
    def get_events(self, from_block: int = 0, to_block: str = 'latest') -> List[Dict[str, Any]]:
        """
        Get MessageUpdated events from the contract.
        
        Args:
            from_block: Starting block number
            to_block: Ending block number or 'latest'
            
        Returns:
            List of event logs
        """
        event_filter = self.contract.events.MessageUpdated.create_filter(
            fromBlock=from_block,
            toBlock=to_block
        )
        return event_filter.get_all_entries()
    
    def get_balance(self) -> int:
        """
        Get the account balance in wei.
        
        Returns:
            The account balance in wei
        """
        return self.w3.eth.get_balance(self.account.address)
    
    def get_balance_eth(self) -> float:
        """
        Get the account balance in ETH.
        
        Returns:
            The account balance in ETH
        """
        balance_wei = self.get_balance()
        return self.w3.from_wei(balance_wei, 'ether')
    
    def get_contract_info(self) -> Dict[str, Any]:
        """
        Get comprehensive contract information.
        
        Returns:
            Dictionary containing contract information
        """
        return {
            'contract_address': self.contract_address,
            'account': self.account.address,
            'balance_eth': self.get_balance_eth(),
            'current_message': self.get_message(),
            'message_length': self.get_message_length(),
            'owner': self.get_owner(),
            'is_owner': self.is_owner(self.account.address),
            'chain_id': self.rpc.chain_id
        }


def main():
    """
    Example usage of HelloBaseClient.
    
    This function demonstrates how to use the HelloBaseClient to interact
    with a deployed HelloBase contract.
    """
    # Replace with your deployed contract address
    contract_address = os.getenv("HELLO_BASE_CONTRACT_ADDRESS", "0x...")
    
    if contract_address == "0x...":
        print("Please set HELLO_BASE_CONTRACT_ADDRESS environment variable")
        print("Example: export HELLO_BASE_CONTRACT_ADDRESS=0x1234...")
        return
    
    try:
        client = HelloBaseClient(contract_address)
        
        # Get contract information
        info = client.get_contract_info()
        
        print("=== HelloBase Contract Information ===")
        print(f"Contract Address: {info['contract_address']}")
        print(f"Account: {info['account']}")
        print(f"Balance: {info['balance_eth']:.4f} ETH")
        print(f"Current Message: {info['current_message']}")
        print(f"Message Length: {info['message_length']} bytes")
        print(f"Owner: {info['owner']}")
        print(f"Is Owner: {info['is_owner']}")
        print(f"Chain ID: {info['chain_id']}")
        
        # Update message if we're the owner
        if info['is_owner']:
            new_message = "Hello from Python web3.py!"
            print(f"\nUpdating message to: {new_message}")
            
            tx_hash = client.update_message(new_message)
            print(f"Transaction hash: {tx_hash}")
            
            # Verify update
            updated_message = client.get_message()
            print(f"New message: {updated_message}")
        else:
            print("\nNote: You are not the contract owner, so you cannot update the message")
        
        # Get recent events
        events = client.get_events()
        print(f"\nRecent events: {len(events)}")
        for event in events[-3:]:  # Show last 3 events
            print(f"  - {event['args']['newMessage']} by {event['args']['updater']}")
            
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have:")
        print("1. Set up your .env file with PRIVATE_KEY and BASE_SEPOLIA_RPC")
        print("2. Deployed the HelloBase contract")
        print("3. Set the correct contract address")


if __name__ == "__main__":
    main()
