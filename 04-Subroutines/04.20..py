x = int(input('Podaj podstawę potęgi: '))
n = int(input('Podaj wykładnik potęgi: '))

def potega(x,n):
    if n==0:
        return 1
    else:
        return x * potega(x,n-1)
    
print(f'{x} do potęgi {n} wynosi {potega(x,n)}')

