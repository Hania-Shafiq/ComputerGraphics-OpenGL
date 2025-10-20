from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# ---- GLOBAL VARIABLES ----
CP = [0.0, 0.0]
width, height = 600, 600
#vp_left = vp_right = vp_bottom = vp_top = 0


# ---- MOVE RELATIVE ----
def moveRel(dx, dy):
    CP[0] += dx
    CP[1] += dy

# ---- LINE RELATIVE ----
def lineRel(dx, dy):
    new_x = CP[0] + dx
    new_y = CP[1] + dy
    glVertex2f(CP[0], CP[1])
    glVertex2f(new_x, new_y)
    CP[0], CP[1] = new_x, new_y


# ---- ARROW FUNCTION ----
def arrow(f, h, t, w):
    glBegin(GL_LINES)
    lineRel(-w - t / 2, -f)  # down-left
    lineRel(w, 0)            # right
    lineRel(0, -h)           # down
    lineRel(t, 0)            # right (tail)
    lineRel(0, h)            # up
    lineRel(w, 0)            # right
    lineRel(-w - t / 2, f)   # up-left (back)
    glEnd()


# ---- DISPLAY FUNCTION ----
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    # move to some position and draw arrow
    CP[0], CP[1] = 300, 500
    arrow(60, 40, 20, 20)
    glFlush()


# ---- RESHAPE FUNCTION ----
def reshape(w, h):
    global width, height, vp_left, vp_right, vp_bottom, vp_top
    width, height = w, h
    
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # --- World window (fixed) ---
    Wleft, Wright, Wbottom, Wtop = 0, 500, 0, 500

    # --- Aspect ratio maintain ---
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    vl, vr = int(Vleft), int(Vright)
    vb, vt = int(Vbottom), int(Vtop)

    glViewport(vl, vb, vr - vl, vt - vb)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


# ---- MAIN PROGRAM ----
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Relative Arrow Drawing with Reshape")
glClearColor(1, 1, 1, 1)
gluOrtho2D(0, width, 0, height)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
