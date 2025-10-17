import turtle

def polyspiral(length, angle, incr, num):
    for i in range(num):
        turtle.forward(length)
        turtle.right(angle)
        length += incr

turtle.speed(0)
turtle.color("red")

polyspiral(5, 170, 2, 180)

turtle.done()
