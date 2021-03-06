class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

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

    @staticmethod
    def wyznaczanie_elementow(tablica,wartość_od,wartość_do):
        licznik = 0
        for x in tablica:
            if (x >= wartość_od) and (x <= wartość_do):
                licznik += 1
            else:
                continue
        return licznik

    @staticmethod
    def zaw_tablicy_wiersz(array):
        tekst = ''
        for x in array:
            tekst = tekst + str(x) + ', '
        print(tekst[:-2])