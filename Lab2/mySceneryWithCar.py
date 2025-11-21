from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

# ---------------- Global Variables ----------------
car_pos = 0.0
wheel_angle = 0.0
animation_running = False

# ---------------- Utilities for Room ----------------
def draw_rect(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_parallelogram_custom(x1, y1, x2, y2, x3, y3, x4, y4, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_trapezoid(x1, y1, x2, y2, x3, y3, x4, y4, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

# ---------------- Utilities for Car ----------------
def draw_filled_circle(cx, cy, r, segments):
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2*math.pi*i/segments
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_filled_arc(cx, cy, r, start_angle, end_angle, segments):
    glBegin(GL_POLYGON)
    for i in range(segments+1):
        angle = math.radians(start_angle + (end_angle-start_angle)*i/segments)
        x = cx + r*math.cos(angle)
        y = cy + r*math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_wheel():
    glColor3f(0,0,0)
    draw_filled_circle(0,0,0.15,30)
    glColor3f(1,1,1)
    small_r = 0.03
    dist = 0.08
    for i in range(4):
        theta = i*2*math.pi/4
        sx = dist*math.cos(theta)
        sy = dist*math.sin(theta)
        draw_filled_circle(sx, sy, small_r, 20)

def draw_car():
    # Body
    glPushMatrix()
    glTranslatef(car_pos, -7.0, 0)  # move car below room scene

    # Left yellow semicircle
    glPushMatrix()
    glTranslatef(-0.25,0,0)
    glColor3f(1,1,0)
    draw_filled_arc(0,0,0.25,0,180,20)
    glPopMatrix()

    # Right yellow semicircle
    glPushMatrix()
    glTranslatef(0.25,0,0)
    glColor3f(1,1,0)
    draw_filled_arc(0,0,0.25,0,180,20)
    glPopMatrix()

    # Blue rectangle body
    glPushMatrix()
    glTranslatef(0,0.125,0)
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-0.25,-0.125)
    glVertex2f(0.25,-0.125)
    glVertex2f(0.25,0.125)
    glVertex2f(-0.25,0.125)
    glEnd()
    glPopMatrix()

    # Red dome
    glPushMatrix()
    glTranslatef(0,0.25,0)
    glColor3f(1,0,0)
    draw_filled_arc(0,0,0.25,0,180,20)
    glPopMatrix()

    # Wheels
    glPushMatrix()
    glTranslatef(-0.2,-0.1,0)
    glRotatef(wheel_angle,0,0,1)
    draw_wheel()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.2,-0.1,0)
    glRotatef(wheel_angle,0,0,1)
    draw_wheel()
    glPopMatrix()

    glPopMatrix()

# ---------------- Scene ----------------
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)

    brown = (0.6, 0.4, 0.3)
    # Window
    draw_rect(-4,4,-0.4,8,(0.4,0.7,1))
    draw_rect(-0.4,4,0.4,8,brown)
    draw_rect(0.4,4,4,8,(0.4,0.7,1))
    # Chair
    draw_rect(-8,-2,-6,0.8,brown)
    draw_parallelogram_custom(-7,-3,-5,-3,-6,-2,-8,-2,brown)
    draw_rect(-8,-4,-7.8,-2,brown)
    draw_rect(-6.2,-4.4,-6,-2,brown)
    draw_rect(-7,-5.4,-6.8,-3,brown)
    draw_rect(-5.2,-5.4,-5,-3,brown)
    # Table
    draw_parallelogram_custom(-2.6,-1.2,3.8,-1.2,2.4,1.6,-4,1.6,brown)
    draw_rect(-4,-4,-3.6,1.6,brown)
    draw_rect(2,-4,2.4,1.6,brown)
    draw_rect(-2.6,-6.8,-2.2,-1.2,brown)
    draw_rect(3.4,-6.8,3.8,-1.2,brown)
    draw_rect(-2.6,-2,3.8,-1.2,brown)
    draw_parallelogram_custom(-2.6,-2,-2.2,-1.2,-4,1.6,-4,-0.2,brown)
    # Laptop
    draw_parallelogram_custom(-2.2,-0.6,0.4,-0.6,-0.4,0.8,-3,0.8,(0.1,0.1,0.1))
    draw_rect(-3,0.8,-0.4,3,(0.1,0.1,0.1))
    # Glass / Cup
    draw_trapezoid(1.2,0.2,1.6,0.2,1.8,1,1,1,(0.4,0.7,1))
    # Lamp
    draw_rect(5,-6,7,-5,brown)
    draw_rect(5.6,-5,6.4,0.8,brown)
    draw_trapezoid(4,0.8,8,0.8,7.2,3.4,4.8,3.4,(1,1,0.4))

    # Draw car below scene
    draw_car()

    glFlush()

# ---------------- Animation ----------------
def animate(value):
    global car_pos, wheel_angle, animation_running
    if not animation_running:
        return
    car_pos += 0.02
    if car_pos > 8:  # reset if off-screen
        car_pos = -8
    wheel_angle += 5
    glutPostRedisplay()
    glutTimerFunc(50, animate, 0)

def menu_control(value):
    global car_pos, wheel_angle, animation_running
    if value == 1:
        if not animation_running:
            animation_running = True
            glutTimerFunc(50, animate, 0)
    elif value == 2:
        car_pos = 0.0
        wheel_angle = 0.0
        animation_running = True
        glutTimerFunc(50, animate, 0)
    elif value == 3:
        sys.exit(0)
    elif value == 4:
        animation_running = False
    glutPostRedisplay()

# ---------------- Reshape ----------------
def reshape(width, height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10,10,-10,10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ---------------- Init ----------------
def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10,10,-10,10)
    glMatrixMode(GL_MODELVIEW)

# ---------------- Main ----------------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(800,800)
    glutCreateWindow(b"2D Room Scene with Car Animation")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutCreateMenu(menu_control)
    glutAddMenuEntry("Start",1)
    glutAddMenuEntry("Restart",2)
    glutAddMenuEntry("Exit",3)
    glutAddMenuEntry("Stop",4)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutMainLoop()

if __name__ == "__main__":
    main()
