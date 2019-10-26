licz = 0
ost = 1
post = 0
sum = 0

print(f'{post} {ost}',end=' ')

while licz<48:
    licz += 1
    sum = ost + post
    post = ost
    ost = sum
    print(f'{sum}',end=' ')
    
    
    
    