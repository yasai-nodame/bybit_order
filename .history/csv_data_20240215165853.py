from datetime import datetime 
import time 

import requests 
import pandas as pd 

url = "https://api.bybit.com/v5/market/kline"

symbol = 'BTCUSD'
category = 'linear'
interval = 15 

timestamp = int(time.time())
print(timestamp)
