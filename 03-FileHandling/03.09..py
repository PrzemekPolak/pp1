n = 0

with open('NoEducation.txt','r') as file:
    for line in file:
        n += 1
        print(f'{n}.', end='')
        print(line, end='')