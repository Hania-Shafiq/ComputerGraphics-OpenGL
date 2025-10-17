from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global values for interactive update
n_sides = 5     # default polygon sides
step_val = 2    # default step size

def rosette(n, cx, cy, radius, step=1):
    vertices = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        vertices.append((x, y))

    glBegin(GL_LINES)
    for i in range(n):
        for j in range(i + step, n, step):
            glVertex2f(*vertices[i])
            glVertex2f(*vertices[j])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)  # black lines

    # Draw interactive rosette in center
    rosette(n_sides, 400, 250, 200, step=step_val)

    glFlush()

def keyboard(key, x, y):
    global n_sides, step_val

    if key == b'+':     # increase sides
        n_sides += 1
    elif key == b'-' and n_sides > 3:  # decrease sides
        n_sides -= 1
    elif key == b's':   # increase step
        step_val += 1
    elif key == b'd' and step_val > 1: # decrease step
        step_val -= 1
    elif key == b'q':   # quit
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Interactive Rosette - Press + / - / s / d")
    gluOrtho2D(0, 800, 0, 600)
    glClearColor(1, 1, 1, 1)  # white background

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
