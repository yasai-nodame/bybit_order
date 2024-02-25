import csv 
import pandas as pd
import ast 

data = []

with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

for row in data:
    print(row)