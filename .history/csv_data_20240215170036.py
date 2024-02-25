from datetime import datetime 
import time 

import requests 
import pandas as pd 

url = "https://api.bybit.com/v5/market/kline"

symbol = 'BTCUSD'
category = 'linear'
interval = 15 

timestamp = int(time.time())
values = []

while True:
    params = {
        'sysmbol': symbol,
        'interval': interval,
        'category': category,
        'start': (timestamp -200 * 60 * interval) * 1000,
        'end': timestamp * 1000,
        'limit': 200
    }
