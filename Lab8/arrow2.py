from OpenGL.GL import *
from OpenGL.GLUT import *  
from OpenGL.GLU import *

width, height =  600, 600
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
    glLineWidth(3)
    glBegin(GL_LINES)
    lineRel(-w - t/2, -f)   # down-left
    lineRel(w, 0)           # right
    lineRel(0, -h)          # down
    lineRel(t, 0)           # right
    lineRel(0, h)           # up
    lineRel(w, 0)           # right
    lineRel(-w - t/2, f)    # up-left (back)
    glEnd()



def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()   

# ---- DISPLAY ----
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)

    # move to top middle and draw arrow
    CP[0], CP[1] = width / 2, height / 2
    arrow(60, 40, 20, 20)

    glFlush()

# ---- MAIN ----
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(100,100)
glutCreateWindow(b"Relative Arrow Drawing")
glClearColor(1, 1, 1, 1)
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutMainLoop()