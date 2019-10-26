pier = int(input('Podaj pierwszą liczbę: '))
dru = int(input('Podaj drugą liczbę: '))
trz = int(input('Podaj trzecią liczbę: '))

tab = [pier, dru, trz]
tab.sort()

print(f'Mediana wynosi {tab[1]}')