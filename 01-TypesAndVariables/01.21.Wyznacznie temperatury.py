print('Podaj temperaturę w stopniach Celsjusza')
temc = int(input())
temk = temc - 273
temf = 9/5 * temc + 32
print(f'{temk} stopni Kelwina')
print(f'{temf} stopni Fahrenheita')