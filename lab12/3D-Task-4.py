from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Global variables
eye_z = 5.0
theta = 0.0
width, height = 800, 600

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-10, 10, -10, 10, -20, 20)  # 3D coordinate system

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     gluLookAt(0.0, 0.0, eye_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # Camera position and orientation

#     glColor3f(0.0, 1.0, 0.0)  # Green color for objects
#     glPushMatrix()
#     glutWireCube(2.0)
#     glPopMatrix()

#     glPushMatrix()
#     glTranslatef(2.0, 0.0, 0.0)
#     glutWireSphere(1.0, 20, 20)
#     glPopMatrix()

#     glPushMatrix()
#     glTranslatef(-2.0, 0.0, 0.0)
#     glutWireTeapot(1.0)
#     glPopMatrix()

#     glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -20, 20)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Orbiting camera
    eye_x = 5.0 * math.cos(math.radians(theta))
    eye_z = 5.0 * math.sin(math.radians(theta))
    gluLookAt(eye_x, 0.0, eye_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glutWireCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0)
    glutWireSphere(1.0, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glutWireTeapot(1.0)
    glPopMatrix()

    glFlush()

    
def reshape(w, h):
    global width, height
    if h == 0:
        h = 1
    width = w
    height = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -20, 20)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global eye_z
    if key == b'q':
        sys.exit(0)
    elif key == b'e':
        eye_z += 0.5
    elif key == b'd':
        eye_z -= 0.5
    glutPostRedisplay()

def animate(value):
    global theta
    theta += 5
    if theta > 360:
        theta -= 360
    glutPostRedisplay()
    glutTimerFunc(50, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Visualization")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(50, animate, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()