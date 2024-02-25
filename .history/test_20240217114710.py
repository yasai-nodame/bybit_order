import csv 
import pandas as pd

data = []
d = []
e = []
result = []

with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a = row[0].strip('[]').split(',')
        d.append(a)


# df = pd.DataFrame(data[0][1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(d)

for i in d:
    for n in i:
        c = n.strip().strip("'")
        e.append(c)

for i in range(0, len(e), 7):
    result.append(e[i:i+7])

df = pd.DataFrame(result, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])