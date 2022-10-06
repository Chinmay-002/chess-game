# imports
from Chesspieces.chesspieces import *
from Chessboard import board, graphics, square, move
import pygame

# variables
white_turn = True
clicks = 0
next_move = None

# initializing pygame and creating a screen to on which all GUI printing will be done
pygame.init()
screen = pygame.display.set_mode((900, 900), flags=pygame.SCALED)
screen.fill((180, 180, 180))

# setting up the board backend of the game
b1 = board.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
graphics.drawSquares(screen)
graphics.drawPieces(screen, b1)


if __name__ == "__main__":
    # Main game while loop
    while True:
        # for loop that iterates over all pygame events that take place at a particular instance
        for event in pygame.event.get():

            # The user wants to close the tab; quit pygame and terminate the program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            # The event is a mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                # A pawn promotion move
                if b1.promotion:
                    next_move.promotion(square.Square.getPromotionSquare(pygame.mouse.get_pos()), b1, screen)

                # Non-promotion move
                else:

                    # getting the square which was clicked by the user
                    clicked_square = square.Square.getSquare(b1, pygame.mouse.get_pos())

                    # the user clicked on a valid square
                    if clicked_square is not None:

                        # White's turn to play
                        if white_turn:

                            # The first click of the current turn
                            if clicks % 2 == 0:

                                # the clicked square has a white piece
                                if clicked_square.piece is not None and clicked_square.piece.color == white:
                                    next_move = move.Move.firstClick(b1, screen, clicked_square)
                                    clicks += 1

                            # Subsequent clicks
                            else:

                                # The subsequent click is on a square with no piece or a black piece
                                if clicked_square.piece is None or clicked_square.piece.color != white:

                                    # The clicked square is a valid a move for the selected piece
                                    if clicked_square.highlighted:
                                        next_move.setSquare2(clicked_square)
                                        next_move.makeMove(b1, screen, game_moves[-1])
                                        clicks += 1
                                        white_turn = False

                                # The clicked square is the same as the first click square
                                elif clicked_square == next_move.square_1:
                                    next_move.unClick(b1, screen)
                                    clicks -= 1

                                # The clicked square contains a different white piece
                                elif clicked_square.piece.color == white:
                                    next_move.unClick(b1, screen)
                                    next_move = move.Move.firstClick(b1, screen, clicked_square)

                        # Black's turn
                        else:

                            # The first click of the current turn
                            if clicks % 2 == 0:

                                # the clicked square has a black piece
                                if clicked_square.piece is not None and clicked_square.piece.color == black:
                                    last_move = next_move
                                    next_move = move.Move.firstClick(b1, screen, clicked_square)
                                    clicks += 1

                            # Subsequent clicks
                            else:

                                # The subsequent click is on a square with no piece or a white piece
                                if clicked_square.piece is None or clicked_square.piece.color != black:

                                    # The clicked square is a valid a move for the selected piece
                                    if clicked_square.highlighted:
                                        next_move.setSquare2(clicked_square)
                                        next_move.makeMove(b1, screen, game_moves[-1])
                                        clicks += 1
                                        white_turn = True

                                # The clicked square is the same as the first click square
                                elif clicked_square == next_move.square_1:
                                    next_move.unClick(b1, screen)
                                    clicks -= 1

                                # The clicked square contains a different black piece
                                elif clicked_square.piece.color == black:
                                    next_move.unClick(b1, screen)
                                    next_move = move.Move.firstClick(b1, screen, clicked_square)

        # Update the display
        pygame.display.update()
