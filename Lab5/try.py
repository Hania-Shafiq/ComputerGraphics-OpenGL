from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import os
import pygame

# ---------- WINDOW SETTINGS ----------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ---------- MARIO SETTINGS ----------
mario_x = -0.2   # fixed position
mario_y = -0.75
y_velocity = 0
gravity = 0.005
jumping = False
moving_right = False
moving_left = False
frame = 0

# ---------- BACKGROUND ----------
bg_x = 0.0
bg_speed = 0.02
bg_width = 2.0   # OpenGL coordinate width of one tile

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# ---------- TEXTURES ----------
textures = {}

def load_texture(file_name):
    img = Image.open(file_name)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return tex_id

def init_textures():
    global textures
    textures['stand'] = load_texture(os.path.join(IMAGE_DIR, 'stand.bmp'))
    textures['jump'] = load_texture(os.path.join(IMAGE_DIR, 'jump.bmp'))
    textures['run'] = [
        load_texture(os.path.join(IMAGE_DIR, 'run1.bmp')),
        load_texture(os.path.join(IMAGE_DIR, 'run2.bmp')),
        load_texture(os.path.join(IMAGE_DIR, 'run3.bmp')),
    ]
    textures['bg'] = load_texture(os.path.join(IMAGE_DIR, 'bg.png'))

# ---------- SOUND ----------
def init_sound():
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

    # Background music
    bg_sound = os.path.join(SOUND_DIR, "gamebgsound.wav")
    if not os.path.exists(bg_sound):  # fallback to mp3
        bg_sound = os.path.join(SOUND_DIR, "gamebgsound.mp3")

    if os.path.exists(bg_sound):
        pygame.mixer.music.load(bg_sound)
        pygame.mixer.music.play(-1)  # loop forever

    # Jump sound
    global jump_sound
    jump_sound = None
    jump_path_wav = os.path.join(SOUND_DIR, "jump.wav")
    jump_path_mp3 = os.path.join(SOUND_DIR, "jump.mp3")

    if os.path.exists(jump_path_wav):
        jump_sound = pygame.mixer.Sound(jump_path_wav)
    elif os.path.exists(jump_path_mp3):
        jump_sound = pygame.mixer.Sound(jump_path_mp3)

# ---------- DRAW FUNCTIONS ----------
def draw_quad(x, y, width, height, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x, y)
    glTexCoord2f(1, 0); glVertex2f(x + width, y)
    glTexCoord2f(1, 1); glVertex2f(x + width, y + height)
    glTexCoord2f(0, 1); glVertex2f(x, y + height)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_background():
    global bg_x, bg_width
    start_x = bg_x - bg_width
    for i in range(3):  # left, center, right → ensures no gap
        draw_quad(start_x + i * bg_width, -1, bg_width, 2, textures['bg'])

def draw_mario():
    global frame
    width = 0.15
    height = 0.25
    if jumping:
        current_texture = textures['jump']
    elif moving_right or moving_left:
        current_texture = textures['run'][frame % len(textures['run'])]
        frame += 1
    else:
        current_texture = textures['stand']
    draw_quad(mario_x, mario_y, width, height, current_texture)

# ---------- GAME LOGIC ----------
def update(value):
    global mario_y, y_velocity, jumping, bg_x, bg_width

    # Mario jumping
    if jumping:
        mario_y += y_velocity
        y_velocity -= gravity
        if mario_y <= -0.75:   # ground level
            mario_y = -0.75
            jumping = False
            y_velocity = 0

    # Background scrolling
    if moving_right:
        bg_x -= bg_speed
    if moving_left:
        bg_x += bg_speed

    # Proper infinite looping both sides
    if bg_x <= -bg_width:
        bg_x += bg_width
    if bg_x >= bg_width:
        bg_x -= bg_width

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 FPS

# ---------- KEYBOARD CONTROLS ----------
def special_down(key, x, y):
    global moving_right, moving_left
    if key == GLUT_KEY_RIGHT:
        moving_right = True
    if key == GLUT_KEY_LEFT:
        moving_left = True

def special_up(key, x, y):
    global moving_right, moving_left
    if key == GLUT_KEY_RIGHT:
        moving_right = False
    if key == GLUT_KEY_LEFT:
        moving_left = False

def key_down(key, x, y):
    global jumping, y_velocity
    if key == b' ' and not jumping:  # spacebar for jump
        jumping = True
        y_velocity = 0.1
        if jump_sound:
            jump_sound.play()

# ---------- OPENGL INIT ----------
def init():
    glClearColor(0.5, 0.8, 1.0, 1)  # sky blue
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    init_textures()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_background()
    draw_mario()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

# ---------- MAIN ----------
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Basic Mario Game")
    init()
    init_sound()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(key_down)
    glutSpecialFunc(special_down)
    glutSpecialUpFunc(special_up)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
