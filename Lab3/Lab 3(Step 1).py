# Step1: Add Reshape, Mouse and Keyboard Handler

# step1.py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

def init():
    glClearColor(1.0, .3, .3, .0)  # Pinkish background
    glColor3f(0.0, 0.0, 0.0)          # Black drawing color
    glPointSize(5.0)                  # Point size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)   # 2D orthographic projection

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h) #tells open gl where to draw
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            print(f"Left click at ({x}, {height - y})")
        elif button == GLUT_RIGHT_BUTTON:
            print(f"Right click at ({x}, {height - y})")

def keyboard(key, x, y):
    if key == b'q':   # quit on 'q'
        print("Exiting program.")
        glutLeaveMainLoop()
    else:
        print(f"Key pressed: {key.decode()}")

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 1")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
