class samolot():
    def __init__(self, numer_lotu):
        self.numer_lotu = numer_lotu
        self.wysokosc_lotu = 0

    def zwieksz_wysokosc(self, zwieksz):
        roznica = zwieksz - self.wysokosc_lotu
        if roznica > 300 and roznica < 1100:
            self.wysokosc_lotu += roznica
        else:
            print('Zmiana wysokości poza zakresem!')

    def zmniejsz_wysokosc(self, zmniejsz):
        roznica = self.wysokosc_lotu - zmniejsz
        if roznica > 300 and roznica < 1100:
            self.wysokosc_lotu -= roznica
        else:
            print('Zmiana wysokości poza zakresem!')

    def laduj(self):
        if self.wysokosc_lotu > 500:
            print('Zbyt duża wysokość dla lądowania. Obniż lot!')
        else:
            self.wysokosc_lotu = 0

    def startuj(self, wysokosc_poczatkowa):
        self.wysokosc_lotu = wysokosc_poczatkowa

    def status_lotu(self):
        print(f'Tu {self.numer_lotu}, moja wysokość lotu to {self.wysokosc_lotu} m')


sam = samolot('LOT881')
sam.startuj(1200)
sam.status_lotu()
sam.zwieksz_wysokosc(8900)
sam.status_lotu()
sam.zmniejsz_wysokosc(200)
sam.status_lotu()
sam.laduj()
sam.status_lotu()
