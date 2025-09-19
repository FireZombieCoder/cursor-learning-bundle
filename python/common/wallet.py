import os

from eth_account import Account


def load_account():
    pk = os.getenv("PRIVATE_KEY")
    if not pk:
        raise RuntimeError("Set PRIVATE_KEY in .env")
    acct = Account.from_key(pk)
    return acct
