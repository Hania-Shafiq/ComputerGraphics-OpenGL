from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# ---------- draw static flurry rectangles ----------
def drawFlurry(num, Width, Height):
    glClear(GL_COLOR_BUFFER_BIT)
    
    for i in range(num):
        x1 = random.randint(0, Width)
        y1 = random.randint(0, Height)
        x2 = random.randint(0, Width)
        y2 = random.randint(0, Height)
        lev = random.randint(0, 10) / 10.0   # gray level between 0.0 to 1.0
        glColor3f(lev, lev, lev)
        glRecti(x1, y1, x2, y2)
    
    glFlush()

# ---------- initialization ----------
def myInit():
    glClearColor(1, 1, 1, 0)   # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)  # window size in world coords

# ---------- display function ----------
def myDisplay():
    drawFlurry(20, 500, 500)  # draw 20 random rectangles

# ---------- main ----------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Static Flurry Rectangles")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

main()
