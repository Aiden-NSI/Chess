import pygame


#création d'une classe Tour
class Tour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vie = 1
        self.image = pygame.image.load('res/rook.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect =self.image.get_rect()
        self.rect.x = 265
        self.rect.y = 15
