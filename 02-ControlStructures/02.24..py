tabi = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

if len(tabi[0]) >= len(tabi[1]) and len(tabi[0]) >= len(tabi[2]) and len(tabi[0]) >= len(tabi[3]) and len(tabi[0]) >= len(tabi[4]) and len(tabi[0]) >= len(tabi[5]):
    print(f'Najdłuższe imię: {tabi[0]}')
elif len(tabi[1]) >= len(tabi[0]) and len(tabi[1]) >= len(tabi[2]) and len(tabi[1]) >= len(tabi[3]) and len(tabi[1]) >= len(tabi[4]) and len(tabi[1]) >= len(tabi[5]):
    print(f'Najdłuższe imię: {tabi[1]}')
elif len(tabi[2]) >= len(tabi[1]) and len(tabi[2]) >= len(tabi[0]) and len(tabi[2]) >= len(tabi[3]) and len(tabi[2]) >= len(tabi[4]) and len(tabi[2]) >= len(tabi[5]):
    print(f'Najdłuższe imię: {tabi[2]}')
elif len(tabi[3]) >= len(tabi[1]) and len(tabi[3]) >= len(tabi[2]) and len(tabi[3]) >= len(tabi[0]) and len(tabi[3]) >= len(tabi[4]) and len(tabi[3]) >= len(tabi[5]):
    print(f'Najdłuższe imię: {tabi[3]}')
elif len(tabi[4]) >= len(tabi[1]) and len(tabi[4]) >= len(tabi[2]) and len(tabi[4]) >= len(tabi[3]) and len(tabi[4]) >= len(tabi[0]) and len(tabi[4]) >= len(tabi[5]):
    print(f'Najdłuższe imię: {tabi[4]}')
else:
    print(f'Najdłuższe imię: {tabi[5]}')

