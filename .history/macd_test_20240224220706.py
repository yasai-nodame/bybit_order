import pandas as pd
import csv 


with open('bybit_BTCUSDT_linear_15') as f:
    reader = csv.reader(f)
    df = pd.DataFrame(reader,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
    print(df)