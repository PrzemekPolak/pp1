#Pobranie odpowiedniego modułu
from random import randint

#Przypisanie 3 zmiennym losowych wartosci całkowitych z zakresu [1,6]
num1 = randint(1,6)
num2 = randint(1,6)
num3 = randint(1,6)

#Pokazanie wyników
print(f'Pierwszy rzut: {num1}')
print(f'Drugi rzut: {num2}')
print(f'Trzeci rzut: {num3}')
print(f'Suma rzutów: {num1 + num2 + num3}')