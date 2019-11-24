def drawSquare(x,y,n):
    import turtle 
    pen = turtle.Turtle()
    pen.penup()
    pen.setposition(x,y)
    pen.pendown()
    for i in range(4):
        pen.forward(n)
        pen.right(90)

