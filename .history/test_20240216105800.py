import pandas as pd 

df = pd.read_csv('test.csv')

all_values = []

for row in df.values:
    for value in row:
        all_values.append(value)
        
print(all_values)