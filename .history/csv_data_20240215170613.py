from datetime import datetime 
import time 

import requests 
import pandas as pd 

url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSD&interval=15&limit=10"

symbol = 'BTCUSD'
category = 'linear'
interval = 15 

timestamp = int(time.time())
values = []

while True:
    response = requests.get(url)
    response_data = response.json()
    print(response_data)
    if len(response_data['result']['list']) == 0:
        break
    
    values += response_data['result']['list']
    timestamp -= 200 * 60 * interval 
    
data = pd.DataFrame(values)
data.to_csv(f'bybit_{symbol}_{category}_{interval}.csv',index=False)

