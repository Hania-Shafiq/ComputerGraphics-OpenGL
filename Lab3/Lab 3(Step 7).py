from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18


# Window size
width, height = 500, 500

# World window bounds (for reshape function)
world_left, world_right = 0, 500
world_bottom, world_top = 0, 500

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)   # White background
    glColor3f(0.0, 0.0, 0.0)           # Default Black text
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)    # Simple 2D projection

def drawText(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    """Helper to draw text at (x,y)"""
    glRasterPos2f(x, y)  # Set starting position where text will be drawn
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a blue rectangle (for reference)
    glColor3f(1.0, 0.0, 1.0)  # Magenta rectangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 400)
    glVertex2f(100, 400)
    glEnd()

    # --- Custom Text with different colors ---
    glColor3f(1.0, 0.7, 0.0)    # Orange
    drawText(150, 300, "Hello,")

    glColor3f(0.0, 0.5, 0.3)    # Green
    drawText(220, 300, "I am")

    glColor3f(0.8, 0.0, 0.8)    # Purple
    drawText(280, 300, "Hania")

    # Second line for style
    glColor3f(0.9, 0.4, 0.0)    # Orange
    drawText(180, 260, "Welcome to Lab3")

    glFlush()

def reshape(w, h):
    global width, height
    width, height = w, h

    # Maintain same aspect ratio of world
    world_aspect = (world_right - world_left) / (world_top - world_bottom)
    viewport_aspect = w / h
    margin = 50

    if viewport_aspect > world_aspect:
        # Window is wider
        new_width = (h - 2 * margin) * world_aspect
        x_offset = (w - new_width) / 2
        Vleft, Vright = x_offset, x_offset + new_width
        Vbottom, Vtop = margin, h - margin
    else:
        # Window is taller
        new_height = (w - 2 * margin) / world_aspect
        y_offset = (h - new_height) / 2
        Vleft, Vright = margin, w - margin
        Vbottom, Vtop = y_offset, y_offset + new_height

    # Apply new viewport
    glViewport(int(Vleft), int(Vbottom),
               int(Vright - Vleft), int(Vtop - Vbottom))

    # Update projection (world window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(world_left, world_right, world_bottom, world_top)

    # Reset model view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutPostRedisplay()

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
