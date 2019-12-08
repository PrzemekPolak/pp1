
class lista_kontaktow():
    class kontakt():
        def __init__(self, nazwa, email, telefon):
            self.nazwa = nazwa
            self.email = email
            self.telefon = telefon

    def __init__(self):
        self.lista = []

    def dodaj_kontakt(self, kontakt):
        self.lista.append(kontakt)

    def wyswietl(self):
        for x in self.lista:
            print(x.nazwa, x.email, x.telefon, sep='\t')
       

k1 = lista_kontaktow.kontakt('Kowalski Jan', 'jank@onet.pl', 555234000)
k2 = lista_kontaktow.kontakt('Borek Patrycja', 'bp@o2.pl', 232000199)
k3 = lista_kontaktow.kontakt('Maj Piotr', 'maj@google.pl', 222999100)
k4 = lista_kontaktow.kontakt('Adamczyk Anna', 'ada@poczta.pl', 100200300) 

kontakty = lista_kontaktow()
kontakty.dodaj_kontakt(k1)
kontakty.dodaj_kontakt(k2)
kontakty.dodaj_kontakt(k3)
kontakty.dodaj_kontakt(k4)

kontakty.wyswietl()
