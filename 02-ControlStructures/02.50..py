lic = int(input('Podaj liczbę: '))
from math import floor
n = lic
pom = 0
txt = ''

print(f'{lic}(10)=',end='')
while n!=0:
    b = n%2
    pom = n/2
    n = floor(pom)
    txt = str(b) + txt
    
print(f'{txt}(2)')
    

