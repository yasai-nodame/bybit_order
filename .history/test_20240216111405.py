import csv 
import pandas as pd

with open('bybit_BTCUSDT_linear_15.csv') as file:
    file_reader = csv.reader(file)
    file_reader_list = list(file_reader)
    print(file_reader_list)

