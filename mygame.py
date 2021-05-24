import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))

player = pygame.Surface((40, 40))
zet = pygame.Surface((40, 40))
arrow = pygame.Surface((20, 40))

x_a = 1000
y_a = 1000

x_z = 0
y_z = 0

x_p = 0
y_p = 360

strike = False
right = True
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
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                x_a = x_p
                y_a = y_p - 40

    if strike:
        y_a -= 0.5
        if y_a < 0:
            strike = False
            x_a = 1000
            y_a = 1000 

    if right:
        x_z += 1
        if x_z > 400:
            x_z -= 1
            right = False
    else:
        x_z -= 1
        if x_z < 0:
            x_z += 1
            right = True

    screen.fill((0, 255, 0))
    screen.blit(player, (x_p, y_p))
    screen.blit(zet, (x_z, y_z))
    screen.blit(arrow, (x_a, y_a))
    window.blit(screen, (0,0))
    pygame.display.update()

pygame.quit()