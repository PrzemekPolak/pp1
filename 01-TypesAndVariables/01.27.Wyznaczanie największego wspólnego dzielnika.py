from math import gcd

print('Podaj pierwszą liczbę')
num1 = int(input())
print('Podaj drugą liczbę')
num2 = int(input())

print(f'Największy wspólny dzielnik wynosi {gcd(num1,num2)}')
