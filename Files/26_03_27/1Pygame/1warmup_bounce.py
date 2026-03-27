# Bounce the image from top to bottom

import pygame 

clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 600

pygame.init() 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

image = pygame.image.load("Files/26_03_20/Resources/anakin.webp").convert_alpha()
image = pygame.transform.scale_by(image,0.2)

y = 0
speed = 5

while True:
    for event in pygame.event.get():
 
        if event.type == 256:
            exit()
    
    screen.fill("black")
    screen.blit(image,(WIDTH//2,y))

    y += speed

    if y >= HEIGHT or y <= 0:
        speed *= -1

    pygame.display.flip()

    clock.tick(60)
            