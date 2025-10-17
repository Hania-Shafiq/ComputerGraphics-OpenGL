import turtle

def polyspiral(length, angle, incr, num):
    for i in range(num):
        turtle.forward(length)
        turtle.right(angle)
        length += incr

turtle.speed(0)
turtle.color("pink")

polyspiral(5, 60, 2, 60)

turtle.done()
