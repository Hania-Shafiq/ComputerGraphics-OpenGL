# 🟦 Lab Activity 6: Drawing Parameterized Regular Polygon (n-gon)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# === Window size ===
width, height = 500, 500

# === Initial viewport boundaries ===
vp_left, vp_right, vp_bottom, vp_top = 0, width, 0, height

# === Draw regular n-gon ===
def ngon(n, cx, cy, r, theta):
    """Draw a regular n-gon centered at (cx, cy) with radius r and rotation theta (degrees)."""
    glBegin(GL_POLYGON)
    for i in range(n):
        angle = 2 * math.pi * i / n + math.radians(theta)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

# === Initialize OpenGL settings ===
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Default black color
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

# === Display callback ===
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Yellow octagon rotated 45°
    glColor3f(1.0, 1.0, 0.0)
    ngon(8, 100, 100, 50,90)

    # Blue hexagon in center
    glColor3f(0.0, 0.8, 1.0)
    ngon(6, 250, 250, 100, 0)

    # Green 30-gon (almost circle)
    glColor3f(0.3, 0.6, 0.0)
    ngon(30, 400, 100, 70, 0)

    glFlush()

# === Reshape callback with aspect ratio fix ===
def reshape(w, h):
    global width, height, vp_left, vp_right, vp_bottom, vp_top
    width, height = w, h

    # --- World window (fixed) ---
    Wleft, Wright, Wbottom, Wtop = 0, 500, 0, 500

    # --- Aspect ratio maintain ---
    world_aspect = (Wright - Wleft) / (Wtop - Wbottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    vp_left, vp_right = int(Vleft), int(Vright)
    vp_bottom, vp_top = int(Vbottom), int(Vtop)

    glViewport(vp_left, vp_bottom, vp_right - vp_left, vp_top - vp_bottom)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()

# === Arrow keys for panning ===
def specialKeys(key, x, y):
    global vp_left, vp_right, vp_bottom, vp_top
    step = 20
    if key == GLUT_KEY_LEFT:
        vp_left -= step
        vp_right -= step
    elif key == GLUT_KEY_RIGHT:
        vp_left += step
        vp_right += step
    elif key == GLUT_KEY_UP:
        vp_bottom += step
        vp_top += step
    elif key == GLUT_KEY_DOWN:
        vp_bottom -= step
        vp_top -= step
    glutPostRedisplay()

# === Main function ===
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Drawing Parameterized Regular Polygon (n-gon)")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(specialKeys)
    glutMainLoop()

if __name__ == "__main__":
    main()
