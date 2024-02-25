import csv 
import pandas as pd
import ast 

with open('bybit_BTCUSDT_linear_15.csv') as file:
    lines = file.readlines()
    data = [eval(line.strip()) for line in lines]

