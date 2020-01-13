try:
    with open('NoEducation.txt','r') as file:
        for line in file:
            print(line)
except:
    print('brak pliku o podanej nazwie lub jego niepoprawne otwarcie')
