import requests 
from bybit import Bybit

api_key = 'V2IcREN12OgIyc3ELR'
api_secret = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

bybit = Bybit(api_key=api_key, secret=api_secret, symbol='BTCUSDT', ws=True,test=True)

position = bybit.get_position()