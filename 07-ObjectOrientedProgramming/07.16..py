class Student():
    def __init__(self, imie, nazwisko, nr_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albumu = nr_albumu

    def wyswietl(self):
        x = self.imie
        x2 = x.casefold()
        x3 = x2.capitalize()

        y = self.nazwisko
        y2 = y.casefold()
        y3 = y2.capitalize()

        print(f'{x3} {y3} {self.nr_albumu}')
    
    def __eq__(self, other):
        return self.nr_albumu == other.nr_albumu
        
    def __lt__(self, other):
        return self.nr_albumu < other.nr_albumu


s1 = Student('Anna', 'Tomaszewska', 141820)
s2 = Student('Wojciech', 'Zbych', 201003)
s3 = Student('Maja', 'Kowalska', 153202)
s4 = Student('Marek', 'Migiel', 138600)

tab = [s1, s2, s3, s4]
for x in tab:
    x.wyswietl()

new = sorted(tab, key=lambda Student : Student.nr_albumu)

for y in new:
    y.wyswietl()