import requests 
import pandas as pd 
import talib
import time 

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


df = pd.read_csv('bybit_BTCUSDT_linear_15.csv',names=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])

macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

print(df)

print(macd,signal)