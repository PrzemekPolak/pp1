print('Podaj długość boku a')
a = int(input())
print('Podaj długość boku b')
b = int(input())
print('Podaj długość boku c')
c = int(input())
pole = ((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))**0.5 / 4  #Wzór Herona
print(f'Pole trójkąta wynosi {pole}')

