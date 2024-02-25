import requests 
import pandas as pd 
import talib

# Bybit APIのエンドポイント
url = 'https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSD&interval=15&limit=10'

# Bybit APIキー
api_key = 'Z9VeZzgUjHurFcd56a'

response = requests.get(url)

# # レスポンスの確認
# if response.status_code == 200:
#     #データの取得
#     candle_data = response.text
#     print(candle_data)
# else:
#     print('エラー:',response.status_code)

data = response.json()['result']['list']


df = pd.DataFrame(data,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(df)


# print(f'MACD: {macd}')
# print(f'SIGNAL: {signal}')

# print(df)