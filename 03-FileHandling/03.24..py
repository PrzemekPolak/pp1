tab=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

with open('TablicaDwuwymiarowa.csv','w') as file:
    file.write('Imie,Nazwisko,Email')
    for i in tab:
        file.write('\n')
        for x in i:
            file.write(f'{x},')

