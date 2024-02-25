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
        "category": "linear",
    "symbol": "ETHUSDT",
    "isLeverage": 0,
    "side": "Buy",
    "orderType": "Limit",
    "qty": "1",
    "price": "1000",
    "triggerPrice": None,
    "triggerDirection": None,
    "triggerBy": None,
    "orderFilter": None,
    "orderIv": None,
    "timeInForce": "GTC",
    "positionIdx": 0,
    "orderLinkId": "test-xx1",
    "takeProfit": None,
    "stopLoss": None,
    "tpTriggerBy": None,
    "slTriggerBy": None,
    "reduceOnly": False,
    "closeOnTrigger": False,
    "smpType": None,
    "mmp": None,
    "tpslMode": None,
    "tpLimitPrice": None,
    "slLimitPrice": None,
    "tpOrderType": None,
    "slOrderType": None
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)