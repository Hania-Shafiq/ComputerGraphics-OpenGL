import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.color("purple")
def drawFigureA():
    # Move to start position
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    t.forward(30); t.right(90)
    t.forward(30); t.left(90)
    t.forward(30); t.left(90)
    t.forward(60); t.left(90)

    t.forward(60); t.right(90)
    t.forward(30); t.right(90)
    t.forward(90); t.right(90)
    t.forward(90); t.left(90)
    
    t.forward(30); t.left(90)
    t.forward(120); t.left(90)
    t.forward(120); t.left(90)
    t.forward(30)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(60); t.left(90)
    t.forward(30)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(30)
# Main
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=400, height=400)

drawFigureA()

t.hideturtle()
turtle.done()
