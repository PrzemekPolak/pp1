a = 5
b = 3
assert b!=0, 'Wartość b równa 0!'
assert type(a) == int and type(b) == int, 'a lub b nie jest liczbą całkowitą'
print(f'{a}/{b} = {a/b}')