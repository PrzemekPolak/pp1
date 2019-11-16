tab = [1,2,3,4,5,6,7,8]

even = lambda x : x%2 == 0

filt = filter(even,tab)

print(f'Liczby parzyste: ',end='')
for i in filt:
    print(f'{i}',end=' ')
