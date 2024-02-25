import time 
from bybit import Bybit 

API_KEY = 'V2IcREN12OgIyc3ELR'
API_SECRET = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

client = Bybit(ws=False, api_key=API_KEY, api_secret=API_SECRET, testnet=True)

symbol = 'BTCUSDT'
side = 'Buy'
order_type = 'Market'
quantity = 0.001

response = client.place_active_order(symbol=symbol, side=side, order_type=order_type, qty=quantity)

print(response)