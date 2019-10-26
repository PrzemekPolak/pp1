n = int(input('Ile liczb: '))
x = 2
li = 1

print(f'Liczby pierwsze: 2 ',end='')

for z in range(1,9999):
    x += 1
    for i in range(2,x):
        if x%i==0 or li>=n:
            break
        elif i==x-1:
            li += 1
            print(f'{x} ',end='')
          


        
    

