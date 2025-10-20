import turtle

# --- SETUP TURTLE ---
t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.color("purple")

# --- DRAW FIGURE B (SPIRAL SQUARE) ---
def figure_b(length=20, increment=15, turns=20):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(turns):
        t.forward(length)
        t.right(90)
        length += increment

# --- MAIN PROGRAM ---
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=400, height=400)

figure_b()
t.hideturtle()
turtle.done()