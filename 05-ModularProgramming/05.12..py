from turtle import *

def kolko(x,y,r):
    up()
    setposition(x,y)
    down()
    circle(r)

def trojkat(x,y,m):
    up()
    setposition(x,y)
    down()
    forward(m)
    right(120)
    forward(m)
    right(120)
    forward(m)
    
def gwiazda(x,y,b):
    up()
    setposition(x,y)
    down()
    for x in range(5):
        forward(b)
        right(144)
        forward(b)
        left(72)
 
def kolkw(kolor,bok):
    color(kolor)
    begin_fill()
    for i in range(4):
        forward(bok)
        right(90)
    end_fill()

def szachownica(il):
    for j in range(il):
        for k in range(il):
            up()
            setposition(j*50,k*50)
            down()
            if (k%2==0 and j%2==0) or (k%2!=0 and j%2!=0):
                kolkw('black',50)
            else:
                kolkw('white',50)
    up()
    setposition(0,(il-1)*50)
    down()
    for i in range(4):
        forward(il*50)
        right(90)

#kolko(50,50,200)
#trojkat(-50,-50,100)
#gwiazda(-100,0,100)
#kolkw('red',80)
#szachownica(6)
