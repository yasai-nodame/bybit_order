from pybit.unified_trading import HTTP
import json 
import requests 
import hmac 
import base64
import time
import hashlib
import security
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
url = "https://api-testnet.bybit.com/v5/order/create"

timestamp = str(int(time.time() * 1000))

payload = {
    "api_key": api_key,
    "category": "spot",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "orderType": "Market",
    "qty": "1",
    "timestamp": timestamp
}

# payload_str = '&'.join([f"{key}={payload[key]}" for key in sorted(payload.keys())])　リスト内包表記ならこれ。
payload_str = ''
for key in sorted(payload.keys()):
    payload_str += f"{key}={payload[key]}&" #payload[key]でvalueが取得し、strの後ろに&をつけて連結させる。
payload_str = payload_str[:-1] # 最後の&だけ消す

'''
api_secret.encode('utf-8')は秘密鍵をutf-8エンコーディングでバイト列に変換
payload_str.encode('utf-8')はpayload_strをutf-8エンコーディングでバイト列に変換
hashlib.sha256()はsha-256ハッシュアルゴリズムを使用してハッシュオブジェクトを作成
hmac.new()は秘密鍵とpayload_strを使用して新しいHMACオブジェクトを作成。sha256を使用して計算される。
hexdigest()はHMACオブジェクトのハッシュ値を16進数文字列にして返す。
署名は秘密鍵と生のデータをハッシュ値にし、送信すること。
'''
signature = hmac.new(api_secret.encode('utf-8'), payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
payload['sign'] = signature 

headers = {
    'Content-Type': 'application/json'
}

# json文字列に変換
payload_json = json.dumps(payload)

# POSTメソッドで送信
response = requests.post(url, data=payload_json, headers=headers)
print(response.text)
