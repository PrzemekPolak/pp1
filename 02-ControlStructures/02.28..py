a = int(input('a: '))    #Pionowy bok
b = int(input('b: '))    #Poziomy bok
pus = ' '
gw = '*'

for x in range(1,a+1):
    if x == 1:
        print(f'{b*gw}')
    elif x == a:
        print(f'{b*gw}')
    else:
        print(f'*{(b-2)*pus}*')
        
