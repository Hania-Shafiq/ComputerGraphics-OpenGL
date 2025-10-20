# Step 5: Keyboard Interaction (Zoom + Color Change)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- Window size ---
width, height = 500, 500

# --- World Window (Logical Coordinates) ---
world_left, world_right = -100, 100
world_bottom, world_top = -100, 100

# --- Current Shape Color (RGB) ---
shape_color = [0.0, 0.0, 1.0]  # Blue

# --- Initialization ---
def init():
    glClearColor(1, 1, 1, 1)  # White background
    glColor3f(*shape_color)

# --- Display Function ---
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw Blue Square
    glColor3f(*shape_color)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    glFlush()

# --- Maintain Aspect Ratio ---
def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspect = w / h if h != 0 else 1
    world_width = world_right - world_left
    world_height = world_top - world_bottom

    if aspect >= 1:
        gluOrtho2D(world_left * aspect, world_right * aspect, world_bottom, world_top)
    else:
        gluOrtho2D(world_left, world_right, world_bottom / aspect, world_top / aspect)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# --- Keyboard Interaction ---
def keyboard(key):
    global shape_color, world_left, world_right, world_bottom, world_top

    if key == b'q':
        print("Exiting program.")
        glutLeaveMainLoop()

    elif key == b'r':
        shape_color = [1.0, 0.0, 0.0]
        print("Changed color to RED")

    elif key == b'g':
        shape_color = [0.0, 1.0, 0.0]
        print("Changed color to GREEN")

    elif key == b'b':
        shape_color = [0.0, 0.0, 1.0]
        print("Changed color to BLUE")

    elif key == b'+':  # Zoom in
        world_left += 10
        world_right -= 10
        world_bottom += 10
        world_top -= 10
        print("Zoom In")

    elif key == b'-':  # Zoom out
        world_left -= 10
        world_right += 10
        world_bottom -= 10
        world_top += 10
        print("Zoom Out")

    reshape(width, height)
    glutPostRedisplay()

# --- Main Function ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 5: Keyboard Interaction")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
