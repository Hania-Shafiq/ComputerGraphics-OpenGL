# Import OpenGL and GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# ===================== MYINIT =====================
def myInit():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glColor3f(1.0, 1.0, 1.0)          # Set drawing color to white
    glPointSize(5.0)                   # Size of each point/star

# ===================== RESHAPE =====================
def myReshape(width, height):
    glViewport(0, 0, width, height)       # Adjust viewport to window size
    glMatrixMode(GL_PROJECTION)           # Switch to projection matrix
    glLoadIdentity()                      # Reset projection matrix
    gluOrtho2D(0, width, 0, height)       # Set 2D coordinate system
    glMatrixMode(GL_MODELVIEW)            # Switch back to modelview

# ===================== DRAW CONSTELLATION =====================
def drawConstellation():
    # Big Dipper star coordinates
    stars = [
        (289, 190),  # Dubhe
        (320, 128),  # Merak
        (239, 67),   # Phecda
        (194, 101),  # Megrez
        (129, 83),   # Alioth
        (75, 73),    # Mizar
        (74, 74),    # Alcor
        (20, 10)     # Alkaid
    ]
    
    glBegin(GL_POINTS)  # Start drawing points
    for x, y in stars:
        glVertex2i(x, y)  # Draw each star
    glEnd()

# ===================== DISPLAY =====================
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear screen
    drawConstellation()           # Draw the Big Dipper
    glFlush()                     # Render everything

# ===================== MAIN PROGRAM =====================
def main():
    glutInit()                               # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)             # Initial window size
    glutInitWindowPosition(100, 150)         # Initial window position
    glutCreateWindow(b"Big Dipper Constellation")  # Window title

    myInit()                                 # Custom initialization
    glutDisplayFunc(myDisplay)               # Register display callback
    glutReshapeFunc(myReshape)               # Register reshape callback

    glutMainLoop()                            # Start event loop

if __name__ == "__main__":
    main()
