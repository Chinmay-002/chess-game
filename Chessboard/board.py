from . import square
from Chesspieces.chesspieces import *


class Board:
    highlights = []
    last_move_square = None
    promotion = False
    state = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]

    def __init__(self, fen):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.state[i][j] = square.Square(i, j, (255, 255, 255))
                else:
                    self.state[i][j] = square.Square(i, j, (0, 100, 100))
        self.setBoard(fen)

    def setBoard(self, fen):
        i = j = 0
        for x in fen:
            if x == 'r':
                self.state[i][j].piece = Rook(black, [i, j])
            elif x == 'n':
                self.state[i][j].piece = Knight(black, [i, j])
            elif x == 'b':
                self.state[i][j].piece = Bishop(black, [i, j])
            elif x == 'q':
                self.state[i][j].piece = Queen(black, [i, j])
            elif x == 'k':
                self.state[i][j].piece = King(black, [i, j])
            elif x == 'p':
                self.state[i][j].piece = Pawn(black, [i, j])
            elif x == '/':
                j += 1
                i = -1
            elif x == 'R':
                self.state[i][j].piece = Rook(white, [i, j])
            elif x == 'N':
                self.state[i][j].piece = Knight(white, [i, j])
            elif x == 'B':
                self.state[i][j].piece = Bishop(white, [i, j])
            elif x == 'Q':
                self.state[i][j].piece = Queen(white, [i, j])
            elif x == 'K':
                self.state[i][j].piece = King(white, [i, j])
            elif x == 'P':
                self.state[i][j].piece = Pawn(white, [i, j])
            elif x.isdigit():
                i += int(x) - 1
            i += 1
