import requests 
import config 
import test 
import time 

api_key = config.API_KEY
recv_window = str(5000)
time_stamp = str(int(time.time() * 1000))

httpClient = requests.Session()

order_id = '1626455659124102401'

url = f'https://api-testnet.bybit.com/spot/v3/private/order?orderLinkId={order_id}'