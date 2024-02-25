import csv 
import pandas as pd

data = []
with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a = row[0].strip('[]').split(',')
        for i in a:
            b = i.strip().strip("'")
            data.append(b)


# df = pd.DataFrame(data[0][1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(a)
print(b)