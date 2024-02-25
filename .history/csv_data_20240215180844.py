from datetime import datetime 
import time 

import requests 
import pandas as pd 

url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSD&interval=15&limit=10"

symbol = 'BTCUSD'
category = 'linear'
interval = 15 

#現在の時刻を取得(ms秒)
timestamp = int(time.time())
values = []

while True:
    response = requests.get(url)
    response_data = response.json()
    
    # timestamp,open,high,low,close,volume,turnoverリストが空ならbreak
    if len(response_data['result']['list']) == 0:
        break
    
    #valuesリストに要素を取得していく
    values += response_data['result']['list']
    timestamp -= 200 * 60 * interval #15分のintervalだから-30分
    
data = pd.DataFrame(values)
data.to_csv(f'bybit_{symbol}_{category}_{interval}.csv',index=False)

