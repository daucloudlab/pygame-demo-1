import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))

done = False

while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    screen.fill((0, 255, 0))
    window.blit(screen, (0,0))
    pygame.display.update()

pygame.quit()