import csv 
import pandas as pd

with open('bybit_BTCUSDT_linear_15.csv') as file:
    file_reader = csv.reader(file)
    for row in file_reader:
        

