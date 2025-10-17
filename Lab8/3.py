import turtle
import math

t = turtle.Turtle()
t.speed(0)

def forward(d, visible=True):
    if visible:
        t.forward(d)
    else:
        t.penup()
        t.forward(d)
        t.pendown()

def turn(angle):
    t.left(angle)

# shorthand commands
commands = "FLFLFLFRFLFLFLFRFLFLFLFR"
for c in commands:
    if c == 'F':
        forward(50, True)
    elif c == 'L':
        turn(60)
    elif c == 'R':
        turn(-60)

turtle.done()
