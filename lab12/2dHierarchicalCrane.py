from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Rotation angles
base_angle = 0
lower_arm_angle = 30
upper_arm_angle = -20

def draw_rectangle(w, h):
    """Draw a rectangle centered at origin"""
    glBegin(GL_QUADS)
    glVertex2f(-w/2, 0)
    glVertex2f(w/2, 0)
    glVertex2f(w/2, h)
    glVertex2f(-w/2, h)
    glEnd()

def draw_circle(r=0.05):
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = math.radians(i)
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()

def crane():
    global base_angle, lower_arm_angle, upper_arm_angle

    # ---- Base ----
    glPushMatrix()
    glRotatef(base_angle, 0, 0, 1)
    glColor3f(0.3, 0.3, 0.3)
    draw_rectangle(0.8, 0.1)

    # ---- Lower Arm ----
    glTranslatef(0, 0.1, 0)
    glPushMatrix()
    glRotatef(lower_arm_angle, 0, 0, 1)
    glColor3f(0.7, 0, 0)
    draw_rectangle(0.2, 0.8)

    # ---- Upper Arm ----
    glTranslatef(0, 0.8, 0)
    glPushMatrix()
    glRotatef(upper_arm_angle, 0, 0, 1)
    glColor3f(0.9, 0.2, 0.2)
    draw_rectangle(0.15, 0.6)

    # ---- Hook ----
    glTranslatef(0, 0.6, 0)
    glColor3f(0, 0, 0)
    draw_circle(0.05)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    crane()
    glFlush()

def keyboard(key, x, y):
    global base_angle, lower_arm_angle, upper_arm_angle

    key = key.decode('utf-8')

    # Control base rotation
    if key == 'a':
        base_angle += 5
    elif key == 'd':
        base_angle -= 5

    # Control lower arm
    elif key == 'w':
        lower_arm_angle += 5
    elif key == 's':
        lower_arm_angle -= 5

    # Control upper arm
    elif key == 'e':
        upper_arm_angle += 5
    elif key == 'q':
        upper_arm_angle -= 5

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"2D Hierarchical Crane - Python OpenGL")
    glClearColor(1, 1, 1, 1)
    glColor3f(0, 0, 0)
    gluOrtho2D(-2, 2, -1, 3)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
