class Pola():
    @staticmethod
    def kolo(promien):
        from math import pi
        return pi * promien**2

    @staticmethod
    def prostokat(a,b):
        return a * b

    @staticmethod
    def trojkat(podstawa, wysokosc):
        return (podstawa * wysokosc) / 2


print(f'Pole koła o promieniu 3 wynosi {Pola.kolo(3)}')
print(f'Pole prostokąta o bokach 4 oraz 7 wynosi {Pola.prostokat(4,7)}')
print(f'Pole trójkąta o podstawie 6 i wysokości 2 wynosi {Pola.trojkat(6,2)}')