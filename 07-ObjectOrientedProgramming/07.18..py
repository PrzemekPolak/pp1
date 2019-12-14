class Wypożyczalnia_samochodowa():
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_pojazdow = []

    def dodaj_pojazd(self, rodzaj, marka, numer_rejestracyjny, ilosc):
        if rodzaj == 'osobowy':
            self.lista_pojazdow.append(Samochod_osobowy(marka,numer_rejestracyjny,ilosc)) 
        elif rodzaj == 'dostawczy':
            self.lista_pojazdow.append(Samochod_dostawczy(marka,numer_rejestracyjny,ilosc))

    def wyswietl_wszystkie(self):
        print(f'"{self.nazwa}"')
        licz = 0
        for x in self.lista_pojazdow:
            licz += 1
            print(f'{licz}. ',end='')
            print(x.wyswietl())

    def wyswietl_dostepne(self):
        print(f'"{self.nazwa}"')
        print('Pojazdy dostępne:')
        licz = 0
        for x in self.lista_pojazdow:
            if x.wypozyczony:
                continue
            else:
                licz += 1
                print(f'{licz}. ',end='')
                print(x.wyswietl())

    def wyswietl_niedostepne(self):
        print(f'"{self.nazwa}"')
        print('Pojazdy niedostępne:')
        licz = 0
        for x in self.lista_pojazdow:
            if x.wypozyczony:
                licz += 1
                print(f'{licz}. ',end='')
                print(x.wyswietl())
            else:
                continue

    def pozycz(self,numer_rejestracyjny):
        for x in self.lista_pojazdow:
            if x.numer_rejestracyjny == numer_rejestracyjny and (not x.wypozyczony):
                x.pozycz()
                
    def oddaj(self,numer_rejestracyjny, przejechane):
        for x in self.lista_pojazdow:
            if x.numer_rejestracyjny == numer_rejestracyjny and x.wypozyczony:
                x.oddaj()
                x.zmien_przebieg(przejechane)


class Pojazd():
    def __init__(self, marka, numer_rejestracyjny):
        self.marka = marka
        self.numer_rejestracyjny = numer_rejestracyjny
        self.przebieg = 0
        self.wypozyczony = False

    def pozycz(self):
        self.wypozyczony = True
        print(f'Wypożyczono: {self.numer_rejestracyjny}')

    def oddaj(self):
        self.wypozyczony = False
        print(f'Zwrócono: {self.numer_rejestracyjny}')

    def zmien_przebieg(self, wartosc):
        self.przebieg += wartosc

    def wyswietl(self):
        if self.wypozyczony:
            return f'{self.marka}, {self.numer_rejestracyjny}, Przebieg: {self.przebieg} km, Pojazd niedostępny'
        else:
            return f'{self.marka}, {self.numer_rejestracyjny}, Przebieg: {self.przebieg} km, Pojazd dostępny'


class Samochod_osobowy(Pojazd):
    def __init__(self, marka, numer_rejestracyjny, ilosc):
        self.liczba_miejsc = ilosc
        super().__init__(marka, numer_rejestracyjny)

    def wyswietl(self):
        tekst = 'Samochód osobowy: ' + Pojazd.wyswietl(self) + f', Ilość miejsc: {self.liczba_miejsc}'
        return tekst


class Samochod_dostawczy(Pojazd):
    def __init__(self, marka, numer_rejestracyjny, ilosc):
        self.ladownosc = ilosc
        super().__init__(marka, numer_rejestracyjny)

    def wyswietl(self):
        tekst = 'Samochód dostawczy: ' + Pojazd.wyswietl(self) + f', Udźwig: {self.ladownosc} t'
        return tekst
                

sklep = Wypożyczalnia_samochodowa('Fajna nazwa')
sklep.dodaj_pojazd('osobowy', 'Audi', 'Kr 34346', 5)
sklep.dodaj_pojazd('osobowy', 'BMW', 'Kr 99123', 4)
sklep.dodaj_pojazd('osobowy', 'Volvo', 'Kr 00800', 7)
sklep.dodaj_pojazd('dostawczy', 'Honda', 'Kr 66555', 15)
sklep.dodaj_pojazd('dostawczy', 'Opel', 'Kr 11000', 8)
sklep.wyswietl_wszystkie()
sklep.pozycz('Kr 34346')
sklep.pozycz('Kr 66555')
sklep.wyswietl_dostepne()
sklep.oddaj('Kr 34346', 950)
sklep.wyswietl_niedostepne()
sklep.wyswietl_dostepne()