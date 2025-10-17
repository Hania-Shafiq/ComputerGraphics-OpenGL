from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH, HEIGHT = 800, 600

# World Window (approx range of dino data)
Wleft, Wright = 0, 640
Wbottom, Wtop = 0, 480

# Viewport (where dinosaur will be drawn on screen)
Vleft, Vright = 50, 750
Vbottom, Vtop = 50, 550


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


# --- WORLD TO VIEWPORT MAPPING ---
def map_to_viewport(xw, yw):
    xv = ((xw - Wleft) / (Wright - Wleft)) * (Vright - Vleft) + Vleft
    yv = ((yw - Wbottom) / (Wtop - Wbottom)) * (Vtop - Vbottom) + Vbottom
    return xv, yv


# --- DISPLAY FUNCTION ---
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw viewport border (Purple)
    glColor3f(0.5, 0.0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex2f(Vleft, Vbottom)
    glVertex2f(Vright, Vbottom)
    glVertex2f(Vright, Vtop)
    glVertex2f(Vleft, Vtop)
    glEnd()

    # Draw dinosaur polylines (Pink)
    glColor3f(1.0, 0.75, 0.8)
    for poly in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (xw, yw) in poly:
            xv, yv = map_to_viewport(xw, yw)
            glVertex2f(xv, yv)
        glEnd()

    glFlush()


# --- RESHAPE FUNCTION ---

# === RESHAPE FUNCTION ===
# === Reshape Function (Preserve Aspect Ratio) ===
def reshape(w, h):
    global Vleft, Vright, Vbottom, Vtop

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)

    # Maintain Dino's aspect ratio (based on world window)
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    window_aspect = w / h

    margin = 50

    if window_aspect > world_aspect:
        # Window is wider → adjust width to keep ratio
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        # Window is taller → adjust height to keep ratio
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height


# --- MAIN FUNCTION ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"DinoPolyLines - World to Viewport Mapping")

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == "__main__":
    main()
