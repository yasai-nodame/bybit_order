import requests 
import time 
import test 
import config 

api_key = config.API_KEY
api_secret = config.API_SECRET

url = 'https://api-testnet.bybit.com'

def get_order_status(order_id):
    endpoint = '/v5/order'
    method = 'GET'
    params = {
        'order_id': order_id
    }
    
    payload_str = '&'.join([f'{key}={params[key]}' for key in sorted(params.keys())])
    time_stamp = str(int(time.time() * 1000))
    signature = test.genSignature(payload_str)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    
    response = requests.request(method, url+endpoint+'?'+payload_str, headers=headers)
    return response.json()


order_id = '1626435149682185472'
order_status = get_order_status(order_id)
print(order_status)