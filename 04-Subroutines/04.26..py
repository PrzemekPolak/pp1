dochod = int(input('Podaj dochód: '))

def podatek(dochod):
    if dochod <= 5000:
        wyn = (dochod*17)/100
        print(f'Podatek należny: {int(wyn)} zł')
    else:
        pon = (5000*17)/100
        pow = ((dochod-5000)*32)/100
        print(f'Podatek należny: {int(pon+pow)} zł')
        
podatek(dochod)



