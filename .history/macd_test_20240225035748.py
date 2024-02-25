import pandas as pd
import csv 
import pandas as pd

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data = row[0].strip('""')
        data_list = eval(data)
        print(data_list)
        print(type(data_list))
        pandas_data = pd.DataFrame(data_list, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
        print(pandas_data)



