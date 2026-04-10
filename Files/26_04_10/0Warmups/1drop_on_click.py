# TASK: Make character printed to the screen when we click

import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

goblin = pygame.image.load("Files/26_04_10/Resources/goblin.png")


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: # exit button pressed
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # mouse button pressed 
            mouse = pygame.mouse.get_pos()
            screen.blit(goblin,mouse)

    pygame.display.update()


    