import pygame
from .square import *
from .board import *


def drawSquares(screen):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, white, (Square.coordinate(i), Square.coordinate(j), Square.size, Square.size))
            else:
                pygame.draw.rect(screen, black, (Square.coordinate(i), Square.coordinate(j), Square.size, Square.size))


def drawPieces(screen, board):
    for i in range(8):
        for j in range(8):
            if board.state[i][j].piece is not None:
                screen.blit(board.state[i][j].piece.image, (Square.coordinateP(i), Square.coordinateP(j)))


def highlightSquares(board: Board, screen, square_set, color):
    for coordinates in square_set:
        sq = board.state[coordinates[0]][coordinates[1]]
        square_piece = sq.piece
        sq.highlighted = True
        pygame.draw.rect(screen, color,
                         (Square.coordinate(coordinates[0]), Square.coordinate(coordinates[1]), Square.size,
                          Square.size))
        pygame.draw.rect(screen, (0, 0, 0),
                         (Square.coordinate(coordinates[0]), Square.coordinate(coordinates[1]), Square.size,
                          Square.size), 1)
        if square_piece is not None:
            screen.blit(square_piece.image, (Square.coordinateP(coordinates[0]), Square.coordinateP(coordinates[1])))
        if coordinates not in board.highlights:
            board.highlights.append(coordinates)


def unhighlightSquares(board, screen):
    for coordinates in board.highlights:
        sq = board.state[coordinates[0]][coordinates[1]]
        square_piece = sq.piece
        sq.highlighted = False
        pygame.draw.rect(screen, sq.color,
                         (Square.coordinate(coordinates[0]), Square.coordinate(coordinates[1]), Square.size,
                          Square.size))
        if square_piece is not None:
            screen.blit(square_piece.image, (Square.coordinateP(coordinates[0]), Square.coordinateP(coordinates[1])))
    board.highlights = []
    redCheck(board, screen)


def redCheck(board, screen):
    for i in range(8):
        for j in range(8):
            sq = board.state[i][j]
            piece = sq.piece
            if type(piece) == King:
                if piece.color == white:
                    if sq.b_protected:
                        pygame.draw.rect(screen, red,
                                         (Square.coordinate(sq.i), Square.coordinate(sq.j), Square.size, Square.size))
                        screen.blit(piece.image, (Square.coordinateP(sq.i), Square.coordinateP(sq.j)))
                        sq.highlighted = True
                        Board.highlights.append((sq.i, sq.j))
                    else:
                        pygame.draw.rect(screen, sq.color,
                                         (Square.coordinate(sq.i), Square.coordinate(sq.j), Square.size,
                                          Square.size))
                        screen.blit(piece.image, (Square.coordinateP(sq.i), Square.coordinateP(sq.j)))
                        sq.highlighted = False
                        if (sq.i, sq.j) in board.highlights:
                            board.highlights.remove((sq.i, sq.j))
                else:
                    if sq.w_protected:
                        pygame.draw.rect(screen, red,
                                         (Square.coordinate(sq.i), Square.coordinate(sq.j), Square.size, Square.size))
                        pygame.draw.rect(screen, (0, 0, 0),
                                         (Square.coordinate(sq.i), Square.coordinate(sq.j), Square.size, Square.size),
                                         1)
                        screen.blit(piece.image, (Square.coordinateP(sq.i), Square.coordinateP(sq.j)))
                        sq.highlighted = True
                        Board.highlights.append((sq.i, sq.j))
                    else:
                        pygame.draw.rect(screen, sq.color,
                                         (Square.coordinate(sq.i), Square.coordinate(sq.j), Square.size, Square.size))
                        screen.blit(piece.image, (Square.coordinateP(sq.i), Square.coordinateP(sq.j)))
                        sq.highlighted = False
                        if (sq.i, sq.j) in board.highlights:
                            board.highlights.remove((sq.i, sq.j))


def drawMove(screen, move):
    pygame.draw.rect(screen, move.square_1.color,
                     (Square.coordinate(move.square_1.i), Square.coordinate(move.square_1.j), Square.size, Square.size))
    pygame.draw.rect(screen, move.square_2.color,
                     (Square.coordinate(move.square_2.i), Square.coordinate(move.square_2.j), Square.size, Square.size))
    if move.square_1.piece is not None:
        screen.blit(move.square_1.piece.image,
                    (Square.coordinateP(move.square_1.i), Square.coordinateP(move.square_1.j)))
    if move.square_2.piece is not None:
        screen.blit(move.square_2.piece.image,
                    (Square.coordinateP(move.square_2.i), Square.coordinateP(move.square_2.j)))


