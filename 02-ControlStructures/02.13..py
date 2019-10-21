x = int(input('Wprowadź x:'))
y = int(input('Wprowadź y:'))

if x==0 and y==0:
    print(f'Punkt P({x},{y}) znajduje się na początku układu współrzędnych')
elif x>0 and y>0:
    print(f'Punkt P({x},{y}) znajduje się w pierwszej ćwiartce układu współrzędnych')
elif x<0 and y>0:
    print(f'Punkt P({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych')
elif x<0 and y<0:
    print(f'Punkt P({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych')
elif x>0 and y<0:
    print(f'Punkt P({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych')