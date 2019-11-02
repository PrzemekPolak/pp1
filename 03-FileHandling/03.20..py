tab = []

with open('numbers.txt','r') as file:
    for line in file:
        line = int(line)
        if line%2==0:
            tab.append(line)
        else:
            continue
        
with open('evennumbers.txt','w') as file:
    for x in tab:
        x = str(x)
        file.write(f'{x}\n')

