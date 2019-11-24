from statistics import *
from csv import *

with open('employees.csv', newline='') as file:
    reader = DictReader(file)
    sum = 0
    tab = []
    for row in reader:
        wyn = int(row['age'])
        tab.append(wyn)
        

print(f'Średnia artymetyczna: {mean(tab)}')
print(f'Mediana: {median(tab)}')
print(f'Odchylenie standardowe: {stdev(tab)}')
