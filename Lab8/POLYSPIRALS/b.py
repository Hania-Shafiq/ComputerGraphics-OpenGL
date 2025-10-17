import turtle

def polyspiral(length, angle, incr, num):
    for i in range(num):
        turtle.forward(length)
        turtle.right(angle)
        length += incr

turtle.speed(0)
turtle.color("purple")

polyspiral(2, 89.5, 2, 150)

turtle.done()
