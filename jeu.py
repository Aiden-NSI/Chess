# ------------- INITIALISATION-------------------
import pygame, sys, os, math
sys.dont_write_bytecode = True
from piecelogique import *

pygame.init()

#-------IMAGES-----------
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

#-----VARIABLES------
tilew, tileh = 45, 45
height = tileh * 8
width = tilew * 8

pygame.display.set_icon(icon)
pygame.display.set_caption("NSIChess")
screen = pygame.display.set_mode((360, 400))

selected = False
pieces = []
wmoves, bmoves = [], []
moves = [wmoves, bmoves]
playerIsWhite = True

black = (51, 51, 102)
White = (255, 225, 225)

class Piece():
	def __init__(self,name,color,startpos):
		global pieces
		self.name = name
		self.color = color
		self.pos = startpos
		self.image = pieceimages[color+name]
		self.hasMoved = False
		self.beingAttacked = False
		board[startpos[0]][startpos[1]] = self
		pieces.append(self)
	def move(self,pos):
		global selected
		global moves
		if playerIsWhite: #fonctionne lorsque le joueur noir se déplace
			moves[1].append((self.name, (self.pos, pos)))
		else: #vice-versa
			moves[0].append((self.name, (self.pos, pos)))
		board[self.pos[0]][self.pos[1]] = VIDE
		self.pos = pos
		board[self.pos[0]][self.pos[1]] = self
		self.hasMoved = True
	def select(self):
		global selected
		selected = self.pos

#mise en place des pions sur l'echequier
for i in range(0, 8):
	Piece('Pawn', 'W', (i, 6))
	Piece('Pawn', 'B', (i, 1))

Piece('Rook',   'W', (0, 7))
Piece('Rook',   'W', (7, 7))
Piece('Knight', 'W', (1, 7))
Piece('Knight', 'W', (6, 7))
Piece('Bishop', 'W', (2, 7))
Piece('Bishop', 'W', (5, 7))
Piece('Queen',  'W', (3, 7))
Piece('King',   'W', (4, 7))
Piece('Rook',   'B', (0, 0))
Piece('Rook',   'B', (7, 0))
Piece('Knight', 'B', (1, 0))
Piece('Knight', 'B', (6, 0))
Piece('Bishop', 'B', (2, 0))
Piece('Bishop', 'B', (5, 0))
Piece('Queen',  'B', (3, 0))
Piece('King',   'B', (4, 0))

font = pygame.font.SysFont("monospace", 20)
def updateText():
	global turnindic, piecesleft
	turnindic = font.render("Turn: "+("white" if playerIsWhite == True else "black"), True, (139, 125, 107), (0, 0, 0, 0))
updateText()

def contains(pos):
	boardpos = board[pos[0]][pos[1]]
	if boardpos == 0:
		return 0 #Renvoie 0 si la position spécifiée ne contient pas de pièce
	if playerIsWhite == True:
		return 1 if boardpos.color == 'W' else 2
	else:
		return 1 if boardpos.color == 'B' else 2

#Renvoie la valeur de pixel en haut à gauche de la position de la grille
def pixelpos(pos): return (pos[0] * tilew, pos[1] * tileh)

#Dessine le plateau en fonction de la valeur
def drawPieces():
	global selected
	for i in range(len(board)):
		row = board[i]
		for i2 in range(len(row)):
			piece = row[i2]

			if selected != False:
				if pieceCanMove(board[selected[0]][selected[1]], (i, i2), False) and selected != (i, i2) and contains((i, i2)) != 1:
					screen.blit(highlightimg, pixelpos((i, i2)))

					(mouseX, mouseY) = pygame.mouse.get_pos()
					curRow = int(math.ceil(mouseX/tilew) - 1)
					curCol = int(math.ceil(mouseY/tileh) - 1)
					if (curRow, curCol) == (i, i2):
						screen.blit(hhoverimg, pixelpos((i, i2)))
					if contains((i, i2)) == 2:
						screen.blit(attackimg, pixelpos((i, i2)))
				else:
					pass
			if piece != VIDE:
				screen.blit(piece.image, (i*45, i2*45))

def getAttacks():
	for piece in pieces:
		piece.beingAttacked = False
		for piece2 in pieces:
			enemyname = "B" if piece.color == 'W' else "W"
			if piece2 != piece and piece2.color == enemyname and pieceCanMove(piece2, piece.pos, False):
				piece.beingAttacked = True

clock = pygame.time.Clock()

while True:
	clock.tick(30)
	pygame.draw.rect(screen, black, [0, 0, width, height])
	for row in range(4):
		for col in range(4):
			pygame.draw.rect(screen, White, [row*90, col*90, tilew, tileh])
			pygame.draw.rect(screen, White, [row*90+tilew, col*90+tileh, tilew, tileh])

	drawPieces()

	screen.blit(turnindic, (0, height+10))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
			elif event.key == pygame.K_r:
				pass
		elif event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] <= height:
			(mouseX, mouseY) = pygame.mouse.get_pos()
			curCol = int(math.ceil(mouseY/tileh) - 1)
			curRow = int(math.ceil(mouseX/tilew) - 1)

			if selected == False:
				if contains((curRow, curCol)) == 1:
					board[curRow][curCol].select()
			else:
				if contains((curRow, curCol)) != 1:
					if pieceCanMove(board[selected[0]][selected[1]], (curRow, curCol), True):
						playerIsWhite = not playerIsWhite
						updateText()
						board[selected[0]][selected[1]].move((curRow, curCol))
						selected = False
						getAttacks()
				else:
					board[curRow][curCol].select()

	pygame.display.update()

