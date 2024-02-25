from pybit.unified_trading import HTTP
import time
import requests 
from matplotlib import pyplot as plt
import pandas as pd
import talib
import json

api = 'XW604zcK1Z8aYj4sPV'


# ローソク足を取得 そこからMACDのゴールデンクロスとデッドクロスを評価する。
def get_kline():
    
    url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=15"

    response = requests.request("GET", url)
    list_text = response.json()['result']['list']
    print(list_text)
    df = pd.DataFrame(list_text, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print(f'macd[-1]: {macd.iloc[-1]}')
    print(f'signal[-1]: {signal.iloc[-1]}')
    print(f'macd[-2]: {macd.iloc[-2]}')
    print(f'signal[-2]: {signal.iloc[-2]}')
    plt.plot(macd)
    plt.plot(signal)
    plt.show()


def order(macd,signal):
    session = HTTP(
        testnet=True,
        api_key='XW604zcK1Z8aYj4sPV',
        api_secret='ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE'
    )
    
    # ゴールデンクロスとデッドクロスを取得する。
    if macd.iloc[-1] > signal.iloc[-1] and macd.iloc[-2] < signal.iloc[-2]:
        params=session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Buy",
            orderType="Market",
            qty="1"
        )
        print(json.dumps(params))
        print('ゴールデンクロス')
        
    elif macd.iloc[-1] < signal.iloc[-1] and macd.iloc[-2] > signal.iloc[-2]:
        params=session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Sell",
            orderType="Market",
            qty="1",
        )
        print(json.dumps(params))
        print('デッドクロス')


session = HTTP(
    testnet=True,
    api_key="XW604zcK1Z8aYj4sPV",
    api_secret="ZUm95kwmdYjMuljMSLzeqrzckTc4d9aJoVeE",
)

params = session.place_order(
    category     = "spot",
    symbol       = "BTCUSDT",
    order_type   = "Market",
    side         = "Buy",  # or "Sell" 
    qty          = "1",    # 購入量(BTC)
    )

headers = {
    'Content-Type': 'application/json'
}

params_json = json.dumps(params)

url = 'https://api-testnet.bybit.com/v5/order/create'

# response = requests.post(url, data=params_json, headers=headers)
# print(response.text)

print(get_kline())