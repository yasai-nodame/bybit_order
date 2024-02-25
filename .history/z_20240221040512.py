import time 
import hashlib 
import hmac 
import base64 
from pybit.unified_trading import HTTP
import requests 

api_key = 'V2IcREN12OgIyc3ELR'
recv_window = '12000'
timestamp = str(int(time.time() * 1000) - int(recv_window))
time_stamp = str(int(time.time() * 1000))

payload = '{"symbol": "BTCUSDT", "side": "Buy", "orderType": "Market", "category": "spot", "qty": "0.1"}'

request_string = 'POST/v5/order/create' +  payload 

signing_string = timestamp + recv_window + request_string 

private_key = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
hashed = hmac.new(private_key.encode('utf-8'), signing_string.encode('utf-8'), hashlib.sha256)
signature = base64.b64encode(hashed.digest()).decode()

print('X-BAPI-SIGN:', signature)

headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }

params = {
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Market",
    "category": "spot",
    "qty": "0.1",
}

httpClient = requests.Session()
url = 'https://api-testnet.bybit.com'
endpoint = '/v5/order/create'
method = 'POST'
response = httpClient.request()