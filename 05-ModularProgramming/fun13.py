def wspak(txt):
    tab = []
    for x in txt:
        tab.append(x)
    tab.reverse()
    for i in tab:
        print(f'{i}',end='')
    print()

def rozstrzelony(txt):
    tab = []
    for x in txt:
        tab.append(x)
    for i in tab:
        print(f'{i} ',end='')
    print()

def duzelit(txt):
    txt2 = txt.casefold()
    txt3 = txt2.title()
    print(txt3)
    