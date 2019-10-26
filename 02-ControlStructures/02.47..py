kw = int(input('Podaj kwotę w zł: '))
from math import floor

p = kw/5
p = floor(p)

d = (kw-p*5)/2
d = floor(d)

j = (kw-p*5-d*2)/1
j = floor(j)

print(f'Kwota {kw} zł w monetach:')
print(f'5 zł - {p} szt')
print(f'2 zł - {d} szt')
print(f'1 zł - {j} szt')
