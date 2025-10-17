import turtle
import math

# ----- Setup turtle -----
t = turtle.Turtle()
t.speed(0)
t.pensize(9)
t.color("black")

# ----- Motif (same as your OpenGL sequence) -----
def draw_motif(d):
    t.pendown()
    t.forward(d); t.left(90)
    t.forward(d / 2); t.left(90)
    t.forward(d * 0.25); t.left(90)
    t.forward(d * 0.25); t.right(90)
    t.forward(d / 3.0); t.right(90)
    t.forward(d / 2.0); t.right(90)
    t.forward(d * 0.75); t.right(90)
    t.forward(d * 0.75); t.right(90)
    # ends on baseline facing 180°

# ----- Continuous Meander Row -----
def draw_meander_row(count, d):
    t.penup()
    t.goto(-400, -100)
    t.setheading(0) #facing right(east)
    t.pendown()

    for i in range(count):
        draw_motif(d)
        t.right(180)
        # 🔧 small correction to avoid end overlap
        t.penup()
        t.forward(d * 0.05)  # fine-tuned offset (remove overlap)
        t.pendown()

# ----- Isolated Motif (Figure b) -----
# def draw_isolated_motif(x, y, d):
#     t.penup()
#     t.goto(x, y)
#     t.setheading(0)
#     t.pendown()
#     draw_motif(d)
#     t.penup()

# ----- Main -----
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=1100, height=400)

draw_meander_row(9, 80)            # left meander row
#draw_isolated_motif(200, -100, 80) # right single motif

t.hideturtle()
turtle.done()
