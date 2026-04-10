# Co dělají jednotlivé části kódu? Co by se stalo, kdybychom je odstranili?

import pygame 

pygame.init() 
screen = pygame.display.set_mode((1200,600)) # nastaví rozměr obrazovky

image = pygame.image.load("Files/26_03_20/Resources/anakin.webp") # nahraje obrázek do image

x = 0

while True:
    for event in pygame.event.get():
        if event.type == 256:
            exit()
    
    screen.blit(image,(x,0)) # tento blit vyblije obrázek image na pozici (x,0)
    screen.fill("black") # překryje celou obrazovku černou barvou

    x += 1

    pygame.display.update() # propíše všechny vizuální změny na obrazovku 
            