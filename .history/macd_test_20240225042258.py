import pandas as pd
import csv 

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data = row[0].strip('""')
        row_list.append(data)

row_list.pop(0)
for i in row_list:
    data = eval(i)
    data_dict = {
        'timestamp': data[0],
        'open': data[1],
        'high': data[2],
        'low': data[3],
        'close': data[4],
        'volume': data[5],
        'turnover': data[6]
    }
    pandas_data = pd.DataFrame(data_dict, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(pandas_data)
