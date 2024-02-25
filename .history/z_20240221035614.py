import time 
import hashlib 
import hmac 
import base64 

api_key = 'V2IcREN12OgIyc3ELR'
recv_window = '12000'
timestamp = str(int(time.time() * 1000) - int(recv_window))

payload = '{"symbol": "BTCUSDT", "side": "Buy", "orderType": "Market", "category": "spot", "qty": "0.1"}'

request_string = 'POST/v5/order/create' +  payload 

signing_string = timestamp + recv_window + request_string 

private_key = 'KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
hashed = hmac.new(private_key.encode('utf-8'), signing_string.encode('utf-8'), hashlib.sha256)
signature = base64.b64encode(hashed.digest()).decode()

print('X-BAPI-SIGN:', signature)