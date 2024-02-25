from pybit.unified_trading import HTTP
import time
import requests 
from matplotlib import pyplot as plt
import pandas as pd
import talib
import json
import config
from datetime import datetime

def get_kline_order():
    # ローソク足を取得 そこからMACDのゴールデンクロスとデッドクロスを評価する。
    url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=15"

    response = requests.request("GET", url)
    list_text = response.json()['result']['list']
    df = pd.DataFrame(list_text, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    df_macd= pd.DataFrame(talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9),index=['MACD','SIGNAL','HISTGRAM']).T
    
    print('###############################')
    print(f'macd[-1]: {df_macd["MACD"].iloc[-1]}')
    print(f'signal[-1]: {df_macd["SIGNAL"].iloc[-1]}')
    print(f'macd[-2]: {df_macd["MACD"].iloc[-2]}')
    print(f'signal[-2]: {df_macd["SIGNAL"].iloc[-2]}')
    print('###############################')
        
    # 条件によって注文する
    session = HTTP(
        testnet=True,
        api_key=config.API_KEY,
        api_secret=config.API_SECRET
    )
    
    # ゴールデンクロスとデッドクロスを取得する。
    if df_macd['MACD'].iloc[-1] > df_macd['SIGNAL'].iloc[-1] and df_macd['MACD'].iloc[-2] < df_macd['SIGNAL'].iloc[-2]:
        params=session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Buy",
            orderType="Market",
            qty="1"
        )
        print(json.dumps(params))
        print(f'ゴールデンクロスで注文しました。: {current_time}')
        
    elif df_macd['MACD'].iloc[-1] < df_macd['SIGNAL'].iloc[-1] and df_macd['MACD'].iloc[-2] > df_macd['SIGNAL'].iloc[-2]:
        params=session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Sell",
            orderType="Market",
            qty="1",
        )
        print(json.dumps(params))
        print(f'デッドクロスで注文しました。: {current_time}')
        


# ◯時間実行し続ける

#開始時刻
start_time = time.time()
# 3時間
five_hour_in_seconds = 3 * 60 * 60
#現在の時刻
current_time = datetime.now().replace(microsecond=0)

while True:
    get_kline_order()
    
    current_time = time.time()
    
    # 経過時間
    elapsed_time = current_time - start_time
    
    if elapsed_time >= five_hour_in_seconds:
        break 
    
    time.sleep(300)

