import requests 
import config 
import test 
import time 

url = 'https://api-testnet.bybit.com/spot/v3/private/order'
order_link_id = '1626460982257915137'
api_key = config.API_KEY  # あなたのAPIキーを入力してください
timestamp = str(int(time.time() * 1000)-5000)  # タイムスタンプを入力してください
recv_window = '5000'  # 受信ウィンドウを設定してください
params = '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"1"}'

signature = test.genSignature(params)

headers = {
    'X-BAPI-SIGN': params,  # あなたの署名を入力してください
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window
}

params = {
    'orderLinkId': order_link_id
}

response = requests.get(url, headers=headers, params=params)
print(response.text)