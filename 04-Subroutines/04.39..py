x = int(input('Początek przedziału: '))
y = int(input('Koniec przedziału: '))
n = int(input('Podaj liczbę: '))

def czyjest(n):
    for i in range(x,y+1):
        if i == n:
            print(f'{n} mieści się w zakresie <{x},{y}>')
            break
        elif i != n and i == y:
            print(f'{n} nie mieści się w zakresie <{x},{y}>')

czyjest(n)




