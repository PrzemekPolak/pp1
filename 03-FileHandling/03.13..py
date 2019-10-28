tab = [32, 16, 5, 8, 24, 7]
dl=len(tab)
x=0

with open('Dodaj do tablicy.txt','a') as file:
    while x<dl:
        x += 1
        file.write(f'{tab[x-1]}\n')
