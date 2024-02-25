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

def get_kline_order():
    # ローソク足を取得 そこからMACDのゴールデンクロスとデッドクロスを評価する。
    url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=15"

    response = requests.request("GET", url)
    list_text = response.json()['result']['list']
    df = pd.DataFrame(list_text, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print('###############################')
    print(f'macd[-1]: {macd.iloc[-1]}')
    print(f'signal[-1]: {signal.iloc[-1]}')
    print(f'macd[-2]: {macd.iloc[-2]}')
    print(f'signal[-2]: {signal.iloc[-2]}')
    print('###############################')
    plt.plot(macd,label='macd')
    plt.plot(signal,label='signal')
    plt.show()