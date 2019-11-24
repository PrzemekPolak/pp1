def czytajWspolczynniki():
    a = int(input('Podaj współczynnik a: '))
    b = int(input('Podaj współczynnik b: '))
    c = int(input('Podaj współczynnik c: '))
    return a,b,c
    
def obliczDelte(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def wyswietlPierwiastki(a,b,delta):
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
    print(f'x1 = {x1}\nx2 = {x2}')


