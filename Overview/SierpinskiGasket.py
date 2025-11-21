from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# ===================== MYINIT =====================
def myInit():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # White color for points
    glPointSize(2.0)                   # Small point size for many dots

# ===================== RESHAPE =====================
def myReshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)

# ===================== DRAW DOT =====================
def drawDot(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# ===================== SIERPINSKI GASKET =====================
def drawSierpinski(num_points=1000):
    # Three fixed triangle points
    T = [(10, 10), (300, 30), (200, 300)]
    
    # Choose initial point randomly among T
    index = random.randint(0, 2)
    point = list(T[index])
    drawDot(point[0], point[1])  # Draw initial point

    # Generate remaining points
    for _ in range(num_points):
        index = random.randint(0, 2)
        # Midpoint between current point and chosen triangle corner
        point[0] = (point[0] + T[index][0]) // 2
        point[1] = (point[1] + T[index][1]) // 2
        drawDot(point[0], point[1])

# ===================== DISPLAY =====================
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    drawSierpinski()  # Draw 1000 dots for Sierpinski Gasket
    glFlush()

# ===================== MAIN PROGRAM =====================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Sierpinski Gasket")

    myInit()
    glutDisplayFunc(myDisplay)
    glutReshapeFunc(myReshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
