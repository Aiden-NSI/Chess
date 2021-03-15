#ici nous allons code le jeu d'échec
# ------------- INITIALISATION-------------------
import pygame
import sys

pygame.init()  # essential for pygame
pygame.font.init()  # text

# DEFINITION DE LA FENETRE
screen = pygame.display.set_mode((800, 60 * 8))
pygame.display.set_caption('ChessNSI')

# importation des images
background = pygame.image.load("assets/menu.jpg").convert()

running = True

# boucle tant que condition est vrai
while running :

    # appliquer l'arrière plan 
    screen.blit(background, (0, 0))

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
