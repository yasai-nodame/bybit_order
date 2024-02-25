from pybit.unified_trading import HTTP 
import time 

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

timestamp = int(time.time() * 1000)
print(f'timestamp:{timestamp}')

print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Marker",
    qty="0.1",
    timestamp=timestamp
))