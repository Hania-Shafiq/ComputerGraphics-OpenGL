# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import sys
# #import math

# # Global variables
# eye_z = 5.0
# theta = 0.0
# width, height = 800, 600

# def init():
#     glClearColor(0.0, 0.0, 0.0, 0.0)
#     glEnable(GL_DEPTH_TEST) # Enable depth testing for 3D rendering so closer objects hide farther ones

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clear old frame 
#     glMatrixMode(GL_PROJECTION) # switch to projection matrix which defines the camera lens
#     glLoadIdentity()
#     glOrtho(-10, 10, -10, 10, -20, 20)  # 3D coordinate system

#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     gluLookAt(0.0, 0.0, eye_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # Camera position and orientation

#     glColor3f(1.0, 0.6, 0.0)  # Orange color for objects
#     glPushMatrix()
#     glutWireCube(2.0)
#     glPopMatrix()

#     glPushMatrix()
#     glTranslatef(2.0, 0.0, 0.0)
#     glutWireSphere(1.0, 20, 20) #radius, slices, stacks
#     glPopMatrix()

#     glPushMatrix()
#     glTranslatef(-2.0, 0.0, 0.0)
#     glutWireTeapot(1.0)
#     glPopMatrix()

#     glFlush()

# def reshape(w, h):
#     global width, height
#     if h == 0:
#         h = 1
#     width = w
#     height = h
#     glViewport(0, 0, w, h)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-10, 10, -10, 10, -20, 20)
#     glMatrixMode(GL_MODELVIEW)

# def keyboard(key, x, y):
#     global eye_z
#     if key == b'q':
#         sys.exit(0)
#     elif key == b'+':
#         eye_z += 0.5
#     elif key == b'-':
#         eye_z -= 0.5
#     glutPostRedisplay()

# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
#     glutInitWindowSize(width, height)
#     glutInitWindowPosition(100, 100)
#     glutCreateWindow(b"3D Visualization")
#     init()
#     glutDisplayFunc(display)
#     glutReshapeFunc(reshape)
#     glutKeyboardFunc(keyboard)
#     glutMainLoop()

# if __name__ == "__main__":
#     main()



from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#import sys
import math

# Global variables
eye_z = 5.0
theta = 0.0
width, height = 800, 600

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST) #enables depth comparison so nearer objects hide the farther ones, creating a real 3D visibility effect. 

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -20, 20)  # 3D coordinate system

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Orbiting camera with manual z adjustment
    eye_x = 5.0 * math.cos(math.radians(theta))
    gluLookAt(eye_x, 0.0, eye_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glColor3f(0.4, 0.0, 0.2)  # Green color for objects
    glPushMatrix()
    glutWireCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0)
    glutWireSphere(1.0, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glutWireTeapot(1.0)
    glPopMatrix()

    glFlush()
    glutSwapBuffers()  # Show new frame by swapping back & front buffers (smooth display)

def reshape(w, h):
    global width, height
    if h == 0:
        h = 1
    width = w
    height = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -20, 20)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global eye_z
    if key == b'q':
        sys.exit(0)
    elif key == b'+':  # Move forward
        eye_z += 0.5
        print(f"Moving forward, eye_z at {eye_z}")  # Debug print
    elif key == b'-':  # Move backward
        eye_z -= 0.5
        print(f"Moving backward, eye_z at {eye_z}")  # Debug print
    glutPostRedisplay()

def animate(value):
    global theta
    theta += 5
    if theta > 360:
        theta -= 360
    glutPostRedisplay()
    glutTimerFunc(50, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Changed to double buffering
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Visualization- Animated")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(50, animate, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()