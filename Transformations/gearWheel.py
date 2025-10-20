from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, time

# ----- Globals -----
angle = 0.0   # for rotation
speed = 0.03  # rotation speed

# ----- Draw a basic single gear tooth -----
def tooth0():
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.6, 0.2)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.2, 0.8)
    glVertex2f(0.0, 1.0)
    glEnd()


# ----- Transform basic tooth to correct position on circle -----
def tooth1(r):
    rad = 6.0 * math.pi/180
    sin6 = math.sin(rad)
    cos6 = math.cos(rad)

    glPushMatrix()
    # translate outward to the gear circle position
    glTranslatef(r * cos6, -r * sin6, 0.0)
    # scale down in both x and y
    glScalef(2.0 * r * sin6, 2.0 * r * sin6, 1.0)
    tooth0()
    glPopMatrix()


# ----- Draw full gear with 30 teeth -----
def gear(r):
    glPushMatrix()
    for i in range(30):
        tooth1(r)
        glRotatef(12.0, 0.0, 0.0, 1.0)  # rotate 360°/30 = 12° per tooth
    glPopMatrix()


# ----- Draw axes and circle (for visual reference) -----
def draw_axes():
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()

def draw_circle(r, n=100):
    glColor3f(0.5, 0.5, 1.0)
    glBegin(GL_LINE_LOOP)
    for i in range(n):
        theta = 2 * math.pi * i / n
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()


# ----- Display -----
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_axes()
    draw_circle(0.7)

    glPushMatrix()
    glRotatef(angle, 0.0, 0.0, 1.0)  # animate rotation
    gear(0.7)
    glPopMatrix()

    glutSwapBuffers()


# ----- Timer-based animation -----
def move():
    global angle
    angle += speed * 360.0 / 60.0  # small increment
    if angle > 360.0:
        angle -= 360.0
    glutPostRedisplay()
    glutTimerFunc(30, move, 0)


# ----- Reshape -----
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# ----- Main -----
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Gear Wheel - Transformations Lab")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(30, move, 0)
    glutMainLoop()


if __name__ == "__main__":
    main()