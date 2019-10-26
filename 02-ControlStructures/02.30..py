ppin = '0805'

q = input('Podaj kod PIN: ')
if q != ppin:
    print('Kod PIN niepoprawny.')
    w = input('Podaj kod PIN: ')
    if w != ppin:
        print('Kod PIN niepoprawny.')
        e = input('Podaj kod PIN: ')
        if e != ppin:
            print('Kod PIN niepoprawny.')
            print('Karta płatnicza zostaje zablokowana.')
        else:
            print('Kod PIN poprawny.')
    else:
        print('Kod PIN poprawny.')
else:
    print('Kod PIN poprawny.')
            
        