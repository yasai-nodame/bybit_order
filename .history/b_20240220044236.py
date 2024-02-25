import requests 
import hashlib 
import uuid 
from Crypto.Hash import SHA256 
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA 
import base64 
import time 


api_key = 'C2jIEwUnERzQBy1ool'
api_secret = "C:\\Users\\user\\Desktop\\bybit_api_secret.txt"

httpClient = requests.Session() 
recv_window = str(12000)
url = 'https://api-testnet.bybit.com'

time_stamp = int(time.time() * 10 ** 3) # time.time() * 1000と同じ 1000は1秒


def genSignature(payload,api_secret):
    param_str = str(time_stamp) + api_key + recv_window + payload 
    
    with open(api_secret, 'r') as private_key_obj:
        private_key_str = private_key_obj.read()
    
    private_key = RSA.import_key(private_key_str)
    encoded_param = SHA256.new(param_str.encode('utf-8'))
    signature = PKCS1_v1_5.new(private_key).sign(encoded_param)
    
    return base64.b64encode(signature).decode()

def HTTP_Request(endpoint,method,payload,Info):
    time_stamp = str(int(time.time() * 1000))
    signature = genSignature(payload, api_secret)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    
    if method == 'POST':
        response = httpClient.request(method, url+endpoint, headers=headers, json=json.loads(payload))
    else:
        response = httpClient.request(method, url+endpoint+'?'+payload, headers=headers)
    
    print(response.text)
    print(response.status_code)
    print(Info + 'Elapsed Time :' + str(response.elapsed))


endpoint = '/v5/order/create'
method = 'POST'
payload = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qtw":"0.1"}'
HTTP_Request(endpoint, method, payload, 'Create')