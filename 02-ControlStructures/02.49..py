nrDniaTygodnia = 2
print('| PN | WT | SR | CZ | PT | SB | ND |')

if nrDniaTygodnia <6:
    for puste in range(nrDniaTygodnia):
        print(f'|    ',end='')
    for i in range(1,36-nrDniaTygodnia):
        if i<10:
            print(f'|  {i} ',end='')
            if i==7-nrDniaTygodnia or i==14-nrDniaTygodnia:
                print('|')
        elif i>=10 and i<31:
            print(f'| {i} ',end='')
            if i==14-nrDniaTygodnia or i==21-nrDniaTygodnia or i==28-nrDniaTygodnia or(nrDniaTygodnia==5 and i==30):
                print('|')
        else:
            print(f'|    ',end='')
            if i==35-nrDniaTygodnia:
                print('|')
        
else:
    if nrDniaTygodnia!=7:
        for puste in range(nrDniaTygodnia):
            print(f'|    ',end='')
    for i in range(1,43-nrDniaTygodnia):
        if i<10:
            print(f'|  {i} ',end='')
            if i==7-nrDniaTygodnia or i==14-nrDniaTygodnia:
                print('|')
        elif i>=10 and i<31:
            print(f'| {i} ',end='')
            if i==14-nrDniaTygodnia or i==21-nrDniaTygodnia or i==28-nrDniaTygodnia or i==35-nrDniaTygodnia:
                print('|')
        else:
            print(f'|    ',end='')
            if i==42-nrDniaTygodnia:
                print('|')


