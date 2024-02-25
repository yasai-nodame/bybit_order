import requests 
import config 
import test 
import time 

api_key = config.API_KEY
recv_window = str(5000)
time_stamp = str(int(time.time() * 1000))

httpClient = requests.Session()

def get_order(order_id,payload,method):
    url = f'https://api-testnet.bybit.com/spot/v3/private/order?orderLinkId={order_id}'

    
    signature = test.genSignature(payload)
    
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    
    response = httpClient.request(method,url,headers=headers,data=payload)
    print(response)
    return response.text

method = 'GET'
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"1"}'
order_id = '1626443226527569152'
get_order(order_id,params,method)
