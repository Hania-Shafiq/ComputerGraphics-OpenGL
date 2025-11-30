def display():
    glClear(GL_COLOR_BUFFER_BIT)

    cols, rows = 10, 10
    dx = (world_right - world_left) / cols   # width of tile in world co-ord
    dy = (world_top - world_bottom) / rows #height of tile in world co-ord

    glPushMatrix() #store coordinate system
    glTranslatef(dx, dy, 0)  # Initial offset to center in tile gave width and height

    for row in range(rows):
        glPushMatrix()  # Save start position of this row
        for col in range(cols):
            glPushMatrix() #ek dino ki tranformation dosray dino ko affect na kare
            glScalef(1, 1, 1)  # scale to fit each tile
            draw_dino()
            glPopMatrix()
            glTranslatef(dx, 0, 0)  # Move to next column (same structure)
        glPopMatrix()  # Return to start of row
        glTranslatef(0, dy, 0)  # Move to next row
    glPopMatrix()  # Back to original
    glFlush()