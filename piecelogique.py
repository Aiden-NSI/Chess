import math

pieceLogique = {}
BlancEnEchec = False
NoirEnEchec = False
VIDE = 0

board = [
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
]

def isFree(pos):
	lig, col = pos[0], pos[1]
	if ((lig < 0) or (col < 0) or (lig > len(board)-1) or (col > len(board)-1)): return
	return board[lig][col] == VIDE

def colLogic(piece, newpos):
	squareamountx = abs(piece.pos[0]-newpos[0])
	squareamounty = abs(piece.pos[1]-newpos[1])
	if piece.name == 'Knight' or piece.name == 'King':
		return True
	elif squareamountx == 0:
		for i in range(1, squareamounty):
			mod = -i if (piece.pos[1] > newpos[1]) else i
			testpos = (piece.pos[0], piece.pos[1]+mod)
			if not isFree(testpos):
				return False
	elif squareamounty == 0:
		for i in range(1, squareamountx):
			mod = -i if (piece.pos[0] > newpos[0]) else i
			testpos = (piece.pos[0]+mod, piece.pos[1])
			if not isFree(testpos):
				return False
	else:
		squareamount = abs(piece.pos[0]-newpos[0])
		for i in range(1, squareamount):
			mod = -i if (piece.pos[0] > newpos[0]) else i
			mod2 = -i if (piece.pos[1] > newpos[1]) else i
			testpos = (piece.pos[0]+mod, piece.pos[1]+mod2)
			if not isFree(testpos):
				return False
		return True
	return True

def rookLogic(piece, newpos):
	return ((piece.pos[0] == newpos[0]) or (piece.pos[1] == newpos[1]))
pieceLogique['Rook']=rookLogic

def knightLogic(piece, newpos):
	diffx = abs(piece.pos[0]-newpos[0])
	diffy = abs(piece.pos[1]-newpos[1])
	return (diffx <= 2 and diffy <= 2 and diffx != 0 and diffy != 0 and diffx != diffy)
pieceLogique['Knight']=knightLogic

def bishopLogic(piece, newpos):
	return (abs(piece.pos[1]-newpos[1]) == abs(piece.pos[0]-newpos[0]))
pieceLogique['Bishop']=bishopLogic

def queenLogic(piece, newpos):
	return (rookLogic(piece, newpos) or bishopLogic(piece, newpos))
pieceLogique['Queen']=queenLogic

def kingLogic(piece, newpos):
	if (piece.pos[1]-newpos[1] == 0 and (abs(piece.pos[0]-newpos[0])>1 and abs(piece.pos[0]-newpos[0]<4)) and piece.hasMoved == False):
		xdir = True if piece.pos[0]-newpos[0] > 0  else False #xdir vaut True si la pièce se déplace vers la gauche, False si elle se déplace vers la droite
		castlerook = board[0][piece.pos[1]] if xdir == True else board[7][piece.pos[1]]
		if xdir == True and castlerook != 0 and (abs(piece.pos[0]-newpos[0]) == 2 and castlerook.hasMoved == False):
			if rc:
				castlerook.move((3, piece.pos[1]))
			return True
		elif xdir == False and castlerook != 0 and (abs(piece.pos[0]-newpos[0]) == 2 and castlerook.hasMoved == False):
			if rc:
				castlerook.move((5, piece.pos[1]))
			return True
	else:
		return (queenLogic(piece, newpos) and (abs(piece.pos[0]-newpos[0]) <= 1 and abs(piece.pos[1]-newpos[1]) <= 1))
pieceLogique['King']=kingLogic

def pawnLogic(piece, newpos):
	squaresallowed = piece.hasMoved and 1 or 2 #piece.hasmoved et 1 ou 2
	movedh = (piece.pos[0] - newpos[0]) if piece.color == 'W' else (newpos[0] - piece.pos[0]) #Je ne peux pas utiliser les abdos comme nous le ferions autrement parce que les pions ne peuvent pas reculer
	movedv = (piece.pos[1] - newpos[1]) if piece.color == 'W' else (newpos[1] - piece.pos[1])
	if board[newpos[0]][newpos[1]] != 0 and (bishopLogic(piece, newpos) and (abs(movedh) == 1 and movedv == 1)):
		return True
	elif board[newpos[0]][newpos[1]] != 0 and movedh == 0:
		return False
	return ((piece.pos[0] == newpos[0]) and (movedv <= squaresallowed) and (movedv > 0))
pieceLogique['Pawn']=pawnLogic

#Pull from table of logics
def pieceCanMove(piece, newpos, realcall):
	global rc
	rc = realcall
	for key in pieceLogique:
		if piece.name == key:
			return (pieceLogique[key](piece, newpos) and colLogic(piece, newpos))
	return True
