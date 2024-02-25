import csv 
import pandas as pd

data = []
format_data = []
index_data = []
result = []

with open('bybit_BTCUSDT_linear_15.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        row_format = row[0].strip('[]').split(',') #最初と末尾の文字列[]を削除して、splitによって、,区切りにしてリストとして返す。
        format_data.append(row_format)


#リスト型になったものの、""と''が混在していておかしいので整形する
for i in format_data:
    for n in i:
        c = n.strip().strip("'") #空白と''を削除してデータを整形する。しかし、二重リストではなくなり、一つのリストにすべての要素が入ってしまう。
        index_data.append(c)

for i in range(0, len(e), 7):
    result.append(e[i:i+7])

df = pd.DataFrame(result, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])

print(df)