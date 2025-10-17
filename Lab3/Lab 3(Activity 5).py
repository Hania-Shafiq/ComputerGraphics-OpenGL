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


def load_dino(filename="C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat"):
    """Load dinosaur polylines from file (skip blanks safely)"""
    polylines = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]  # remove blanks
        i = 0
        while i < len(lines):
            try:
                count = int(lines[i])   # number of vertices
                i += 1
                poly = []
                for _ in range(count):
                    if i >= len(lines):
                        break
                    parts = lines[i].split()
                    if len(parts) == 2:  # valid (x,y)
                        x, y = map(int, parts)
                        poly.append((x, y))
                    i += 1
                polylines.append(poly)
            except ValueError:
                i += 1
    return polylines


def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)


def draw_dino():
    """Draw the dinosaur polylines"""
    glColor3f(1.0, 0.0, 1.0)  # pink
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in poly:
            glVertex2f(x, y)
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # --- Draw Dino inside current viewport ---
    glViewport(vp_left, vp_bottom, vp_right - vp_left, vp_top - vp_bottom)
    setWindow(0, 640, 0, 480)  # world window fixed
    draw_dino()

    # --- Draw viewport border (in full window coordinates) ---
    glViewport(0, 0, width, height)      # switch back to full window
    setWindow(0, width, 0, height)
    glColor3f(1.0, 0.0, 0.0)  # red border
    glBegin(GL_LINE_LOOP)
    glVertex2f(vp_left, vp_bottom)
    glVertex2f(vp_right, vp_bottom)
    glVertex2f(vp_right, vp_top)
    glVertex2f(vp_left, vp_top)
    glEnd()

    glFlush()


def reshape(w, h):
    global width, height
    width, height = w, h
    glutPostRedisplay()


def specialKeys(key, x, y):
    """Move viewport with arrow keys"""
    global vp_left, vp_right, vp_bottom, vp_top
    step = 20  # move step

    if key == GLUT_KEY_LEFT:
        vp_left -= step
        vp_right -= step
    elif key == GLUT_KEY_RIGHT:
        vp_left += step
        vp_right += step
    elif key == GLUT_KEY_UP:
        vp_bottom += step
        vp_top += step
    elif key == GLUT_KEY_DOWN:
        vp_bottom -= step
        vp_top -= step

    glutPostRedisplay()


def keyboard(key, x, y):
    global vp_left, vp_right, vp_bottom, vp_top

    if key == b'q':  # quit
        print("Exiting program.")
        glutLeaveMainLoop()

    elif key == b'r':  # reset viewport
        vp_left, vp_right, vp_bottom, vp_top = 100, 700, 100, 500
        glutPostRedisplay()


def main():
    global dino_polylines
    dino_polylines = load_dino("C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab Activity 5: Dynamic Viewport (Panning Dino)")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(specialKeys)   # arrow keys
    glutKeyboardFunc(keyboard)     # normal keys
    glutMainLoop()


if __name__ == "__main__":
    main()

# Arrow keys → viewport move hoga
# r → reset viewport
# q → quit
