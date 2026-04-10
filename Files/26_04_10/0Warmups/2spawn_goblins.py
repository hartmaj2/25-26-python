# TASK: Make goblins run after they are spawned

import pygame
import random

pygame.init()

clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

goblin = pygame.image.load("Files/26_04_10/Resources/goblin.png")

coords = []
speed = 5

def blit_goblins():
    for coord in coords:
        screen.blit(goblin,coord)

def move_goblins():
    for i in range(len(coords)):
        x,y = coords[i]
        coords[i] = (x+speed,y)
        # coords[i] = (x+random.randint(-2,7),y)
        

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: # exit button pressed
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # mouse button pressed 
            mouse = pygame.mouse.get_pos()
            coords.append(mouse)

    move_goblins()

    screen.fill("black")

    blit_goblins()

    clock.tick(60)
    pygame.display.update()


    