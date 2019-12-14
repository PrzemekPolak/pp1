class Point(): 
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
        
    def __str__(self): 
        return f'P({self.x},{self.y})'

    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)


p1 = Point(1,1)
p2 = Point(2,2)

if p1 == p2:
    print('Punkty są identyczne')
else:
    odl = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
    print(f'Odlogłość wynosi: {odl}')