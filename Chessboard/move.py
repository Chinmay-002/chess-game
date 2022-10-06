from .square import *
from .graphics import *
from .otherfunctions import *
from Chesspieces.chesspieces import *
from pygame import mouse


class Move:
    piece = None
    square_1 = None
    square_2 = None
    notation = ''

    is_castle = False
    is_promotion = False
    is_enpassant = False

    def __init__(self, square_1):
        self.square_1 = square_1
        self.piece = square_1.piece

    def setSquare1(self, square_1):
        self.square_1 = square_1
        self.piece = square_1.piece

    def setSquare2(self, square_2):
        self.square_2 = square_2

    @staticmethod
    def highlightMoves(board, screen, piece):
        board.highlights += piece.getMoves(board.state)
        # TODO: legalise piece.getMoves
        highlightSquares(board, screen, board.highlights, green)

    def makeMove(self, board, screen, last_move):
        piece = self.square_1.piece
        unhighlightSquares(board, screen)
        if type(piece) == King:
            if self.isCastle():
                self.castle(board)
                drawCastle(screen, board, self)
            else:
                self.updateBoard()
                drawMove(screen, self)
            piece.moved = True
        elif type(piece) == Pawn:
            if self.isEnPassant(last_move):
                self.enPassant(last_move)
                drawEnPassant(screen, self, last_move)
            elif self.isPromotion():
                drawPrePromotion(screen, self.piece.color)
                board.promotion = True
                self.is_promotion = True
                return
            else:
                self.updateBoard()
            drawMove(screen, self)
        else:
            # TODO: create Notation for move
            self.updateBoard()
            drawMove(screen, self)
        game_moves.append(self)
        updateProtections(board)
        redCheck(board, screen)

    def unClick(self, board, screen):
        unhighlightSquares(board, screen)
        self.square_1 = None
        self.piece = None

    @staticmethod
    def firstClick(board, screen, clicked_square):
        piece = clicked_square.piece
        if piece is not None:
            current_move = Move(clicked_square)
            Move.highlightMoves(board, screen, piece)
            return current_move
        else:
            return None

    def updateBoard(self):
        self.square_2.piece = self.square_1.piece
        self.square_1.piece.position = [self.square_2.i, self.square_2.j]
        self.square_1.piece = None

    def isEnPassant(self, last_move):
        if last_move:
            if type(last_move.piece) == Pawn:
                if last_move.piece.color == black:
                    if last_move.square_1.j == 1 and last_move.square_2.j == 3:
                        if self.square_1.j == 3 and (
                                self.square_1.i == last_move.square_2.i + 1 or self.square_1.i == last_move.square_2.i - 1):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if last_move.square_1.j == 6 and last_move.square_2.j == 4:
                        if self.square_1.j == 4 and (
                                self.square_1.i == last_move.square_2.i + 1 or self.square_1.i == last_move.square_2.i - 1):
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False

    def enPassant(self, last_move):
        if last_move:
            # TODO: Create notation
            self.square_2.piece = self.square_1.piece
            self.square_1.piece.position = [self.square_2.i, self.square_2.j]
            self.square_1.piece = None
            last_move.square_2.piece = None

    def isCastle(self):
        piece = self.piece
        if piece.color == white:
            if not piece.moved and self.square_2.j == 7:
                if self.square_2.i == 6 or self.square_2.i == 2:
                    return True
        else:
            if not piece.moved and self.square_2.j == 0:
                if self.square_2.i == 6 or self.square_2.i == 2:
                    return True
        return False

    def castle(self, board):
        self.is_castle = True
        king = self.piece
        if king.color == white:
            j_value = 7
        else:
            j_value = 0
        if self.square_2.i == 6:
            rook = board.state[7][j_value].piece
            board.state[7][j_value].piece = None
            self.square_1.piece = None
            self.square_2.piece = king
            king.position = [self.square_2.i, self.square_2.j]
            rook.position = [5, j_value]
            board.state[5][j_value].piece = rook
        else:
            rook = board.state[0][j_value].piece
            board.state[0][j_value].piece = None
            self.square_1.piece = None
            self.square_2.piece = king
            king.position = [self.square_2.i, self.square_2.j]
            rook.position = [3, j_value]
            board.state[3][j_value].piece = rook

    def isPromotion(self):
        if self.square_2.j == 0 or self.square_2.j == 7:
            return True
        else:
            return False

    def promotion(self, choice, board, screen):
        if self.piece.color == white:
            if choice == 1:
                piece = Rook(white, (self.square_2.i, self.square_2.j))
            elif choice == 2:
                piece = Bishop(white, (self.square_2.i, self.square_2.j))
            elif choice == 3:
                piece = Knight(white, (self.square_2.i, self.square_2.j))
            else:
                piece = Queen(white, (self.square_2.i, self.square_2.j))
        else:
            if choice == 1:
                piece = Rook(black, (self.square_2.i, self.square_2.j))
            elif choice == 2:
                piece = Bishop(black, (self.square_2.i, self.square_2.j))
            elif choice == 3:
                piece = Knight(black, (self.square_2.i, self.square_2.j))
            else:
                piece = Queen(black, (self.square_2.i, self.square_2.j))
        # board.promotion = True
        # self.is_promotion = True
        self.square_2.piece = piece
        self.square_1.piece = None
        drawMove(screen, self)
        unDrawPrePromotion(screen)
        game_moves.append(self)
        updateProtections(board)
        redCheck(board, screen)
        board.promotion = False
        self.is_promotion = True



