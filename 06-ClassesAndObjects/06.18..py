class kostka():
    def rzuc(self):
        import random
        return random.randrange(1,7)


kos1 = kostka()
kos2 = kostka()
kos3 = kostka()

for x in range(5):
    wyn1 = kos1.rzuc()
    wyn2 = kos2.rzuc()
    wyn3 = kos3.rzuc()
    sum = wyn1 + wyn2 + wyn3 
    print(f'kostka1: {wyn1}, kostka1: {wyn2}, kostka1: {wyn3}  Suma: {sum}') 
