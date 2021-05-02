import pygame
#charge les images et autres.
highlightimg = pygame.image.load("res/pieces/highlight.png")
hhoverimg = pygame.image.load("res/pieces/hhover.png")
attackimg = pygame.image.load("res/pieces/attack.png")
icon = pygame.image.load('res/chess_icon.jpg')

pieceimages = {}
pieceimages["WPawn"] = pygame.image.load("res/pieces/wpawn.png")
pieceimages["WRook"] = pygame.image.load("res/pieces/wrook.png")
pieceimages["WKnight"] = pygame.image.load("res/pieces/wknight.png")
pieceimages["WBishop"] = pygame.image.load("res/pieces/wbishop.png")
pieceimages["WQueen"] = pygame.image.load("res/pieces/wqueen.png")
pieceimages["WKing"] = pygame.image.load("res/pieces/wking.png")

pieceimages["BPawn"] = pygame.image.load("res/pieces/bpawn.png")
pieceimages["BRook"] = pygame.image.load("res/pieces/brook.png")
pieceimages["BKnight"] = pygame.image.load("res/pieces/bknight.png")
pieceimages["BBishop"] = pygame.image.load("res/pieces/bbishop.png")
pieceimages["BQueen"] = pygame.image.load("res/pieces/bqueen.png")
pieceimages["BKing"] = pygame.image.load("res/pieces/bking.png")
