# Lab Activity 10: Drawing Circle using Equation x = cx + r cos(φ), y = cy + r sin(φ)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 600, 600


def draw_circle(cx, cy, r, segments=200):
    """Draw a circle centered at (cx,cy) with radius r"""
    glBegin(GL_LINE_LOOP)  # line loop to close circle
    for i in range(segments):
        phi = 2 * math.pi * i / segments   # angle in radians
        x = cx + r * math.cos(phi)
        y = cy + r * math.sin(phi)
        glVertex2f(x, y)
    glEnd()


def init():
    glClearColor(1, 1, 1, 1)  # white background
    glColor3f(0, 0, 0)        # black circle
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # 2D projection


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Example circles
    draw_circle(300, 300, 100)   # main circle
    draw_circle(300, 300, 150)   # bigger circle
    draw_circle(300, 300, 50)    # smaller circle

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab Activity 10: Circle with Equation")
    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
