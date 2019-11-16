tab = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8]

def npow(tab):
    pom = []
    minil = tab.count(min(tab, key=tab.count))
    while tab.count(min(tab, key=tab.count)) == minil:
        x = min(tab, key=tab.count)
        for i in range(minil):
            tab.remove(x)
        pom.append(x)
    return pom
    
print(tab)
print(f'Wartości które się nie powtarzają: {npow(tab)}')