import pygame


#création d'une classe Tour
class Plateau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/plateau_light.jpg')
        self.rect =self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 0