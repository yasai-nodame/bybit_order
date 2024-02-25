import pandas as pd
import csv 
import pandas as pd

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data = row[0].strip('""')

    row_list.append(data)

print(row_list)