from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

# --- World Window (logical coordinate system) ---
world_left, world_right = -100, 100
world_bottom, world_top = -100, 100

# --- Viewport (screen area inside actual window) ---
vp_left, vp_right = 50, 450
vp_bottom, vp_top = 50, 450


# INITIALIZATION
def init():
    glClearColor(1, 1, 1, 1)   # White background
    glColor3f(0, 0, 0)         # Black drawing color

    # Set world window directly
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)

    # Set viewport directly
    glViewport(vp_left, vp_bottom, vp_right - vp_left, vp_top - vp_bottom)


# DRAW CONTENT
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # --- Blue Square ---
    glColor3f(0, 0, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    # --- Red Diagonal ---
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-50, -50)
    glVertex2f(50, 50)
    glEnd()

    glFlush()


# HANDLE RESHAPE + MAINTAIN ASPECT RATIO
def reshape(w, h):
    global width, height
    width, height = w, h

    # Maintain same aspect ratio
    world_aspect = (world_right - world_left) / (world_top - world_bottom)
    viewport_aspect = w / h
    margin = 50

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

    # Apply viewport and world window directly
    glViewport(int(Vleft), int(Vbottom),
               int(Vright - Vleft), int(Vtop - Vbottom))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutPostRedisplay()


# MAIN FUNCTION
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 4: ViewPort and World Window")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
