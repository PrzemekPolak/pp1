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
    dic = {
        'je': tab.count(1),
        'dw': tab.count(2),
        'tr': tab.count(3)
        }
    
  
  
  

mediana(tab)
dominanta(tab)