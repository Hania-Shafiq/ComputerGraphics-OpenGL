def reshape(w, h):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = w, h          # update global size
    glViewport(0, 0, w, h)        # define full drawing area
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)        # adjust coordinate system to new size
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()           # force redraw after resize