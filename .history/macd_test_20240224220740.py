import pandas as pd
import csv 


with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    # df = pd.DataFrame(reader,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    # macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print(reader)