from pybit.unified_trading import HTTP 
import time 

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

server_time = session.get_server_time()['time']
recv_window = 5000

timestamp = int(time.time() * 1000) + 8000 


if server_time - recv_window <= timestamp < server_time + 1000:
    print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    qty="50",
    timestamp=timestamp
))



