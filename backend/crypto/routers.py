import json

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

import requests

router = APIRouter(
    prefix='/marketplace',
    tags=['marketplace'],
)

MAIN_WALLET_KEYS = (
    '0x23079e657e898398c12e54D79BC191a193fA0e3b', 'e74439709384312484b9a545ae3d0cd55ca8f302b901e3446a30c3b30481ba72')


def create_wallet() -> (str, str):  # public key, private key
    url = "https://hackathon.lsp.team/hk/v1/wallets/new"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    return res["publicKey"], res["privateKey"]


def get_nft_balance(address: str) -> str:
    import requests

    url = f"https://hackathon.lsp.team/hk/v1/wallets/{address}/nft/balance"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_money_balance(address: str) -> str:
    import requests

    url = f"https://hackathon.lsp.team/hk/v1/wallets/{address}/balance"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def transfer_from_main_wallet():
    pass


if __name__ == '__main__':
    print(get_money_balance(MAIN_WALLET_KEYS[0]))

