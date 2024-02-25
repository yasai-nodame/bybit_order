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
    print(type(data))
    pandas_data = pd.DataFrame([data_dict])
print(pandas_data)
