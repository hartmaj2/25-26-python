import pygame

pygame.init() # do some magic

screen = pygame.display.set_mode((900,600)) # create screen object

image = pygame.image.load('Files/26_03_20/Resources/gandalf_bg.png') # create image object
image = pygame.transform.scale_by(image,0.5) # make image smaller

screen.blit(image, (450, 300)) # draw the character on the screen (just on the background)
pygame.display.flip() # show all changes since last flip

while True:
    for event in pygame.event.get(): # check if some events happened and loop through them
        if event.type == 256:
            exit()