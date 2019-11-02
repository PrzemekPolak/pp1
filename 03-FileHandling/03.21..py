tab = []
ilosc = 0
suma = 0

with open('numbersinrows.txt','r') as file:
    for line in file:
        st = line.rsplit(',')
        ilosc += len(st)
        tab.extend(st)
        
for i in tab:
    suma += int(i)
    
print(f'Ilość liczb: {ilosc}\nSuma liczb: {suma}')
        

