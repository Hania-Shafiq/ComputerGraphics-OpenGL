from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window size
width, height = 600, 600

# ------------------------------
# Flake motif (branch)
# ------------------------------
def flakeMotif():
    glBegin(GL_LINE_STRIP)
    glVertex2f(0, 5)
    glVertex2f(20, 5)
    glVertex2f(30, 25)
    glVertex2f(35,18)
    glVertex2f(25,5)
    glVertex2f(30,5)
    glVertex2f(45,15)
    glVertex2f(50,13)
    glVertex2f(35,5)
    glVertex2f(55,5)
    glVertex2f(60, 0)
    glEnd()

# ------------------------------
# Draw Snowflake (rotational symmetry)
# ------------------------------
def drawFlake():
    for i in range(6):   # 6 branches around 360°
        # draw branch
        flakeMotif()

        # draw mirrored branch
        glPushMatrix()
        glScalef(1.0, -1.0, 0)
        flakeMotif()
        glPopMatrix()

        # rotate for next branch
        glRotatef(60, 0, 0, 1)

# ------------------------------
# Display Function
# ------------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0, 0, 0)   # black like in lab sheet
    glLineWidth(2)

    glPushMatrix()
    drawFlake()
    glPopMatrix()

    glFlush()

# ------------------------------
# Main
# ------------------------------
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Snowflake - Rotational Symmetry")

    # White background
    glClearColor(1, 1, 1, 1)

    # Setup projection (cover enough space for motif up to x=60)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-80, 80, -80, 80)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
