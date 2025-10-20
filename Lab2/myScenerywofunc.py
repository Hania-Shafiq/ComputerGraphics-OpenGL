from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# RECTANGLE DRAW KARNE KA FUNCTION
def draw_rect(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    brown = (0.6, 0.4, 0.3)

    # WINDOW
    draw_rect(-4, 4, -0.4, 8, (0.4, 0.7, 1))
    draw_rect(-0.4, 4, 0.4, 8, brown)
    draw_rect(0.4, 4, 4, 8, (0.4, 0.7, 1))

    # CHAIR
    draw_rect(-8, -2, -6, 0.8, brown)  # backrest
    glColor3f(*brown)
    glBegin(GL_QUADS)  # seat parallelogram
    glVertex2f(-7, -3)
    glVertex2f(-5, -3)
    glVertex2f(-6, -2)
    glVertex2f(-8, -2)
    glEnd()
    draw_rect(-8, -4, -7.8, -2, brown)
    draw_rect(-6.2, -4.4, -6, -2, brown)
    draw_rect(-7, -5.4, -6.8, -3, brown)
    draw_rect(-5.2, -5.4, -5, -3, brown)

    # TABLE
    glColor3f(*brown)
    glBegin(GL_QUADS)  # top surface
    glVertex2f(-2.6, -1.2)
    glVertex2f(3.8, -1.2)
    glVertex2f(2.4, 1.6)
    glVertex2f(-4, 1.6)
    glEnd()
    draw_rect(-4, -4, -3.6, 1.6, brown)
    draw_rect(2, -4, 2.4, 1.6, brown)
    draw_rect(-2.6, -6.8, -2.2, -1.2, brown)
    draw_rect(3.4, -6.8, 3.8, -1.2, brown)
    draw_rect(-2.6, -2, 3.8, -1.2, brown)

    # Laptop base (parallelogram)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-2.2, -0.6)
    glVertex2f(0.4, -0.6)
    glVertex2f(-0.4, 0.8)
    glVertex2f(-3, 0.8)
    glEnd()
    draw_rect(-3, 0.8, -0.4, 3, (0.1, 0.1, 0.1))

    # Cup (trapezoid)
    glColor3f(0.4, 0.7, 1)
    glBegin(GL_QUADS)
    glVertex2f(1.2, 0.2)
    glVertex2f(1.6, 0.2)
    glVertex2f(1.8, 1)
    glVertex2f(1, 1)
    glEnd()

    # Lamp
    draw_rect(5, -6, 7, -5, brown)
    draw_rect(5.6, -5, 6.4, 0.8, brown)
    glColor3f(1, 1, 0.4)
    glBegin(GL_QUADS)
    glVertex2f(4, 0.8)
    glVertex2f(8, 0.8)
    glVertex2f(7.2, 3.4)
    glVertex2f(4.8, 3.4)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Room Scene (Simplified)")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10, 10, -10, 10)
    glutDisplayFunc(draw_scene)
    glutMainLoop()

if __name__ == "__main__":
    main()
