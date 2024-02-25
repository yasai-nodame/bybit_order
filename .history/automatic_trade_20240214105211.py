import requests 

# Bybit APIのエンドポイント
endpoint = 'https://api.bybit.com/v5/market/kline'

# パラメータの設定
sysmbol = 'BTCUSD'
interval = '15' #10分足
limit = '10'

# APIリクエストの送信
response = requests.get(endpoint, params={'sysmbol': sysmbol, 'interval': interval, 'limit': limit})

# レスポンスの確認
if response.status_code == 200:
    #データの取得
    candle_data = response.json()
    print(candle_data)
else:
    print('エラー:',response.status_code)