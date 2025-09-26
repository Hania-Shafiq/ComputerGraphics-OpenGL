from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Utility: Draw rectangle using 2 corners (bottom-left and top-right)
def draw_rect(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

# Utility: Draw custom parallelogram using four corners
def draw_parallelogram_custom(x1, y1, x2, y2, x3, y3, x4, y4, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)  # Bottom-left
    glVertex2f(x2, y2)  # Bottom-right
    glVertex2f(x3, y3)  # Top-right
    glVertex2f(x4, y4)  # Top-left
    glEnd()

# Utility: Draw quadrilateral (trapezoid) with four specific corners
def draw_trapezoid(x1, y1, x2, y2, x3, y3, x4, y4, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)  # Bottom-left
    glVertex2f(x2, y2)  # Bottom-right
    glVertex2f(x3, y3)  # Top-right
    glVertex2f(x4, y4)  # Top-left
    glEnd()

# Utility: Draw parallelogram from one point with given width, height, slant
def draw_parallelogram(x, y, width, height, slant, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x + slant, y)             # Bottom-left
    glVertex2f(x + width + slant, y)     # Bottom-right
    glVertex2f(x + width, y + height)    # Top-right
    glVertex2f(x, y + height)            # Top-left
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)

    brown = (0.6, 0.4, 0.3)  # Common brown color used for all wooden items

    # ---------------- Window ----------------
    draw_rect(-4, 4, -0.4, 8, (0.4, 0.7, 1))     # Left blue glass
    draw_rect(-0.4, 4, 0.4, 8, brown)            # Brown divider
    draw_rect(0.4, 4, 4, 8, (0.4, 0.7, 1))       # Right blue glass

    # ---------------- Chair ----------------
    draw_rect(-8, -2, -6, 0.8, brown)                              # Backrest (square)
    draw_parallelogram_custom(-7, -3, -5, -3, -6, -2, -8, -2, brown)  # Seat
    draw_rect(-8, -4, -7.8, -2, brown)                            # Back left leg
    draw_rect(-6.2, -4.4, -6, -2, brown)                          # Back right leg
    draw_rect(-7, -5.4, -6.8, -3.0, brown)                        # Front left leg
    draw_rect(-5.2, -5.4, -5, -3, brown)                          # Front right leg

    # ---------------- Table ----------------
    draw_parallelogram_custom(-2.6, -1.2, 3.8, -1.2, 2.4, 1.6, -4, 1.6, brown)  # Top surface
    draw_rect(-4, -4, -3.6, 1.6, brown)                         # Back left leg
    draw_rect(2, -4, 2.4, 1.6, brown)                           # Back right leg
    draw_rect(-2.6, -6.8, -2.2, -1.2, brown)                    # Front left leg
    draw_rect(3.4, -6.8, 3.8, -1.2, brown)                      # Front right leg
    draw_rect(-2.6, -2, 3.8, -1.2, brown)                       # Under surface
    draw_parallelogram_custom(-2.6, -2, -2.2, -1.2, -4, 1.6, -4, -0.2, brown)  # Side panel

    # ---------------- Laptop ----------------
    draw_parallelogram_custom(-2.2, -0.6, 0.4, -0.6, -0.4, 0.8, -3, 0.8, (0.1, 0.1, 0.1))  # Base
    draw_rect(-3, 0.8, -0.4, 3, (0.1, 0.1, 0.1))                                           # Screen

    # ---------------- Glass / Cup ----------------
    draw_trapezoid(1.2, 0.2, 1.6, 0.2, 1.8, 1, 1, 1, (0.4, 0.7, 1))  # Blue flipped trapezoid

    # ---------------- Lamp ----------------
    draw_rect(5, -6, 7, -5, brown)                                  # Base
    draw_rect(5.6, -5, 6.4, 0.8, brown)                             # Rod
    draw_trapezoid(4, 0.8, 8, 0.8, 7.2, 3.4, 4.8, 3.4, (1, 1, 0.4))  # Light shade

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D Room Scene Based on Grid")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10, 10, -10, 10)  # Coordinate grid range
    glutDisplayFunc(draw_scene)
    glutMainLoop()

if __name__ == "__main__":
    main()
