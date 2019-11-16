def losowa():
    from random import randrange
    return randrange(1,51)

pa = 0
np = 0

for x in range(1000):
    ll = losowa()
    if ll%2==0:
        pa += 1
    else:
        np += 1

print('Dla 1000 liczb losowych z przedziału <1,50>:')
print(f'Liczby parzyste: {pa/10}%')
print(f'Liczby nieparzyste: {np/10}%')
