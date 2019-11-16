tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def sum(tab):
    s = 0
    for x in range(len(tab)):
        if isinstance(tab[x],list) == True:
            s += sum(tab[x])
        else:
            s += tab[x]
    return s
    
print(tab)
print(f'Suma wartości: {sum(tab)}')