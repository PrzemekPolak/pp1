class Student():
    numer_albumu = 100000
    uczelnia = 'UEK Kraków'

    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_albumu = Student.numer_albumu
        self.kierunek = kierunek
        self.uczelnia = Student.uczelnia
        Student.numer_albumu += 1

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.numer_albumu}), {self.kierunek}, {self.uczelnia}'

student1 = Student('Imie1', 'Nazwisko1', 'Kierunek1')
student2 = Student('Imie2', 'Nazwisko2', 'Kierunek2')
student3 = Student('Imie3', 'Nazwisko3', 'Kierunek3')

print(student1)
print(student2)
print(student3)
