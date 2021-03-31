# ------------- INITIALISATION-------------------
import pygame
from pygame.locals import *
import board

pygame.init()  # essential for pygame
pygame.font.init()  # text

#variable de la pos de chaque carré de l'échiquier








# DEFINITION DE LA FENETRE
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('ChessNSI')

# Création de la Police (pas la prison)
policem = pygame.font.SysFont("monospace", 38)
polices = pygame.font.SysFont("monospace", 20)

#Definition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#images de l'échiquier
echiquier = pygame.image.load("res/echiquier.jpg").convert()
pion = pygame.image.load("res/pion.png")
pion = pygame.transform.scale(pion,(90,90))


#apparition des images
screen.blit(echiquier,(0,0))
screen.blit(pion,(30,35))
screen.blit(pion,(120,125))


pygame.display.flip()
running = 1
while running :
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = 0
            pygame.quit()
