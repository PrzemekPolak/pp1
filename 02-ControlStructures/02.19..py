n = int(input('Podaj n:'))
tab = []

for x in range(1,n+1):
    wyraz = 1 + (x - 1)*3
    tab.append(wyraz)

print(f'Ciąg arytmetyczny o różnicy 3: {tab}')
    
