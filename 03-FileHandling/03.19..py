tab = []

with open('universities.txt','r') as file:
    for line in file:
        tab.append(line)
        
tab.sort()

with open('universities.txt','w') as file:
    for i in tab:
        file.write(i)

