from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH, HEIGHT = 800, 600

# Bounding box from dataset
Wleft, Wright = 0, 635
Wbottom, Wtop = 0, 439

# === LOAD DINO DATA FROM FILE ===
def load_dino(filename):
    polylines = []
    with open(filename, "r") as f:
        num_polylines = int(f.readline().strip())
        for _ in range(num_polylines):
            count = int(f.readline().strip())
            points = []
            for _ in range(count):
                x, y = map(int, f.readline().split())
                points.append((x, y))
            polylines.append(points)
    return polylines

# Global dinosaur data
dino_polylines = []

# === DRAW DINOSAUR ===
def draw_dino():
    glColor3f(1.0, 0.4, 0.7)  # PINK dinosaur
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (xw, yw) in poly:
            glVertex2f(xw, yw)
        glEnd()

# === DISPLAY FUNCTION ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range(5):
        for j in range(5):
            # Viewport for each tile
            glViewport(i * (WIDTH // 5), j * (HEIGHT // 5), WIDTH // 5, HEIGHT // 5)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

            # Flip alternate tiles vertically
            if (i + j) % 2 == 0:
                gluOrtho2D(Wleft, Wright, Wbottom, Wtop)
            else:
                gluOrtho2D(Wleft, Wright, Wtop, Wbottom)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            draw_dino()

    glFlush()

# === ADVANCED RESHAPE FUNCTION (keeps aspect ratio) ===
def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h  # Update global window size

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # --- Aspect Ratio Logic ---
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        # Window is wider → adjust width to keep ratio
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        # Window is taller → adjust height
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    glViewport(int(Vleft), int(Vbottom), int(Vright - Vleft), int(Vtop - Vbottom))  # x, y, width, height
    glutPostRedisplay()  # Redraw after resize

# === MAIN SETUP ===
def main():
    global dino_polylines
    dino_polylines = load_dino("C:/Users/PMLS/Desktop/ComputerGraphics/Lab3/dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Dinosaur Tiling with Flipping & Aspect Ratio")
    glClearColor(0, 0, 0, 1)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
