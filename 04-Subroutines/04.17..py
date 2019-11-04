def rzucK():
    from random import randint
    x = randint(1,6) 
    return x

suma = 0
print('Wyrzucone oczka: ',end='')
for x in range(3):
    re = rzucK()
    suma += re
    print(f'{re} ',end='')
print()
print(f'Suma oczek: {suma}')


    
    
    