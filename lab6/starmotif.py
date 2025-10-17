from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# ----------------------------
# Draw a single star arm
# ----------------------------
def starMotif():
    glBegin(GL_LINE_STRIP)
    glVertex2f(3, 3)
    glVertex2f(0,8)
    glVertex2f(-3,0)
    glVertex2f(-2,-1)
    glVertex2f(0,5)
    glVertex2f(2,3)
    glVertex2f(3,3)
    glEnd()

# ----------------------------
# Draw full star with rotation
# ----------------------------
def drawStar():
    for i in range(5):      # 5-fold symmetry
        starMotif()
        glRotatef(72, 0, 0, 1)  # rotate around Z axis

# ----------------------------
# Display function
# ----------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0, 0, 0)   # black star
    glLineWidth(2)

    glPushMatrix()
    drawStar()
    glPopMatrix()

    glFlush()

# ----------------------------
# Main
# ----------------------------
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Star Motif - Rotational Symmetry")

    # Background white
    glClearColor(1, 1, 1, 1)

    # Setup projection (make sure star fits)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-20, 20, -20, 20)  # enough space

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
