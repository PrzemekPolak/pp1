wzrost = input('Podaj wzrost w cm: ')
assert type(int(wzrost)) == int, 'Błędny wzrost'
wzrost = int(wzrost)
assert wzrost <= 220 and wzrost >= 150, 'Błędny wzrost'

waga = input('Podaj wagę w kg: ')
assert type(float(waga)) == float, 'Błedna waga'
waga = float(waga)
assert waga >= 40.0 and waga <= 150.0, 'Błedna waga'

bmi = waga / (wzrost**2 / 10000)

print(f'BMI: {bmi}')