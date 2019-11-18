import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    a = -1
    for row in reader:
        a += 1
        if a == 0:
            print('#',end='\t')
            print('==')
       
        else:
            print(a,end='\t')
            print(row[1],row[0],row[2],row[3],sep='\t\t')

