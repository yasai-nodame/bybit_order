import requests 
import config 
import test 
import time 

api_key = config.API_KEY
recv_window = str(5000)
time_stamp = str(int(time.time() * 1000))

httpClient = requests.Session()

order_id = '1626455659124102401'
api_key = config.API_KEY
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"1"}'
signature = test.genSignature(params)

url = f'https://api-testnet.bybit.com/spot/v3/private/order?orderLinkId={order_id}'

headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }

response = httpClient.request('GET',url,headers=headers,data=params)

print(response.text)