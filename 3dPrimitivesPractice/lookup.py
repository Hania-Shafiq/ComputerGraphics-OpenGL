from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 👁️ CAMERA POSITION (same for all)
eyeX, eyeY, eyeZ = 0.0, 3.0, 6.0
centerX, centerY, centerZ = 0.0, 0.0, 0.0

# 🟢 CASE 1: Normal (Y-axis is UP)
# 👉 Scene upright, teapot seedha
# up vector = (0, 1, 0)
#upX, upY, upZ = 0.0, 1.0, 0.0

# 🔴 CASE 2: Upside Down (Y-axis DOWN)
# 👉 Scene ulta ho jayega
# up vector = (0, -1, 0)
#upX, upY, upZ = 0.0, -1.0, 0.0

# 🔵 CASE 3: Side Tilted (X-axis UP)
# 👉 Scene side pe rotate dikhega
# up vector = (1, 0, 0)
upX, upY, upZ = 1.0, 0.0, 0.0

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # 🎯 Set camera using gluLookAt
    gluLookAt(eyeX, eyeY, eyeZ,
              centerX, centerY, centerZ,
              upX, upY, upZ)

    # 🫖 Draw teapot
    glColor3f(0.8, 0.4, 0.1)
    glutSolidTeapot(1.0)

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 50)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"gluLookAt UP Vector Visualization")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
