from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

angle_arm = 0
angle_leg = 0

def draw_circle(r=0.1):
    glBegin(GL_LINE_STRIP)
    for i in range(360):
        theta = math.radians(i)
        glVertex2f(r * math.cos(theta), r * math.sin(theta))
    glEnd()

def draw_square(size=0.8):
    glBegin(GL_LINE_LOOP)
    glVertex2f(-size/2, -size/2)
    glVertex2f(size/2, -size/2)
    glVertex2f(size/2, size/2)
    glVertex2f(-size/2, size/2)
    glEnd()

def human():
    # BODY
    glPushMatrix()
    #rect -> height double
    glScalef(1, 2.0, 1)
    glTranslatef(0, -0.5, 0)
    draw_square()
    glPopMatrix()

    # HEAD
    glPushMatrix()
    #glScalef(1.8,1.5,1)
    glTranslatef(0,0.1, 0) 
    draw_circle(0.3)
    glPopMatrix()

    # RIGHT ARM
    glPushMatrix()
    glTranslatef(0.5, -0.6, 0)
    glRotatef(30, 0, 0, 1)
    glScalef(0.2, 1, 1)
    draw_square()
    glPopMatrix()

    #hand
    glPushMatrix()
    glScalef(0.3,0.2,1)
    glTranslatef(-2.5,-5, 0) 
    draw_circle(0.3)
    glPopMatrix()

    # LEFT ARM
    glPushMatrix()
    glTranslatef(-0.5, -0.6, 0)
    glRotatef(-30, 0, 0, 1)
    glScalef(0.2, 1, 1)
    draw_square()
    glPopMatrix()

    #HAND
    glPushMatrix()
    glScalef(0.3,0.2,1)
    glTranslatef(2.5,-5, 0) 
    draw_circle(0.3)
    glPopMatrix()

    # RIGHT LEG
    glPushMatrix()
    glTranslatef(0.3, -2.2, 0)
    glRotatef(angle_leg, 0, 0, 1)
    glScalef(0.2, 1, 1)
    draw_square()
    glPopMatrix()

    #FOOT
    glPushMatrix()
    glScalef(0.3,0.2,1)
    glTranslatef(1,-13.3, 0) 
    draw_circle(0.3)
    glPopMatrix()

    # LEFT LEG
    glPushMatrix()
    glTranslatef(-0.3, -2.2, 0)
    glRotatef(angle_leg, 0, 0, 1)
    glScalef(0.2, 1, 1)
    draw_square()
    glPopMatrix()

    #FOOT
    glPushMatrix()
    glScalef(0.3,0.2,1)
    glTranslatef(-1,-13.3, 0) 
    draw_circle(0.3)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    human()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"2D Hierarchical Human")
    
    # Set up
    glClearColor(1, 1, 1, 1)
    glColor3f(0, 0, 0)

    # ✅ Viewport setup
    glViewport(0, 0, 500, 500)
    
    # ✅ Projection setup
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3, 3, -5, 3)
    
    # Back to model view
    glMatrixMode(GL_MODELVIEW)
    
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
