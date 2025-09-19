from web3 import Web3
from dataclasses import dataclass
import os

@dataclass
class RPC:
    url: str
    chain_id: int

def get_rpc() -> RPC:
    url = os.getenv("BASE_SEPOLIA_RPC") or os.getenv("BASE_MAINNET_RPC")
    if not url:
        raise RuntimeError("Set BASE_SEPOLIA_RPC or BASE_MAINNET_RPC in .env")
    w3 = Web3(Web3.HTTPProvider(url, request_kwargs={"timeout": 30}))
    cid = w3.eth.chain_id
    exp = int(os.getenv("CHAIN_ID", cid))
    if cid != exp:
        raise RuntimeError(f"Connected chain_id {cid} != expected {exp}")
    return RPC(url, cid)
