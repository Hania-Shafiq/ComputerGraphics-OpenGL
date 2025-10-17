import turtle

t = turtle.Turtle()
t.speed(0)

def triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def logo():
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    for i in range(3):
        triangle(100)
        t.penup()
        t.forward(100)
        t.right(120)
        t.pendown()

logo()
turtle.done()
