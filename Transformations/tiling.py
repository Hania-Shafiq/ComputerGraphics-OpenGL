# tiling_book_exact.py
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window and layout parameters
WIN_W, WIN_H = 700, 420   # rectangular window similar to book figure
COLS, ROWS = 4, 3         # as in book code: col < 4, row < 3
L = 120                   # horizontal spacing (center-to-center)
D = 120                   # vertical spacing (center-to-center)
W = 120                   # starting x offset for first motif
H = 100                   # starting y offset for first motif

# motif geometry tuning (change to tweak look)
SPIRAL_STEPS = 48
SPIRAL_TURNS = 2.2
SPIRAL_RADIUS = 18.0
INNER_DOT = 5.0
LINE_WIDTH = 2.6
CURLS = 4   # four curls in motif (book-like)

def draw_spiral_curve(radius=SPIRAL_RADIUS, turns=SPIRAL_TURNS, steps=SPIRAL_STEPS):
    """
    Draw one spiral curve starting at center and spiraling outward.
    The curve goes from t=0..1, angle = turns*2*pi*t, radius = r0 + (radius)*t
    We'll draw as a line strip to get the curly appearance.
    """
    glBegin(GL_LINE_STRIP)
    for s in range(steps + 1):
        t = s / float(steps)
        ang = turns * 2.0 * math.pi * t
        r = radius * t
        x = r * math.cos(ang)
        y = r * math.sin(ang)
        glVertex2f(x, y)
    glEnd()

def draw_motif():
    """
    Draw the book-style motif centered at the origin.
    Structure:
      - small filled center dot
      - four spiral curls rotated by 90 degrees each
      - optional small ring around to match the ornamental look
    """
    # center filled disk
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)
    steps = 24
    for i in range(steps + 1):
        a = 2.0 * math.pi * i / steps
        glVertex2f(INNER_DOT * math.cos(a), INNER_DOT * math.sin(a))
    glEnd()

    # spiral curls (line strips) rotated around center
    glLineWidth(LINE_WIDTH)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(CURLS):
        glPushMatrix()
        glRotatef(i * (360.0 / CURLS), 0.0, 0.0, 1.0)
        # translate outward a little so curl doesn't start fully at center
        glTranslatef(0.0, INNER_DOT + 4.0, 0.0)
        # draw a spiral curve (this forms a curl)
        draw_spiral_curve(radius=SPIRAL_RADIUS, turns=SPIRAL_TURNS, steps=SPIRAL_STEPS)
        glPopMatrix()

    # small outer decorative outline (subtle)
    glBegin(GL_LINE_LOOP)
    r = INNER_DOT + SPIRAL_RADIUS + 6.0
    for i in range(36):
        a = 2.0 * math.pi * i / 36.0
        glVertex2f(r * math.cos(a), r * math.sin(a))
    glEnd()

# ----- display and tiling -----
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Book-like tiling: push CT, translate to (W,H) for first motif, then nested loops
    glPushMatrix()                # cvs.pushCT()  in book
    glTranslatef(W, H, 0.0)       # cvs.translate2D(W, H)

    for row in range(ROWS):       # for(row = 0; row < 3; row++)
        glPushMatrix()            # start-of-row push (so we can return to row start)
        for col in range(COLS):   # for(col = 0; col < 4; col++)
            draw_motif()          # motif()
            glTranslatef(L, 0.0, 0.0)  # cvs.translate2D(L, 0)
        glPopMatrix()             # back to start of this row (cvs.popCT())
        glTranslatef(0.0, D, 0.0) # move up to next row (cvs.translate2D(0, D))
    glPopMatrix()                 # restore CT to initial (cvs.popCT())

    glutSwapBuffers()

# ----- nice reshape to preserve proportions similar to book layout -----
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Keep a fixed world frame so motifs keep their proportions:
    WORLD_W, WORLD_H = WIN_W, WIN_H
    aspect_world = WORLD_W / float(WORLD_H)
    aspect_view = w / float(h) if h != 0 else 1.0

    if aspect_view >= aspect_world:
        # window is wider -> expand world x-range proportionally
        extra = (w / float(h)) / aspect_world
        half_w = (WORLD_W * extra) / 2.0
        gluOrtho2D(-half_w, half_w, -WORLD_H / 2.0, WORLD_H / 2.0)
    else:
        # window is taller -> expand world y-range proportionally
        extra = aspect_world / (w / float(h))
        half_h = (WORLD_H * extra) / 2.0
        gluOrtho2D(-WORLD_W / 2.0, WORLD_W / 2.0, -half_h, half_h)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glLineWidth(LINE_WIDTH)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIN_W, WIN_H)
    glutCreateWindow(b"Tiling Example - exact book style")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
