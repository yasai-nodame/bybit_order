import requests 
import time 
import hashlib 
import hmac 
import uuid 

api_key = 'XW604zcK1Z8aYj4sPV'
secret_key = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
httpClient = requests.Session() 
recv_window = str(5000)
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
        'Content-Type': 'application/json'
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

def get_order_list():
    orderLinkId = '885f96eb9bbb4d43b0f1b3b63a2bb741'
    endpoint = '/spot/v3/private/order'
    method = 'GET'
    params='orderLinkId=' + orderLinkId
    HTTP_Request(endpoint,method,params,"List")

endpoint = "/v5/order/create"
method = 'POST'
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"1"}'
# HTTP_Request(endpoint, method, params, 'Create')


from pybit.unified_trading import HTTP
session = HTTP(
    testnet=True,
    api_key=api_key,
    api_secret=secret_key
)

response=session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    qty="1"
)


print(response)

def gen_sig(data):
    signature = hmac.new(secret_key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

def get_order_status(order_id):
    timestamp = str(int(time.time() * 1000))
    data = f"order_id={order_id}&api_key={api_key}&timestamp={timestamp}&recv_window={recv_window}"
    signature = gen_sig(data)

    url = f"https://api-testnet.bybit.com/spot/v3/private/order?{data}&sign={signature}"

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)
    return response.json()

# 注文IDを設定
order_id = '1626538029466522880'

# 注文の状態を取得
order_status = get_order_status(order_id)
print(order_status)