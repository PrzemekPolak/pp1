pesel = input('Podaj Pesel: ')
obecny_rok = 18

if int(pesel[9]) == 0 or int(pesel[9]) == 2 or int(pesel[9]) == 4 or int(pesel[9]) == 6 or int(pesel[9]) == 8:
    plec = 'kobieta'
else:
    plec = 'mężczyzna'
    
rok = int(pesel[0:2])

if int(pesel[2:4]) > 12:
    wiek = obecny_rok - rok
else:
    wiek = 100 - rok + obecny_rok
    
print(f'Płeć: {plec}')
print(f'Wiek: {wiek}')
