import pandas as pd
import csv 

row_list=[]
with open('bybit_BTCUSDT_linear_15.csv') as f:
    read = csv.read(f)