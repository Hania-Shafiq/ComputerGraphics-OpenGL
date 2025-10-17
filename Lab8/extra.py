import turtle

def polyspiral(length, angle, incr, num):
    """
    Draws a polyspiral with given parameters.
    length : initial length of first segment
    angle  : turning angle (in degrees)
    incr   : amount to increase length after each segment
    num    : number of segments
    """
    for i in range(num):
        turtle.forward(length)
        turtle.right(angle)
        length += incr

# --- Example Usage ---
turtle.speed(0)           # Fastest drawing speed
turtle.pensize(1)
turtle.color("black")

# You can test different combinations like these:
polyspiral(5, 60, 2, 60)      # hexagonal type
turtle.penup(); turtle.goto(200, 0); turtle.pendown()
polyspiral(2, 89.5, 2, 150)   # square-like spiral
turtle.penup(); turtle.goto(-200, -200); turtle.pendown()
polyspiral(5, -144, 2, 120)   # star type
turtle.penup(); turtle.goto(200, -200); turtle.pendown()
polyspiral(5, 170, 2, 180)    # dense spiky spiral

turtle.done()
