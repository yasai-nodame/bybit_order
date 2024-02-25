import csv 
import pandas as pd

with open('bybit_BTCUSDT_linear_15.csv') as file:
    file_reader = csv.reader(file)
    file_eval = file_reader.apply(eval)
    print(type(file_eval))

