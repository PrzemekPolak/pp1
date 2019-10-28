suma = 0
x = 0

with open('numbers.txt','r') as file:
    for line in file:
        x = int(line)
        suma += x
        
print(f'Suma liczb: {suma}')