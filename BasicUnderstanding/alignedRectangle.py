from OpenGL.GL import *      # OpenGL core functions (drawing, colors, vertices)
from OpenGL.GLUT import *    # OpenGL Utility Toolkit (window creation, event handle, input)
from OpenGL.GLU import *     # OpenGL Utility Library (projection/mmatrix helpers)

# Window Size
W, H = 800, 600  # in pixels

# Display function (draw everything here)
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the window with the background color

    # Rectangle 1 - bright gray
    glColor3f(0.6, 0.6, 0.6)         # Set current color (R,G,B) for rectangle
    glRecti(20, 20, 100, 70)         # Draw rectangle with opposite corners (x1,y1) & (x2,y2)

    # Rectangle 2 - dark gray
    glColor3f(0.2, 0.2, 0.2)         # Change current color
    glRecti(70, 50, 150, 130)        # Draw second rectangle

    glFlush()                         # Ensure all drawing commands are executed immediately

# Main function
def main():
    glutInit()                        # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffer, RGB color mode
    glutInitWindowSize(W, H)          # Set initial window size
    glutCreateWindow(b"Aligned Rectangles Example")  # Create window with title

    # Setup Orthographic projection
    glMatrixMode(GL_PROJECTION)       # Switch to projection matrix
    glLoadIdentity()                  # Reset projection matrix
    gluOrtho2D(0, W, 0, H)            # Set 2D orthographic projection (pixel-like coords)
    glMatrixMode(GL_MODELVIEW)        # Switch back to model-view matrix

    # Set background color
    glClearColor(1.0, 1.0, 1.0, 0.0)  # White background (R,G,B,Alpha)
    glutDisplayFunc(display)          # Tell GLUT to call display() to render window
    glutMainLoop()                    # Enter GLUT event processing loop
    
main()
