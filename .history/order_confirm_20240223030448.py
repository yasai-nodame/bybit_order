import requests 
import config 
import test 
import time 

url = 'https://api-testnet.bybit.com/spot/v3/private/order'
order_link_id = '1626457576139134209'
api_key = 'XXXXX'  # あなたのAPIキーを入力してください
timestamp = '1659076396894'  # タイムスタンプを入力してください
recv_window = '5000'  # 受信ウィンドウを設定してください

headers = {
    'X-BAPI-SIGN': 'XXXXX',  # あなたの署名を入力してください
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window
}

params = {
    'orderLinkId': order_link_id
}

response = requests.get(url, headers=headers, params=params)
print(response.text)