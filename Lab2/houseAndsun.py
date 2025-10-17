from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# ------------------ DISPLAY FUNCTION ------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # -------- SKY BACKGROUND --------
    glColor3f(0.5, 0.8, 1.0)   # light blue
    glBegin(GL_QUADS)
    glVertex2f(-1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    # -------- GROUND --------
    glColor3f(0.2, 0.7, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.5)
    glVertex2f(-1.0, -0.5)
    glEnd()

    # -------- HOUSE BODY (POLYGON) --------
    glColor3f(0.8, 0.5, 0.2)
    glBegin(GL_POLYGON)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-0.2, -0.5)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.6, -0.2)
    glEnd()

    # -------- HOUSE ROOF (TRIANGLE) --------
    glColor3f(0.6, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.65, -0.2)
    glVertex2f(-0.15, -0.2)
    glVertex2f(-0.4, 0.05)
    glEnd()

    # -------- SUN (TRIANGLE FAN) --------
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.6, 0.7)  # center
    for angle in range(0, 361, 10):
        x = 0.6 + 0.1 * math.cos(math.radians(angle))
        y = 0.7 + 0.1 * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

    # -------- SUN RAYS (LINE STRIPS) --------
    glColor3f(1.0, 1.0, 0.0)
    for angle in range(0, 360, 45):
        x1 = 0.6 + 0.1 * math.cos(math.radians(angle))
        y1 = 0.7 + 0.1 * math.sin(math.radians(angle))
        x2 = 0.6 + 0.2 * math.cos(math.radians(angle))
        y2 = 0.7 + 0.2 * math.sin(math.radians(angle))
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    # -------- TREE TRUNK (LINE STRIP) --------
    glColor3f(0.4, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.05, -0.5)
    glVertex2f(0.05, -0.3)
    glVertex2f(0.0, -0.3)
    glEnd()

    # -------- TREE FOLIAGE (TRIANGLE FAN) --------
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.025, -0.2)
    for angle in range(0, 361, 15):
        x = 0.025 + 0.15 * math.cos(math.radians(angle))
        y = -0.2 + 0.15 * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

    glFlush()

# ------------------ SETUP WINDOW ------------------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"House and Tree")
glClearColor(0.7, 0.9, 1.0, 1.0)
glutDisplayFunc(display)
glutMainLoop()
