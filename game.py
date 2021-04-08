import pygame
from tour import Tour
from plateau import Plateau

#Création d'une classe Game
class Game:

    def __init__(self):

        #définir si le jeu a commencé ou non
        self.is_playing = False

        #générer notre plateau
        self.plateau = Plateau()

        #générer notre Tour
        self.tour = Tour()




    def update(self, screen):
        #appliquer l'image de mon plateau
        screen.blit(self.plateau.image, self.plateau.rect)
        # appliquer l'image de mon joueur
        screen.blit(self.tour.image, self.tour.rect)
