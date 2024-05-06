import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def spiral(myTurtle,length):
    if length > 0:
        myTurtle.forward(length)
        myTurtle.left(130)
        spiral(myTurtle, length-2)

myTurtle.pencolor('red')
spiral(myTurtle,100)
myWin.exitonclick()