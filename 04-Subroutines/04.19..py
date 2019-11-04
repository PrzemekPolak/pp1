n = int(input('Podaj liczbę: '))

def suma(n):
    if n==1:
        return 1
    else:
        return n+suma(n-1)
    
print(f'Suma {n} liczb wynosi: {suma(n)}')