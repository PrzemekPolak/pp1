macierz = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]

def transpozycja(macierz):
    for x in range(len(macierz)):
        for y in range(len(macierz)):
            print(f'{macierz[y][x]}',end=' ')
        print()


for row in macierz:
        for num in row:
            print(f'{num}',end=' ')
        print()

print('Transpozycja:')
transpozycja(macierz)