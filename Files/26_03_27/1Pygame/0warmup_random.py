# Spawn image on random location when space pressed

import pygame 
import random

pygame.init() 
screen = pygame.display.set_mode((1200,600)) # nastaví rozměr obrazovky

image = pygame.image.load("Files/26_03_20/Resources/anakin.webp") # nahraje obrázek do image
image = pygame.transform.scale_by(image,0.2)

while True:
    for event in pygame.event.get():
        if event.type == 768:
            print(event.dict)
            if event.dict["unicode"] == " ":
                x = random.randint(0,1000)
                y = random.randint(0,500)
                screen.blit(image,(x,y))
        if event.type == 256:
            exit()
    

    pygame.display.flip() # propíše všechny vizuální změny na obrazovku 
            