najd = int(input('Największa długość: '))
zli = najd 
gw = '*'

for x in range(najd+1):
    print(f'{x*gw}')
    
for y in range(najd,2*najd):
    zli += -1
    print(f'{zli*gw}')

