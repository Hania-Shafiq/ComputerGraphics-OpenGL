import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Mario Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Load Sprites with Auto Chroma Key (uses top-left pixel color)
def load_sprite(path):
    image = pygame.image.load(path).convert()   # convert for speed
    colorkey = image.get_at((0, 0))             # take top-left pixel as background
    image.set_colorkey(colorkey)                # make it transparent
    return image

# Mario sprites
mario_run = [
    load_sprite("Lab4/images/run1.bmp"),
    load_sprite("Lab4/images/run2.bmp"),
    load_sprite("Lab4/images/run3.bmp"),
]
mario_jump = load_sprite("Lab4/images/jump.bmp")


# Scale sprites
mario_run = [pygame.transform.scale(img, (50, 70)) for img in mario_run]
mario_jump = pygame.transform.scale(mario_jump, (50, 70))

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Mario setup
mario_x, mario_y = 100, HEIGHT - 70 - 40  # sprite height + ground
mario_vel = 5
jump = False
jump_count = 10
ground_height = 40

# Animation variables
frame_index = 0
frame_delay = 0

# Obstacles
obstacles = []
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 2000)

# Score & Game State
font = pygame.font.SysFont("Arial", 30)
score = 0
game_over = False


def reset_game():
    global mario_x, mario_y, jump, jump_count, obstacles, score, game_over
    mario_x, mario_y = 100, HEIGHT - 70 - ground_height
    jump = False
    jump_count = 10
    obstacles = []
    score = 0
    game_over = False


# Game Loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - ground_height, WIDTH, ground_height))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_EVENT and not game_over:
            obs_height = 40
            obs = pygame.Rect(WIDTH, HEIGHT - ground_height - obs_height, 40, obs_height)
            obstacles.append(obs)
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and mario_x > 0:
            mario_x -= mario_vel
        if keys[pygame.K_RIGHT] and mario_x < WIDTH - 50:
            mario_x += mario_vel
        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                mario_y -= (jump_count ** 2) * 0.3 * neg
                jump_count -= 1
            else:
                jump = False
                jump_count = 10

        # Animate Mario
        if jump:
            mario_img = mario_jump
        else:
            frame_delay += 1
            if frame_delay >= 10:  # controls animation speed
                frame_index = (frame_index + 1) % len(mario_run)
                frame_delay = 0
            mario_img = mario_run[frame_index]

        # Draw Mario
        screen.blit(mario_img, (mario_x, mario_y))

        # Obstacles
        for obs in obstacles[:]:
            obs.x -= 5
            pygame.draw.rect(screen, BROWN, obs)
            if obs.right < 0:
                obstacles.remove(obs)
                score += 1
            if obs.colliderect(pygame.Rect(mario_x, mario_y, mario_img.get_width(), mario_img.get_height())):
                game_over = True
    else:
        over_text = font.render("GAME OVER! Press R to Restart", True, BLACK)
        screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2))

    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
