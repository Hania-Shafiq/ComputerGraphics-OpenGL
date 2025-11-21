# Step2: Placing Dots with Mouse

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500
points = []  # store clicked points

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # White background
    glColor3f(1.0, 1.0, 1.0)          # Black drawing color
    glPointSize(7.0)                  # Dot size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)   # 2D orthographic projection

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw all points stored in the list
    glColor3f(1.0, 1.0, 1.0)  # Black
    glBegin(GL_POINTS)
    for (x, y) in points:
        glVertex2f(x, y)
    glEnd()

    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            # Save the clicked point and request redraw
            points.append((x, height - y))
            print(f"Placed dot at ({x}, {height - y})")
            glutPostRedisplay()
        elif button == GLUT_RIGHT_BUTTON:
            # Clear all points and redraw
            points.clear()
            print("Screen cleared")
            glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 2: Placing Dots with Mouse")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == "__main__":
    main()


# Mouse Click → Coordinate saved in list → glutPostRedisplay()
# → display() called → glVertex2f(x, y) → OpenGL draws dot
