def wyst(licz,tab):
    print(f'Liczba: {licz}')
    print(f'Tablica: ',end='')
    for i in tab:
        print(f'{i} ',end='')
    print()    
    for x in tab:
        if licz==x:
            print('Rezultat: Podana liczba występuje w tablicy')
            break
        elif licz!=x and x==tab[len(tab)-1]:
            print('Rezultat: Podana liczba nie występuje w tablicy')

        
        
        
tab = [15, 38, 7, 23, 14]
wyst(23,tab)

