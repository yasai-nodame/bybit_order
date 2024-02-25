import pandas as pd
import csv 

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data = row[0].strip('""')
        row_list.append(data)
        # pandas_data = pd.DataFrame(data_list, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
        # print(pandas_data)



print(type(row_list))
print(row_list[0][0])