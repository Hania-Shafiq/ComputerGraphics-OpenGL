from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#<<<<<<<<<<<<<<<<<<< axis >>>>>>>>>>>>>>
def axis(length):
    """Draws an axis along the Z-axis with a cone at the end"""
    glPushMatrix()
    glBegin(GL_LINES)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, length)
    glEnd()
    glTranslated(0, 0, length - 0.2)
    glutWireCone(0.04, 0.2, 12, 9)
    glPopMatrix()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<< displayWire >>>>>>>>>>>>>>>>>>>>>>
def displayWire():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0 * 64 / 48.0, 2.0 * 64 / 48.0, -2.0, 2.0, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.0, 2.0, 2.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0, 0, 0)  # black lines

    # Axes
    axis(0.5)  # z-axis

    glPushMatrix()
    glRotated(90, 0, 1.0, 0)
    axis(0.5)  # y-axis
    glRotated(-90.0, 1, 0, 0)
    axis(0.5)  # x-axis
    glPopMatrix()

    # Wire cube
    glPushMatrix()
    glTranslated(0.5, 0.5, 0.5)
    glutWireCube(1.0)
    glPopMatrix()

    # Wire sphere
    glPushMatrix()
    glTranslated(1.0, 1.0, 0.0)
    glutWireSphere(0.25, 10, 8)
    glPopMatrix()

    # Wire cone
    glPushMatrix()
    glTranslated(1.0, 0.0, 1.0)
    glutWireCone(0.2, 0.5, 10, 8)
    glPopMatrix()

    # Wire teapot
    glPushMatrix()
    glTranslated(1.0, 1.0, 1.0)
    glutWireTeapot(0.2)
    glPopMatrix()

    # Wire torus
    glPushMatrix()
    glTranslated(0.0, 1.0, 0.0)
    glRotated(90.0, 1, 0, 0)
    glutWireTorus(0.1, 0.3, 10, 10)
    glPopMatrix()

    # Wire dodecahedron
    glPushMatrix()
    glTranslated(1.0, 0.0, 0.0)
    glScaled(0.15, 0.15, 0.15)
    glutWireDodecahedron()
    glPopMatrix()

    # Small cube
    glPushMatrix()
    glTranslated(0.0, 1.0, 1.0)
    glutWireCube(0.25)
    glPopMatrix()

    # Cylinder
    glPushMatrix()
    glTranslated(0.0, 0.0, 1.0)
    qobj = gluNewQuadric()
    gluQuadricDrawStyle(qobj, GLU_LINE)
    gluCylinder(qobj, 0.2, 0.2, 0.4, 8, 8)
    glPopMatrix()

    glFlush()

#<<<<<<<<<<<<<<<<<<<<<< main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Transformation testbed - wireframes")
    glutDisplayFunc(displayWire)
    glClearColor(1.0, 1.0, 1.0, 0.0)  # white background
    glViewport(0, 0, 640, 480)
    glutMainLoop()

if __name__ == "__main__":
    main()
