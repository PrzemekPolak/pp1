import csv
import statistics
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    a = -1
    for row in reader:
        a += 1
        if a == 0:
            print('#',row[1],row[0],row[2],row[3],sep='\t\t')
            print('==================================================================================================')
        else:
            print(a,row[1],row[0],row[2],row[3],sep='\t\t')
            
with open('employees.csv', newline='') as f:    
    reader2 = csv.DictReader(f)
    tab = []
    for row in reader2:
        wyn = int(row['age'])
        tab.append(wyn)
        
print(f'Średnia artymetyczna: {statistics.mean(tab)}')    
