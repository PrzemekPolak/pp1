wiek = int(input('Podaj wiek psa w ludzkich latach:'))

if wiek>2:
    x= 2*10.5 + (wiek-2)*4
    print(f'Wiek w latach ludzkich: {x}')
else:
    x=wiek*10.5
    print(f'Wiek w latach ludzkich: {x}')
    
    