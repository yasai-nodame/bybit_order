import requests 

# Bybit APIのエンドポイント
url = 'https://api-testnet.bybit.com/v5/market/kline'

# Bybit APIキー
api_key = 'Z9VeZzgUjHurFcd56a'

#パラメータ取得
sysmbol = 'BTCUSD'
interval = '15'
limit = '10'

response = requests.get('GET', url, )

# レスポンスの確認
if response.status_code == 200:
    #データの取得
    candle_data = response.json()
    print(candle_data)
else:
    print('エラー:',response.status_code)