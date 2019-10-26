uczelnia = 'UEK w Krakowie'
x = len(uczelnia)
y = 0
z = ''
pus = ' '

for i in range(0,x):
    y = uczelnia[i] + pus
    z += y
    
print(f'Uczelnia: {uczelnia}')    
print(f'Szeroko: {z}')
    
    
    