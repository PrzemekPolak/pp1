imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
imie = input('Podaj imie: ')

def jestimie(imie,imiona):
    for x in imiona:
        if x == imie:
            print('Rezultat: imię zawarte jest w wykazie imion')
            break
        if x != imie and x == imiona[len(imiona)-1]:
            print('Rezultat: imię nie jest zawarte w wykazie imion')

print('Imiona: ',end='')
for i in imiona:
    print(f'{i}',end=' ')
print()
print(f'Imie: {imie}')
jestimie(imie,imiona)


            