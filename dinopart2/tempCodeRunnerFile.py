from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH, HEIGHT = 800, 600

# Dino data bounds
Wleft, Wright = 0, 635
Wbottom, Wtop = 0, 439

# === LOAD DINO DATA ===
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

# Global data
dino_polylines = []
center_x, center_y = 0, 0

# === COMPUTE TRUE CENTER ===
def compute_center():
    global center_x, center_y
    xs, ys = [], []
    for poly in dino_polylines:
        for (x, y) in poly:
            xs.append(x)
            ys.append(y)
    center_x = (min(xs) + max(xs)) / 2
    center_y = (min(ys) + max(ys)) / 2


# === DRAW SINGLE DINO ===
def draw_dino():
    glPushMatrix()
    glTranslatef(-center_x, -center_y, 0)
    glScalef(0.22, 0.22, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in poly:
            glVertex2f(x, y)
        glEnd()
    glPopMatrix()


# === ROTATIONAL SYMMETRY ===
def transform_dinos():
    num_dinos = 12
    radius = 250.0

    for i in range(num_dinos):
        glPushMatrix()
        glRotatef(i * (360 / num_dinos), 0, 0, 1)
        glTranslatef(0.0, radius, 0.0)
        glRotatef(-i * (360 / num_dinos), 0, 0, 1)
        draw_dino()
        glPopMatrix()


# === DISPLAY FUNCTION ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # ✅ Center the viewport inside the window
    view_x = (WIDTH - 600) // 2     # center horizontally
    view_y = (HEIGHT - 500) // 2    # center vertically
    glViewport(view_x, view_y, 600, 500)  # centered viewport (adjust 600x500 if needed)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -400, 400)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Move slightly upward to align circle perfectly
    glTranslatef(0.0, 60.0, 0.0)

    transform_dinos()
    glFlush()


# === MAIN ===
def main():
    global dino_polylines
    dino_polylines = load_dino("dinopart2\dino.dat")
    compute_center()

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Rotational Symmetry of Dinosaurs - Perfect Center View")
    glClearColor(0, 0, 0, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()