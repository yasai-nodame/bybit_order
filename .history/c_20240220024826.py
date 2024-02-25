from pybit.unified_trading import HTTP 
import time 

session = HTTP(
    testnet=True,
    api_key='V2IcREN12OgIyc3ELR',
    api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
)

server_time = session.get_server_time()['time']
recv_window = 5000
a = server_time - recv_window 

b = int(time.time() * 1000 + 8000) 

c = server_time + 1000

print(a)
print(b)
print(c)



