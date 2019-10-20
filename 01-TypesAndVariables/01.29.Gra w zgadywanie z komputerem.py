#pobranie odpowiedniego modułu
from random import randint

#Wylosowanie liczby przez komputer
numc = randint(1,6)

#Podanie przez użytkownika liczby
print('Podaj, ile oczek kostki wyrzucił komputer')
numu = int(input())

#Określenie czy użytkownik miał rację i przedstawienie wyniku 
if numc == numu:
    print(f'Komputer wyrzucił: {numc}')
    print('Zgadłeś: True')
else:
    print(f'Komputer wyrzucił: {numc}')
    print('Zgadłeś: False')
