from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

# Store the three clicked corners
corners = []
numCorners = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # Drawing color white
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

# Dummy Sierpinski function for now
def Sierpinski(corner_points, depth=5):
    # You can replace this with your Sierpinski drawing logic
    # For now, it will just draw the triangle outline
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for (x, y) in corner_points:
        glVertex2i(x, y)
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

def mouse(button, state, x, y):
    global corners, numCorners
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        corners.append((x, height - y))  # Flip y-coordinate
        numCorners += 1

        if numCorners == 3:
            Sierpinski(corners)
            corners = []
            numCorners = 0

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Sierpinski Gasket with Mouse")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
