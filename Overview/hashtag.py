from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawHashtag():
    # -------- THIN LINE --------
    glColor3f(0, 0, 1)  # Blue
    glLineWidth(1)      # Thin
    glBegin(GL_LINES)
    glVertex2i(50, 150); glVertex2i(150, 150)
    glVertex2i(50, 100); glVertex2i(150, 100)
    glVertex2i(80, 50); glVertex2i(80, 200)
    glVertex2i(120, 50); glVertex2i(120, 200)
    glEnd()

    # -------- THICK LINE --------
    glColor3f(1, 0, 0)  # Red
    glLineWidth(5)      # Thick
    glBegin(GL_LINES)
    glVertex2i(200, 150); glVertex2i(300, 150)
    glVertex2i(200, 100); glVertex2i(300, 100)
    glVertex2i(230, 50); glVertex2i(230, 200)
    glVertex2i(270, 50); glVertex2i(270, 200)
    glEnd()

    # -------- STIPPLED LINE --------
    glColor3f(0, 1, 0)  # Green
    glLineWidth(2)
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0x00FF)  # Dashed pattern
    glBegin(GL_LINES)
    glVertex2i(350, 150); glVertex2i(450, 150)
    glVertex2i(350, 100); glVertex2i(450, 100)
    glVertex2i(380, 50); glVertex2i(380, 200)
    glVertex2i(420, 50); glVertex2i(420, 200)
    glEnd()
    glDisable(GL_LINE_STIPPLE)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear screen
    drawHashtag()                 # Call the function to draw hashtags
    glFlush()                     # Render everything

def myInit():
    glClearColor(1, 1, 1, 0)  # White background
    glColor3f(0, 0, 0)        # Default color
    glPointSize(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 250)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Hashtag Lines")
    glutDisplayFunc(myDisplay)  # Register myDisplay as callback
    myInit()
    glutMainLoop()

# Run the program
if __name__ == "__main__":
    main()
