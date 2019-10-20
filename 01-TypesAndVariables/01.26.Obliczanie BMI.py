#Wprowadzanie danych przez użytkownika
print('Podaj wzrost w cm:')
wzrost = int(input())
print('Podaj wagę w kg:')
waga = int(input())

bmi = waga / (wzrost/100)**2    #Wzór na BMI

#Określenie czy waga jest odpowiednia
if bmi >= 18.5 and bmi <= 24.9:
    print(f'Wskaźnik BMI: {bmi} (waga prawidłowa)')
else:
    print(f'Wskaźnik BMI: {bmi} (waga nieprawidłowa)')
        
