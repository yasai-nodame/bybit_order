import requests 
import time 
import hashlib 
import hmac 
import config

api_key = config.API_KEY
secret_key = config.API_SECRET
httpClient = requests.Session() 
recv_window = str(10000)
url = 'https://api-testnet.bybit.com'

def HTTP_Request(endpoint,method,payload,Info):
    global time_stamp
    time_stamp = str(int(time.time() * 1000))
    signature = genSignature(payload)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/jso'
    }
    
    if method == 'POST':
        response = httpClient.request(method, url+endpoint, headers=headers, data=payload)
    else:
        response = httpClient.request(method, url+endpoint+'?'+payload, headers=headers)
    print(response.text)
    print(Info + 'Elapsed time : ' + str(response.elapsed))
    
def genSignature(payload):
    param_str = str(time_stamp) + api_key + recv_window + payload
    hash = hmac.new(bytes(secret_key, 'utf-8'), param_str.encode('utf-8'), hashlib.sha256)
    signature = hash.hexdigest()
    return signature 

endpoint = "/v5/order/create"
method = 'POST'
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"1"}'


HTTP_Request(endpoint, method, params, 'Create')


