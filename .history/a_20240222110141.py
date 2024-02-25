from pybit.unified_trading import HTTP
import json 
import requests 

if __name__ == "__main__":
    session = HTTP(
        api_key='XW604zcK1Z8aYj4sPV',
        api_secret='ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
    )
    
    r = session.get_tickers(category="spot",symbol="BTCUSDT")
    
    url = "https://api-testnet.bybit.com/v5/order/create"

    payload = json.dumps({
        "category": "spot",
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Market",
        "qty": "1",
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    # response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)