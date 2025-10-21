from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# --- Global variables for rotation angles ---
year = 0.0       # Planet orbit around Sun
day = 0.0        # Planet rotation on its axis
moon_year = 0.0  # Moon orbit around Planet
moon_day = 0.0   # Moon rotation on its axis

# --- OpenGL Initialization ---
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)  # Enable depth test for correct 3D overlapping

# --- Draw Scene Function ---
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # --- Projection ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -3, 3, -20, 20)  # Orthographic view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # --- Camera setup ---
    gluLookAt(0, 5, 5,  # Eye position
              0, 0, 0,  # Center position (look at origin)
              0, 1, 0)  # Up vector (Y-axis up)

    # --- Sun ---
    glPushMatrix()  # Save coordinate system for Sun
    glColor3f(1.0, 1.0, 0.0)  # Yellow Sun
    glRotatef(day / 10, 0.0, 1.0, 0.0)  # Slow rotation of Sun on its axis
    glutWireSphere(0.5, 20, 16)
    glPopMatrix()  # Restore coordinate system

    # --- Planet orbit and rotation ---
    glPushMatrix()  # Save coordinate system for Planet orbit
    glRotatef(year, 0.0, 1.0, 0.0)  # Planet orbit around Sun
    glTranslatef(2.0, 0.0, 0.0)     # Move planet away from Sun
    
    # Planet rotation on its axis
    glPushMatrix()
    glRotatef(day, 0.0, 1.0, 0.0)   # Planet spins on its own axis
    glColor3f(0.0, 0.0, 1.0)        # Blue Planet
    glutWireSphere(0.2, 10, 8)
    glPopMatrix()  # Restore after planet rotation

    # --- Moon orbit and rotation ---
    glPushMatrix()  # Save coordinate system for Moon
    glRotatef(moon_year, 0.0, 1.0, 0.0)  # Moon orbit around Planet
    glTranslatef(0.5, 0.0, 0.0)          # Distance from Planet
    glRotatef(moon_day, 0.0, 1.0, 0.0)   # Moon spins on its axis
    glColor3f(0.5, 0.5, 0.5)             # Gray Moon
    glutWireSphere(0.1, 10, 8)
    glPopMatrix()  # Restore after Moon

    glPopMatrix()  # Restore after Planet orbit

    glutSwapBuffers()  # Swap buffers for double buffering

# --- Animation update function ---
def animate(value):
    global year, day, moon_year, moon_day
    year = (year + 0.5) % 360       # Planet orbit angle
    day = (day + 2.0) % 360         # Planet rotation angle
    moon_year = (moon_year + 4.0) % 360  # Moon orbit angle
    moon_day = (moon_day + 8.0) % 360    # Moon rotation angle
    glutPostRedisplay()             # Redraw scene
    glutTimerFunc(20, animate, 0)  # Call animate again after 20 ms

# --- Handle window resize ---
def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -3, 3, -20, 20)
    glMatrixMode(GL_MODELVIEW)

# --- Main function ---
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Solar System Hierarchical Model")
    init()
    glutDisplayFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutTimerFunc(20, animate, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()


# World (Origin / Root)
# │
# ├── Sun
# │   └── rotate(day/10)
# │
# └── Planet (Earth)
#     ├── orbit(year)      # around Sun
#     ├── translate(2,0,0)
#     ├── rotate(day)      # Planet spin
#     └── Moon
#         ├── orbit(moon_year)  # around Planet
#         ├── translate(0.5,0,0)
#         └── rotate(moon_day)  # Moon spin