from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Global window and world coordinates
WIDTH, HEIGHT = 600, 600
Wleft, Wright = -20, 20
Wbottom, Wtop = -20, 20

# Draw a single star arm
def starMotif():
    glBegin(GL_LINE_STRIP)
    glVertex2f(3, 3)
    glVertex2f(0, 8)
    glVertex2f(-3, 0)
    glVertex2f(-2, -1)
    glVertex2f(0, 5)
    glVertex2f(2, 3)
    glVertex2f(3, 3)
    glEnd()

# Draw full star with rotation
def drawStar():
    for i in range(5):      # 5-fold symmetry
        starMotif()
        glRotatef(72, 0, 0, 1)  # rotate around Z axis

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0.6, 0, 1)  
    glLineWidth(2)

    glPushMatrix()        # optional: for future transformations
    drawStar()
    glPopMatrix()

    glFlush()

# Reshape function
def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h

    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        new_width = (h - 2*margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        new_height = (w - 2*margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    # Projection update
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(Wleft, Wright, Wbottom, Wtop)

    # Set viewport
    glViewport(int(Vleft), int(Vbottom), int(Vright - Vleft), int(Vtop - Vbottom))

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutPostRedisplay()

# Main
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Star Motif - Rotational Symmetry")

    glClearColor(1, 0, 1, 1)

    # Initial projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(Wleft, Wright, Wbottom, Wtop)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
