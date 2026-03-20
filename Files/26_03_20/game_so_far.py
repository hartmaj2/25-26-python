import pygame # naimportuj pygame

clock = pygame.time.Clock()

pygame.init() # proveď černou magii vol. 1
screen = pygame.display.set_mode((1200,600)) # vytvoř obrazovku 600x400

image = pygame.image.load("Files/26_03_20/Resources/anakin.webp")
image = pygame.transform.scale_by(image,0.05)

x = 0

while True:
    for event in pygame.event.get(): # černá magie vol. 2
        if event.type == 768:
            if event.dict["unicode"] == "d":
                x += 10
            if event.dict["unicode"] == "a":
                x -= 10
 
        if event.type == 256:
            exit()
    
    screen.fill("black")
    screen.blit(image,(x,0))
    pygame.display.flip()

    clock.tick(60)
            