def sumat(tab):
    suma = 0
    print('Tablica: ',end='')
    for x in tab:
        suma += x
        print(f'{x} ',end='')
    print()
    print(f'Suma wartości: {suma}')
    
tab = [4,3,7,1,3]
sumat(tab)
    

