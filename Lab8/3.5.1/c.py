import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()
def triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

for _ in range(3):
    triangle(100)
    t.forward(100)
    t.right(120)

t.hideturtle()
turtle.done()
