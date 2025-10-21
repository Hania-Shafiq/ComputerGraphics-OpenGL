from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# ---- Joint angles ----
body_angle = 0
left_leg_angle = 20
right_leg_angle = -20
left_arm_angle = -30
right_arm_angle = 30

# ---- Skeleton position ----
x_pos = 0.0

def draw_joint(x, y):
    """Draws a red joint (circle)"""
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    for i in range(30):
        theta = 2 * math.pi * i / 30
        glVertex2f(x + 0.05 * math.cos(theta), y + 0.05 * math.sin(theta))
    glEnd()

def draw_bone(x1, y1, x2, y2):
    """Draws a line (bone)"""
    glColor3f(0, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_skeleton():
    global body_angle, left_leg_angle, right_leg_angle, left_arm_angle, right_arm_angle, x_pos

    glPushMatrix()
    glTranslatef(x_pos, 0, 0)
    glRotatef(body_angle, 0, 0, 1)

    # ---- Hip Joint ----
    draw_joint(0, 0)

    # ---- Spine to Neck ----
    draw_bone(0, 0, 0, 0.8)
    draw_joint(0, 0.8)  # Neck Joint

    # ---- Head ----
    glPushMatrix()
    glTranslatef(0, 0.8, 0)
    glBegin(GL_LINE_LOOP)
    for i in range(40):
        theta = 2 * math.pi * i / 40
        glVertex2f(0.0 + 0.3 * math.cos(theta), 0.5 + 0.3 * math.sin(theta))
    glEnd()
    glPopMatrix()

    # ---- Left Arm (Shoulder to Elbow to Hand) ----
    glPushMatrix()
    glTranslatef(0, 0.8, 0)  # Start at neck
    glRotatef(left_arm_angle, 0, 0, 1)
    draw_bone(0, 0, -0.5, 0)  # Upper arm (shoulder to elbow)
    draw_joint(-0.5, 0)  # Elbow Joint
    glTranslatef(-0.5, 0, 0)
    glRotatef(left_arm_angle / 2, 0, 0, 1)  # Adjust lower arm angle
    draw_bone(0, 0, -0.5, 0)  # Lower arm (elbow to hand)
    draw_joint(-0.5, 0)  # Hand Joint
    glPopMatrix()

    # ---- Right Arm (Shoulder to Elbow to Hand) ----
    glPushMatrix()
    glTranslatef(0, 0.8, 0)  # Start at neck
    glRotatef(right_arm_angle, 0, 0, 1)
    draw_bone(0, 0, 0.5, 0)  # Upper arm (shoulder to elbow)
    draw_joint(0.5, 0)  # Elbow Joint
    glTranslatef(0.5, 0, 0)
    glRotatef(right_arm_angle / 2, 0, 0, 1)  # Adjust lower arm angle
    draw_bone(0, 0, 0.5, 0)  # Lower arm (elbow to hand)
    draw_joint(0.5, 0)  # Hand Joint
    glPopMatrix()

    # ---- Left Leg (Hip to Knee to Foot) ----
    glPushMatrix()
    glRotatef(left_leg_angle, 0, 0, 1)
    draw_bone(0, 0, 0, -0.8)  # Upper leg angled from hip
    draw_joint(0, -0.8)  # Knee Joint
    glTranslatef(0, -0.8, 0)
    glRotatef(-left_leg_angle / 2, 0, 0, 1)
    draw_bone(0, 0, 0, -0.7)  # Lower leg (knee to foot)
    draw_joint(0, -0.7)  # Foot Joint
    glPopMatrix()

    # ---- Right Leg (Hip to Knee to Foot) ----
    glPushMatrix()
    glRotatef(right_leg_angle, 0, 0, 1)
    draw_bone(0, 0, 0, -0.8)  # Upper leg angled from hip
    draw_joint(0, -0.8)  # Knee Joint
    glTranslatef(0, -0.8, 0)
    glRotatef(-right_leg_angle / 2, 0, 0, 1)
    draw_bone(0, 0, 0, -0.7)  # Lower leg (knee to foot)
    draw_joint(0, -0.7)  # Foot Joint
    glPopMatrix()

    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.5, 0)
    draw_skeleton()
    glFlush()

def keyboard(key, x, y):
    global body_angle, left_leg_angle, right_leg_angle
    global left_arm_angle, right_arm_angle, x_pos

    key = key.decode("utf-8")

    if key == 'w': body_angle += 5
    elif key == 's': body_angle -= 5
    elif key == 'j': left_leg_angle += 5
    elif key == 'k': left_leg_angle -= 5
    elif key == 'n': right_leg_angle += 5
    elif key == 'm': right_leg_angle -= 5
    elif key == 'u': left_arm_angle += 5
    elif key == 'i': left_arm_angle -= 5
    elif key == 'o': right_arm_angle += 5
    elif key == 'p': right_arm_angle -= 5
    elif key == 'a': x_pos -= 0.1
    elif key == 'd': x_pos += 0.1
    elif key == 'r':  # reset
        body_angle = left_leg_angle = right_leg_angle = left_arm_angle = right_arm_angle = 0
        x_pos = 0

    glutPostRedisplay()

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3, 3, -2, 3)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"2D Hierarchical Skeleton System - Keyboard Controlled")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()