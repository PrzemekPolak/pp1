wiek = 25
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
elif wiek < 0 or wiek >= 120:
    raise ValueError('Wiek poza zakresem')
print(f'Masz {wiek} lat')
