# Step5: Adding Keyboard Interaction

#i zoom in o zoom out  
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

# World window (logical coordinates)
world_left, world_right = -100, 100
world_bottom, world_top = -100, 100

# Current shape color (RGB)
shape_color = [0.0, 0.0, 1.0]  # start as blue

def setWindow(left, right, bottom, top):
    global world_left, world_right, world_bottom, world_top
    world_left, world_right = left, right
    world_bottom, world_top = bottom, top
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right - left, top - bottom)

def init():
    glClearColor(1.0, 0.0, 1.0, 1.0)  # background
    setWindow(world_left, world_right, world_bottom, world_top)
    setViewport(50, width - 50, 50, height - 50)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw square
    glColor3f(*shape_color)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    # # Draw diagonal
    # glColor3f(1.0, 0.0, 0.0)  # red diagonal always
    # glBegin(GL_LINES)
    # glVertex2f(-50, -50)
    # glVertex2f(50, 50)
    # glEnd()

    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    setViewport(50, w - 50, 50, h - 50)
    setWindow(world_left, world_right, world_bottom, world_top)

def keyboard(key, x, y):
    global shape_color, world_left, world_right, world_bottom, world_top

    if key == b'q':  # Quit
        print("Exiting program.")
        glutLeaveMainLoop()

    elif key == b'r':  # Red
        shape_color = [1.0, 0.0, 0.0]
        print("Changed color to RED")

    elif key == b'g':  # Green
        shape_color = [0.0, 1.0, 0.0]
        print("Changed color to GREEN")

    elif key == b'b':  # Blue
        shape_color = [0.0, 0.0, 1.0]
        print("Changed color to BLUE")

    elif key == b'i':  # Zoom in
        world_left += 10
        world_right -= 10
        world_bottom += 10
        world_top -= 10
        print("Zoom In")
        setWindow(world_left, world_right, world_bottom, world_top)

    elif key == b'o':  # Zoom out
        world_left -= 10
        world_right += 10
        world_bottom -= 10
        world_top += 10
        print("Zoom Out")
        setWindow(world_left, world_right, world_bottom, world_top)

    glutPostRedisplay()

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



# r → change shape color to red
# g → change shape color to green
# b → change shape color to blue
# z → zoom in (shrink world window)
# x → zoom out (expand world window)
# q → quit program