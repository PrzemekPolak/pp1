tab = ['zero ', 'jeden ', 'dwa ', 'trzy ', 'cztery ', 'pięć ', 'sześć ', 'siedem ', 'osiem ', 'dziewięć ']
li = input('Liczba: ')
dl = len(li)
wynik = ''
pom = 0

for x in range(dl):
    pom = int(li[x])
    wynik += tab[pom]
    
print(f'{li} - {wynik}')
    
    


