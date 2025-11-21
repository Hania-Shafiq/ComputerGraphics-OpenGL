from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# WINDOW SIZE
width = 600
height = 600

# Checkerboard grid size
rows = 8
cols = 8

def drawCheckerboard():
    glClear(GL_COLOR_BUFFER_BIT)

    cell_w = width // cols
    cell_h = height // rows

    for i in range(rows):
        for j in range(cols):

            # If sum even → white, odd → black
            if (i + j) % 2 == 0:
                glColor3f(1, 1, 1)      # white
            else:
                glColor3f(0, 0, 0)      # black

            glBegin(GL_POLYGON)
                # Bottom-left corner of the cell
            glVertex2i(j * cell_w, i * cell_h)           # (x0, y0)
            
            # Bottom-right corner
            glVertex2i((j+1) * cell_w, i * cell_h)      # (x1, y0)
            
            # Top-right corner
            glVertex2i((j+1) * cell_w, (i+1) * cell_h)  # (x1, y1)
            
            # Top-left corner
            glVertex2i(j * cell_w, (i+1) * cell_h)      # (x0, y1)
            glEnd()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Checkerboard Pattern")

    gluOrtho2D(0, width, 0, height)
    glClearColor(0.7, 0.7, 0.7, 1)  # background light gray

    glutDisplayFunc(drawCheckerboard)
    glutMainLoop()


main()
