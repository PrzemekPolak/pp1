licz = []

with open('numbers.txt','r') as file:
    for line in file:
        line = int(line)
        licz.append(line)
        
licz.sort()
for i in licz:
    print(f'{i}',end=',')

    

