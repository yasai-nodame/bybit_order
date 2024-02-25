import csv 
import pandas as pd

data = []
eval_list = []
with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

# eval_list = eval(data)

df = pd.read_csv(data[0][1],columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])


print(df)