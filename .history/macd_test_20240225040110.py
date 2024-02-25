import pandas as pd
import csv 
import pandas as pd

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for i,row in enumerate(reader):
        data = row[0].strip('""')
        data_list = eval(data)
        pandas_data = pd.DataFrame(data_list[i], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
        print(pandas_data)



