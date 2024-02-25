import pandas as pd


df = pd.read_csv('bybit_BTCUSDT_linear_15.csv',names=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])

print(df)