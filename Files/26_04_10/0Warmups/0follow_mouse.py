# TASK: Make character follow mouse
# TASK2: Make character not make trace

import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

goblin = pygame.image.load("Files/26_04_10/Resources/goblin.png")


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    mouse = pygame.mouse.get_pos()

    # screen.fill("black")
    screen.blit(goblin,mouse)

    pygame.display.update()


    