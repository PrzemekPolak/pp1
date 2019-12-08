class rachunek_bankowy():
    def __init__(self, numer):
        self.numer = numer
        self.saldo = 0

    def wyswietl_stan(self):
        s = str(self.numer)
        print(f'Rachunek nr: {s[0:2]} {s[2:6]} {s[6:10]} {s[10:14]} {s[14:18]} {s[18:22]} {s[22:26]}')
        print(f'Saldo: {self.saldo:.2f} zł')

    def wplac(self, wplata):
        self.saldo += wplata

    def wyplac(self, wyplata):
        if wyplata <= self.saldo:
            self.saldo -= wyplata
        else:
            print('Niewystarczająca ilość środków na rachunku')


rach = rachunek_bankowy(12345655559090111100007722)
rach.wyswietl_stan()
rach.wplac(25.30)
rach.wyswietl_stan()
rach.wplac(31.70)
rach.wyswietl_stan()
rach.wyplac(14)
rach.wyswietl_stan()
