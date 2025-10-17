from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Current Position (CP)
CP = [0.0, 0.0]

# ---- MOVE RELATIVE ---- move current position by (dx, dy) doesnot draw line
def moveRel(dx, dy):
    CP[0] += dx
    CP[1] += dy

# ---- LINE RELATIVE ---- draw cp form line to (cp.x+dx, cp.y+dy) and update cp
def lineRel(dx, dy):
    new_x = CP[0] + dx
    new_y = CP[1] + dy
    glVertex2f(CP[0], CP[1])
    glVertex2f(new_x, new_y)
    CP[0], CP[1] = new_x, new_y

# ---- ARROW FUNCTION ----
def arrow(f, h, t, w):
    glBegin(GL_LINES)
    lineRel(-w - t/2, -f)   # down-left
    lineRel(w, 0)           # right
    lineRel(0, -h)          # down
    lineRel(t, 0)           # right
    lineRel(0, h)           # up
    lineRel(w, 0)           # right
    lineRel(-w - t/2, f)    # up-left (back)
    glEnd()

# ---- DISPLAY ----
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)

    # move to top middle and draw arrow
    CP[0], CP[1] = 300, 500
    arrow(60, 40, 20, 20)

    glFlush()

# ---- MAIN ----
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Relative Arrow Drawing")
glClearColor(1, 1, 1, 1)
gluOrtho2D(0, 600, 0, 600)
glutDisplayFunc(display)
glutMainLoop()
