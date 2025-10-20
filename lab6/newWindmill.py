from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# ---------------- Global Variables ----------------
angle = 0.0          # Windmill rotation
plane_x = 225.0      # Plane X position
plane_y = 260.0      # Plane Y position
crashed = False       # To check if plane hit the ground
break_offset = 0.0    # Separation distance after crash

# ---------------- Draw Single Blade ----------------
def drawBlade():
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.8, 0.8)
    glVertex2f(0.0, 0.0)
    glVertex2f(20.0, 40.0)
    glVertex2f(40.0, 20.0)
    glEnd()

# ---------------- Windmill ----------------
def drawWindmill():
    global angle
    # --- Stand ---
    glColor3f(0.6, 0.5, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(145.0, 50.0)
    glVertex2f(135.0, 100.0)
    glVertex2f(115.0, 100.0)
    glVertex2f(105.0, 50.0)
    glEnd()

    # --- Blades ---
    glPushMatrix()
    glTranslatef(125.0, 100.0, 0.0)
    glRotatef(angle, 0, 0, 1)

    for i in range(4):
        glRotatef(i * 90, 0, 0, 1)
        drawBlade()

    glPopMatrix()

# ---------------- Plane ----------------
def drawPlane():
    global plane_x, plane_y, crashed, break_offset

    glPushMatrix()
    glTranslatef(plane_x, plane_y, 0.0)

    if not crashed:
        # --- Normal Plane ---
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(-30.0, 5.0)

        glColor3f(0.2, 0.2, 0.2)
        glVertex2f(-2.0, -2.0)
        glVertex2f(-2.0, 7.0)
        glVertex2f(-15.0, 7.0)
        glEnd()
    else:
        # --- Broken Plane ---
        # Front (nose) moves right
        glPushMatrix()
        glTranslatef(break_offset, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(-15.0, 5.0)
        glEnd()
        glPopMatrix()

        # Back (tail) moves left
        glPushMatrix()
        glTranslatef(-break_offset, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.2, 0.2, 0.2)
        glVertex2f(-15.0, 5.0)
        glVertex2f(-30.0, 7.0)
        glVertex2f(-30.0, 3.0)
        glEnd()
        glPopMatrix()

    glPopMatrix()

# ---------------- Landscape ----------------
def drawLandscape():
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(250.0, 0.0)
    glColor3f(0.0, 0.9, 0.0)
    glVertex2f(250.0, 50.0)
    glColor3f(0.0, 0.8, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 0.7, 0.0)
    glVertex2f(0.0, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.6)
    glVertex2f(250.0, 50.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(200.0, 150.0)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(150.0, 50.0)

    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(200.0, 50.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(150.0, 150.0)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(100.0, 50.0)

    glColor3f(0.0, 0.0, 0.7)
    glVertex2f(150.0, 50.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(100.0, 150.0)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(50.0, 50.0)

    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(100.0, 50.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(50.0, 150.0)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(0.0, 50.0)
    glEnd()

# ---------------- Display ----------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawLandscape()
    drawWindmill()
    drawPlane()
    glutSwapBuffers()

# ---------------- Timer ----------------
def Timer(value):
    global angle, plane_y, crashed, break_offset

    # Rotate windmill
    angle += 5
    if angle >= 360:
        angle = 0

    # Drop plane
    if not crashed:
        if plane_y > 50:
            plane_y -= 1.0
        else:
            crashed = True
    else:
        # Increase split distance until fixed gap
        if break_offset < 5.0:
            break_offset += 0.3

    glutTimerFunc(30, Timer, 1)
    glutPostRedisplay()

# ---------------- Reshape ----------------
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 250.0, 0.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ---------------- Init ----------------
def init():
    glClearColor(0.3, 0.4, 0.7, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 250.0, 0.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ---------------- Main ----------------
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Lab #8 - Windmill and Plane Crash (Miss Demo Style)")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(30, Timer, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()
