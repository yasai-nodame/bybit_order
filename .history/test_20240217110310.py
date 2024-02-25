import csv 
import pandas as pd

data = []
with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)


df = pd.DataFrame(data,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])


print(data[1:])