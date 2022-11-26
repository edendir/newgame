# Python program to try Pygame

import pygame, sys, random
from pygame.locals import *

pygame.init()

# Set display window
# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
display_surf = pygame.display.set_mode((400, 600))
display_surf.fill(WHITE)
screen_width = 400
screen_height = 600
pygame.display.set_caption("Game")

# Set Frames per second
FPS = pygame.time.Clock()
FPS.tick(60)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if(self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = player()
E1 = enemy()

# Game loop begins
while True:
    # Quit loop. Must be used in all games
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    display_surf.fill(WHITE)
    P1.draw(display_surf)
    E1.draw(display_surf)

    pygame.display.update()
    FPS.tick(60)
    
