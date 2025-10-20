from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# ---------------- Window Setup ----------------
WIDTH, HEIGHT = 800, 600
Wleft, Wright = 0, 635
Wbottom, Wtop = 0, 439

# ---------------- Load Dino Data ----------------
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

# ---------------- Global Vars ----------------
dino_polylines = []
center_x, center_y = 0, 0 # Dino’s local center

# ---------------- Draw Single Dino ----------------
def draw_dino():
    glPushMatrix()
    glTranslatef(center_x, center_y, 0)
    glScalef(0.22, 0.22, 1.0)
    glColor3f(1.0, 1.0, 0.0)
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in poly:
            glVertex2f(x, y)
        glEnd()
    glPopMatrix()

# ---------------- Rotational Symmetry ----------------
def transform_dinos():
    num_dinos = 12
    radius = 250.0

    for i in range(num_dinos):
        theta = i * (360 / num_dinos)
        glPushMatrix()
        glRotatef(theta, 0, 0, 1)      # rotate by theta around origin
        glTranslatef(0.0, radius, 0.0) # move outward along local Y
        glRotatef(-theta, 0, 0, 1)     # rotate back so dino stays upright
        draw_dino()
        glPopMatrix()

# ---------------- Display Function ----------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    transform_dinos()
    glFlush()

# ---------------- Reshape Function ----------------
def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    view_size = 500
    if aspect >= 1:
        gluOrtho2D(-view_size * aspect, view_size * aspect, -view_size, view_size)
    else:
        gluOrtho2D(-view_size, view_size, -view_size / aspect, view_size / aspect)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ---------------- Main ----------------
def main():
    global dino_polylines
    dino_polylines = load_dino("C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Rotational Symmetry of Dinosaurs - Upright Circular")
    glClearColor(0, 0, 0, 1)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
