import pygame

pygame.init() # do some magic

screen = pygame.display.set_mode((900,600)) # create screen object

image = pygame.image.load('Files/26_03_20/Resources/gandalf_bg.png') # create image object
image = pygame.transform.scale_by(image,0.5) # make image smaller

gandalf_rect = image.get_rect() # get frame that fits the image which we can move and detect collisions
gandalf_rect.center = (450,300)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): # check if some events happened and loop through them
        if event.type == 256:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] == True:
        gandalf_rect.y -= 5
    if keys[pygame.K_s] == True:
        gandalf_rect.y += 5
    if keys[pygame.K_a] == True:
        gandalf_rect.x -= 5
    if keys[pygame.K_d] == True:
        gandalf_rect.x += 5

    screen.fill("black")
    screen.blit(image, gandalf_rect) # draw the character on the screen (just on the background)
    pygame.display.flip() # show all changes since last flip
    
    clock.tick(60)

    