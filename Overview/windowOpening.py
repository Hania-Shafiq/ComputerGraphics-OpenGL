# Import OpenGL and GLUT modules
from OpenGL.GL import *       # OpenGL functions for drawing (points, lines, polygons, etc.)
from OpenGL.GLUT import *     # GLUT functions for window management and event handling, window open close
from OpenGL.GLU import *      # GLU functions (utility functions like setting camera, projection, etc.)

# ---------------- CALLBACK FUNCTIONS ---------------- #

# Function to handle screen redraw events
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the window with the background color
    glFlush()                     # Force execution of OpenGL commands immediately

# Function to handle window resize events
def myReshape(width, height):
    glViewport(0, 0, width, height)  # Set viewport to cover the entire window
    glMatrixMode(GL_PROJECTION)       # Switch to projection matrix mode
    glLoadIdentity()                  # Reset the projection matrix
    gluOrtho2D(0, width, 0, height)  # Set 2D orthographic coordinate system: (0,0) bottom-left, (width,height) top-right
    glMatrixMode(GL_MODELVIEW)        # Switch back to modelview matrix for drawing

# Function to handle mouse click events
def myMouse(button, state, x, y):
    # 'button' = which mouse button clicked
    # 'state' = GLUT_DOWN or GLUT_UP
    # 'x' & 'y' = mouse position in window coordinates
    print(f"Mouse clicked at ({x}, {y})")  # Just print mouse position

# Function to handle keyboard events
def myKeyboard(key, x, y):
    # 'key' = pressed key
    # 'x' & 'y' = mouse position when key was pressed
    print(f"Key pressed: {key.decode()} at ({x}, {y})")  # Decode byte key to string & print

# Function to perform any custom initialization
def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set window background color to white (RGBA)
    glColor3f(0.0, 0.0, 0.0)          # Set default drawing color to black (RGB)
    glPointSize(4.0)                  # Set default point size for drawing points

# ---------------- MAIN PROGRAM ---------------- #
def main():
    glutInit()  # Initialize the GLUT library

    # Set display mode
    # GLUT_SINGLE = single buffer (no double buffering)
    # GLUT_RGB = RGB color mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(640, 480)       # Set initial window size to 640x480 pixels
    glutInitWindowPosition(100, 150)   # Set initial window position (100 pixels right, 150 pixels down)
    glutCreateWindow(b"My First Attempt")  # Create window and set its title (byte string required)

    # Register callback functions for events
    glutDisplayFunc(myDisplay)       # Called whenever window needs redraw
    glutReshapeFunc(myReshape)       # Called whenever window is resized
    glutMouseFunc(myMouse)           # Called on mouse click events
    glutKeyboardFunc(myKeyboard)     # Called on key press events

    myInit()                         # Perform custom initialization (background, color, point size)
    glutMainLoop()                    # Enter infinite loop to process events (mouse, keyboard, display)
                                      # Program runs until user closes the window

# Run the main program
if __name__ == "__main__":
    main()
