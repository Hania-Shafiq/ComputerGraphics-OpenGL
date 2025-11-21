from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500
screenHeight = height

# Variables to store corners
corner = []
numCorners = 0

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # White background
    glColor3f(0.2, 0.2, 0.8)          # Rectangle color
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)   # 2D orthographic projection

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()  # just clear for now; rectangles drawn in mouse callback

def reshape(w, h):
    global width, height, screenHeight
    width, height = w, h
    screenHeight = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

def myMouse(button, state, x, y):
    global corner, numCorners
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Save first or second corner, flip y-coordinate
        corner.append((x, screenHeight - y))
        numCorners += 1

        if numCorners == 2:
            # Draw rectangle
            x0, y0 = corner[0]
            x1, y1 = corner[1]
            glColor3f(0.2, 0.2, 0.8)  # color for rectangle
            glRecti(x0, y0, x1, y1)
            glFlush()
            # Reset for next rectangle
            corner = []
            numCorners = 0

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Clear screen on right click
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Draw Rectangle with Mouse")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(myMouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
