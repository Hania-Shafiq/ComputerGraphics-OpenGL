from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500
NUM = 20  # Maximum points in polyline

# Store polyline points
points = []
last = -1

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)          # White drawing color
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if points:
        glBegin(GL_LINE_STRIP)
        for (x, y) in points:
            glVertex2i(x, y)
        glEnd()
    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

def mouse(button, state, x, y):
    global points, last
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and last < NUM - 1:
        last += 1
        points.append((x, height - y))  # Flip y-coordinate
        glutPostRedisplay()             # Redraw entire polyline

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        points = []
        last = -1
        glutPostRedisplay()             # Clear screen

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Polyline Drawer with Mouse")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
