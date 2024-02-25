from pybit.unified_trading import HTTP 
import time 
import hashlib 
import hmac 
import base64
import requests 

api_key = 'V2IcREN12OgIyc3ELR'
api_secret = 'C:\\Users\\user\\bybit_automatic_trade\\test.pem'

endpoint = "/v5/order/create"
method = "POST"
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"0.1"}'



session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

server_time = session.get_server_time()['time']
recv_window = str(12000)

timestamp = str(int(time.time() * 1000))


request_params = f'{timestamp} {api_key} {recv_window}'

signature = hmac.new(api_secret.encode(), request_params.encode(), hashlib.sha256).digest()

encoded_signature = base64.b64encode(signature).decode()

x_bapi_sign_header = encoded_signature

headers = {
    'X-BAPI-SIGN': x_bapi_sign_header,
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'Content-Type': 'application/json',
}

response = requests.get('https://api-testnet.bybit.com/v5/order/create', headers=headers)

print(response)