import csv 
import pandas as pd
import talib 
from matplotlib import pyplot as plt
import requests 

# Bybit APIのエンドポイント
url = 'https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSD&interval=15&limit=10'

# Bybit APIキー
api_key = 'Z9VeZzgUjHurFcd56a'

response = requests.get(url)

data = []
format_data = []
index_data = []
result = []

with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        row_format = row[0].strip('[]').split(',') #最初と末尾の文字列[]を削除して、splitによって、,区切りにしてリストとして返す。
        format_data.append(row_format)


#リスト型になったものの、""と''が混在していておかしいので整形する
for i in format_data:
    for n in i:
        c = n.strip().strip("'") #空白と''を削除してデータを整形する。しかし、二重リストではなくなり、一つのリストにすべての要素が入ってしまう。
        index_data.append(c)

for i in range(0, len(index_data), 7): # 二重リストに戻すために、7つの要素ずつ新しいリストresultに追加していく。
    result.append(index_data[i:i+7])

df = pd.DataFrame(result, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])

macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

data = response.json()['result']['list']

df2 = pd.DataFrame(data,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])

print(df2)