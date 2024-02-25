import time 
import hashlib 
import hmac 
import base64 
from pybit.unified_trading import HTTP
import requests 
import json 

api_key = 'XW604zcK1Z8aYj4sPV'
recv_window = 12000
timestamp = str(int(time.time() * 1000) - int(recv_window))
time_stamp = str(int(time.time() * 1000))

payload = {
    "category": "spot",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Market",
    "qty": "0.1",
}

payload_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)

request_string = ' POST/v5/order/create' +  payload_str

signing_string = timestamp + recv_window + request_string 

private_key = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
hashed = hmac.new(private_key.encode('utf-8'), signing_string.encode('utf-8'), hashlib.sha256)
signature = base64.b64encode(hashed.digest()).decode()

print('X-BAPI-SIGN:', signature)


headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': str(recv_window),
        'Content-Type': 'application/json'
    }

httpClient = requests.Session()
url = 'https://api-testnet.bybit.com'
endpoint = '/v5/order/create'
method = 'POST'
response = httpClient.request(method, url+endpoint, headers=headers, data=payload_str)
print(response.text)
print(response.status_code)