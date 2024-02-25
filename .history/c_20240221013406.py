import requests
import time
import hashlib
import uuid
from Crypto.Hash import SHA256  # install pycryptodome libaray
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

api_key='''
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC79FwtV9u8gMLw
iewk8EMqZlNSEXZR7qxX7VqfFziXuEqyPYAjip+Yrg6PhwAwMu4x/TH+ErkQO1/O
zC8O52y39Y9BnhD9u0IIQ3eu+4HRiRydm5C391reTe+yPdVTQqyzOWAZZIRRi57m
9/OF12b7FGY98QEH0qWMrjgMvklFpKZm6pYOWQjFqRqOaZXu0irH8ZudRZ7Yf6qk
tUVw6LWK6xYbft3QuAIjwzDrocmN2S1HTmYAkI8Niz0BarEfnUZ4COpIHq534eJg
HSXyANPF52vIMjXt+XAbtloAkyh6bmaAjpMPJCmnLYe1+A0kHAL7KGa7ODs2XAV+
E77h3AshAgMBAAECggEACtJzmkLESrLJRqtSVwAkheT1aDTMMMSC1N88SAvAvO+m
EWQ8JA+/x71B5l66EoxkLamr/rqaQEaC6jfUf9Gwb1kqwfb1eH6XOz2TPxaJL4Tr
CmIiL42FBGbNZeBsj4o3wmwLzfp9KerVn+vn8C1qZwuSJX/idM5arOJ9JLKyKlnK
uqs9bAQ+m9mtoc8tAv5wS7PEqraTC0nzKYgvv8Q+r+ncSWZZ8KGx0DY+RHNBMorf
xQtC9ch/AiDPxwmHd/6xU8XpJTe/s0VRlsRKhX/Iua08cx5cqmztCNmPoD/kt8iL
+v8AF/w/WZHzAwpdPqc6u7/m1qhonE0aynRfmtPUjwKBgQDzovoc9clHqdEs21ED
H4cxk1bL6jfTs+Ww7IzkKCbcFKZyOYcGIBHOL/V1llN1LJsOEiQvCWsvBXw1CgQ5
WtV5QL3EzH1TQsWiLpMLLpagYeS9E5aWoDzo+DUVo+fwlMkUYaIYWhd7iZA17Wz1
Z98ndRMiGYfi6Gc6zlLx50lzOwKBgQDFfgffSCQdgKLyCtP/ckkWkkFwYiLxUCf4
mekh9RM6f6CElw/NLP5d4oAN/Ckkdqz82fvYQW944xA5iO7275yH4l+si/QPh2ad
VYmcL26HAgzIQffvcF0CfWNzy8q7oiAhRaDug4CH3Y1E9kbkg4YiUVxtiTcYC1rr
wVjLrRodUwKBgFXyJUc4EWQ9bLPlPkPayGddsZ3HpyAAc0OhfuYxn9u9USY0UwR/
JajV1EJB4HkSXjRtg+Qv72asCa/wM6ND/tCCXS9ib8eCY5Od2HN2YN59CiMFGPdT
2YjZnmhe5MBCzFhrRLJQfb4vvfa4JdrAZMFXlINP/Fa4Y0okZLA/RfLnAoGAEFqe
ZkQAEZ1cYPS6l3WsTb0wxBCsWhVMKg78uj4kKHz3GuOzgEcQjU+7UO0nrwhQzON0
MnVAuN78sfb/6tzutmXtjElOnZaVzcOOkKtw2Kc3zcGAuYgxe4pMmQMwN5d2V6r/
Z6DmHNog36wRNM0bZ24bXEq3kDsofUtWgg9EkVcCgYAf5sFg/HUtWMmbGZViVZIs
dVapMOpJcNlM2BYM3F1C0wBBD+L4So8HmBNlZ4/Z7K5Udp8u8n64ZH3e/6OxPTAC
dKWk13Bumlhd0f/zlo3WECyMICpvYuQi5H+k5vK/WV1qgG+U1SUQQp5hWXHDQTf4
ZqM1qCCSzAUCZlSvf2bMjw==
-----END PRIVATE KEY-----
'''
rsa_private_key_path = 'private.pem' # use absolute path

httpClient=requests.Session()
recv_window=str(5000)
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
    param_str= str(time_stamp) + api_key + recv_window + payload

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

#Get unfilled Orders
endpoint="/v5/order/realtime"
method="GET"
params='category=linear&settleCoin=USDT'
HTTP_Request(endpoint,method,params,"UnFilled")

#Cancel Order
endpoint="/v5/order/cancel"
method="POST"
params='{"category":"linear","symbol": "BTCUSDT","orderLinkId": "'+orderLinkId+'"}'
HTTP_Request(endpoint,method,params,"Cancel")