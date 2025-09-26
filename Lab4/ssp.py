import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game with Spiders")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

# ----------------------------
# Load Sprites with Auto Chroma Key
# ----------------------------
def load_sprite(path):
    image = pygame.image.load(path).convert()
    colorkey = image.get_at((0, 0))  # top-left pixel color ko transparent treat karega
    image.set_colorkey(colorkey)
    return image

# Mario sprites
mario_run = [
    load_sprite("Lab4/images/run1.bmp"),
    load_sprite("Lab4/images/run2.bmp"),
    load_sprite("Lab4/images/run3.bmp"),
]
mario_jump = load_sprite("Lab4/images/jump.bmp")

# Scale sprites for Mario
mario_run = [pygame.transform.scale(img, (50, 70)) for img in mario_run]
mario_jump = pygame.transform.scale(mario_jump, (50, 70))

# Spider sprites
spider_img = load_sprite("Lab4/images/spider.bmp")
splash_img = load_sprite("Lab4/images/splash.bmp")
spider_img = pygame.transform.scale(spider_img, (60, 60))
splash_img = pygame.transform.scale(splash_img, (60, 60))

# Beautified Colors
SKY_BLUE = (120, 180, 255)     # soft sky blue
GROUND_GREEN = (20, 120, 20)   # dark green grass
OBSTACLE_BROWN = (120, 80, 40) # warm brown
BULLET_BROWN = (150, 75, 0)    # pentagon bullet
TEXT_WHITE = (255, 255, 255)

# ----------------------------
# Mario setup
# ----------------------------
mario_x, mario_y = 100, HEIGHT - 70 - 40  # Mario ki initial position (ground ke upar)
mario_vel = 5                             # Mario ki horizontal speed
jump = False                              # jump flag
jump_count = 11                           # jump strength / height
ground_height = 40                        # ground rectangle ki height

# Animation variables
frame_index = 0
frame_delay = 0

# ----------------------------
# Obstacles setup
# ----------------------------
obstacles = []
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 2000)  # har 2 sec me naya obstacle spawn hoga

# ----------------------------
# Bullets setup
# ----------------------------
bullets = []

# ----------------------------
# Spiders setup
# ----------------------------
spiders = []
SPIDER_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPIDER_EVENT, 3000)  # har 3 sec me 2 spiders spawn hongi

# ----------------------------
# Score & Game State
# ----------------------------
font = pygame.font.SysFont("Arial", 30)
score = 0
game_over = False

# ----------------------------
# Reset function for restart
# ----------------------------
def reset_game():
    global mario_x, mario_y, jump, jump_count, obstacles, bullets, spiders, score, game_over
    mario_x, mario_y = 100, HEIGHT - 70 - ground_height
    jump = False
    jump_count = 11
    obstacles = []
    bullets = []
    spiders = []
    score = 0
    game_over = False

