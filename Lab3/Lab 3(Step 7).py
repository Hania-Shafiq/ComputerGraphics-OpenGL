# Step7: Writing Text to the Screen

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18

from OpenGL.GLU import *

# Window size
width, height = 500, 500

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)   # White background
    glColor3f(0.0, 0.0, 0.0)           # Default Black text
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)    # Simple 2D projection

def drawText(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    """Helper to draw text at (x,y)"""
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a blue rectangle (for reference)
    glColor3f(1.0, 0.0, 1.0)  # Blue rectangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 400)
    glVertex2f(100, 400)
    glEnd()

    # --- Custom Text with different colors ---
    glColor3f(1.0, 0.7, 0.0)    # Red
    drawText(150, 300, "Hello,")

    glColor3f(0.0, 0.5, 0.3)    # Green
    drawText(220, 300, "I am")

    glColor3f(0.8, 0.0, 0.8)    # Purple
    drawText(280, 300, "Hania")

    # Second line for style
    glColor3f(0.9, 0.4, 0.0)    # Orange
    drawText(180, 260, "Welcome to Lab 3 Step 7")

    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Step 7: Writing Text to the Screen")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
