#ici nous allons code le jeu d'échec
# ------------- INITIALISATION-------------------
import pygame
import sys

pygame.init()  # essential for pygame
pygame.font.init()  # text

# DEFINITION DE LA FENETRE
screen = pygame.display.set_mode((800, 60 * 8))
pygame.display.set_caption('ChessNSI')
