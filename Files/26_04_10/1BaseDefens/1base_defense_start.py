import pygame
import sys
import os
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Base Defense")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Hero
hero_img = pygame.image.load("Files/26_04_10/Resources/mage.png")
hero_rect = hero_img.get_rect()
hero_speed = 5
hero_rect.center = (50,HEIGHT//2)

# Enemies
enemy_next_spawn = time.time()

enemy_img = pygame.image.load("Files/26_04_10/Resources/skeleton.png")
enemy_img = pygame.transform.flip(enemy_img,flip_x=True,flip_y=False)

enemy_rects : list[pygame.Rect] = []
enemy_speed = 3


while True:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # KEYS & PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        hero_rect.y -= hero_speed
    if keys[pygame.K_s]:
        hero_rect.y += hero_speed

    # SPAWNING ENEMIES
    if time.time() > enemy_next_spawn:
        en_rect = enemy_img.get_rect()
        en_rect.midright = (WIDTH,random.randint(50,HEIGHT-50))
        enemy_rects.append(en_rect)
        enemy_next_spawn = time.time() + 2
        # enemy_next_spawn += random.randint(2,4)

    # MOVING ENEMIES
    for enemy in enemy_rects:
        enemy.x -= enemy_speed


    # BLITTING
    screen.fill((186, 220, 255))  # Pastel blue background
    screen.blit(hero_img,hero_rect)
    for enemy in enemy_rects:
        screen.blit(enemy_img,enemy)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)




# FOR TESTING
# -----------

# pygame.draw.rect(screen,"red",hero_rect,1) # test rectangle

# os.system("clear")
# print("".join(["1" if key else "0" for key in keys]))