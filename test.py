# ------------- INITIALISATION-------------------
import pygame
from pygame.locals import *
import board

pygame.init()  # essential for pygame
pygame.font.init()  # text

#variable de la pos de chaque carré de l'échiquier
pos=[
(30,35),(120,35),(210,35),(300,35),(390,35),(480,35),(570,35),(660,35),
(30,125),(120,125),(210,125),(300,125),(390,125),(480,125),(570,125),(660,125),
(30,215),(120,215),(210,215),(300,215),(390,215),(480,215),(570,215),(660,215),
(30,305),(120,305),(210,305),(300,305),(390,305),(480,305),(570,305),(660,305),
(30,395),(120,395),(210,395),(300,395),(390,395),(480,395),(570,395),(660,395),
(30,485),(120,485),(210,485),(300,485),(390,485),(480,485),(570,485),(660,485),
(30,575),(120,575),(210,575),(300,575),(390,575),(480,575),(570,575),(660,575),
(30,665),(120,665),(210,665),(300,665),(390,665),(480,665),(570,665),(660,665),
]







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

tour = pygame.image.load("res/rook.png")
tour = pygame.transform.scale(tour,(90,90))


#apparition des images
screen.blit(echiquier,(0,0))
screen.blit(pion,pos[9])
screen.blit(tour,pos[0])













pygame.display.flip()
running = 1
while running :
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = 0
            pygame.quit()

