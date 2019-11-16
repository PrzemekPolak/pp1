tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

def mediana(tab):
    tab.sort()
    dl = len(tab)
    if dl%2==0:
        med = (tab[int(dl/2-1)] + tab[int(dl/2)])/2
        print(f'Mediana: {med}')
    else:
        import math
        med = math.ceil(tab[dl/2])
        print(f'Mediana: {med}')
        

def dominanta(tab):
    print(f'Dominanta: ',end='')
    najwil = tab.count(max(tab, key=tab.count))
    while tab.count(max(tab, key=tab.count)) == najwil:
        x = max(tab, key=tab.count)
        for i in range(najwil):
            tab.remove(x)
        print(f'{x}',end=' ')
    print()
    
    
    
  
mediana(tab)
dominanta(tab)