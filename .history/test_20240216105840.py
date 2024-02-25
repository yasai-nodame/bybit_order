import pandas as pd 

df = pd.read_csv('bybit_BTCUSDT_linear_15.csv')

all_values = []

for row in df.values:
    for value in row:
        all_values.append(value)
        
print(all_values)