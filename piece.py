class Piece:
    VIDE='.'
    nomPiece=(VIDE,'ROI','DAME','TOUR','CAVALIER','FOU','PION')
    color=(VIDE,'BLANC','NOIR')
    valeurPiece=(0,0,9,5,3,3,1)
    deplacements_tour=(-10,10,-1,1)
    deplacements_fou=(-11,-9,11,9)
    deplacements_cavalier=(-12,-21,-19,-8,12,21,19,8)
    def __init__(self,nomPiece,couleur):
        self.nomPiece = nomPiece
        self.couleur = color
        self.valeur = valeurPiece


tour = Piece('TOUR','NOIR')


