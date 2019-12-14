class Arrays():

    znak = ','

    @staticmethod
    def ustal_seperator(zmieniony_znak):
        Arrays.znak = zmieniony_znak

    @staticmethod
    def zaw_tablicy_wiersz(array):
        tekst = ''
        for x in array:
            tekst = tekst + str(x) + Arrays.znak
        print(tekst[:-1])

    @staticmethod
    def tworzenie_jednakowe_wartosci(liczba_elementow_tablicy,wartosc_elementow_tablicy):
        tab = []
        for x in range(liczba_elementow_tablicy):
            tab.append(wartosc_elementow_tablicy)
        return tab

    @staticmethod
    def tworzenie_losowa_wartosc(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        from random import randrange
        tab = []
        for x in range(liczba_elementow_tablicy):                
            los = randrange(wartosc_od,wartosc_do + 1)
            tab.append(los)
        return tab


tablica1 = Arrays.tworzenie_jednakowe_wartosci(10,4)
Arrays.zaw_tablicy_wiersz(tablica1)

Arrays.ustal_seperator(';')

tablica2 = Arrays.tworzenie_losowa_wartosc(20,-7,8)
Arrays.zaw_tablicy_wiersz(tablica2)