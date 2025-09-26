from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH, HEIGHT = 800, 600

# World Window (fixed for all tiles)
Wleft, Wright = 0, 640
Wbottom, Wtop = 0, 480


# --- LOAD DINO POLYLINES FROM FILE ---
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


# Load dataset from file
dino_polylines = load_dino("C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat")


# --- DRAW DINO IN CURRENT VIEWPORT ---
def draw_dino():
    glColor3f(1.0, 0.75, 0.8)  # Pink dinosaur
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (xw, yw) in poly:
            glVertex2f(xw, yw)
        glEnd()


# --- DISPLAY FUNCTION ---
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # 5x5 tiling
    for i in range(5):  # columns
        for j in range(5):  # rows
            # Each viewport cell (scaled to fit window)
            glViewport(i * (WIDTH // 5), j * (HEIGHT // 5), WIDTH // 5, HEIGHT // 5)

            # Reset projection for each viewport
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluOrtho2D(Wleft, Wright, Wbottom, Wtop)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            # Draw the dinosaur in this tile
            draw_dino()

    glFlush()


# --- RESHAPE FUNCTION ---
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)


# --- MAIN FUNCTION ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Dinosaur Multi-Tiling Viewports")

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == "__main__":
    main()
