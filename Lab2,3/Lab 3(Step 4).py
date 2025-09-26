# Step4: Using both ViewPort and World Window

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

# Default world window (world coordinates)
world_left, world_right = -100, 100
world_bottom, world_top = -100, 100

# Default viewport (screen coordinates)
vp_left, vp_right = 50, 450
vp_bottom, vp_top = 50, 450

def setWindow(left, right, bottom, top):
    """Define the logical world window"""
    global world_left, world_right, world_bottom, world_top
    world_left, world_right = left, right
    world_bottom, world_top = bottom, top
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)

def setViewport(left, right, bottom, top):
    """Define the screen viewport"""
    global vp_left, vp_right, vp_bottom, vp_top
    vp_left, vp_right = left, right
    vp_bottom, vp_top = bottom, top
    glViewport(left, bottom, right - left, top - bottom)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Black drawing color
    setWindow(world_left, world_right, world_bottom, world_top)
    setViewport(vp_left, vp_right, vp_bottom, vp_top)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a square
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glBegin(GL_LINE_LOOP)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    # Draw diagonal inside square
    glColor3f(1.0, 0.0, 0.0)  # Red
    glBegin(GL_LINES)
    glVertex2f(-50, -50)
    glVertex2f(50, 50)
    glEnd()

    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    # keep same viewport in resized window
    setViewport(50, w - 50, 50, h - 50)
    setWindow(world_left, world_right, world_bottom, world_top)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 4: ViewPort and World Window")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
