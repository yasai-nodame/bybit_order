from pybit.unified_trading import HTTP
import json 
import requests 
import hmac 
import base64
import time
import hashlib
import security
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
url = "https://api-testnet.bybit.com/v5/order/create"

timestamp = str(int(time.time() * 1000))

payload = {
    "api_key": api_key,
    "category": "spot",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Market",
    "qty": "1",
    "timestamp": timestamp
}


# payload_str = '&'.join([f"{key}={payload[key]}" for key in sorted(payload.keys())])　リスト内包表記ならこれ。
payload_str = ''
for key in sorted(payload.keys()):
    payload_str += f"{key}={payload[key]}&" #payload[key]でvalueが取得し、strの後ろに&をつけて連結させる。
payload_str = payload_str[:-1] # 最後の&だけ消す
print(payload_str)

