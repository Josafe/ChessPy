class GameState():

    def __init__(self):
#Tauler ajedrez 8x8, la "n" es refereix a negres i la "b" en blanques,
# també el primer caracter indica el tipus de peça,
# el -- indica que no hi ha ninguna peça alli.
        self.tablero = [
            ["tn", "cn", "an", "kn", "qn", "an", "cn", "tn"],
            ["pn", "pn", "pn", "pn", "pn", "pn", "pn", "pn"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
            ["tb", "cb", "ab", "kb", "qb", "ab", "cb", "tb"]
            ]

        self.whiteToMove = True
        self.moveLog = []