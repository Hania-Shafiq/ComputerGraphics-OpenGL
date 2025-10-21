from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

car_pos = 0.0  # Centered at origin
wheel_angle = 0.0
animation_running = False

def draw_filled_circle(cx, cy, r, segments):
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2*math.pi* i / segments
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_filled_arc(cx, cy, r, start_angle, end_angle, segments):
    glBegin(GL_POLYGON)
    for i in range(segments + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_wheel():
    # Black wheel base
    glColor3f(0.0, 0.0, 0.0)
    draw_filled_circle(0.0, 0.0, 0.15, 30)

    # Small white circles around the center
    glColor3f(1.0, 1.0, 1.0)
    small_r = 0.03
    dist = 0.08
    for i in range(4):
        theta = i * 2.0 * math.pi / 4.0
        sx = dist * math.cos(theta)
        sy = dist * math.sin(theta)
        draw_filled_circle(sx, sy, small_r, 20)

def draw_car():
    # Left yellow vertical semicircle (same height as rectangle, 0.25)
    glPushMatrix()
    glTranslatef(-0.25, 0.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    draw_filled_arc(0.0, 0, 0.25, 0, 180, 20)
    glPopMatrix()

    # Right yellow vertical semicircle (same height as rectangle, 0.25)
    glPushMatrix()
    glTranslatef(0.25, 0.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    draw_filled_arc(0.0, 0, 0.25, 0, 180, 20)
    glPopMatrix()

  # Blue quad layer (forward and back per yellow arcs)
    glPushMatrix()
    glTranslatef(0.0, 0.125, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.25, -0.125)
    glVertex2f(0.25, -0.125)
    glVertex2f(0.25, 0.125)
    glVertex2f(-0.25, 0.125)
    glEnd()
    glPopMatrix()

    # Red dome semicircle
    glPushMatrix()
    glTranslatef(0.0, 0.25, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    draw_filled_arc(0.0, 0.0, 0.25, 0, 180, 20)
    glPopMatrix()

    # Left wheel
    glPushMatrix()
    glTranslatef(-0.2, -0.1, 0.0)
    glRotatef(wheel_angle, 0.0, 0.0, 1.0)
    draw_wheel()
    glPopMatrix()

    # Right wheel
    glPushMatrix()
    glTranslatef(0.2, -0.1, 0.0)
    glRotatef(wheel_angle, 0.0, 0.0, 1.0)
    draw_wheel()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(car_pos, 0.0, 0.0)
    draw_car()
    glFlush()

def animate(value):
    global car_pos, wheel_angle, animation_running
    if not animation_running:
        return

    car_pos += 0.02
    if car_pos > 1.5:
        car_pos = -1.5

    wheel_angle += 5.0

    glutPostRedisplay()
    glutTimerFunc(50, animate, 0)

def menu_control(value):
    global car_pos, wheel_angle, animation_running
    if value == 1:  # Start
        if not animation_running:
            animation_running = True
            glutTimerFunc(50, animate, 0)
    elif value == 2:  # Restart
        car_pos = 0.0
        wheel_angle = 0.0
        animation_running = True
        glutTimerFunc(50, animate, 0)
    elif value == 3:  # Exit
        sys.exit(0)
        quit()
    elif value == 4:  # Stop
        animation_running = False
    glutPostRedisplay()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.5, 1.5, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Hierarchical Car Model")
    init()
    glutDisplayFunc(display)
    glutCreateMenu(menu_control)
    glutAddMenuEntry("Start", 1)
    glutAddMenuEntry("Restart", 2)
    glutAddMenuEntry("Exit", 3)
    glutAddMenuEntry("Stop", 4)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutMainLoop()

if __name__ == "__main__":
    main()


# Hierarchical Structure

# Car (root)

# Body (rectangle + dome + arcs)

# Left Wheel (child → rotate on its axis)

# Right Wheel (child → rotate on its axis)

# Important:

# Wheels rotate relative to car position

# Car moves on X-axis, wheels spin — hierarchical animation