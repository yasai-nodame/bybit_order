from pybit.unified_trading import HTTP
import json 
import requests 
import hmac 
import base64
import time
import hashlib

api_key = 'XW604zcK1Z8aYj4sPV'
api_secret = 'ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
url = "https://api-testnet.bybit.com/v5/order/create"


if __name__ == "__main__":
    # session = HTTP(
    #     api_key='XW604zcK1Z8aYj4sPV',
    #     api_secret='C:\\Users\\user\\bybit_automatic_trade\\private.pem'
    # )
    
    # r = session.get_tickers(category="spot",symbol="BTCUSDT")

    payload = json.dumps({
        "category": "spot",
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Market",
        "qty": "0.000048",
    })
    
    payload['api_key'] = api_key
    payload['timestamp'] = str(int(time.time() * 1000))
    
    payload_str = '&'.join([f"{key}={payload[key]}" for key in sorted(payload.keys())])
    
    signature = hmac.new(api_secret.encode('utf-8'), payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
    payload['sign'] = signature 
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)