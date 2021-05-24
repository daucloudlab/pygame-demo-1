import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))

player = pygame.Surface((40, 40))
x_p = 0
y_p = 0

done = False

while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            y_p += 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            y_p -= 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            x_p -= 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            x_p += 1


    screen.fill((0, 255, 0))
    screen.blit(player, (x_p, y_p))

    window.blit(screen, (0,0))
    pygame.display.update()

pygame.quit()