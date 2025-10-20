import turtle
t = turtle.Turtle()
t.speed(3)
L = 100

# Start at bottom-left point of left triangle
t.penup()
t.goto(-L, -L/2)
t.pendown()

# Draw bottom-left triangle
t.setheading(0)
for _ in range(3):
    t.forward(L)
    t.left(120)

# Move to bottom-right triangle (shared edge)
t.right(120)
t.forward(L)
t.left(120)

# Draw bottom-right triangle (shares one edge)
for _ in range(2):
    t.forward(L)
    t.left(120)

# Move to top triangle
t.right(120)
t.forward(L)
t.left(120)

# Draw top triangle (shares edge)
for _ in range(2):
    t.forward(L)
    t.left(120)

t.hideturtle()
turtle.done()