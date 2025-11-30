def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clear old frame 
    glMatrixMode(GL_PROJECTION) # switch to projection matrix which defines the camera lens
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -20, 20)  # 3D coordinate system

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, eye_z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # Camera position and orientation

    glColor3f(1.0, 0.6, 0.0)  # Orange color for objects
    glPushMatrix()
    glutWireCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0)
    glutWireSphere(1.0, 20, 20) #radius, slices, stacks
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glutWireTeapot(1.0)
    glPopMatrix()

    glFlush()