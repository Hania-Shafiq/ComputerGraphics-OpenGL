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

# World coordinates
Wleft, Wright = 0.0, 250.0
Wbottom, Wtop = 0.0, 250.0

# Particle system (no sin/cos)
class Particle:
    def __init__(self):
        self.x, self.y = 0.0, 0.0
        self.vx = random.uniform(-2.0, 2.0)
        self.vy = random.uniform(1.0, 3.0)
        self.life = random.uniform(30.0, 60.0)
        self.color = [1.0, random.uniform(0.5, 1.0), 0.0]

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1.0
        self.color[1] = max(0.0, self.color[1] - 0.02)
        self.color[2] = min(0.5, self.color[2] + 0.01)

particles = []

def triggerExplosion(x, y, count=150):
    global particles
    particles = [Particle() for _ in range(count)]
    for p in particles:
        p.x, p.y = x, y

def drawExplosion():
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
    if plane_crashed:
        drawExplosion()
    glutSwapBuffers()

def drawWind():
    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.8, 0.8)
    glVertex2f(0.0, 0.0)
    glVertex2f(20.0, 40.0)
    glVertex2f(40.0, 20.0)
    glEnd()

def drawwindmill():
    global blade_angle
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.0)
    glVertex2f(145.0, 50.0)
    glVertex2f(135.0, 100.0)
    glVertex2f(115.0, 100.0)
    glVertex2f(105.0, 50.0)
    glEnd()

    glPushMatrix()
    glTranslatef(125.0, 100.0, 0.0)
    glRotatef(blade_angle, 0, 0, 1)

    for i in range(4):
        glPushMatrix()
        glRotatef(i * 90.0, 0, 0, 1)
        drawWind()
        glPopMatrix()

    glPopMatrix()

def drawplane():
    global plane_x, plane_y, plane_crashed

    if not plane_crashed:
        glPushMatrix()
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

def Timer(value):
    global blade_angle, plane_x, plane_y, plane_crashed
    blade_angle += 2.0
    if blade_angle >= 360.0:
        blade_angle -= 360.0

    if not plane_crashed:
        plane_y -= 1.0
        plane_x -= 0.5
        if plane_y <= 50.0:
            plane_crashed = True
            triggerExplosion(plane_x, 50.0, count=150)

    glutPostRedisplay()
    glutTimerFunc(30, Timer, 1)

def drawlandscape():
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

def init():
    glClearColor(0.8, 0.8, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(Wleft, Wright, Wbottom, Wtop)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)

def reshape(w, h):
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 20

    if viewport_aspect > world_aspect:
        new_width = (h - 2*margin) * world_aspect
        x_offset = (w - new_width)/2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        new_height = (w - 2*margin)/world_aspect
        y_offset = (h - new_height)/2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    glViewport(int(Vleft), int(Vbottom), int(Vright-Vleft), int(Vtop-Vbottom))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(Wleft, Wright, Wbottom, Wtop)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()

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
