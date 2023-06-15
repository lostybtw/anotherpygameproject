import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = location[0]
        self.rect.top = location[1]
        self.size = self.image.get_size()
    
    def render(self,win):
        win.blit(self.image, self.rect)

    def scale(self, scalar_x, scalar_y):
        size_x = self.size[0]
        size_y = self.size[1]
        self.image = pygame.transform.scale(self.image, (int(size_x * scalar_x), int(size_y * scalar_y)))
    
    def move(self, move_x, move_y):
        self.rect[0] += move_x
        self.rect[1] += move_y

