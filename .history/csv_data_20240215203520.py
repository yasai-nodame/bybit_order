from datetime import datetime 
import time 

import requests 
import pandas as pd 

url = "https://api-testnet.bybit.com/v5/market/kline"

symbol = 'BTCUSDT'
category = 'linear'
interval = 15 

#現在の時刻を取得(ms秒)
timestamp = int(time.time())
values = []

try:
    while True:
        params = {
            'symbol': symbol,
            'interval': interval,
            'category': category,
            'start': (timestamp - 200 * 60 * interval) * 1000,
            'end': timestamp * 1000,
            'limit': 200
        }
        
        
        response = requests.get(url)
        response_data = response.json()
        print(response_data['result']['list'])
        # timestamp,open,high,low,close,volume,turnoverリストが空ならbreak
        if len(response_data['result']['list']) == 0:
            break
        
        #valuesリストに要素を取得していく
        values.append(response_data['result']['list'])
        timestamp -= 200 * 60 * interval #15分のintervalだから-30分
except requests.exceptions.RequestException as e:
    print(f'Request Error: {e}')    
    
        
data = pd.DataFrame(values)
data.to_csv(f'bybit_{symbol}_{category}_{interval}.csv',index=False)

