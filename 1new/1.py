from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initial Window size
WIDTH, HEIGHT = 800, 600

# World Window (Dino range)
Wleft, Wright = 0, 640
Wbottom, Wtop = 0, 480

# Dynamic viewport variables
Vleft, Vright, Vbottom, Vtop = 0, 0, 0, 0


# === Load Dino Data ===
def load_dino(filename):
    polylines = []
    with open(filename, "r") as f:
        num_polylines = int(f.readline().strip())
        for _ in range(num_polylines):
            count = int(f.readline().strip())
            points = [tuple(map(int, f.readline().split())) for _ in range(count)]
            polylines.append(points)
    return polylines


# Global dinosaur data
dino_polylines = []


# === World → Viewport Mapping ===
def map_to_viewport(xw, yw):
    xv = ((xw - Wleft) / (Wright - Wleft)) * (Vright - Vleft) + Vleft
    yv = ((yw - Wbottom) / (Wtop - Wbottom)) * (Vtop - Vbottom) + Vbottom
    return xv, yv


# === Display ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 1, 0)
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (xw, yw) in poly:
            xv, yv = map_to_viewport(xw, yw)
            glVertex2f(xv, yv)
        glEnd()

    glFlush()


# === reshape() using your given logic ===
def reshape(W, H):
    global Vleft, Vright, Vbottom, Vtop

    # Set full viewport for drawing
    glViewport(0, 0, W, H)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, W, 0, H)
    glMatrixMode(GL_MODELVIEW)
    # Aspect ratio R = world_width / world_height
    R = (Wright - Wleft) / (Wtop - Wbottom)

    # ------ MATCHING YOUR C CODE EXACTLY ------
    if R > (W / H):
        # setViewport(0, W, 0, W/R)
        Vleft = 0
        Vright = W
        Vbottom = 0
        Vtop = W / R
    else:
        # setViewport(0, H*R, 0, H)
        Vleft = 0
        Vright = H * R
        Vbottom = 0
        Vtop = H
    # -----------------------------------------

    glutPostRedisplay()


# === Main ===
def main():
    global dino_polylines
    dino_polylines = load_dino("dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Dino with Exact Aspect Ratio Reshape")

    glClearColor(0, 0, 0, 1)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if _name_ == "_main_":
    main()