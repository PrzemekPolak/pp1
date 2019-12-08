class statystyka():
    
    def __init__(self, tab_poczatkowa):
        self.tablica = tab_poczatkowa

    def dodaj_liczbe(self, nowa_liczba):
        self.tablica.append(nowa_liczba)

    def wyswietl_tabele(self):
        tekst = ''
        for x in self.tablica:
            tekst += str(x) + ', '
        print(f'{tekst[:-2]}')

    def wyznacz_najwieksza(self):
        self.najwieksza = max(self.tablica)

    def wyznacz_najmniejsza(self):
        self.najmniejsza = min(self.tablica)

    def oblicz_srednia(self):
        import statistics
        self.sred = statistics.mean(self.tablica)

    def mediana(self):
        import statistics
        self.median = statistics.median(self.tablica)

    def wyswietl(self):
        print(f'Minimum: {self.najmniejsza}\nMaksimum: {self.najwieksza}')
        print(f'Średnia: {self.sred}\nMediana: {self.median}')


stat = statystyka([12, 37, 6, 9])
stat.dodaj_liczbe(17)
stat.wyswietl_tabele()
stat.wyznacz_najmniejsza()
stat.wyznacz_najwieksza()
stat.oblicz_srednia()
stat.mediana()
stat.wyswietl()