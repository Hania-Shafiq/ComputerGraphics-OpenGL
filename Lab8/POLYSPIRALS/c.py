import turtle

def polyspiral(length, angle, incr, num):
    for i in range(num):
        turtle.forward(length)
        turtle.right(angle)
        length += incr

turtle.speed(0)
turtle.color("brown")

polyspiral(5, -144, 2, 120)

turtle.done()
