def ngon(n, cx, cy, r, theta):
    """Draw a regular n-gon centered at (cx,cy) with radius r and rotation theta (degrees)."""
    glBegin(GL_POLYGON)
    for i in range(n):
        angle = 2 * math.pi * i / n + math.radians(theta)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()