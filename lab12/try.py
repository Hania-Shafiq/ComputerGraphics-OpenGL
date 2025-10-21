from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Global variables
eye_z = 5.0
width, height = 800, 600

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)

def display():
    global eye_z
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Increased z-range so zoom movement stays visible
    glOrtho(-10, 10, -10, 10, -100, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Move the whole scene back/forth
    glTranslatef(0.0, 0.0, -eye_z)

    # Draw objects
    glColor3f(1.0, 0.6, 0.0)

    glPushMatrix()
    glutWireCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.0, 0.0, 0.0)
    glutWireSphere(1.0, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.0, 0.0, 0.0)
    glutWireTeapot(1.0)
    glPopMatrix()

    glFlush()

def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -100, 100)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global eye_z
    if key == b'q':
        sys.exit(0)
    elif key == b'e':   # move camera back (zoom out)
        eye_z += 1.0
    elif key == b'd':   # move camera forward (zoom in)
        eye_z -= 1.0
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Visualization with Ortho Zoom")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