# ----------------------------
# Main Game Loop
# ----------------------------
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)

    # Draw ground
    pygame.draw.rect(screen, GROUND_GREEN, (0, HEIGHT - ground_height, WIDTH, ground_height))

    # ----------------------------
    # Event Handling
    # ----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Spawn obstacles
        if event.type == SPAWN_EVENT and not game_over:
            obs_height = 28
            obs = pygame.Rect(WIDTH, HEIGHT - ground_height - obs_height, 28, obs_height)
            obstacles.append(obs)

        # Spawn spiders
        if event.type == SPIDER_EVENT and not game_over:
            for _ in range(2):  # ek sath 2 spiders
                sx = random.randint(50, WIDTH - 100)
                sy = random.randint(30, 120)  # sirf upar hi rahengi
                spiders.append({
                    "rect": pygame.Rect(sx, sy, 60, 60),
                    "zigzag_x": random.choice([-1, 1]),
                    "zigzag_y": random.choice([-1, 1]),
                    "alive": True,
                    "splash_timer": 0
                })

        # Restart on game over
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

        # Fire bullet with "F" key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and not game_over:
                bullet = {"x": mario_x + 25, "y": mario_y, "speed": 7}
                bullets.append(bullet)

    # ----------------------------
    # Game Logic (when not over)
    # ----------------------------
    if not game_over:
        # Mario movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and mario_x > 0:
            mario_x -= mario_vel
        if keys[pygame.K_RIGHT] and mario_x < WIDTH - 50:
            mario_x += mario_vel
        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            if jump_count >= -11:
                neg = 1
                if jump_count < 0:
                    neg = -1
                mario_y -= (jump_count ** 2) * 0.3 * neg
                jump_count -= 1
            else:
                jump = False
                jump_count = 11

        # Mario animation (run/jump)
        if jump:
            mario_img = mario_jump
        else:
            frame_delay += 1
            if frame_delay >= 10:
                frame_index = (frame_index + 1) % len(mario_run)
                frame_delay = 0
            mario_img = mario_run[frame_index]

        # Draw Mario
        screen.blit(mario_img, (mario_x, mario_y))

        # Obstacles movement + collision
        for obs in obstacles[:]:
            obs.x -= 5
            pygame.draw.rect(screen, OBSTACLE_BROWN, obs)
            if obs.right < 0:
                obstacles.remove(obs)
                score += 1
            if obs.colliderect(pygame.Rect(mario_x, mario_y, mario_img.get_width(), mario_img.get_height())):
                game_over = True

        # Bullets movement
        for bullet in bullets[:]:
            bullet["y"] -= bullet["speed"]
            # Draw pentagon bullet
            points = [
                (bullet["x"], bullet["y"]),
                (bullet["x"] - 6, bullet["y"] + 10),
                (bullet["x"] - 3, bullet["y"] + 20),
                (bullet["x"] + 3, bullet["y"] + 20),
                (bullet["x"] + 6, bullet["y"] + 10),
            ]
            pygame.draw.polygon(screen, BULLET_BROWN, points)
            if bullet["y"] < 0:
                bullets.remove(bullet)

        # Spiders movement + collision
        for spider in spiders[:]:
            if spider["alive"]:
                # Zigzag movement
                spider["rect"].x += spider["zigzag_x"] * 2
                spider["rect"].y += spider["zigzag_y"] * 1

                # Boundaries for zigzag
                if spider["rect"].left < 20 or spider["rect"].right > WIDTH - 20:
                    spider["zigzag_x"] *= -1
                if spider["rect"].top < 20 or spider["rect"].top > 120:
                    spider["zigzag_y"] *= -1

                # Draw spider
                screen.blit(spider_img, spider["rect"])

                # Bullet collision with spider
                for bullet in bullets[:]:
                    if spider["rect"].collidepoint(bullet["x"], bullet["y"]):
                        spider["alive"] = False
                        spider["splash_timer"] = pygame.time.get_ticks()
                        bullets.remove(bullet)
            else:
                # Show splash for 0.5 sec
                screen.blit(splash_img, spider["rect"])
                if pygame.time.get_ticks() - spider["splash_timer"] > 500:
                    spiders.remove(spider)

        # Spider-to-spider collision (NEW)
        for i in range(len(spiders)):
            for j in range(i + 1, len(spiders)):
                s1 = spiders[i]
                s2 = spiders[j]
                if s1["alive"] and s2["alive"] and s1["rect"].colliderect(s2["rect"]):
                    s1["alive"] = False
                    s2["alive"] = False
                    s1["splash_timer"] = pygame.time.get_ticks()
                    s2["splash_timer"] = pygame.time.get_ticks()

    # ----------------------------
    # Game Over Screen
    # ----------------------------
    else:
        over_text = font.render("GAME OVER! Press R to Restart", True, TEXT_WHITE)
        screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2))

    # ----------------------------
    # Score Display (no shadow)
    # ----------------------------
    score_surface = font.render(f"Score: {score}", True, TEXT_WHITE)
    screen.blit(score_surface, (10, 10))

    # Update screen
    pygame.display.update()
