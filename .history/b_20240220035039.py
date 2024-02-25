import requests 
import hashlib 
import uuid 
from Crypto.Hash import SHA256 
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA 
import base64 
import time 

api_key = 'V2IcREN12OgIyc3ELR'
api_secret = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'

httpClient = requests.Session() 
recv_window = str(12000)
url = 'https://api-testnet.bybit.com'

time_stamp = int(time.time() * 10 ** 3)

print(time_stamp)