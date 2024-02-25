from pybit.unified_trading import HTTP 
import time 

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

server_time = session.get_server_time()['time']
recv_window = 10000

timestamp = int(time.time() * 1000) 

a = server_time - recv_window
b = timestamp

print(a)
print(b)


