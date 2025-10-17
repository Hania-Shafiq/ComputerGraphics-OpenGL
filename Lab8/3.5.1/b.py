import turtle

def figure_b(length=20, increment=15, turns=20):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(turns):
        t.forward(length)
        t.right(90)
        length += increment

if __name__ == "__main__":
    wn = turtle.Screen()
    figure_b(10, 10, 20)
    wn.mainloop()
