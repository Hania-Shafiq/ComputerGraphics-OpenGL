from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 800, 600

# Viewport (start in middle of window)
vp_left, vp_right = 100, 700
vp_bottom, vp_top = 100, 500

# Dino data storage
dino_polylines = []


# ---- LOAD DINO FILE ----
def load_dino(filepath):
    polylines = []
    with open(filepath, "r") as f:
        num_polylines = int(f.readline().strip())
        for _ in range(num_polylines):
            n = int(f.readline().strip())
            points = []
            for _ in range(n):
                x, y = map(int, f.readline().split())
                points.append((x, y))
            polylines.append(points)
    return polylines


# ---- DEFINE WORLD WINDOW ----
def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)


# ---- DRAW DINO ----
def draw_dino():
    glColor3f(0.0, 0.0, 0.0)  # black
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in poly:
            glVertex2f(x, y)
        glEnd()


# ---- DISPLAY FUNCTION ----
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw Dino inside current viewport
    glViewport(vp_left, vp_bottom, vp_right - vp_left, vp_top - vp_bottom)
    setWindow(0, 640, 0, 480)
    draw_dino()

    # Draw red border for viewport
    glViewport(0, 0, width, height)
    setWindow(0, width, 0, height)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(vp_left, vp_bottom)
    glVertex2f(vp_right, vp_bottom)
    glVertex2f(vp_right, vp_top)
    glVertex2f(vp_left, vp_top)
    glEnd()

    glFlush()


# ---- HANDLE RESIZE ----
def reshape(w, h):
    global width, height
    width, height = w, h
    glutPostRedisplay()


# ---- MOUSE HANDLER ----
def mouse(button, state, x, y):
    global vp_left, vp_right, vp_bottom, vp_top
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            vp_left -= 30
            vp_right -= 30
        elif button == GLUT_RIGHT_BUTTON:
            vp_left += 30
            vp_right += 30
        glutPostRedisplay()


# ---- MAIN FUNCTION ----
def main():
    global dino_polylines
    # ✅ Full absolute path (your path)
    dino_polylines = load_dino("C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab Activity 5: Dynamic Viewport (Panning Dino)")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()


if __name__ == "__main__":
    main()
