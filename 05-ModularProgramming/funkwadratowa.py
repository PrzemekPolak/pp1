a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

if a != 0:
    delta = a**2 - 4*a*c
    if a < 0:
        print('Brak miejsc zerowych')
    elif a == 0:
        x0 = -b / 2*a
        print(f'Miejsce zerowe x0 = {x0}')
    else:
        pierwdelta = delta**0.5
        x1 = (-b - pierwdelta) / 2*a
        x2 = (-b + pierwdelta) / 2*a
        print(f'Miejsca zerowe: x1 = {x1}  x2 = {x2}')
else:
    if b == 0:
        if c == 0:
            print('Nieskończenie wiele rozwiązań')
        else:
            print('Równanie sprzeczne')
    else:
        x3 = -c / b
        print(f'Miejsce zerowe x0 = {x3}')