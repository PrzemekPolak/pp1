class ulamek_zwykly():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def uprosc(self):
        a = self.licznik
        b = self.mianownik 
        while a != b:
            a, b = max(a, b), min(a, b)
            a = a - b
        print(f'{int(self.licznik/a)}/{int(self.mianownik/a)}')

    def wyswietl(self):
        print(f'{self.licznik}/{self.mianownik}')


ul1 = ulamek_zwykly(1, 2)
ul2 = ulamek_zwykly(12, 21)
ul3 = ulamek_zwykly(5, 15)

ul1.wyswietl()
ul1.uprosc()
ul2.wyswietl()
ul2.uprosc()
ul3.wyswietl()
ul3.uprosc()