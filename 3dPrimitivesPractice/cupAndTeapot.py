from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- FUNCTION TO DRAW SCENE ---
def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #remove old frame
    glLoadIdentity() #reset transformation

    # CAMERA MOVE BACKWARD
    glTranslatef(0.0, 0.0, -16.0) #move 16 units backward

    # --- DRAW SOLID TEAPOT ---
    glPushMatrix()
    glColor3f(1.0, 0.8, 0.2)     
    glTranslatef(-1.5, 0.0, 0.0)    # move left
    glutSolidTeapot(0.9)
    glPopMatrix()

    # --- DRAW WIRE CUP (CYLINDER) ---
    glPushMatrix()
    glColor3f(0.3, 0.8, 1.0)        # blue color
    glTranslatef(1.5, -0.5, 0.0)    # move right and down
    glRotatef(-90, 1, 0, 0)         # make cylinder stand up
    glutSolidCylinder(0.5, 1.2, 20, 10)
    glPopMatrix()

    glutSwapBuffers() #double buffering to avoid flickering

# --- INITIALIZATION FUNCTION ---
def init():
    glEnable(GL_DEPTH_TEST) # enable depth testing for 3D means closer objects hide farther ones
    glClearColor(0.1, 0.1, 0.1, 1)

# --- HANDLE WINDOW RESIZE ---
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(25, w / h, 1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# --- MAIN FUNCTION ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Teapot and Cup (Static)")
    init()
    glutDisplayFunc(drawScene)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
