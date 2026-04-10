import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

image = pygame.image.load("Files/26_04_10/Resources/skeleton.png")
# image = pygame.transform.scale_by()



while True:

    seznam = pygame.event.get()

    for ovoce in seznam:
        print(ovoce)
        if ovoce.type == pygame.QUIT:
            exit()


    # for event in pygame.event.get():
    #     # print(event)
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         pos = pygame.mouse.get_pos()
    #         screen.blit(image,pos)

    # screen.fill("black")
    

    pygame.display.update()

