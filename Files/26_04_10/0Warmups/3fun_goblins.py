# TASK: Make goblins run after they are spawned

import pygame
import random
import math

pygame.init()

clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

goblin = pygame.image.load("Files/26_04_10/Resources/goblin.png")

coords = []
times = []
speed = 5

def blit_goblins():
    for i in range(len(coords)):
        coord = coords[i]
        time = pygame.time.get_ticks()
        t = time - times[i]
        new = (coord[0],coord[1] + math.sin(t * 0.3 * 2 * math.pi / 360 ) * 200)
        screen.blit(goblin,new)

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
            time = pygame.time.get_ticks()
            times.append(time)
            coords.append(mouse)

    move_goblins()

    screen.fill("black")

    blit_goblins()

    clock.tick(60)
    pygame.display.update()


    