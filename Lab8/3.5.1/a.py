import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.color("black")

def drawFigureA():
    # Move to start position
    t.penup()
    t.goto(-400, -100)
    t.setheading(0)
    t.pendown()

    # ----- same sequence as your C++ code -----
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
    t.forward(30); t.left(180)
    t.penup()
    t.forward(30); t.left(180)
    t.pendown()
    t.forward(120); t.left(90)
    t.forward(90); t.left(90)
    # -----------------------------------------

# Main
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=1000, height=600)

drawFigureA()

t.hideturtle()
turtle.done()
