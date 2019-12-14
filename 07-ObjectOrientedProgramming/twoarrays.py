from arrays import *

tablica1 = Arrays.tworzenie_jednakowe_wartosci(10,4)
Arrays.zaw_tablicy_wiersz(tablica1)

tablica2 = Arrays.tworzenie_losowa_wartosc(20,-7,8)
Arrays.zaw_tablicy_wiersz(tablica2)

print(f'Tablica 20-elementowa zawiera {Arrays.wyznaczanie_elementow(tablica2,-1,1)} wartości z przedziału <-1,1>')