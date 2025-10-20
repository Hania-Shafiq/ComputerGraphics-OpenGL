import turtle
import math

# ----- Setup turtle -----
t = turtle.Turtle()
t.speed(0)
t.pensize(6)
t.color("black")
t.penup()
t.goto(-500, 0)
t.setheading(0)
t.pendown()
# ----- Motif  -----
def draw_motif():
    t.forward(75); t.left(90)
    t.forward(50); t.left(90)
    t.forward(25); t.left(90)
    t.forward(25); t.right(90)
    t.forward(25); t.right(90)
    t.forward(50); t.right(90)
    t.forward(75); t.right(90)
    t.forward(75); t.left(90)

# ----- Continuous Motifs -> Meander Row -----
def draw_meander_row(count):
    for i in range(count):
        draw_motif()
        
# # ----- Single Meander Motif (Figure b) -----
def draw_isolated_motif(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    draw_motif()
    t.penup()

# ----- Main -----
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=1100, height=400)

draw_meander_row(9)            # left meander row
draw_isolated_motif(200, 100) # right single motif

t.hideturtle()
turtle.done()