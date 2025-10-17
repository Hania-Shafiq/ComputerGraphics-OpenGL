# Lab Activity 7: Drawing a Simple Arc

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 500, 500


def draw_arc(cx, cy, r, start_angle, end_angle, segments=100):
    """Draw an arc centered at (cx, cy), radius r, from start_angle to end_angle (degrees)."""
    glBegin(GL_LINE_STRIP)
    for i in range(segments + 1):
        theta = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glColor3f(1.0, 1.0, 1.0)          
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Example arcs
    glColor3f(1.0, 1.0, 0.0)  
    draw_arc(250, 250, 100, 0, 90)   # Quarter circle

    glColor3f(1.0, 0.0, 1.0)  # 
    draw_arc(250, 250, 100, 90, 180)  # Another quarter circle

    glColor3f(1.0, 0.6, 0.0)  # Green arc
    draw_arc(250, 250, 150, 180, 360)  # Half circle

    glColor3f(1.0, 0.0, 1.0)  
    draw_arc(250, 250, 170, 90, 180)  # Another quarter circle

    glFlush()


def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab Activity 7: Drawing Simple Arc")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
