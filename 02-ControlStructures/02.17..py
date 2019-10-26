p=0
n=0

for x in range(1,51):
    if x%2==0:
        p += x
    else:
        n += x
print(f'Parzyste: {p}')
print(f'Nieparzyste: {n}')
        