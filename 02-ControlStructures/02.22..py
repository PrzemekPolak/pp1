tab= [15,8,31,47,2,19]
suma = 0
n = 0

for x in tab:
    if x%2!=0:
        suma += x
        n += 1
print(f'Średnia arytmetyczna wynosi {suma/n}')
    
    