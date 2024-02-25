import csv

a = [[1,2,3]]
n = [[1,2,3]]


with open('test.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(a)
    writer.writerow(n)