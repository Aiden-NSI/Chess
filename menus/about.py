'''
This file is a part of My-PyChess application.
In this file, we manage the about menu which is called when user clicks
about button on main menu.
'''

import pygame
import pygame.gfxdraw
import os.path
pygame.init()  # essential for pygame
pygame.font.init()  # text


large = pygame.font.SysFont("monospace", 50)
vsmall = pygame.font.SysFont("monospace", 17)
WHITE = (255, 255, 255)

# This function needs to be called when user wants to draw a rounded rect
def rounded_rect(surf, color, rect, radius=10, border=2, incolor=(0, 0, 0)):
    if min(rect[2], rect[3]) > 2 * (radius + border):
        _filled_rounded_rect(surf, color, rect, radius)
        rect = (rect[0] + border, rect[1] + border,
                rect[2] - 2*border, rect[3] - 2*border)
        _filled_rounded_rect(surf, incolor, rect, radius)

def _filled_rounded_rect(surf, color, rect, r):
    for x, y in [(rect[0] + r, rect[1] + r),
                 (rect[0] + rect[2] - r - 1, rect[1] + r),
                 (rect[0] + r, rect[1] + rect[3] - r - 1),
                 (rect[0] + rect[2] - r - 1, rect[1] + rect[3] - r - 1)]:
        pygame.gfxdraw.aacircle(surf, x, y, r, color)
        pygame.gfxdraw.filled_circle(surf, x, y, r, color)

    pygame.draw.rect(surf, color, (rect[0] + r, rect[1], rect[2] - 2*r, rect[3]))
    pygame.draw.rect(surf, color, (rect[0], rect[1] + r, rect[2], rect[3] - 2*r))


class ABOUT:
    HEAD = large.render("About PyChess", True, WHITE)

    with open(os.path.join("res", "about.txt"), "r") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

BACK = pygame.image.load(os.path.join("res","back.png"))

# This shows the screen
def showScreen(screen):
    screen.fill((0, 0, 0))
    rounded_rect(screen, (255, 255, 255), (70, 10, 360, 60), 16, 4)
    rounded_rect(screen, (255, 255, 255), (10, 80, 480, 410), 10, 4)

    screen.blit(ABOUT.HEAD, (74, 12))
    for cnt, i in enumerate(ABOUT.TEXT):
        screen.blit(i, (20, 90 + cnt*18))

    screen.blit(BACK, (460, 0))
    pygame.display.update()

# This is the main function, called from main menu
def main(screen):
    showScreen(screen)
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    return 1
