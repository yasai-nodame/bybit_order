import requests
import time
import hashlib
import uuid
from Crypto.Hash import SHA256  # install pycryptodome libaray
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

api_key='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4Wl5Tw3Dee/x7xbx8boRE8L9IumTwFSEksf3E/blP8GxLdIkTl1s8lMEIQF8f/PVfOunlTK61AH2pujhCbyqMHJUcFrizb9wC9V1TFfUwoXHMfxHtaFY3Mw36zS4ed8XOr8tw7EadMvYb3A2hKoXZacx90bFND5VPiiVzQ/un7EbHnzr9bI8Sdiq5OvlcH/BqKJMN89OWQMLXDsT+Z7sGC+nE67G27vXt3mJjYjEbQWROMPEbQ9sna+Szh77MHvjXPnB1lHIR7q0g/fJZ+AY6EafM2Tv+yRJ9fGxWcR7qJJmuOGycDlF6vysO6p19976ebaxL1MUe96FeSL1GW10MQIDAQAB'
rsa_private_key_path = 'C:\\Users\\user\\bybit_automatic_trade\\private.pem' # use absolute path

httpClient=requests.Session()
recv_window=str(12000)
url="https://api-testnet.bybit.com" # Testnet endpoint

def HTTP_Request(endPoint,method,payload,Info):
    global time_stamp
    time_stamp=str(int(time.time() * 10 ** 3))
    signature=genSignature(payload, rsa_private_key_path)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    if(method=="POST"):
        response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
    else:
        response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
    print(response.text)
    print(response.status_code)
    print(Info + " Elapsed Time : " + str(response.elapsed))


"""
Load private_key.pem, then generate base64 signature
"""
def genSignature(payload, rsa_private_key_path):
    param_str= str(time_stamp) + api_key + recv_window 

    with open(rsa_private_key_path, "r") as private_key_obj:
        private_key_str = private_key_obj.read()
    private_key = RSA.importKey(private_key_str)
    encoded_param = SHA256.new(param_str.encode("utf-8"))
    signature = PKCS1_v1_5.new(private_key).sign(encoded_param)

    return base64.b64encode(signature).decode()

#Create Order
endpoint="/v5/order/create"
method="POST"
orderLinkId=uuid.uuid4().hex
params='{"category":"linear","symbol": "BTCUSDT","side": "Buy","positionIdx": 0,"orderType": "Limit","qty": "0.001","price": "10000","timeInForce": "GTC","orderLinkId": "' + orderLinkId + '"}'
HTTP_Request(endpoint,method,params,"Create")

