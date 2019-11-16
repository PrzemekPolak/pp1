licz = int(input('Podaj liczbę: '))

def sumcyf(licz):
    from math import floor
    if licz < 10:
        return floor(licz)
    else:
        return floor(licz%10) + sumcyf(licz/10)
    
print(sumcyf(licz))