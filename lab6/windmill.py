from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import time
import random
from math import radians, sin, cos

windmill_count = 1
last_creation_time = time.time()
plane_y = 230
plane_crashed = False

# blade rotation
blade_count = 4
blade_angle = 0.0

# explosion
explosion_radius = 0.9
explosion_grow = True


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawlandscape()
    drawplane()
    drawwindmill()
    glutSwapBuffers()


def drawWind():
    """One blade drawn relative to pivot (0,0)"""
    glPushMatrix()
    glScalef(1.0, 1.5, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.8, 0.8)
    glVertex2f(0.0, 0.0)
    glVertex2f(15.0, 30.0)
    glVertex2f(35.0, 30.0)
    glEnd()
    glPopMatrix()


def drawwindmill():
    """Draw windmill body and blades with timed transitions"""
    global blade_count, blade_angle

    # Tower
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.0)
    glVertex2f(145.0, 50.0)
    glVertex2f(135.0, 100.0)
    glVertex2f(115.0, 100.0)
    glVertex2f(105.0, 50.0)
    glEnd()

    # Blades
    glPushMatrix()
    glTranslatef(125.0, 100.0, 0.0)
    glRotatef(blade_angle, 0, 0, 1)

    for i in range(blade_count):
        glPushMatrix()
        glRotatef(i * 90, 0, 0, 1)
        drawWind()
        glPopMatrix()

    glPopMatrix()



def cos_deg(angle): return cos(radians(angle))
def sin_deg(angle): return sin(radians(angle))
# Particle class
class Particle:
    def __init__(self):
        angle = random.uniform(0, 360)
        speed = random.uniform(1, 5)
        self.x, self.y = 0, 0
        self.vx = cos(radians(angle)) * speed
        self.vy = sin(radians(angle)) * speed
        self.life = random.uniform(30, 60)  # frames
        self.color = [1.0, random.uniform(0.5, 1.0), 0.0]  # yellow/orange

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        # fade color from yellow→red→grey
        self.color[1] = max(0.0, self.color[1] - 0.02)  
        self.color[2] = min(0.5, self.color[1] + 0.1)  

# Global particle list
particles = []

def triggerExplosion(x, y):
    global particles
    particles = [Particle() for _ in range(200)]  # 200 sparks
    for p in particles:
        p.x, p.y = x, y
def drawExplosion(x, y):
    global particles
    glPointSize(4)
    glBegin(GL_POINTS)
    for p in particles:
        if p.life > 0:
            glColor4f(p.color[0], p.color[1], p.color[2], p.life / 60.0)
            glVertex2f(p.x, p.y)
            p.update()
    glEnd()

 # adding positions for plane to move diagonally
plane_x = 0     
plane_y = 230
plane_crashed = False
def drawplane():
    global plane_x, plane_y, plane_crashed

    if not plane_crashed:
        glPushMatrix()
        # move diagonally (x + y)
        glTranslatef(plane_x, plane_y - 230.0, 0.0)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(245.0, 230.0)
        glVertex2f(245.0, 240.0)
        glVertex2f(215.0, 230.0)

        glColor3f(0.2, 0.2, 0.2)
        glVertex2f(244.0, 228.0)
        glVertex2f(244.0, 235.0)
        glVertex2f(228.0, 235.0)
        glEnd()

        glPopMatrix()
    else:
        drawExplosion(230, 50)

def Timer(value):
    global blade_angle, plane_y, plane_x, plane_crashed

    # Windmill rotation
    blade_angle += 2
    if blade_angle > 360:
        blade_angle -= 360

    # Plane diagonal crash
    if not plane_crashed:
        plane_y -= 1       # going down
        plane_x -= 0.2     # going left (negative → left, positive → right)

        if plane_y <= 50:   # ground reached
            plane_crashed = True
            triggerExplosion(180, 50)

    glutPostRedisplay()
    glutTimerFunc(30, Timer, value + 1)


def drawlandscape():
    # Draw a box of grass
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

    # Mountains
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

def init():
    glClearColor(0.8, 0.8, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 250.0, 0.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 250.0, 0.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    if key == b'\x1b':
        sys.exit(0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"BSCS 514 Lab #8 - Python Version")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(30, Timer, 1)
    glutMainLoop()


if __name__ == "__main__":
    main()



