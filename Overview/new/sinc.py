from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Window size
width = 640
height = 480

#--------------- setWindow --------------------
def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

#--------------- setViewport ------------------
def setViewport(left, right, bottom, top):
    glViewport(int(left), int(bottom),
               int(right - left), int(top - bottom))

#--------------- Display Function -------------
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    # Window: world coordinates
    setWindow(-5.0, 5.0, -0.3, 1.0)

    # Viewport: screen coordinates
    setViewport(0, width, 0, height)

    glBegin(GL_LINE_STRIP)
    for i in range(-40, 40):
        x = i / 10.0
        if x == 0:
            y = 1
        else:
            y = math.sin(math.pi * x) / (math.pi * x)
        glVertex2f(x, y)
    glEnd()

    glFlush()


#--------------- Main -------------------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Sinc Function Plot")

    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)         # Black drawing

    glutDisplayFunc(myDisplay)
    glutMainLoop()


main()
