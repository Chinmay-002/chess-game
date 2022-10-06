class Square:
    i = None
    j = None
    size = 75
    color = None
    w_protected = False
    b_protected = False
    highlighted = False
    piece = None

    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    @staticmethod
    def coordinate(loc):
        return 50 + Square.size * loc

    @staticmethod
    def coordinateP(loc):
        return 55 + Square.size * loc

    @staticmethod
    def getSquare(board, coordinates):
        """
        :rtype: Square
        """
        x = coordinates[0]
        y = coordinates[1]
        for i in range(8):
            for j in range(8):
                s = board.state[i][j]
                if (Square.coordinate(i) <= x <= Square.coordinate(i) + Square.size) and (
                        Square.coordinate(j) <= y <= Square.coordinate(j) + Square.size):
                    return s
        return None

    @staticmethod
    def getPromotionSquare(coordinates):
        x = coordinates[0]
        y = coordinates[1]
        for i in range(4):
            if (Square.coordinate(2+ i) <= x <= Square.coordinate(2 + i) + Square.size) and (
                    Square.coordinate(8) <= y <= Square.coordinate(8) + Square.size):
                return i
        return -1
