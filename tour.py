import pygame


#création d'une classe Tour
class Tour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vie = 1
        self.image = pygame.image.load('res/rook.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect =self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 50