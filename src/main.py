import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        pygame.display.update()
        clock.tick(60)
