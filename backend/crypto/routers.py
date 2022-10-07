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


def create_wallet() -> (str, str):  # public key, private key
    url = "https://hackathon.lsp.team/hk/v1/wallets/new"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    return res["publicKey"], res["privateKey"]


if __name__ == '__main__':
    print(create_wallet())


