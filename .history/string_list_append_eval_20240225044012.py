import pandas as pd
import csv 

row_list=[]
a = []
with open('bybit_BTCUSDT_linear_15.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # "['1599636600000', '10142', '10164.5', '10131', '10164.5', '22.091', '224543.9695']" の""　だけ消す。
        data = row[0].strip('""')
        # それをrow_listに追加していく
        row_list.append(data)
# リストの0番目が0なので、これを消す。
row_list.pop(0)
# row_listを回していき、type(data)が文字列だったので、eval()でリストにする。
'''
dataをeval(i)にしても形骸的に "['1599636600000', '10142', '10164.5', '10131', '10164.5', '22.091', '224543.9695']"
となるだけで、type(data) をすると文字列のまま（リストとはならない) 文字列を評価して形骸的なリストにしているだけ。
しかし、形骸的なリストを新しいリストにいれると、二重リストになる。つまり形骸的なリスト(typeは文字列のまま)から
列記としたリストになる。だから、リストとして評価されるため、新しいリストaにappendしていく。
'''
for i in row_list:
    data = eval(i)
    # それを新しいリストaに追加していく。
    a.append(data)
    
# この段階でaリストは二重リストになり、pandasでデータフレームできるようになる。
pandas_data = pd.DataFrame(a, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
print(pandas_data)