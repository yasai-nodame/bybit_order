from pybit.unified_trading import HTTP 
import time 
import hashlib 
import hmac 
import base64

api_key = 'V2IcREN12OgIyc3ELR'
api_secret = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

server_time = session.get_server_time()['time']
recv_window = 12000

timestamp = int(time.time() * 1000)


# if server_time - recv_window <= timestamp < server_time + 1000:
#     print(session.place_order(
#     category="spot",
#     symbol="BTCUSDT",
#     side="Buy",
#     orderType="Market",
#     qty="50",
#     timestamp=timestamp
# ))

headers = {
    'X-BAPI-SIGN': 'XXXXX',
    'X-BAPI-API-KEY': 'V2IcREN12OgIyc3ELR',
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'Content-Type': 'application/json',
}

request_params = f'{timestamp} {api_key} {recv_window}category=spot&symbol=BTCUSDT'

signature = hmac.new()
