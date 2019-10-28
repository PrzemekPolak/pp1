pr = input('Podaj nazwę produktu: ')

with open('shoppinglist.txt','a') as file:
    file.write(f'{pr}\n')