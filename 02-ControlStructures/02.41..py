li = 0
su = 0
x = 1

while x!=0:
    li += 1
    x=int(input('Podaj liczbę: '))
    su += x
    
print(f'REZULTAT: Liczb={li-1}, Suma={su}, Średnia={su/(li-1)}')
    