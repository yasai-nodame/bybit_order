import csv 
import pandas as pd

data = []
d = []
with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a = row[0].strip('[]').split(',')
        d.append(a)
        for i in d:
            b = i.strip().strip("'")
            data.append(d)


# df = pd.DataFrame(data[0][1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(d)