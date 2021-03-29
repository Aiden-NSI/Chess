class Board:
    def __init__(self):
        # Iinitialise l'échequier à la position initial
        coord=[
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1'
        ]# 64 cases numéroté avec la numérotation algébrique

        tab64 = [
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42, 43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
        ] #cases suivant leur position dans tab120 (voir ci-dessous)
        tab120 =[
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, 0, 1, 2, 3, 4, 5, 6, 7, -1,
        -1, 8, 9, 10, 11, 12, 13, 14, 15, -1,
        -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
        -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
        -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
        -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
        -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
        -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
        ]# échiquier pour les movements

    def init(self):
        """
        Remet les pièces à leurs positions de départ.
        Les pièces sont dans un tableau allant de 0 à 63.
        """

        self.cases = [
                Piece('TOUR','noir'),Piece('CAVALIER','noir'),Piece('FOU','noir'),Piece('DAME','noir'),Piece('ROI','noir'),Piece('FOU','noir'),Piece('CAVALIER','noir'),Piece('TOUR','noir'),
                Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),Piece('PION','noir'),
                Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
                Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
                Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
                Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),Piece(),
                Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),Piece('PION','blanc'),
                Piece('TOUR','blanc'),Piece('CAVALIER','blanc'),Piece('FOU','blanc'),Piece('DAME','blanc'),Piece('ROI','blanc'),Piece('FOU','blanc'),Piece('CAVALIER','blanc'),Piece('TOUR','blanc')
                ]

    def gen_moves_list(self,color='',dontCallIsAttacked=False):

        """
        Retourne tout les mouvement possible pour la couleur donnée.
        Si la couleur n'est pas donnée, elle est considerée comme le côté à déplacer
        dontCallIsAttacked est une valeur booléenne pour éviter les appels récursifs
        par la fonction is_attacked() appelant cette fonction gen_moves_list().
        Un mouvement est défini par :
        - le numéro de sa case de départ (pos1)
        - le numéro de sa case de destination (pos2)
        - le nom de la promotion de la pièce '','q','r','b','n'
        ('q':reine, 'r': tour, 'b': fou, 'n': cavalier)
        """

