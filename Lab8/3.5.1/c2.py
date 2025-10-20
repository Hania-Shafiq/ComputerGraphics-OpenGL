import turtle

t = turtle.Turtle()
t.speed(0)

def triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# --- 1st triangle ---
t.penup()
t.goto(0, 0)
t.pendown()
triangle(100)

# --- 2nd triangle ---
t.penup()
t.forward(100)
t.right(120)
t.pendown()
triangle(100)

# --- 3rd triangle ---
t.penup()
t.forward(100)
t.right(120)
t.pendown()
triangle(100)

t.hideturtle()
turtle.done()
