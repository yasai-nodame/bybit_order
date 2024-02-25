from pybit.unified_trading import HTTP
import time
import requests 
from matplotlib import pyplot as plt
import pandas as pd
import talib
import json
import config
from datetime import datetime

current_time = datetime.now().replace(microsecond=0)

# ローソク足を取得 そこからMACDのゴールデンクロスとデッドクロスを評価する。
def get_kline():
    macd_and_signal = []
    url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=15"

    response = requests.request("GET", url)
    list_text = response.json()['result']['list']
    df = pd.DataFrame(list_text, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print(f'macd[-1]: {macd.iloc[-1]}')
    print(f'signal[-1]: {signal.iloc[-1]}')
    print(f'macd[-2]: {macd.iloc[-2]}')
    print(f'signal[-2]: {signal.iloc[-2]}')
    # plt.plot(macd)
    # plt.plot(signal)
    # plt.show()
    macd_data = macd.tolist()
    signal_data = signal.tolist()
    macd_and_signal.append(macd_data)
    macd_and_signal.append(signal_data)

def order(macd,signal):
    session = HTTP(
        testnet=True,
        api_key=config.API_KEY,
        api_secret=config.API_SECRET
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
        print(f'ゴールデンクロスで注文しました。: {current_time}')
        
    elif macd.iloc[-1] < signal.iloc[-1] and macd.iloc[-2] > signal.iloc[-2]:
        params=session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Sell",
            orderType="Market",
            qty="1",
        )
        print(json.dumps(params))
        print(f'デッドクロスで注文しました。: {current_time}')


get_kline()


