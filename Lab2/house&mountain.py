from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # -------- FIELD (QUAD) --------
    glColor3f(0.0, 0.8, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.4)
    glVertex2f(-1.0, -0.4)
    glEnd()

    # -------- MOUNTAINS (TRIANGLES) --------
    glColor3f(0.4, 0.3, 0.2)
    for i in range(-1, 2, 1):
        glBegin(GL_TRIANGLES)
        glVertex2f(i * 0.5 - 0.5, -0.4)
        glVertex2f(i * 0.5, 0.3)
        glVertex2f(i * 0.5 + 0.5, -0.4)
        glEnd()

    # -------- CABIN WALLS (QUADS) --------
    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.4)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.2, -0.1)
    glVertex2f(-0.2, -0.1)
    glEnd()

    # -------- CABIN ROOF (TRIANGLE) --------
    glColor3f(0.5, 0.2, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.25, -0.1)
    glVertex2f(0.25, -0.1)
    glVertex2f(0.0, 0.1)
    glEnd()

    # -------- CABIN LINES (DETAILS) --------
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    # Door
    glVertex2f(-0.05, -0.4)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.4)
    glVertex2f(0.05, -0.2)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.2)
    glEnd()

    glFlush()

# -------- SETUP --------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Mountains and House")
glClearColor(0.5, 0.8, 1.0, 1)
glutDisplayFunc(display)
glutMainLoop()
