from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def parameterizedHouse(peak, width, height):
    # shell of house
    glBegin(GL_LINE_LOOP)
    glVertex2i(peak.x, peak.y)
    glVertex2i(peak.x + width//2, peak.y - (3*height)//8)
    glVertex2i(peak.x + width//2, peak.y - height)
    glVertex2i(peak.x - width//2, peak.y - height)
    glVertex2i(peak.x - width//2, peak.y - (3*height)//8)
    glEnd()

    # chimney
    glBegin(GL_LINE_STRIP)
    glVertex2i(peak.x + width//4, peak.y - 10)
    glVertex2i(peak.x + width//4, peak.y + 20)
    glVertex2i(peak.x + width//4 + 10, peak.y + 20)
    glEnd()

    # door
    glBegin(GL_LINE_LOOP)
    glVertex2i(peak.x - 10, peak.y - height)
    glVertex2i(peak.x - 10, peak.y - height + 30)
    glVertex2i(peak.x + 10, peak.y - height + 30)
    glVertex2i(peak.x + 10, peak.y - height)
    glEnd()

    # window
    glBegin(GL_LINE_LOOP)
    glVertex2i(peak.x - 30, peak.y - height + 40)
    glVertex2i(peak.x - 10, peak.y - height + 40)
    glVertex2i(peak.x - 10, peak.y - height + 60)
    glVertex2i(peak.x - 30, peak.y - height + 60)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0,0,0)

    # multiple houses
    parameterizedHouse(Point(100, 180), 80, 100)
    parameterizedHouse(Point(200, 150), 60, 80)
    parameterizedHouse(Point(300, 200), 100, 120)

    glFlush()

def myInit():
    glClearColor(1,1,1,1)
    gluOrtho2D(0,400,0,300)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,400)
glutCreateWindow(b"Parameterized House")
myInit()
glutDisplayFunc(display)
glutMainLoop()
