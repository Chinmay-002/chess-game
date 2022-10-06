from abc import ABC, abstractmethod

from pygame.image import load as img_load


class Chesspiece(ABC):
    color = None
    position = None
    image = None
    eval = None
    notation = ""
    points = None

    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abstractmethod
    def getMoves(self, board):
        pass

    @abstractmethod
    def getProtected(self, board):
        pass


class King(Chesspiece):
    moved = False

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = 'K'
        self.points = 20000
        if color == white:
            self.image = wk
            self.eval = [[-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-20, -30, -30, -40, -40, -30, -30, -20],
                         [-10, -20, -20, -20, -20, -20, -20, -10],
                         [15, 20, 0, 0, 0, 0, 20, 15],
                         [20, 50, 40, -10, -20, 5, 40, 20]]
        else:
            self.image = bk
            self.eval = [[20, 50, 40, -20, -10, 5, 40, 20],
                         [15, 20, 0, 0, 0, 0, 20, 15],
                         [-10, -20, -20, -20, -20, -20, -20, -10],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-20, -30, -30, -40, -40, -30, -30, -20],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30],
                         [-30, -40, -40, -50, -50, -40, -40, -30]]

    def getMoves(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]
        if self.color == white:
            # top moves
            if j - 1 >= 0:
                if board[i][j - 1].piece is None or board[i][j - 1].piece.color != self.color:
                    if board[i][j - 1].b_protected is False:
                        moveset.append((i, j - 1))

                if i - 1 >= 0:
                    if board[i - 1][j - 1].piece is None or board[i - 1][j - 1].piece.color != self.color:
                        if board[i - 1][j - 1].b_protected is False:
                            moveset.append((i - 1, j - 1))

                if i + 1 <= 7:
                    if board[i + 1][j - 1].piece is None or board[i + 1][j - 1].piece.color != self.color:
                        if board[i + 1][j - 1].b_protected is False:
                            moveset.append((i + 1, j - 1))
            # bottom moves
            if j + 1 <= 7:
                if board[i][j + 1].piece is None or board[i][j + 1].piece.color != self.color:
                    if board[i][j + 1].b_protected is False:
                        moveset.append((i, j + 1))

                if i - 1 >= 0:
                    if board[i - 1][j + 1].piece is None or board[i - 1][j + 1].piece.color != self.color:
                        if board[i - 1][j + 1].b_protected is False:
                            moveset.append((i - 1, j + 1))

                if i + 1 <= 7:
                    if board[i + 1][j + 1].piece is None or board[i + 1][j + 1].piece.color != self.color:
                        if board[i + 1][j + 1].b_protected is False:
                            moveset.append((i + 1, j + 1))
            # left move
            if i - 1 >= 0:
                if board[i - 1][j].piece is None or board[i - 1][j].piece.color != self.color:
                    if board[i - 1][j].b_protected is False:
                        moveset.append((i - 1, j))
            # right move
            if i + 1 <= 7:
                if board[i + 1][j].piece is None or board[i + 1][j].piece.color != self.color:
                    if board[i + 1][j].b_protected is False:
                        moveset.append((i + 1, j))

            # castling
            if self.position == [4, 7]:
                if not self.moved and board[5][7].piece is None and board[6][7].piece is None and type(
                        board[7][7].piece) == Rook and board[7][7].piece.color == white:
                    if board[5][7].b_protected is False and board[6][7].b_protected is False:
                        moveset.append((6, 7))

                if not self.moved and board[3][7].piece is None and board[2][7].piece is None and board[1][7].piece is None and type(board[0][7].piece) == Rook and board[0][7].piece.color == white:
                    if board[3][7].b_protected is False and board[2][7].b_protected is False and board[1][7].b_protected is False:
                        moveset.append((2, 7))

        else:
            # top moves
            if j - 1 >= 0:
                if board[i][j - 1].piece is None or board[i][j - 1].piece.color != self.color:
                    if board[i][j - 1].w_protected is False:
                        moveset.append((i, j - 1))

                if i - 1 >= 0:
                    if board[i - 1][j - 1].piece is None or board[i - 1][j - 1].piece.color != self.color:
                        if board[i - 1][j - 1].w_protected is False:
                            moveset.append((i - 1, j - 1))

                if i + 1 <= 7:
                    if board[i + 1][j - 1].piece is None or board[i + 1][j - 1].piece.color != self.color:
                        if board[i + 1][j - 1].w_protected is False:
                            moveset.append((i + 1, j - 1))
            # bottom moves
            if j + 1 <= 7:
                if board[i][j + 1].piece is None or board[i][j + 1].piece.color != self.color:
                    if board[i][j + 1].w_protected is False:
                        moveset.append((i, j + 1))

                if i - 1 >= 0:
                    if board[i - 1][j + 1].piece is None or board[i - 1][j + 1].piece.color != self.color:
                        if board[i - 1][j + 1].w_protected is False:
                            moveset.append((i - 1, j + 1))

                if i + 1 <= 7:
                    if board[i + 1][j + 1].piece is None or board[i + 1][j + 1].piece.color != self.color:
                        if board[i + 1][j + 1].w_protected is False:
                            moveset.append((i + 1, j + 1))
            # left move
            if i - 1 >= 0:
                if board[i - 1][j].piece is None or board[i - 1][j].piece.color != self.color:
                    if board[i - 1][j].w_protected is False:
                        moveset.append((i - 1, j))
            # right move
            if i + 1 <= 7:
                if board[i + 1][j].piece is None or board[i + 1][j].piece.color != self.color:
                    if board[i + 1][j].w_protected is False:
                        moveset.append((i + 1, j))

            # castling
            if self.position == [4, 0]:  # TODO check if king is in check
                if not self.moved and board[5][0].piece is None and board[6][0].piece is None and type(
                        board[7][0].piece) == Rook and \
                        board[7][0].piece.color == black:
                    if board[5][0].w_protected is False and board[6][0].w_protected is False:
                        moveset.append((6, 0))

                if not self.moved and board[3][0].piece is None and board[2][0].piece is None and board[1][0].piece is None and type(board[0][0].piece) == Rook and board[0][0].piece.color == black:
                    if board[3][0].w_protected is False and board[2][0].w_protected is False and board[1][0].w_protected is False:
                        moveset.append((2, 0))

        return moveset

    def getProtected(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # top moves
        if j - 1 >= 0:
            moveset.append((i, j - 1))

            if i - 1 >= 0:
                moveset.append((i - 1, j - 1))

            if i + 1 <= 7:
                moveset.append((i + 1, j - 1))

        # bottom moves
        if j + 1 <= 7:
            moveset.append((i, j + 1))

            if i - 1 >= 0:
                moveset.append((i - 1, j + 1))

            if i + 1 <= 7:
                moveset.append((i + 1, j + 1))
        # left move
        if i - 1 >= 0:
            moveset.append((i - 1, j))
        # right move
        if i + 1 <= 7:
            moveset.append((i + 1, j))


class Queen(Chesspiece):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = 'B'
        self.points = 900
        if color == white:
            self.image = wq
            self.eval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                         [-10, 0, 0, 0, 0, 0, 0, -10],
                         [-10, 0, 5, 5, 5, 5, 0, -10],
                         [-5, 0, 5, 5, 5, 5, 0, -5],
                         [0, 0, 5, 5, 5, 5, 0, 0],
                         [-10, 15, -15, 5, 5, -15, -5, -10],
                         [-10, 0, 10, 0, 0, 0, 0, -10],
                         [-20, -10, -10, -5, -5, -10, -10, -20]]
        else:
            self.image = bq
            self.eval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                         [-10, 0, 10, 0, 0, 0, 0, -10],
                         [-10, 15, -15, 5, 5, -15, -5, -10],
                         [0, 0, 5, 5, 5, 5, 0, 0],
                         [-5, 0, 5, 5, 5, 5, 0, -5],
                         [-10, 0, 5, 5, 5, 5, 0, -10],
                         [-10, 0, 0, 0, 0, 0, 0, -10],
                         [-20, -10, -10, -5, -5, -10, -10, -20]]

    def getMoves(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking up movement
        n = 1
        while True:
            if 0 <= j - n <= 7:
                if board[i][j - n].piece is None:
                    moveset.append((i, j - n))
                elif board[i][j - n].piece.color != self.color:
                    moveset.append((i, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking down movement
        n = 1
        while True:
            if 0 <= j + n <= 7:
                if board[i][j + n].piece is None:
                    moveset.append((i, j + n))
                elif board[i][j + n].piece.color != self.color:
                    moveset.append((i, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking left movement
        n = 1
        while True:
            if 0 <= i - n <= 7:
                if board[i - n][j].piece is None:
                    moveset.append((i - n, j))
                elif board[i - n][j].piece.color != self.color:
                    moveset.append((i - n, j))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking right movement
        n = 1
        while True:
            if 0 <= i + n <= 7:
                if board[i + n][j].piece is None:
                    moveset.append((i + n, j))
                elif board[i + n][j].piece.color != self.color:
                    moveset.append((i + n, j))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking down left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j + n <= 7:
                if board[i - n][j + n].piece is None:
                    moveset.append((i - n, j + n))
                elif board[i - n][j + n].piece.color != self.color:
                    moveset.append((i - n, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking down right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j + n <= 7:
                if board[i + n][j + n].piece is None:
                    moveset.append((i + n, j + n))
                elif board[i + n][j + n].piece.color != self.color:
                    moveset.append((i + n, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking up right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j - n <= 7:
                if board[i + n][j - n].piece is None:
                    moveset.append((i + n, j - n))
                elif board[i + n][j - n].piece.color != self.color:
                    moveset.append((i + n, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking up left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j - n <= 7:
                if board[i - n][j - n].piece is None:
                    moveset.append((i - n, j - n))
                elif board[i - n][j - n].piece.color != self.color:
                    moveset.append((i - n, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        return moveset

    def getProtected(self, board):

        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking up movement
        n = 1
        while True:
            if 0 <= j - n <= 7:
                if board[i][j - n].piece is None:
                    moveset.append((i, j - n))
                elif board[i][j - n].piece.color != self.color:
                    moveset.append((i, j - n))
                    if type(board[i][j - n].piece) != King:
                        break
                else:
                    moveset.append((i, j - n))
                    break
            else:
                break
            n += 1

        # checking down movement
        n = 1
        while True:
            if 0 <= j + n <= 7:
                if board[i][j + n].piece is None:
                    moveset.append((i, j + n))
                elif board[i][j + n].piece.color != self.color:
                    moveset.append((i, j + n))
                    if type(board[i][j + n].piece) != King:
                        break
                else:
                    moveset.append((i, j + n))
                    break
            else:
                break
            n += 1

        # checking left movement
        n = 1
        while True:
            if 0 <= i - n <= 7:
                if board[i - n][j].piece is None:
                    moveset.append((i - n, j))
                elif board[i - n][j].piece.color != self.color:
                    moveset.append((i - n, j))
                    if type(board[i - n][j].piece) != King:
                        break
                else:
                    moveset.append((i - n, j))
                    break
            else:
                break
            n += 1

        # checking right movement
        n = 1
        while True:
            if 0 <= i + n <= 7:
                if board[i + n][j].piece is None:
                    moveset.append((i + n, j))
                elif board[i + n][j].piece.color != self.color:
                    moveset.append((i + n, j))
                    if type(board[i + n][j].piece) != King:
                        break
                else:
                    moveset.append((i + n, j))
                    break
            else:
                break
            n += 1

        # checking down left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j + n <= 7:
                if board[i - n][j + n].piece is None:
                    moveset.append((i - n, j + n))
                elif board[i - n][j + n].piece.color != self.color:
                    moveset.append((i - n, j + n))
                    if type(board[i - n][j + n].piece) != King:
                        break
                else:
                    moveset.append((i - n, j + n))
                    break
            else:
                break
            n += 1

        # checking down right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j + n <= 7:
                if board[i + n][j + n].piece is None:
                    moveset.append((i + n, j + n))
                elif board[i + n][j + n].piece.color != self.color:
                    moveset.append((i + n, j + n))
                    if type(board[i + n][j + n].piece) != King:
                        break
                else:
                    moveset.append((i + n, j + n))
                    break
            else:
                break
            n += 1

        # checking up right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j - n <= 7:
                if board[i + n][j - n].piece is None:
                    moveset.append((i + n, j - n))
                elif board[i + n][j - n].piece.color != self.color:
                    moveset.append((i + n, j - n))
                    if type(board[i + n][j - n].piece) != King:
                        break
                else:
                    moveset.append((i + n, j - n))
                    break
            else:
                break
            n += 1

        # checking up left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j - n <= 7:
                if board[i - n][j - n].piece is None:
                    moveset.append((i - n, j - n))
                elif board[i - n][j - n].piece.color != self.color:
                    moveset.append((i - n, j - n))
                    if type(board[i - n][j - n].piece) != King:
                        break
                else:
                    moveset.append((i - n, j - n))
                    break
            else:
                break
            n += 1

        return moveset


class Rook(Chesspiece):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = 'R'
        self.points = 500
        if color == white:
            self.image = wr
            self.eval = [[0, 10, 10, 10, 10, 10, 10, 0],
                         [0, 20, 30, 30, 30, 30, 20, 0],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 10, 15, 15, 10, 0, -5],
                         [0, 0, 10, 30, 30, 20, 0, 0]]
        else:
            self.image = br
            self.eval = [[0, 0, 10, 30, 30, 20, 0, 0],
                         [-5, 0, 10, 15, 15, 10, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [-5, 0, 0, 0, 0, 0, 0, -5],
                         [0, 20, 30, 30, 30, 30, 20, 0],
                         [0, 10, 10, 10, 10, 10, 10, 0]]

    def getMoves(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking up movement
        n = 1
        while True:
            if 0 <= j - n <= 7:
                if board[i][j - n].piece is None:
                    moveset.append((i, j - n))
                elif board[i][j - n].piece.color != self.color:
                    moveset.append((i, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking down movement
        n = 1
        while True:
            if 0 <= j + n <= 7:
                if board[i][j + n].piece is None:
                    moveset.append((i, j + n))
                elif board[i][j + n].piece.color != self.color:
                    moveset.append((i, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking left movement
        n = 1
        while True:
            if 0 <= i - n <= 7:
                if board[i - n][j].piece is None:
                    moveset.append((i - n, j))
                elif board[i - n][j].piece.color != self.color:
                    moveset.append((i - n, j))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking right movement
        n = 1
        while True:
            if 0 <= i + n <= 7:
                if board[i + n][j].piece is None:
                    moveset.append((i + n, j))
                elif board[i + n][j].piece.color != self.color:
                    moveset.append((i + n, j))
                    break
                else:
                    break
            else:
                break
            n += 1

        return moveset

    def getProtected(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking up movement
        n = 1
        while True:
            if 0 <= j - n <= 7:
                if board[i][j - n].piece is None:
                    moveset.append((i, j - n))
                elif board[i][j - n].piece.color != self.color:
                    moveset.append((i, j - n))
                    if type(board[i][j - n].piece) != King or board[i][j - n].piece.color == self.color:
                        break
                else:
                    moveset.append((i, j - n))
                    break
            else:
                break
            n += 1

        # checking down movement
        n = 1
        while True:
            if 0 <= j + n <= 7:
                if board[i][j + n].piece is None:
                    moveset.append((i, j + n))
                elif board[i][j + n].piece.color != self.color:
                    moveset.append((i, j + n))
                    if type(board[i][j + n].piece) != King or board[i][j + n].piece.color == self.color:
                        break
                else:
                    moveset.append((i, j + n))
                    break
            else:
                break
            n += 1

        # checking left movement
        n = 1
        while True:
            if 0 <= i - n <= 7:
                if board[i - n][j].piece is None:
                    moveset.append((i - n, j))
                elif board[i - n][j].piece.color != self.color:
                    moveset.append((i - n, j))
                    if type(board[i - n][j].piece) != King or board[i - n][j].piece.color == self.color:
                        break
                else:
                    moveset.append((i - n, j))
                    break
            else:
                break
            n += 1

        # checking right movement
        n = 1
        while True:
            if 0 <= i + n <= 7:
                if board[i + n][j].piece is None:
                    moveset.append((i + n, j))
                elif board[i + n][j].piece.color != self.color:
                    moveset.append((i + n, j))
                    if type(board[i + n][j].piece) != King or board[i + n][j].piece.color == self.color:
                        break
                else:
                    moveset.append((i + n, j))
                    break
            else:
                break
            n += 1

        return moveset


class Bishop(Chesspiece):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = 'B'
        self.points = 330
        if color == white:
            self.image = wb
            self.eval = [[-20, -10, -10, -10, -10, -10, -10, -20],
                         [-10, -10, -10, -10, -10, -10, -10, -10],
                         [-10, 0, 5, 5, 5, 5, 0, -10],
                         [-10, 15, 5, 10, 10, 5, 15, -10],
                         [-10, 5, 25, 10, 10, 25, 5, -10],
                         [-10, 10, 10, 10, 10, 10, 10, -10],
                         [0, 30, 0, 5, 5, 0, 30, 0],
                         [-10, -10, -10, -10, -10, -10, -10, -10]]
        else:
            self.image = bb
            self.eval = [[-10, -10, -10, -10, -10, -10, -10, -10],
                         [-10, 25, 0, 5, 5, 0, 25, -10],
                         [-10, 5, 10, 10, 10, 10, 5, -10],
                         [-10, 5, 15, 10, 10, 15, 5, -10],
                         [-10, 15, 5, 10, 10, 5, 15, -10],
                         [-10, 0, 5, 5, 5, 5, 0, -10],
                         [-10, -10, -10, -10, -10, -10, -10, -10],
                         [-20, -10, -10, -10, -10, -10, -10, -20]]

    def getMoves(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking down left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j + n <= 7:
                if board[i - n][j + n].piece is None:
                    moveset.append((i - n, j + n))
                elif board[i - n][j + n].piece.color != self.color:
                    moveset.append((i - n, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking down right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j + n <= 7:
                if board[i + n][j + n].piece is None:
                    moveset.append((i + n, j + n))
                elif board[i + n][j + n].piece.color != self.color:
                    moveset.append((i + n, j + n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking up right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j - n <= 7:
                if board[i + n][j - n].piece is None:
                    moveset.append((i + n, j - n))
                elif board[i + n][j - n].piece.color != self.color:
                    moveset.append((i + n, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        # checking up left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j - n <= 7:
                if board[i - n][j - n].piece is None:
                    moveset.append((i - n, j - n))
                elif board[i - n][j - n].piece.color != self.color:
                    moveset.append((i - n, j - n))
                    break
                else:
                    break
            else:
                break
            n += 1

        return moveset

    def getProtected(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # checking down left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j + n <= 7:
                if board[i - n][j + n].piece is None:
                    moveset.append((i - n, j + n))
                else:
                    moveset.append((i - n, j + n))
                    if type(board[i - n][j + n].piece) != King or board[i - n][j + n].piece.color == self.color:
                        break
            else:
                break
            n += 1

        # checking down right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j + n <= 7:
                if board[i + n][j + n].piece is None:
                    moveset.append((i + n, j + n))
                else:
                    moveset.append((i + n, j + n))
                    if type(board[i + n][j + n].piece) != King or board[i + n][j + n].piece.color == self.color:
                        break
            else:
                break
            n += 1

        # checking up right diagonal
        n = 1
        while True:
            if 0 <= i + n <= 7 and 0 <= j - n <= 7:
                if board[i + n][j - n].piece is None:
                    moveset.append((i + n, j - n))
                else:
                    moveset.append((i + n, j - n))
                    if type(board[i + n][j - n].piece) != King or board[i + n][j - n].piece.color == self.color:
                        break
            else:
                break
            n += 1
        # print(moveset)

        # checking up left diagonal
        n = 1
        while True:
            if 0 <= i - n <= 7 and 0 <= j - n <= 7:
                if board[i - n][j - n].piece is None:
                    moveset.append((i - n, j - n))
                else:
                    moveset.append((i - n, j - n))
                    if type(board[i - n][j - n].piece) != King or board[i - n][j - n].piece.color == self.color:
                        break
            else:
                break
            n += 1
        # print(moveset)
        return moveset


class Knight(Chesspiece):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = 'N'
        self.points = 320
        if color == white:
            self.image = wn
            self.eval = [[-20, -40, -30, -30, -30, -30, -40, -20],
                         [-40, -20, 0, 0, 0, 0, -20, -40],
                         [-30, 0, 10, 10, 10, 10, 0, -30],
                         [-30, 15, 15, 15, 15, 15, 15, -30],
                         [-30, 5, 15, 20, 20, 15, 5, -30],
                         [-10, 5, 30, 15, 15, 30, 5, -10],
                         [-40, -20, 0, 5, 5, 0, -20, -40],
                         [-40, -10, -20, -20, -20, -20, -10, -40]]
        else:
            self.image = bn
            self.eval = [[-40, -10, -20, -20, -20, -20, -10, -40],
                         [-40, -20, 0, 5, 5, 0, -20, -40],
                         [-10, 5, 30, 15, 15, 30, 5, -10],
                         [-30, 5, 15, 20, 20, 15, 5, -30],
                         [-30, 15, 15, 15, 15, 15, 15, -30],
                         [-30, 0, 10, 10, 10, 10, 0, -30],
                         [-40, -20, 0, 0, 0, 0, -20, -40],
                         [-20, -40, -30, -30, -30, -30, -40, -20]]

    def getMoves(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # anticlockwise legal moves starting top right
        if 0 <= i + 1 <= 7 and 0 <= j - 2 <= 7:
            if board[i + 1][j - 2].piece is None or board[i + 1][j - 2].piece.color != self.color:
                moveset.append((i + 1, j - 2))

        if 0 <= i - 1 <= 7 and 0 <= j - 2 <= 7:
            if board[i - 1][j - 2].piece is None or board[i - 1][j - 2].piece.color != self.color:
                moveset.append((i - 1, j - 2))

        if 0 <= i - 2 <= 7 and 0 <= j - 1 <= 7:
            if board[i - 2][j - 1].piece is None or board[i - 2][j - 1].piece.color != self.color:
                moveset.append((i - 2, j - 1))

        if 0 <= i - 2 <= 7 and 0 <= j + 1 <= 7:
            if board[i - 2][j + 1].piece is None or board[i - 2][j + 1].piece.color != self.color:
                moveset.append((i - 2, j + 1))

        if 0 <= i - 1 <= 7 and 0 <= j + 2 <= 7:
            if board[i - 1][j + 2].piece is None or board[i - 1][j + 2].piece.color != self.color:
                moveset.append((i - 1, j + 2))

        if 0 <= i + 1 <= 7 and 0 <= j + 2 <= 7:
            if board[i + 1][j + 2].piece is None or board[i + 1][j + 2].piece.color != self.color:
                moveset.append((i + 1, j + 2))

        if 0 <= i + 2 <= 7 and 0 <= j + 1 <= 7:
            if board[i + 2][j + 1].piece is None or board[i + 2][j + 1].piece.color != self.color:
                moveset.append((i + 2, j + 1))

        if 0 <= i + 2 <= 7 and 0 <= j - 1 <= 7:
            if board[i + 2][j - 1].piece is None or board[i + 2][j - 1].piece.color != self.color:
                moveset.append((i + 2, j - 1))
        return moveset

    def getProtected(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]

        # anticlockwise legal moves starting top right
        if 0 <= i + 1 <= 7 and 0 <= j - 2 <= 7:
            moveset.append((i + 1, j - 2))

        if 0 <= i - 1 <= 7 and 0 <= j - 2 <= 7:
            moveset.append((i - 1, j - 2))

        if 0 <= i - 2 <= 7 and 0 <= j - 1 <= 7:
            moveset.append((i - 2, j - 1))

        if 0 <= i - 2 <= 7 and 0 <= j + 1 <= 7:
            moveset.append((i - 2, j + 1))

        if 0 <= i - 1 <= 7 and 0 <= j + 2 <= 7:
            moveset.append((i - 1, j + 2))

        if 0 <= i + 1 <= 7 and 0 <= j + 2 <= 7:
            moveset.append((i + 1, j + 2))

        if 0 <= i + 2 <= 7 and 0 <= j + 1 <= 7:
            moveset.append((i + 2, j + 1))

        if 0 <= i + 2 <= 7 and 0 <= j - 1 <= 7:
            moveset.append((i + 2, j - 1))
        return moveset


class Pawn(Chesspiece):
    moved = False

    def __init__(self, color, position):
        super().__init__(color, position)
        self.notation = ''
        self.points = 100
        if color == white:
            self.image = wp
            self.eval = [[100, 100, 100, 100, 100, 100, 100, 100],
                         [50, 50, 50, 50, 50, 50, 50, 50],
                         [10, 10, 20, 30, 30, 20, 10, 10],
                         [10, 15, 10, 45, 45, 10, 15, 10],
                         [0, -10, 20, 40, 40, 5, -10, 0],
                         [5, 10, -5, 10, 10, -5, 10, 5],
                         [5, 5, 10, -30, -30, 10, 5, 5],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
        else:
            self.image = bp
            self.eval = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [5, 5, 10, -30, -30, 10, 5, 5],
                         [5, 15, -5, 5, 5, -5, 15, 5],
                         [0, -10, 20, 40, 40, 5, -10, 0],
                         [10, 15, 10, 45, 45, 10, 15, 10],
                         [10, 10, 20, 30, 30, 20, 10, 10],
                         [50, 50, 50, 50, 50, 50, 50, 50],
                         [100, 100, 100, 100, 100, 100, 100, 100]]

    def getMoves(self, board):
        moveset = []
        if game_moves:
            last_move = game_moves[-1]
        else:
            last_move = None
        i = self.position[0]
        j = self.position[1]
        if self.color == white:
            if j != 0:
                if board[i][j - 1].piece is None:
                    moveset.append((i, j - 1))
                    if j == 6 and board[i][j - 2].piece is None:
                        moveset.append((i, j - 2))

                if i != 0 and board[i - 1][j - 1].piece is not None and board[i - 1][j - 1].piece.color != self.color:
                    moveset.append((i - 1, j - 1))
                if i != 7 and board[i + 1][j - 1].piece is not None and board[i + 1][j - 1].piece.color != self.color:
                    moveset.append((i + 1, j - 1))

                if last_move is not None and type(last_move.piece) == Pawn:
                    if last_move.square_1.j == 1 and last_move.square_2.j == 3:
                        if j == 3 and (i == last_move.square_2.i + 1 or i == last_move.square_2.i - 1):
                            moveset.append((last_move.square_2.i, j - 1))
                # if j == 3:
                #     moveset.append((i - 1, j - 1))
                #     moveset.append((i + 1, j - 1))
            else:
                return moveset
        else:
            if j != 7:
                if board[i][j + 1].piece is None:
                    moveset.append((i, j + 1))
                    if j == 1 and board[i][j + 2].piece is None:
                        moveset.append((i, j + 2))

                if i != 0 and board[i - 1][j + 1].piece is not None and board[i - 1][j + 1].piece.color != self.color:
                    moveset.append((i - 1, j + 1))
                if i != 7 and board[i + 1][j + 1].piece is not None and board[i + 1][j + 1].piece.color != self.color:
                    moveset.append((i + 1, j + 1))

                if last_move is not None and type(last_move.piece) == Pawn:
                    if last_move.square_1.j == 6 and last_move.square_2.j == 4:
                        if j == 4 and (i == last_move.square_2.i + 1 or i == last_move.square_2.i - 1):
                            moveset.append((last_move.square_2.i, j + 1))
            else:
                return moveset
        return moveset

    def getProtected(self, board):
        moveset = []
        i = self.position[0]
        j = self.position[1]
        if self.color == white:
            if j != 0:
                if i != 0:
                    moveset.append((i - 1, j - 1))
                if i != 7:
                    moveset.append((i + 1, j - 1))
            else:
                return moveset
        else:
            if j != 7:
                if i != 0:
                    moveset.append((i - 1, j + 1))
                if i != 7:
                    moveset.append((i + 1, j + 1))
            else:
                return moveset
        return moveset


# variables common to pieces
game_moves = [None]
white = (255, 255, 255)
black = (0, 100, 100)
wp = img_load("./images/wp.png")
wn = img_load("./images/wn.png")
wb = img_load("./images/wb.png")
wr = img_load("./images/wr.png")
wq = img_load("./images/wq.png")
wk = img_load("./images/wk.png")
bn = img_load("./images/bn.png")
bp = img_load("./images/bp.png")
bb = img_load("./images/bb.png")
br = img_load("./images/br.png")
bq = img_load("./images/bq.png")
bk = img_load("./images/bk.png")
