#done
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# === Window size ===
WIDTH, HEIGHT = 800, 600

# === World window (dino coordinates range) ===
world_left, world_right = 0, 640
world_bottom, world_top = 0, 480

# === Global dinosaur data ===
dino_polylines = []

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

# === Draw Single Dino ===
def draw_dino():
    glColor3f(0.8, 0.5, 0)
    glScalef(0.09, 0.09, 1.0)   # scale to fit tile
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in poly:
            glVertex2f(x, y)
        glEnd()

# === Display Function (Modified for Exam Logic) ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    cols, rows = 10, 10
    dx = (world_right - world_left) / cols   # width of tile in world co-ord
    dy = (world_top - world_bottom) / rows #height of tile in world co-ord

    glPushMatrix() #store coordinate system
    glTranslatef(dx, dy, 0)  # Initial offset to center in tile gave width and height

    for row in range(rows):
        glPushMatrix()  # Save start position of this row
        for col in range(cols):
            glPushMatrix() #ek dino ki tranformation dosray dino ko affect na kare
            glScalef(1, 1, 1)  # scale to fit each tile
            draw_dino()
            glPopMatrix()
            glTranslatef(dx, 0, 0)  # Move to next column (same structure)
        glPopMatrix()  # Return to start of row
        glTranslatef(0, dy, 0)  # Move to next row
    glPopMatrix()  # Back to original
    glFlush()

# === Reshape Function ===
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

# === Main Function ===
def main():
    global dino_polylines
    dino_polylines = load_dino("C:\\Users\\PMLS\\Desktop\\ComputerGraphics\\Lab3\\dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Exam: Dino Tiling using Push/PopMatrix")
    glClearColor(0, 0, 0, 1)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()