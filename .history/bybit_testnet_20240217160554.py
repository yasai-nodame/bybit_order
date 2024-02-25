from pybit.unified_trading import HTTP
import time
import requests 
from matplotlib import pyplot as plt
import pandas as pd
import talib

url = 'api-testnet.bybit.com'
api = 'Z9VeZzgUjHurFcd56a'


# # 現在時刻(ms)を取得
# def get_time():
#     session = HTTP(testnet=True)
#     get_time = session.get_server_time()['time']
#     return get_time


#現在時刻取得
current_time = int(time.time())

interval_minutes = 15 * 60

#encパラメーター計算
end_time = current_time + interval_minutes


# ローソク足を取得 そこからMACDのゴールデンクロスとデッドクロスを評価する。
def get_kline():
    kline_list = []
    session = HTTP(testnet=True)
    
    url = "https://api-testnet.bybit.com/v5/market/kline?symbol=BTCUSDT&interval=15"

    response = requests.request("GET", url,)
    list_text = response.json()['result']['list']
    df = pd.DataFrame(list_text, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    plt.plot(macd)
    plt.plot(signal)
    plt.show()


def order(macd,signal):
    session = HTTP(
        testnet=True,
        api_key='V2IcREN12OgIyc3ELR',
        api_secret='KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT'
    )
    
    # ゴールデンクロスとデッドクロスを取得する。
    if macd.iloc[-1] > signal.iloc[-1] and macd.iloc[-2] < signal.iloc[-2]:
        session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Buy",
            orderType="Limit",
            qty="0.1",
            timeInForce="PostOnly",
            orderLinkId="spot-test-postonly",
            isLeverage=0,
        )
        
        print('ゴールデンクロス')
        
    elif macd.iloc[-1] < signal.iloc[-1] and macd.iloc[-2] > signal.iloc[-2]:
        session.place_order(
            category="spot",
            symbol="BTCUSDT",
            side="Sell",
            orderType="Limit",
            qty="0.1",
            timeInForce="PostOnly",
            orderLinkId="spot-test-postonly",
            isLeverage=0,
        )
        
        print('デッドクロス')


session = HTTP(
    testnet=True,
    api_key="V2IcREN12OgIyc3ELR",
    api_secret="KPVxY5RmMg9HVCbZDVWdiusrEko6rwd4gSwT",
)
params = session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.1",
    timeInForce="PostOnly",
    orderLinkId="spot-test-postonly",
    isLeverage=0,
    orderFilter="Order",
)

print(params)