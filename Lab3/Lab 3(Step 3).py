# Step3: Free Hand Drawing with Fat Brush

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500
drawing = False       # track if mouse button is pressed
strokes = []          # store drawn points

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)   # White background
    glColor3f(0.0, 1.0, 0.0)           # green brush
    glPointSize(7.0)                  # Fat brush size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)    # 2D orthographic projection

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw strokes as points
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for (x, y) in strokes:
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

def mouse(button, state, x, y):
    global drawing
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            drawing = True
            strokes.append((x, height - y))  # start stroke
            glutPostRedisplay()
        elif state == GLUT_UP:
            drawing = False   # stop drawing

def motion(x, y):
    """Draw while mouse moves with button pressed"""
    if drawing:
        strokes.append((x, height - y))
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 3: Free Hand Drawing with Fat Brush")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)  # mouse drag handler
    glutMainLoop()

if __name__ == "__main__":
    main()


# Logic: motion() function hi “free-hand” drawing ka kaam karta hai, kyunki har drag ke point store hote hain aur display function draw karta hai.