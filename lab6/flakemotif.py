from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window size
WIDTH, HEIGHT = 600, 600

# Snowflake world coordinates
Wleft, Wright = -80, 80
Wbottom, Wtop = -80, 80


# Flake motif (branch)
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

# Draw Snowflake (rotational symmetry)
def drawFlake():
    for i in range(6):   # 6 branches around 360°/6 = 60°
        # Draw original branch
        flakeMotif()
        # Draw mirrored branch
        glPushMatrix()
        glScalef(1.0, -1.0, 0)
        flakeMotif()
        glPopMatrix()
        # Rotate coordinate system for next branch
        glRotatef(60, 0, 0, 1)

# Display Function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0.6, 0, 1)   # Purple color
    glLineWidth(1)

    glPushMatrix()
    drawFlake()
    glPopMatrix()

    glFlush()

# Reshape Function
def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h

    # Calculate aspect ratios
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        # Window wider → adjust width
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        # Window taller → adjust height
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    # Projection matrix update
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(Wleft, Wright, Wbottom, Wtop)

    glViewport(int(Vleft), int(Vbottom), int(Vright - Vleft), int(Vtop - Vbottom))

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutPostRedisplay()

# Main
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Snowflake - Rotational Symmetry")

    glClearColor(1, 0.5, 0.5, 1)  # Light pink background

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
