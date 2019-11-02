tab=[]
pom=[]
pom2=[]
li = 0
x = 0
pus=' '

with open('students.txt','r') as file:
    for line in file:
        st = line.rsplit(',')
        li += 1
        if li>1 and int(st[2])<30:
            tab.append(st)
            
for i in tab:
    x = len(i[0])
    pom.append(x)
    pom.sort()
    pom.reverse()
    
    x = len(i[1])
    pom2.append(x)
    pom2.sort()
    pom2.reverse()
    
for i in tab:
    print(f'{i[0]+(pom[0]-len(i[0]))*pus}  {i[1]+(pom2[0]-len(i[1]))*pus}  {i[4]}')
        
        
        