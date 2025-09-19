import os, json
from dotenv import load_dotenv
from web3 import Web3
from eth_account.messages import encode_defunct
from common.rpc import get_rpc
from common.wallet import load_account

def main():
    load_dotenv()
    rpc = get_rpc()
    w3 = Web3(Web3.HTTPProvider(rpc.url))
    acct = load_account()

    msg = encode_defunct(text="hello base")
    sig = w3.eth.account.sign_message(msg, private_key=acct.key)
    print("Address:", acct.address)
    print("ChainID:", rpc.chain_id)
    print("Sig (r,s,v):", sig.r, sig.s, sig.v)

if __name__ == "__main__":
    main()
