import csv 
import pandas as pd

data = []
d = []
e = []
with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a = row[0].strip('[]').split(',')
        d.append(a)
        for i in d[0]:
            b = i.strip().strip("'")
            data.append(e)


# df = pd.DataFrame(data[0][1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(d[0])