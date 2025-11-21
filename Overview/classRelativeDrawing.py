from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#=========================
# POINT CLASS
#=========================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#=========================
# POINTARRAY CLASS (list of vertices)
#=========================
class PointArray:
    def __init__(self):
        self.num = 0
        self.pt = []      # list of Point objects

#=========================
# DRAW POLYLINE / POLYGON
#=========================
def drawPolyLine(poly, closed):
    glBegin(GL_LINE_LOOP if closed else GL_LINE_STRIP)

    for p in poly.pt:
        glVertex2i(p.x, p.y)

    glEnd()
    glFlush()

#=========================
# DISPLAY FUNCTION
#=========================
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    # -------- SAMPLE 1: OPEN POLYLINE --------
    poly1 = PointArray()
    poly1.pt = [Point(50, 50), Point(100, 80), Point(150, 40), Point(200, 100)]
    poly1.num = len(poly1.pt)

    glColor3f(1, 0, 0)     # Red
    glLineWidth(2)
    drawPolyLine(poly1, closed=0)   # open polyline


    # -------- SAMPLE 2: CLOSED POLYGON --------
    poly2 = PointArray()
    poly2.pt = [Point(300, 50), Point(350, 120), Point(400, 50)]
    poly2.num = len(poly2.pt)

    glColor3f(0, 0, 1)     # Blue
    glLineWidth(3)
    drawPolyLine(poly2, closed=1)   # closed polygon

    glFlush()

#=========================
# INIT WINDOW
#=========================
def myInit():
    glClearColor(1, 1, 1, 0)
    glColor3f(0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 300)

#=========================
# MAIN FUNCTION
#=========================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 300)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Polyline & Polygon Example")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

main()
