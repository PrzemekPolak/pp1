from random import randrange
li = 0
je=0
dw=0
tr=0
cz=0
pi=0
sz=0

while li<100:
    li += 1
    r = randrange(1,7)
    if r==1:
        je +=  1
    elif r==2:
        dw += 1
    elif r==3:
        tr += 1
    elif r==4:
        cz += 1
    elif r==5:
        pi += 1
    else:
        sz += 1
        
print(f'Szóstka: {sz}')
print(f'Piątka: {pi}')
print(f'Czwórka: {cz}')
print(f'Trójka: {tr}')
print(f'Dwójka: {dw}')
print(f'Jedynka: {je}')
  