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
    url = f"https://hackathon.lsp.team/hk/v1/wallets/{address}/nft/balance"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_money_balance(address: str) -> str:
    url = f"https://hackathon.lsp.team/hk/v1/wallets/{address}/balance"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def transfer_roubles(from_private: str, to_public: str,
                     roubles: float):
    url = "https://hackathon.lsp.team/hk/v1/transfers/ruble"

    payload = json.dumps({
        "fromPrivateKey": from_private,
        "toPublicKey": to_public,
        "amount": roubles
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def transfer_nft(from_private: str, to_public: str, nft_id: int):
    url = "https://hackathon.lsp.team/hk/v1/transfers/nft"

    payload = json.dumps({
        "fromPrivateKey": from_private,
        "toPublicKey": to_public,
        "tokenId": nft_id
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def buy_nft(nft_id: int, buyer_private: str, seller_public: str, seller_private: str, buyer_public: str,
            roubles: float):
    transfer_nft(nft_id=nft_id, to_public=buyer_public, from_private=seller_private)
    transfer_roubles(roubles=roubles, to_public=seller_public, from_private=buyer_private)
    return 200


def generate_nft_collection(to_public: str, uri: str, count: int = 1):
    import requests
    import json

    url = "https://hackathon.lsp.team/hk/v1/nft/generate"

    payload = json.dumps({
        "toPublicKey": f"{to_public}",
        "uri": f"{uri}",
        "nftCount": count
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.text


def get_nft_tokens(transaction_hash: str):
    url = f"https://hackathon.lsp.team/hk/v1/nft/generate/{transaction_hash}"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_nft_info(nft_id: int):
    url = f"https://hackathon.lsp.team/hk/v1/nft/{nft_id}"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


if __name__ == '__main__':
    print(get_money_balance(MAIN_WALLET_KEYS[0]))
    generate_nft_collection(MAIN_WALLET_KEYS[0], 'new_nft', 2)
