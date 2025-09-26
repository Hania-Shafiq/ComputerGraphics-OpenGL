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

# === Drawing Functions ===
def draw_dino():
    glColor3f(1.0, 0.4, 0.7)  # PINK dinosaur (R,G,B)
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (xw, yw) in poly:
            glVertex2f(xw, yw)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    cols, rows = 5, 5
    tile_w, tile_h = WIDTH // cols, HEIGHT // rows

    for i in range(cols):
        for j in range(rows):
            glViewport(i * tile_w, j * tile_h, tile_w, tile_h)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

            if (i + j) % 2 == 0:  # upright
                gluOrtho2D(Wleft, Wright, Wbottom, Wtop)
            else:  # flipped vertically
                gluOrtho2D(Wleft, Wright, Wtop, Wbottom)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            draw_dino()

    glFlush()

# === Main Setup ===
def main():
    global dino_polylines
    dino_polylines = load_dino("C:/Users/PMLS/Desktop/ComputerGraphics/Lab3/dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Dinosaur Tiling with Flipping")
    glClearColor(0, 0, 0, 1)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
