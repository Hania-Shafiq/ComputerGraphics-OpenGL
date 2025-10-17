from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random

# Global animation variables
blade_angle = 0.0
plane_x = 245.0
plane_y = 230.0
plane_crashed = False

# Particle system (no sin/cos)
class Particle:
    def __init__(self):
        self.x, self.y = 0.0, 0.0
        # random velocity in both directions (no trig)
        self.vx = random.uniform(-3.0, 3.0)
        self.vy = random.uniform(-3.0, 3.0)
        self.life = random.uniform(30.0, 60.0)  # frames
        # start as yellow-ish
        self.color = [1.0, random.uniform(0.5, .0), 0.0]

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1.0
        # fade color from yellow → red → grey-ish
        self.color[1] = max(0.0, self.color[1] - 0.02)
        self.color[2] = min(0.5, self.color[1] + 0.1)


particles = []

def triggerExplosion(x, y, count=200):
    """Initialize particles centered at (x, y)."""
    global particles
    particles = [Particle() for _ in range(count)]
    for p in particles:
        p.x, p.y = x, y

def drawExplosion():
    """Draw and update particles. Particles fade out and move without trig."""
    global particles
    if not particles:
        return

    glPointSize(4)
    glBegin(GL_POINTS)
    for p in particles:
        if p.life > 0:
            alpha = max(0.0, min(1.0, p.life / 60.0))
            glColor4f(p.color[0], p.color[1], p.color[2], alpha)
            glVertex2f(p.x, p.y)
            p.update()
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawlandscape()
    drawplane()
    drawwindmill()
    # draw explosion on top (if any)
    if plane_crashed:
        drawExplosion()
    glutSwapBuffers()


def drawWind():
    """Draw a single windmill blade (triangle) with pivot at origin."""
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.8, 0.8)
    glVertex2f(0.0, 0.0)      # pivot
    glVertex2f(20.0, 40.0)    # top
    glVertex2f(40.0, 20.0)    # side
    glEnd()


def drawwindmill():
    """Draw windmill tower and rotating blades using transforms only."""
    global blade_angle

    # Tower (static)
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.0)
    glVertex2f(145.0, 50.0)
    glVertex2f(135.0, 100.0)
    glVertex2f(115.0, 100.0)
    glVertex2f(105.0, 50.0)
    glEnd()

    # Blades — position pivot, rotate, draw 4 blades
    glPushMatrix()
    glTranslatef(125.0, 100.0, 0.0)   # pivot to center of blades
    glRotatef(blade_angle, 0, 0, 1)   # rotate blades (no trig)

    for i in range(4):
        glPushMatrix()
        glRotatef(i * 90.0, 0, 0, 1)  # place each blade 90° apart
        drawWind()
        glPopMatrix()

    glPopMatrix()


def drawplane():
    """Draw and animate a plane moving diagonally. Use translate only."""
    global plane_x, plane_y, plane_crashed

    if not plane_crashed:
        glPushMatrix()
        # Use translation to move the plane. We shift so the drawn vertices stay consistent.
        glTranslatef(plane_x - 215.0, plane_y - 230.0, 0.0)

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
        # After crash, optionally draw a small wreck or leave explosion to show
        # (we can still draw a darker small rectangle as a wreck marker)
        # glColor3f(0.2, 0.0, 0.0)
        # glBegin(GL_QUADS)
        # glVertex2f(plane_x - 10.0, 45.0)
        # glVertex2f(plane_x + 10.0, 45.0)
        # glVertex2f(plane_x + 10.0, 55.0)
        # glVertex2f(plane_x - 10.0, 55.0)
        # glEnd()


def Timer(value):
    global blade_angle, plane_x, plane_y, plane_crashed

    # Windmill animation (rotate only)
    blade_angle += 2.0
    if blade_angle >= 360.0:
        blade_angle -= 360.0

    # Plane diagonal motion (translate only)
    if not plane_crashed:
        plane_y -= 1.0    # move down
        plane_x -= 0.5    # move left
        if plane_y <= 50.0:
            plane_crashed = True
            # trigger explosion at plane's current position (use ground y)
            triggerExplosion(plane_x, 50.0, count=200)

    glutPostRedisplay()
    glutTimerFunc(30, Timer, 1)


def drawlandscape():
    # Grass
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

    # optional nice point rendering
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)


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
