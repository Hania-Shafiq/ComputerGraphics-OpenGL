from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

# Movement and rotation angles
base_x = 0.0
lower_arm_angle = 30
upper_arm_angle = -30


# ---------- BASIC SHAPES ----------
def draw_circle(r, filled=False):
    mode = GL_POLYGON if filled else GL_LINE_LOOP
    glBegin(mode)
    for i in range(100):
        theta = 2 * math.pi * i / 100
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()


def draw_rectangle(w, h, filled=False):
    mode = GL_POLYGON if filled else GL_LINE_LOOP
    glBegin(mode)
    glVertex2f(-w / 2, 0)
    glVertex2f(w / 2, 0)
    glVertex2f(w / 2, h)
    glVertex2f(-w / 2, h)
    glEnd()


def draw_half_circle(r):
    glBegin(GL_LINE_LOOP)
    for i in range(181):
        theta = math.radians(i)
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()


def draw_wheel():
    draw_circle(0.1)
    glBegin(GL_LINES)
    glVertex2f(-0.1, 0)
    glVertex2f(0.1, 0)
    glEnd()


# ---------- HIERARCHICAL CRANE ----------
def crane():
    global base_x, lower_arm_angle, upper_arm_angle

    # Move base forward/backward
    glPushMatrix()
    glTranslatef(base_x, 0, 0)

    # --- Base Rectangle (Car body) ---
    glColor3f(1, 0, 0)
    draw_rectangle(1.0, 0.2)

    # --- Wheels ---
    glPushMatrix()
    glTranslatef(-0.3, -0.1, 0)
    draw_wheel()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, -0.1, 0)
    draw_wheel()
    glPopMatrix()

    # --- Dome (half circle) ---
    glPushMatrix()
    glTranslatef(0, 0.2, 0)
    draw_half_circle(0.5)
    glPopMatrix()

    # --- Lower Arm ---
    glPushMatrix()
    glTranslatef(0, 0.2, 0)  # attach to top of dome
    glRotatef(lower_arm_angle, 0, 0, 1)
    draw_rectangle(0.15, 0.8)

    # --- Upper Arm ---
    glTranslatef(0, 0.8, 0)
    glPushMatrix()
    glRotatef(upper_arm_angle, 0, 0, 1)
    draw_rectangle(0.1, 0.6)

    # --- Hook ---
    glTranslatef(0, 0.6, 0)
    draw_circle(0.05)
    glPopMatrix()  # End upper arm

    glPopMatrix()  # End lower arm
    glPopMatrix()  # End base

    glFlush()


# ---------- DISPLAY ----------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    crane()
    glFlush()


# ---------- KEYBOARD CONTROLS ----------
def keyboard(key, x, y):
    global base_x, lower_arm_angle, upper_arm_angle
    key = key.decode('utf-8')

    # Move base left/right
    if key == 'a':
        base_x -= 0.1
    elif key == 'd':
        base_x += 0.1

    # Lower arm rotate
    elif key == 'w':
        lower_arm_angle += 5
    elif key == 's':
        lower_arm_angle -= 5

    # Upper arm rotate
    elif key == 'e':
        upper_arm_angle += 5
    elif key == 'q':
        upper_arm_angle -= 5

    glutPostRedisplay()


# ---------- INITIALIZATION ----------
def init():
    glClearColor(1, 1, 1, 1)
    glColor3f(1, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3, 3, -1, 3)  # left, right, bottom, top
    glMatrixMode(GL_MODELVIEW)


# ---------- MAIN ----------
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 600)
    glutCreateWindow(b"2D Hierarchical Crane - Move & Rotate Arms")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()

# 🔹 A / D → crane aagay (right) aur peechay (left) move kare,
# rotate na ho.
# 🔹 W / S → lower arm upar–neeche move kare
# 🔹 E / Q → upper arm upar–neeche move kare