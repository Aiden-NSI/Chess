#ici nous allons code le jeu d'échec
# ------------- INITIALISATION-------------------
import pygame
import sound
import menus
from game import Game


pygame.init()  # essential for pygame
pygame.font.init()  # text



#-----VARIABLES------
pygame.display.set_caption('ChessNSI')
screen = pygame.display.set_mode((1280, 720))


# Création de la Police
policem = pygame.font.Font("res/Polices/MilkyNice-Clean.ttf", 45)
polices = pygame.font.Font("res/Polices/MilkyNice-Clean.ttf", 32)
policexs = pygame.font.Font("res/Polices/MilkyNice-Clean.ttf", 10)

#Definition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLEU = (0, 255, 255)
VIOLET = (51, 51, 102)

# importation des images
background = pygame.image.load("res/fondfull.jpg").convert()
background = pygame.transform.scale(background, (1280, 720))

#charger notre accueil
logo= pygame.image.load("res/logo.png")

#lancement de la sicmu
music = sound.Music()
music.play(load={})


#Charger notre jeu
game = Game()

running = True
while running:

    # appliquer l'arrière plan
    screen.blit(background, (0, 0))



    #vérifier si notre jeu a commencé ou non
    if game.is_playing:
        #déclancher les instruction de la partie
        game.update(screen)

    #vérifier si notre jeu n'a pas commencé
    else:
        #ajouter l'écran de bienvenue
        screen.blit(logo, (270, -100))
        # Boutons sur le Menu
        screen.blit(policexs.render("Version 0.16 Alpharoméo", True, VIOLET), (600, 700, 0, 40))
        screen.blit(policem.render("SinglePlayer", True, WHITE), (520, 310, 240, 40))
        screen.blit(polices.render("Preferences", True, VIOLET), (20, 680, 210, 40))
        screen.blit(polices.render("About", True, VIOLET), (1160, 680, 110, 40))

        #position de la souris
        x, y = pygame.mouse.get_pos()

        #si souris sur texte devient noir
        if (520, 310, 240, 40)[0] < x < sum((520, 310, 240, 40)[::2]) and (520, 310, 240, 40)[1] < y < sum((520, 310, 240, 40)[1::2]):
            screen.blit(policem.render("SinglePlayer", True, BLACK), (520, 310, 240, 40)[:2])
        if (20, 680, 210, 40)[0] < x < sum((20, 680, 210, 40)[::2]) and (20, 680, 210, 40)[1] < y < sum((20, 680, 210, 40)[1::2]):
            screen.blit(polices.render("Préférences", True, WHITE), (20, 680, 210, 40)[:2])
        if (1160, 680, 110, 40)[0] < x < sum((1160, 680, 110, 40)[::2]) and (1160, 680, 110, 40)[1] < y < sum((1160, 680, 110, 40)[1::2]):
            screen.blit(polices.render("About", True, WHITE), (1160, 680, 110, 40)[:2])
        if (230, 100, 0, 40)[0] < x < sum((230, 100, 0, 40)[::2]) and (230, 100, 0, 40)[1] < y < sum((230, 100 , 0, 40)[1::2]):
            screen.blit(policexs.render("Version Alpharoméo", True, BLACK), (230, 100, 0, 40)[:2])



    # mettre a jour l'ecran
    pygame.display.flip()


    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
         #que l'évenement est appuyer sur un bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (680, 440, 110, 40)[0] < x < sum((1160, 680, 110, 40)[::2]) and (1160, 680, 110, 40)[1] < y < sum((1160, 680, 110, 40)[1::2]):
                run = menus.aboutmenu(screen)

            elif (20, 680, 210, 40)[0] < x < sum((20, 680, 210, 40)[::2]) and (20, 680, 210, 40)[1] < y < sum((20, 680, 210, 40)[1::2]):
                run = menus.prefmenu(screen)
            #savoir si la souris est en collision avec notre bouton de démarage

            elif (520, 310, 240, 40)[0] < x < sum((520, 310, 240, 40)[::2]) and (520, 310, 240, 40)[1] < y < sum((520, 310, 240, 40)[1::2]):
                #mode le jeu en mode lancé
                game.is_playing = True


music.stop()
pygame.quit()
print("fermeture du jeu")

