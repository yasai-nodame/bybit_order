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


# payload_str = '&'.join([f"{key}={payload[key]}" for key in sorted(payload.keys())])
str_test = ''
for key in sorted(payload.keys()):
    str_test += f"{key}={payload[key]}"
    print(payload[key])
print(str_test)

