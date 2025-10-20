# Lab Activity 6: Drawing Parameterized Regular Polygon (n-gon)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 500, 500

def ngon(n, cx, cy, r, theta):
    """Draw a regular n-gon centered at (cx,cy) with radius r and rotation theta (degrees)."""
    glBegin(GL_POLYGON)
    for i in range(n):
        angle = 2 * math.pi * i / n + math.radians(theta)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Black polygon
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)   # 2D world window

def display():
    glClear(GL_COLOR_BUFFER_BIT)
   
    glColor3f(1.0, 1.0, 0.0)   # Red polygon
    ngon(8, 100, 100, 50, 45)  # Octagon rotated 45°

    glColor3f(0.0, 0.8, 1.0)   # Blue polygon
    ngon(6, 250, 250, 100, 0)  # Hexagon in center

    glColor3f(0.3, 0.6, 0.0)   # Green polygon
    ngon(30, 400, 100, 70, 0)  # Approximates a circle

    glFlush()

# === RESHAPE FUNCTION ===
def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h          # update global size
    glViewport(0, 0, w, h)        # define full drawing area
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)        # adjust coordinate system to new size
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()           # force redraw after resize

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Drawing Parameterized Regular Polygon (n-gon)")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
if __name__ == "__main__":
    main()
