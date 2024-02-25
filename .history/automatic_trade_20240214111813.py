import requests 

# Bybit APIのエンドポイント
url = 'https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSD&interval=15&limit=10'

# Bybit APIキー
api_key = 'Z9VeZzgUjHurFcd56a'

payload = {}
headers = {}

response = requests.get(url, headers=headers, data=payload)

# レスポンスの確認
if response.status_code == 200:
    #データの取得
    candle_data = response.text
    print(candle_data)
else:
    print('エラー:',response.status_code)