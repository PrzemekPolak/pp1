lim = int(input('Podaj limit prędkości (km/h): '))
pred = int(input('Podaj prędkość pojazdu (km/h): '))

if (pred-lim)<=10:
    man = (pred-lim)*5
    print(f'Mandat (zł): {man}')
elif (pred-lim)>10:
    man = (pred-lim-10)*15 + 50
    print(f'Mandat (zł): {man}')