def unhighlightLastMove(board, screen):
    if board.last_move_square is not None:
        pygame.draw.rect(screen, board.last_move_square.color, (Square.coordinate(board.last_move_square.i),
                                                                Square.coordinate(board.last_move_square.j),
                                                                Square.size, Square.size))

    if board.last_move_square.piece is not None:
        screen.blit(board.last_move_square.piece.image,
                    (Square.coordinateP(board.last_move_square.i), Square.coordinateP(board.last_move_square.j)))


def drawEnPassant(screen, move, last_move):
    pygame.draw.rect(screen, move.square_1.color,
                     (Square.coordinate(move.square_1.i), Square.coordinate(move.square_1.j), Square.size,
                      Square.size))
    pygame.draw.rect(screen, move.square_2.color,
                     (Square.coordinate(move.square_2.i), Square.coordinate(move.square_2.j), Square.size,
                      Square.size))
    pygame.draw.rect(screen, last_move.square_2.color,
                     (Square.coordinate(last_move.square_2.i), Square.coordinate(last_move.square_2.j),
                      Square.size,
                      Square.size))
    screen.blit(move.square_2.piece.image,
                (Square.coordinateP(move.square_2.i), Square.coordinateP(move.square_2.j)))


def drawCastle(screen, board, move):
    pygame.draw.rect(screen, move.square_1.color,
                     (Square.coordinate(move.square_1.i), Square.coordinate(move.square_1.j), Square.size, Square.size))
    pygame.draw.rect(screen, move.square_2.color,
                     (Square.coordinate(move.square_2.i), Square.coordinate(move.square_2.j), Square.size, Square.size))
    screen.blit(move.piece.image,
                (Square.coordinateP(move.square_2.i), Square.coordinateP(move.square_2.j)))

    if move.square_2.i == 6:
        if move.square_2.j == 7:
            pygame.draw.rect(screen, board.state[7][7].color,
                             (Square.coordinate(7), Square.coordinate(7), Square.size,
                              Square.size))
            pygame.draw.rect(screen, board.state[5][7].color,
                             (Square.coordinate(5), Square.coordinate(7), Square.size,
                              Square.size))
            screen.blit(board.state[5][7].piece.image,
                        (Square.coordinateP(5), Square.coordinateP(7)))

        else:
            pygame.draw.rect(screen, board.state[7][0].color,
                             (Square.coordinate(7), Square.coordinate(0), Square.size,
                              Square.size))
            pygame.draw.rect(screen, board.state[5][0].color,
                             (Square.coordinate(5), Square.coordinate(0), Square.size,
                              Square.size))
            screen.blit(board.state[5][0].piece.image,
                        (Square.coordinateP(5), Square.coordinateP(0)))
    else:
        if move.square_2.j == 7:
            pygame.draw.rect(screen, board.state[0][7].color,
                             (Square.coordinate(0), Square.coordinate(7), Square.size,
                              Square.size))
            pygame.draw.rect(screen, board.state[3][7].color,
                             (Square.coordinate(3), Square.coordinate(7), Square.size,
                              Square.size))
            screen.blit(board.state[3][7].piece.image,
                        (Square.coordinateP(3), Square.coordinateP(7)))

        else:
            pygame.draw.rect(screen, board.state[0][0].color,
                             (Square.coordinate(0), Square.coordinate(0), Square.size,
                              Square.size))
            pygame.draw.rect(screen, board.state[3][0].color,
                             (Square.coordinate(3), Square.coordinate(0), Square.size,
                              Square.size))
            screen.blit(board.state[3][0].piece.image,
                        (Square.coordinateP(3), Square.coordinateP(0)))


def drawPrePromotion(screen, turn):
    if turn == white:
        pieces = [wq, wr, wb, wn]
    else:
        pieces = [bq, br, bb, bn]

    for i in range(4):
        pygame.draw.rect(screen, red,
                         (Square.coordinate(2 + i), Square.coordinate(8), Square.size, Square.size))
        pygame.draw.rect(screen, (0, 0, 0),
                         (Square.coordinate(2 + i), Square.coordinate(8), Square.size, Square.size), 1)
        screen.blit(pieces[i], (Square.coordinateP(2 + i), Square.coordinateP(8)))


def unDrawPrePromotion(screen):
    for i in range(4):
        pygame.draw.rect(screen, (180, 180, 180),
                         (Square.coordinate(2 + i), Square.coordinate(8), Square.size, Square.size))


black = (0, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
