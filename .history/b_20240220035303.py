import requests 
import hashlib 
import uuid 
from Crypto.Hash import SHA256 
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA 
import base64 
import time 
from pybit.unified_trading import HTTP 

api_key = 'V2IcREN12OgIyc3ELR'
api_secret = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

session = HTTP(
    testnet=True,
    api_key=api_key,
    api_secret=api_secret
)


httpClient = requests.Session() 
recv_window = str(12000)
url = 'https://api-testnet.bybit.com'

time_stamp = int(time.time() * 10 ** 3)
b = int(time.time() * 1000)
print(time_stamp)
print(a)
server_time = session.get_server_time()['time'] - 12000
print(server_time)