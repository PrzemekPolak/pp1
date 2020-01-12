from json import load

print('NBP – 10 ostatnich notowań EURO')
print()
with open('Euro_10_notowan.json') as file:
    data = load(file)
    print('Data         Kupno    Sprzedaż')
    print('==============================')
    for x in range(10):
        day = data['rates'][x]['effectiveDate']
        buy = data['rates'][x]['bid']
        sell = data['rates'][x]['ask']
        print(f'{day}   {buy:.4f}   {sell:.4f}')