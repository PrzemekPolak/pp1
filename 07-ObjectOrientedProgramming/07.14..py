class Telefon():
    def __init__(self,numer,kolor):
        self.numer = numer
        self.kolor = kolor
        self.wlaczony = True

    def wylacz(self):
        self.wlaczony = False
        print('Telefon wyłączony')

    def zalacz(self):
        self.wlaczony = True
        print('Telefon załączony') 

    def wyswietl_stan(self):
        print(f'Kolor: {self.kolor}')
        print(f'Numer: {self.numer}')
        if self.wlaczony:
            print(f'Stan: Załączony')
        else:
            print(f'Stan: Wyłączony')


tel1 = Telefon(444333555, 'Czarny')
tel2 = Telefon(111222333, 'Biały')

tel1.wylacz()
tel1.wyswietl_stan()
print('')
tel2.wyswietl_stan()
print('')
tel1.zalacz()
tel1.wyswietl_stan()
print('')
tel2.wyswietl_stan()