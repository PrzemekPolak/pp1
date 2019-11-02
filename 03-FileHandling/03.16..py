import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma = 0
li = 0

for x in cyfry:
    suma += int(x)
    li += 1
    
srednia = suma / li
print(f'Średnia prognozowana temperatura wynosi {srednia}.')



