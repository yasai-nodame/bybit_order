import pandas as pd
import csv 

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    # df = pd.DataFrame(reader,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    # macd, signal, histgram = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    for row in reader:
        # df = pd.DataFrame(row,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
        output = eval(row)
        print(type(row))