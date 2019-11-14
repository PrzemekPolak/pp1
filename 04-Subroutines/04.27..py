tekst = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'

def wyznsam(tekst):
    el = 0
    yl = 0
    ul = 0
    il = 0
    ol = 0
    al = 0
    for x in tekst:
        if x == 'e':
            el += 1
        elif x == 'y':
            yl += 1
        elif x == 'u':
            ul += 1
        elif x == 'o':
            ol += 1
        elif x == 'a':
            al += 1
        elif x == 'i':
            il += 1
    print(f'a: {al}')
    print(f'e: {el}')
    print(f'i: {il}')
    print(f'o: {ol}')
    print(f'u: {ul}')
    print(f'y: {yl}')
    
wyznsam(tekst)
    
    
    
    


