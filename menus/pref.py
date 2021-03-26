#importation des modules nécessaires
import pygame
import pygame.gfxdraw
import os.path
pygame.init()  # essential for pygame
pygame.font.init()  # text

#créations des variables nécessaires
background = pygame.image.load(os.path.join("res","menu.jpg"))
BACK = pygame.image.load(os.path.join("res","back.png"))
large = pygame.font.SysFont("monospace", 38)
vsmall = pygame.font.SysFont("monospace", 17)
WHITE = (255, 255, 255)

# Cette fonction crée des rectangle avec des angles arrondis
def rounded_rect(surf, color, rect, radius=10, border=2, incolor=(0, 0, 0)):
    if min(rect[2], rect[3]) > 2 * (radius + border):
        _filled_rounded_rect(surf, color, rect, radius)
        rect = (rect[0] + border, rect[1] + border,
                rect[2] - 2*border, rect[3] - 2*border)
        _filled_rounded_rect(surf, incolor, rect, radius)


class PREF:
    HEAD = large.render("Preferences", True, WHITE)

    SOUNDS = large.render("Sounds", True, WHITE)
    FLIP = large.render("Flip screen", True, WHITE)
    CLOCK = large.render("Show Clock", True, WHITE)
    SLIDESHOW = large.render("Slideshow", True, WHITE)
    MOVE = large.render("Moves", True, WHITE)
    UNDO = large.render("Allow undo", True, WHITE)

    COLON = large.render(":", True, WHITE)

    TRUE = large.render("True", True, WHITE)
    FALSE = large.render("False", True, WHITE)

    SOUNDS_H = (
        large.render("Play different sounds", True, WHITE),
        large.render("and music", True, WHITE),
    )
    FLIP_H = (
        large.render("This flips the screen", True, WHITE),
        large.render("after each move", True, WHITE),
    )
    CLOCK_H = (
        large.render("Show a clock in chess", True, WHITE),
        large.render("when timer is disabled", True, WHITE),
    )
    SLIDESHOW_H = (
        large.render("This shows a slide of", True, WHITE),
        large.render("backgrounds on screen", True, WHITE),
    )
    MOVE_H = (
        large.render("This shows all the legal", True, WHITE),
        large.render("moves of a selected piece", True, WHITE),
    )
    UNDO_H = (
        large.render("This allowes undo if", True, WHITE),
        large.render("set to be true", True, WHITE),
    )

    BSAVE = large.render("Save", True, WHITE)
    TIP = large.render("TIP: Hover the mouse over the feature", True, WHITE)
    TIP2 = large.render("name to know more about it.", True, WHITE)

    PROMPT = (
        large.render("Are you sure you want to leave?", True, WHITE),
        large.render("Any changes will not be saved.", True, WHITE),
    )

    YES = vsmall.render("YES", True, WHITE)
    NO = vsmall.render("NO", True, WHITE)
