from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

year = 0.0
day = 0.0
moon_year = 0.0
moon_day = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0, 5, 5, 0, 0, 0, 0, 1, 0)  # Camera position

    # Sun
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glRotatef(day / 10, 0.0, 1.0, 0.0)  # Slow sun rotation
    glutWireSphere(0.5, 20, 16)
    glPopMatrix()

    # Planet orbit and rotation
    glPushMatrix()
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(2.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(day, 0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glutWireSphere(0.2, 10, 8)
    glPopMatrix()

    # Moon
    glRotatef(moon_year, 0.0, 1.0, 0.0)
    glTranslatef(0.5, 0.0, 0.0)
    glRotatef(moon_day, 0.0, 1.0, 0.0)
    glColor3f(0.5, 0.5, 0.5)  # Gray
    glutWireSphere(0.1, 10, 8)
    glPopMatrix()

    glutSwapBuffers()

def animate(value):
    global year, day, moon_year, moon_day
    year = (year + 0.5) % 360
    day = (day + 2.0) % 360
    moon_year = (moon_year + 4.0) % 360
    moon_day = (moon_day + 8.0) % 360
    glutPostRedisplay()
    glutTimerFunc(20, animate, 0)

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Solar System Hierarchical Model")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutTimerFunc(20, animate, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()