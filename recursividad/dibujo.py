import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def spiral(myTurtle,length):
    if length > 0:
        myTurtle.forward(length)
        myTurtle.left(130)
        spiral(myTurtle, length-2)

colors=['#ff0000','#ff8000','#ffff00','#ffff00','#00ff00','#00ff80','#00ffff','#007fff','#0000ff','#8000ff','#ff00ff','#ff0000','#ff8000','#ffff00','#ffff00','#00ff00']

for color in colors:
    myTurtle.pencolor(color)
    spiral(myTurtle,100)

myWin.exitonclick()