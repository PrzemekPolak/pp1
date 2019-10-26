a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

delta = b**2 -4*a*c
pdelta = delta**0.5
if delta > 0:
    pjeden = (-b -pdelta) / (2*a)
    pdwa = (-b +pdelta) / (2*a)
    print(f'Pierwiastki: {pjeden} i {pdwa}')
else:
    print('Brak pierwiastków')
    


