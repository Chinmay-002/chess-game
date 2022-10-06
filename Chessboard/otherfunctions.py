from .square import *
from .graphics import *
from .move import *
from Chesspieces.chesspieces import *


def updateProtections(board):
    for i in range(8):
        for j in range(8):
            board.state[i][j].w_protected = False
            board.state[i][j].b_protected = False
    for i in range(8):
        for j in range(8):
            sq = board.state[i][j]
            piece = sq.piece
            if piece is not None:
                moves = piece.getProtected(board.state)
                if moves is not None:
                    if piece.color == white:
                        for loc in moves:
                            board.state[loc[0]][loc[1]].w_protected = True
                    else:
                        for loc in moves:
                            board.state[loc[0]][loc[1]].b_protected = True


def isInCheck(board):
    w_check = 0
    b_check = 0
    for i in range(8):
        for j in range(8):
            sq = board.state[i][j]
            piece = sq.piece
            if piece is not None and type(piece) == King:
                if piece.color == white and sq.b_protected:
                    w_check = 1
                if piece.color == black and sq.w_protected:
                    b_check = 1
    if w_check and b_check:
        return 0
    elif w_check:
        return 1
    elif b_check:
        return -1
    else:
        return 2

