import pygame

win = pygame.display.set_mode((800,800))
run = True
while run:
    pygame.time.delay(100)
    pygame.draw.circle(win, (255, 0, 0), (400, 400), 20)
    pygame.display.update()