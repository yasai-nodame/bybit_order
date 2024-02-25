from pybit.unified_trading import HTTP 
import time 
import hashlib 
import hmac 
import base64
import requests 
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

api_key = 'C:\\Users\\user\\bybit_automatic_trade\\api_text.pem'
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


request_params = timestamp + api_key + recv_window + params

with open(api_secret, 'r') as f:
    private_key_str = f.read()
private_key = RSA.importKey(private_key_str)
encoded_param = SHA256.new(request_params.encode('utf-8'))
signature = PKCS1_v1_5.new(private_key).sign(encoded_param)
secret_test = base64.b64encode(signature).decode()

# signature = hmac.new(api_secret.encode(), request_params.encode(), hashlib.sha256).digest()

# encoded_signature = base64.b64encode(signature).decode()

# x_bapi_sign_header = encoded_signature



url = 'https://api-testnet.bybit.com'

httpClient = requests.Session()

method = 'POST'

headers = {
    'X-BAPI-SIGN': secret_test,
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'Content-Type': 'application/json',
}

response = httpClient.request(method,url+endpoint, headers=headers,data=params)

print(response.json())