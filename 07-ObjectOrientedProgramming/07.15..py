class Ksiazka():

    class Ebook():
        def __init__(self, nazwa_pliku):
            self.nazwa_pliku = nazwa_pliku
    
        def wyswietl(self):
            print(f'Ebook. Nazwa pliku: {self.nazwa_pliku}')


    class Ksiazka_papierowa():
        def __init__(self,ilosc_stron):
            self.ilosc_stron = ilosc_stron

        def wyswietl(self):
            print(f'Ksiażka papierowa. Ilość stron: {self.ilosc_stron} ')


papierowa = Ksiazka.Ksiazka_papierowa(250)
elektroniczna = Ksiazka.Ebook('plik zrodlowy')

papierowa.wyswietl()
elektroniczna.wyswietl()