import pygame

pygame.init() # do some magic

screen = pygame.display.set_mode((1200,600)) # create screen object

image = pygame.image.load("/Users/janhartman/25-26-python/Files/26_03_20/Resources/gandalf_bg.png")
image = pygame.transform.scale_by(image,0.5)

x = 100
y = 0

while True:
    for event in pygame.event.get(): # check if some events happened and loop through them
        print(event.type)
        if event.type == 771:
            x += 15
        if event.type == 256:
            exit()
    
    screen.blit(image,(x,y))
    pygame.display.update()