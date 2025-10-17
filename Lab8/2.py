import turtle
import math

def draw_diamond(t, side):
    """Draw one filled diamond centered at the current position."""
    h = math.sqrt(3) * side / 2
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(90)
    t.forward(h / 2)
    t.setheading(210)
    for _ in range(2):
        t.forward(side)
        t.left(120)
        t.forward(side)
        t.left(60)
    t.setheading(270)
    t.forward(h / 2)
    t.end_fill()

def logo_3_diamonds(side=100):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    h = math.sqrt(3) * side / 2

    # Slight overlap fix (remove tiny gap)
    overlap = h * 0.08  # adjust this if needed (0.05–0.1 works best)

    # Top diamond (slightly lower)
    t.penup()
    t.goto(0, h - overlap)
    t.pendown()
    draw_diamond(t, side)

    # Left diamond (slightly higher)
    t.penup()
    t.goto(-side + overlap / 2, -h + overlap / 2)
    t.pendown()
    draw_diamond(t, side)

    # Right diamond (slightly higher)
    t.penup()
    t.goto(side - overlap / 2, -h + overlap / 2)
    t.pendown()
    draw_diamond(t, side)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Figure 3.37 — A Famous Logo (Final Aligned)")
    logo_3_diamonds(100)
    wn.mainloop()
