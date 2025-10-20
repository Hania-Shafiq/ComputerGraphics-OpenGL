import turtle

t = turtle.Turtle()
t.speed(1)
t.pensize(3)
#turtle.tracer(0) #turn off animation, full drawing shown at the start

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()
t.fillcolor("black")

def draw_diamond(size):  
    t.begin_fill()              # ← fill start
    for _ in range(2):
        t.forward(size)
        t.right(60)
        t.forward(size)
        t.right(120)
    t.end_fill()                # ← fill end

for i in range(3):
    draw_diamond(100)
    t.penup()
    t.goto(0, 0)
    t.right(120)
    t.pendown()

turtle.update()
t.hideturtle()
turtle.done()
