# Lab Activity 8: Plotting Parametric Form of Curves

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 600, 600


def draw_parametric_curve(func_x, func_y, t_min, t_max, steps=500):
    """General parametric curve drawer"""
    glBegin(GL_LINE_STRIP)
    for i in range(steps + 1):
        t = t_min + (t_max - t_min) * i / steps
        x = func_x(t)
        y = func_y(t)
        glVertex2f(x, y)
    glEnd()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Black curve
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)  # Symmetric world window


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Circle (radius 100, center at origin)
    glColor3f(1.0, 1.0, 0.0)
    draw_parametric_curve(
        lambda t: 100 * math.cos(t),  #100 cos
        lambda t: 100 * math.sin(t),
        0, 2 * math.pi
    )

    # Ellipse (a=150, b=80)
    glColor3f(1.0, 0.0, 1.0)
    draw_parametric_curve(
        lambda t: 150 * math.cos(t),
        lambda t: 80 * math.sin(t),
        0, 2 * math.pi
    )

    # Spiral (r increases with t)
    glColor3f(0.9, 0.6, 0.0)
    draw_parametric_curve(
        lambda t: (10 + 2 * t) * math.cos(t),
        lambda t: (10 + 2 * t) * math.sin(t),
        0, 6 * math.pi
    )

    glFlush()


def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab Activity 8: Parametric Curves")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()




# A curve can be described by parametric equations:
# 𝑥(𝑡)=𝑓(𝑡),𝑦(𝑡)=𝑔(𝑡),𝑡∈[𝑡𝑚𝑖𝑛,𝑡𝑚𝑎𝑥]
# Common examples:
# Circle: 𝑥=𝑐𝑥+𝑟cos⁡(𝑡), 𝑦=𝑐𝑦+𝑟sin⁡(𝑡)
# Ellipse: x=cx+acos(t),y=cy+bsin(t)
# Spiral: x=cx+(a+bt)cos(t),y=cy+(a+bt)sin(t)