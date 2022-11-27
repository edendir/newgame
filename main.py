# Python program to try Pygame

import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Set display window

# Set Frames per second
FramesPerSec = pygame.time.Clock()
FPS = 60

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set other Variables
screen_width = 400
screen_height = 600
SPEED = 5
SCORE = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, BLACK)
retry = font_small.render("Press SPACE to retry", False, BLACK)

# Set display
background = pygame.image.load("venv/AnimatedStreet.png")
display_surf = pygame.display.set_mode((400, 600))
display_surf.fill(WHITE)
pygame.display.set_caption("Game")


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("venv/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP, K_w]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN, K_s]:
        # self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT, K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT, K_d]:
                self.rect.move_ip(5, 0)


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("venv/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)


# Setup Sprites
P1 = player()

E1 = enemy()

# Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop begins
while True:
    # Cycle through all events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        # Quit loop. Must be used in all games
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surf.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    display_surf.blit(scores, (10, 10))

    # Move and re-draw sprites
    for entity in all_sprites:
        display_surf.blit(entity.image, entity.rect)
        entity.move()

    # If Player and Enemy collide:
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('venv/crash.wav').play()
        time.sleep(0.5)
        display_surf.fill(RED)
        display_surf.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        display_surf.blit(retry, (30, 250))
        pygame.display.update()
        if pygame.key.get_pressed()

    pygame.display.update()
    FramesPerSec.tick(60)
