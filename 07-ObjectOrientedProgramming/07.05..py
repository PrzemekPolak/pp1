class Piosenki():
    def __init__(self, wykonawca, tytul, rok, album):
        self.wykonawca = wykonawca
        self.tytul = tytul
        self.rok = rok
        self.album = album

    def __str__(self):
        return '''
Wykonawca: {}
Utwór: {}
Album: {}
Rok: {}
                '''.format(self.wykonawca, self.tytul, self.album, self.rok)
        

utwor1 = Piosenki('Wykonawca1', 'Tytul1', 'Utwor1', 'Album1')
utwor2 = Piosenki('Wykonawca2', 'Tytul2', 'Utwor2', 'Album2')
utwor3 = Piosenki('Wykonawca3', 'Tytul3', 'Utwor3', 'Album3')

print(utwor1)
print(utwor2)
print(utwor3)
