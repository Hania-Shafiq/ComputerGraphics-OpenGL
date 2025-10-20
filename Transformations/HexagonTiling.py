from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# --- Window setup ---
WIDTH, HEIGHT = 800, 600
world_left, world_right = 0, 640
world_bottom, world_top = 0, 480

# --- Hexagon radius ---
R = 30.0  # distance from center to vertex

# --- Derived spacing values ---
dx = 3 * R/2             # horizontal distance between centers
dy = math.sqrt(3) * R    # vertical distance between centers


# === Draw one regular hexagon centered at origin ===
def draw_hexagon():
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 0.0)  # yellow
    for i in range(6):
        angle = math.radians(60 * i)
        x = R * math.cos(angle)
        y = R * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


# === Draw full hexagonal tiling using push/pop and translate ===
def hex_tiling(cols=9, rows=8):
    glPushMatrix()
    glTranslatef(60, 60, 0)  # starting offset (so all visible)

    for c in range(cols):
        glPushMatrix()  # save column start
        # For odd columns, offset vertically by half dy
        if c % 2 == 1:
            glTranslatef(0, dy / 2, 0)

        for r in range(rows):
            glPushMatrix()
            draw_hexagon()
            glPopMatrix()
            glTranslatef(0, dy, 0)  # move up for next row

        glPopMatrix()
        glTranslatef(dx, 0, 0)  # move right for next column

    glPopMatrix()


# === Display ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    hex_tiling(9, 8)
    glFlush()


# === Reshape ===
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# --- Initial window size ---
WIDTH, HEIGHT = 800, 600

# --- Hexagon geometry constants ---
R = 30.0  # radius
# dx = 1.5 * R
# dy = math.sqrt(3) * R


# === Draw one regular hexagon centered at origin ===
def draw_hexagon():
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 0.0)
    for i in range(6):
        angle = math.radians(60 * i)
        x = R * math.cos(angle)
        y = R * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


# === Draw full tiling using push/pop/translate ===
def hex_tiling():
    cols, rows = 8,8
    dx = 3 * R/2
    dy = math.sqrt(3) * R

    glPushMatrix()
    glTranslatef(60, 60, 0)  # start offset

    for r in range(rows):
        glPushMatrix()
        if r % 2 == 1:
            glTranslatef(0, dy / 2, 0)

        for c in range(cols):
            glPushMatrix()
            draw_hexagon()
            glPopMatrix()
            glTranslatef(0, dy, 0)

        glPopMatrix()
        glTranslatef(dx, 0, 0)

    glPopMatrix()


# === Display ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    hex_tiling()
    glFlush()

# === Reshape ===
def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h

    world_aspect = (world_right - world_left) / (world_top - world_bottom)
    viewport_aspect = w / h
    margin = 10

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

    glViewport(int(Vleft), int(Vbottom), int(Vright - Vleft), int(Vtop - Vbottom))

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


# === Main ===
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Hexagonal Tiling (with Working Reshape)")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()

# === Main ===
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Hexagonal Tiling using Transformations")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()