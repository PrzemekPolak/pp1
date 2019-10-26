for x in range(1,8):
    for y in range(0,7):
        if x>2:
            print(f'{x+y*7} ',end='')
        else:
            if y==1:
                print(f' {x+y*7} ',end='')
            else:
                print(f'{x+y*7} ',end='')
    print()

