import re
suma = 0

with open('land.txt','r') as file:
    tekst = file.read()

x = re.findall('\d',tekst)
    
for i in x:
    suma += int(i)
    
print(f'Suma cyfr wynosi: {suma}')
    
