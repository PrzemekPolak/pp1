jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Androit', ]
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

def rysujwykres(jezyki,wartosci):
    sym = '#'
    pus = ' '
    dl = len(jezyki)

    tab = []
    for i in jezyki:
        pom = len(i)
        tab.append(pom)
    tab.sort()
    najdl = tab[dl-1]
    
    for x in range(dl):
        print(f'{(najdl-len(jezyki[x]))*pus}{jezyki[x]}: {wartosci[x]*sym}')
        
rysujwykres(jezyki,wartosci)




