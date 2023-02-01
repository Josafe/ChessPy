class GameState():

    def __init__(self):

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