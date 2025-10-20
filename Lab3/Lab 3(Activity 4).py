from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global world window
world_left, world_right, world_bottom, world_top = 0, 640, 0, 480

# LOAD DINO DATA FROM FILE
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

# Global variable
dino_polylines = []

# Draw Dinosaur
def drawDino():
    glColor3f(1.0, 0.4, 0.7)  # pink lines
    for polyline in dino_polylines:
        glBegin(GL_LINE_STRIP)
        for (x, y) in polyline:
            glVertex2f(x, y)
        glEnd()

# Display + Keyboard
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Directly apply projection and viewport setup
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_MODELVIEW)  # → ab drawing (model) mode me shift ho gaye
    glLoadIdentity() 
    drawDino()
    glFlush()

def keyboard(key, x, y):
    global world_left, world_right, world_bottom, world_top
    zoomFactor = 20

    if key == b'+':  # zoom in
        world_left += zoomFactor
        world_right -= zoomFactor
        world_bottom += zoomFactor
        world_top -= zoomFactor
    elif key == b'-':  # zoom out
        world_left -= zoomFactor
        world_right += zoomFactor
        world_bottom -= zoomFactor
        world_top += zoomFactor
    elif key == b'r':  # reset
        world_left, world_right, world_bottom, world_top = 0, 640, 0, 480
    elif key == b'c':
        print(f"Key pressed at mouse position: ({x}, {y})")
    glutPostRedisplay()

def main():
    global dino_polylines
    dino_polylines = load_dino("C:/Users/PMLS/Desktop/ComputerGraphics/Lab3/dino.dat")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"Full Dinosaur with Zoom Controls")
    glClearColor(0, 0, 0, 0)  # black background
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
