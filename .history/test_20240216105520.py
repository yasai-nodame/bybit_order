import csv

a = [['a','b','c']]
b = [['a','b','c']]


with open('test.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(a)
    writer.writerow(b)