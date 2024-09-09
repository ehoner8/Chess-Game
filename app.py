"""
Two player chess game program using pygame
"""

import os
import pygame
import copy
from constants import *


pygame.font.init()

moves = {"white": [], "black": []}
move_count = 0
promoting = 0


def square_to_coordinate(square: tuple) -> tuple:
    x, y = square
    x_position = x * 100 + 2
    y_position = (7-y) * 100 + 2
    return (x_position, y_position)


def get_current_square():
    for i in range(8):
        for j in range(8):
            if squares[i][j].collidepoint(pygame.mouse.get_pos()):
                return (i, j)


def setup_board():
    global board

    board[0][0] = WHITE_ROOK
    board[1][0] = WHITE_KNIGHT
    board[2][0] = WHITE_BISHOP
    board[3][0] = WHITE_QUEEN
    board[4][0] = WHITE_KING
    board[5][0] = WHITE_BISHOP
    board[6][0] = WHITE_KNIGHT
    board[7][0] = WHITE_ROOK
    for s in range(8):
        board[s][1] = WHITE_PAWN

    board[0][7] = BLACK_ROOK
    board[1][7] = BLACK_KNIGHT
    board[2][7] = BLACK_BISHOP
    board[3][7] = BLACK_QUEEN
    board[4][7] = BLACK_KING
    board[5][7] = BLACK_BISHOP
    board[6][7] = BLACK_KNIGHT
    board[7][7] = BLACK_ROOK
    for s in range(8):
        board[s][6] = BLACK_PAWN

    for r in range(8):
        for c in range(2, 6):
            board[r][c] = None



def draw_board(board):
    for i in range(8):
        for j in range(8):
            if not board[i][j]:
                continue
            if board[i][j] == WHITE_ROOK:
                WINDOW.blit(WHITE_ROOK, square_to_coordinate((i, j)))
            if board[i][j] == WHITE_KNIGHT:
                WINDOW.blit(WHITE_KNIGHT, square_to_coordinate((i, j)))
            if board[i][j] == WHITE_BISHOP:
                WINDOW.blit(WHITE_BISHOP, square_to_coordinate((i, j)))
            if board[i][j] == WHITE_QUEEN:
                WINDOW.blit(WHITE_QUEEN, square_to_coordinate((i, j)))
            if board[i][j] == WHITE_KING:
                WINDOW.blit(WHITE_KING, square_to_coordinate((i, j)))
            if board[i][j] == WHITE_PAWN:
                WINDOW.blit(WHITE_PAWN, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_ROOK:
                WINDOW.blit(BLACK_ROOK, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_KNIGHT:
                WINDOW.blit(BLACK_KNIGHT, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_BISHOP:
                WINDOW.blit(BLACK_BISHOP, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_QUEEN:
                WINDOW.blit(BLACK_QUEEN, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_KING:
                WINDOW.blit(BLACK_KING, square_to_coordinate((i, j)))
            if board[i][j] == BLACK_PAWN:
                WINDOW.blit(BLACK_PAWN, square_to_coordinate((i, j)))
    #pygame.display.update()


def move_piece(chessboard, from_square_x, from_square_y, to_square_x, to_square_y, actual_board):
    if chessboard[to_square_x][to_square_y]:
        captured = 1
    else:
        captured = 0
    piece = chessboard[from_square_x][from_square_y]
    chessboard[from_square_x][from_square_y] = None
    chessboard[to_square_x][to_square_y] = piece

    #check for en passant
    if captured == 0 and piece == WHITE_PAWN and to_square_x != from_square_x:
        chessboard[to_square_x][to_square_y - 1] = None
    if captured == 0 and piece == BLACK_PAWN and to_square_x != from_square_x:
        chessboard[to_square_x][to_square_y + 1] = None

    #check for castling
    if piece == WHITE_KING and from_square_x == 4 and from_square_y == 0 and to_square_x == 6 and to_square_y == 0:
        chessboard[5][0] = WHITE_ROOK
        chessboard[7][0] = None
    if piece == WHITE_KING and from_square_x == 4 and from_square_y == 0 and to_square_x == 2 and to_square_y == 0:
        chessboard[3][0] = WHITE_ROOK
        chessboard[0][0] = None
    if piece == BLACK_KING and from_square_x == 4 and from_square_y == 7 and to_square_x == 6 and to_square_y == 7:
        chessboard[5][7] = BLACK_ROOK
        chessboard[7][7] = None
    if piece == BLACK_KING and from_square_x == 4 and from_square_y == 7 and to_square_x == 2 and to_square_y == 7:
        chessboard[3][7] = BLACK_ROOK
        chessboard[0][7] = None
    if actual_board == 1:
        global moves
        global move_count
        if move_count % 2 == 0:
            moves["white"].append(((from_square_x, from_square_y), (to_square_x, to_square_y)))
        if move_count % 2 == 1:
            moves["black"].append(((from_square_x, from_square_y), (to_square_x, to_square_y)))
        move_count += 1
        if move_count == 10:
            print(moves)






#returns a list of all possible rook moves
def get_all_rook_moves(board, turn: int, rook_position_x, rook_position_y, include_castling = 0):
    if turn == 0:
        friends_pieces = 0
        opponents_pieces = 1
    if turn == 1:
        friends_pieces = 1
        opponents_pieces = 0
    possible_moves = []
    starting_square = (rook_position_x, rook_position_y)
    for x in range(rook_position_x + 1, 8):
        if board[x][rook_position_y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, rook_position_y)))
        if board[x][rook_position_y] in pieces[opponents_pieces]:
            break
    for x in range(rook_position_x - 1, -1, -1):
        if board[x][rook_position_y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, rook_position_y)))
        if board[x][rook_position_y] in pieces[opponents_pieces]:
            break
    for y in range(rook_position_y + 1, 8):
        if board[rook_position_x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (rook_position_x, y)))
        if board[rook_position_x][y] in pieces[opponents_pieces]:
            break
    for y in range(rook_position_y - 1, -1, -1):
        if board[rook_position_x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (rook_position_x, y)))
        if board[rook_position_x][y] in pieces[opponents_pieces]:
            break

    return possible_moves



def get_all_bishop_moves(board, turn: int, bishop_position_x, bishop_position_y, include_castling = 0):
    if turn == 0:
        friends_pieces = 0
        opponents_pieces = 1
    if turn == 1:
        friends_pieces = 1
        opponents_pieces = 0
    possible_moves = []
    starting_square = (bishop_position_x, bishop_position_y)
    x = bishop_position_x + 1
    y = bishop_position_y + 1
    while x < 8 and y < 8:
        if board[x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, y)))
        if board[x][y] in pieces[opponents_pieces]:
            break
        x += 1
        y += 1

    x = bishop_position_x + 1
    y = bishop_position_y - 1
    while x < 8 and y > -1:
        if board[x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, y)))
        if board[x][y] in pieces[opponents_pieces]:
            break
        x += 1
        y -= 1

    x = bishop_position_x - 1
    y = bishop_position_y + 1
    while x > -1 and y < 8:
        if board[x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, y)))
        if board[x][y] in pieces[opponents_pieces]:
            break
        x -= 1
        y += 1

    x = bishop_position_x - 1
    y = bishop_position_y - 1
    while x > -1 and y > -1:
        if board[x][y] in pieces[friends_pieces]:
            break
        possible_moves.append((starting_square, (x, y)))
        if board[x][y] in pieces[opponents_pieces]:
            break
        x -= 1
        y -= 1

    return possible_moves


def get_all_queen_moves(board, turn: int, queen_position_x, queen_position_y, include_castling = 0):
    possible_moves = []
    possible_moves.extend(get_all_rook_moves(board, turn, queen_position_x, queen_position_y))
    possible_moves.extend(get_all_bishop_moves(board, turn, queen_position_x, queen_position_y))
    return possible_moves


def get_all_knight_moves(board, turn: int, knight_position_x, knight_position_y, include_castling = 0):
    if turn == 0:
        friends_pieces = 0
        opponents_pieces = 1
    if turn == 1:
        friends_pieces = 1
        opponents_pieces = 0
    possible_moves = []
    starting_square = (knight_position_x, knight_position_y)
    x = knight_position_x + 2
    y = knight_position_y + 1
    if x < 8 and y < 8 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x + 2
    y = knight_position_y - 1
    if x < 8 and y > -1 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x + 1
    y = knight_position_y + 2
    if x < 8 and y < 8 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x + 1
    y = knight_position_y - 2
    if x < 8 and y > -1 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x - 1
    y = knight_position_y + 2
    if x > -1 and y < 8 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x - 1
    y = knight_position_y - 2
    if x > -1 and y > -1 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x - 2
    y = knight_position_y + 1
    if x > -1 and y < 8 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    x = knight_position_x - 2
    y = knight_position_y - 1
    if x > -1 and y > -1 and board[x][y] not in pieces[friends_pieces]:
        possible_moves.append((starting_square, (x, y)))

    return possible_moves


def get_all_king_moves(board, turn: int, king_position_x, king_position_y, include_castling = 0):
    if turn == 0:
        friends_pieces = 0
        opponents_pieces = 1
    if turn == 1:
        friends_pieces = 1
        opponents_pieces = 0
    possible_moves = []
    starting_square = (king_position_x, king_position_y)
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if king_position_x + x > -1 and king_position_x + x < 8 and king_position_y + y > -1 and king_position_y + y < 8 and \
                board[king_position_x + x][king_position_y + y] not in pieces[friends_pieces]:
                    possible_moves.append((starting_square, (king_position_x + x, king_position_y + y)))

    if include_castling == 1:
        if can_castle_kingside(board, turn):
            if turn == 0:
                possible_moves.append(((4, 0), (6, 0)))
            if turn == 1:
                possible_moves.append(((4, 7), (6, 7)))

        if can_castle_queenside(board, turn):
            if turn == 0:
                possible_moves.append(((4, 0), (2, 0)))
            if turn == 1:
                possible_moves.append(((4, 7), (2, 7)))
    return possible_moves



def get_all_pawn_moves(board, turn, pawn_position_x, pawn_position_y, include_castling = 0):
    possible_moves = []
    if turn == 0:
        if pawn_position_y == 7:
            return []
        friends_pieces = 0
        opponents_pieces = 1
        opponent = "black"
        starting_square = (pawn_position_x, pawn_position_y)
        if not board[pawn_position_x][pawn_position_y + 1]:
            possible_moves.append((starting_square, (pawn_position_x, pawn_position_y+1)))
            if pawn_position_y == 1 and not board[pawn_position_x][pawn_position_y+2]:
                possible_moves.append((starting_square, (pawn_position_x, pawn_position_y+2)))
        if pawn_position_x in range(1, 7):
            if board[pawn_position_x - 1][pawn_position_y + 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y + 1)))
            if board[pawn_position_x + 1][pawn_position_y + 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y + 1)))
        if pawn_position_x == 0:
            if board[pawn_position_x + 1][pawn_position_y + 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y + 1)))
        if pawn_position_x == 7:
            if board[pawn_position_x - 1][pawn_position_y + 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y + 1)))
        #en passant
        if len(moves[opponent]) > 0 and moves[opponent][-1] == ((pawn_position_x - 1, 6), (pawn_position_x - 1, 4)) and pawn_position_y == 4:
            possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y + 1)))
        if len(moves[opponent]) > 0 and moves[opponent][-1] == ((pawn_position_x + 1, 6), (pawn_position_x + 1, 4)) and pawn_position_y == 4:
            possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y + 1)))
    if turn == 1:
        if pawn_position_y == 0:
            return []
        friends_pieces = 1
        opponents_pieces = 0
        opponent = "white"
        starting_square = (pawn_position_x, pawn_position_y)
        if not board[pawn_position_x][pawn_position_y - 1]:
            possible_moves.append((starting_square, (pawn_position_x, pawn_position_y - 1)))
            if pawn_position_y == 6 and not board[pawn_position_x][pawn_position_y - 2]:
                possible_moves.append((starting_square, (pawn_position_x, pawn_position_y - 2)))
        if pawn_position_x in range(1, 7):
            if board[pawn_position_x - 1][pawn_position_y - 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y - 1)))
            if board[pawn_position_x + 1][pawn_position_y - 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y - 1)))
        if pawn_position_x == 0:
            if board[pawn_position_x + 1][pawn_position_y - 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y - 1)))
        if pawn_position_x == 7:
            if board[pawn_position_x - 1][pawn_position_y - 1] in pieces[opponents_pieces]:
                possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y - 1)))
        #en passant
        if len(moves[opponent]) > 0 and moves[opponent][-1] == ((pawn_position_x - 1, 1), (pawn_position_x - 1, 3)) and pawn_position_y == 3:
            possible_moves.append((starting_square, (pawn_position_x - 1, pawn_position_y - 1)))
        if len(moves[opponent]) > 0 and moves[opponent][-1] == ((pawn_position_x + 1, 1), (pawn_position_x + 1, 3)) and pawn_position_y == 3:
            possible_moves.append((starting_square, (pawn_position_x + 1, pawn_position_y - 1)))
    return possible_moves




piece_to_function = {
    WHITE_ROOK: get_all_rook_moves,
    BLACK_ROOK: get_all_rook_moves,
    WHITE_KNIGHT: get_all_knight_moves,
    BLACK_KNIGHT: get_all_knight_moves,
    WHITE_BISHOP: get_all_bishop_moves,
    BLACK_BISHOP: get_all_bishop_moves,
    WHITE_QUEEN: get_all_queen_moves,
    BLACK_QUEEN: get_all_queen_moves,
    WHITE_KING: get_all_king_moves,
    BLACK_KING: get_all_king_moves,
    WHITE_PAWN: get_all_pawn_moves,
    BLACK_PAWN: get_all_pawn_moves
}


#side 0 is white, side 1 is black
def find_king_square(board, side: int) -> tuple:
    if side == 0:
        piece = WHITE_KING
    if side == 1:
        piece = BLACK_KING
    for i in range(8):
        for j in range(8):
            if board[i][j] == piece:
                return (i, j)



#side 0 is white, side 1 is black
def is_in_check(board, side: int):
    king_square = find_king_square(board, side)
    if side == 0:
        opponent = 1
    if side == 1:
        opponent = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces[opponent]:
                check_moves_of_piece = piece_to_function[board[i][j]]
                for move in check_moves_of_piece(board, opponent, i, j):
                    if move[1] == king_square:
                        return True

    return False


def is_legal(board, side: int, from_square_x, from_square_y, to_square_x, to_square_y):
    temp_board = [[0 for _ in range(8)] for __ in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j]:
                temp_board[i][j] = (board[i][j])
            else:
                temp_board[i][j] = None
    move_piece(temp_board, from_square_x, from_square_y, to_square_x, to_square_y, 0)
    if is_in_check(temp_board, side):
        return False

    return True


def is_in_checkmate(board, side):
    if not is_in_check(board, side):
        return False
    if side == 0:
        opponent = 1
    if side == 1:
        opponent = 0
    temp_board = [[0 for _ in range(8)] for __ in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j]:
                temp_board[i][j] = (board[i][j])
            else:
                temp_board[i][j] = None
    all_moves = []
    for i in range(8):
        for j in range(8):
            if temp_board[i][j] in pieces[side]:
                piece_function = piece_to_function[temp_board[i][j]]
                all_moves.extend(piece_function(board, side, i, j))
    for move in all_moves:
        from_square = move[0]
        to_square = move[1]
        from_square_x = from_square[0]
        from_square_y = from_square[1]
        to_square_x = to_square[0]
        to_square_y = to_square[1]
        if is_legal(board, side, from_square_x, from_square_y, to_square_x, to_square_y):
            return False
    return True



def can_castle_kingside(board, side):
    if side == 0:
        opponent = 1
        through_square = (5, 0)
    if side == 1:
        opponent = 0
        through_square = (5, 7)


    if is_in_check(board, side):
        return False
    if side == 0 and (board[5][0] or board[6][0]):
        return False
    if side == 1 and (board[5][7] or board[6][7]):
        return False
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces[opponent]:
                piece_function = piece_to_function[board[i][j]]
                for move in piece_function(board, opponent, i, j):
                    if move[1] == through_square:
                        return False
    global moves
    if side == 0:
        for move in moves["white"]:
            if move[0] == (4, 0) or move[0] == (7, 0):
                return False
    if side == 1:
        for move in moves["black"]:
            if move[0] == (4, 7) or move[0] == (7, 7):
                return False

    return True


def check_promotion(board):
    for i in range(8):
        if board[i][7] == WHITE_PAWN:
            return (i, 7)
    for i in range(8):
        if board[i][0] == BLACK_PAWN:
            #print(f"lkkk {}")
            return (i, 0)

    return False


def promote(board, promotion_square_x, promotion_square_y):
    if promotion_square_y == 7:
        square_1 = pygame.Rect(260, 365, 70, 70)
        square_2 = pygame.Rect(330, 365, 70, 70)
        square_3 = pygame.Rect(400, 365, 70, 70)
        square_4 = pygame.Rect(470, 365, 70, 70)
        pygame.draw.rect(WINDOW, BLUE, square_1)
        pygame.draw.rect(WINDOW, BLUE, square_2)
        pygame.draw.rect(WINDOW, BLUE, square_3)
        pygame.draw.rect(WINDOW, BLUE, square_4)
        WINDOW.blit(WHITE_QUEEN_SMALL, (267, 372))
        WINDOW.blit(WHITE_ROOK_SMALL, (337, 372))
        WINDOW.blit(WHITE_BISHOP_SMALL, (407, 372))
        WINDOW.blit(WHITE_KNIGHT_SMALL, (477, 372))
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x_pos = pos[0]
            y_pos = pos[1]
            if y_pos > 365 and y_pos < 435:
                if x_pos > 267 and x_pos < 337:
                    board[promotion_square_x][promotion_square_y] = WHITE_QUEEN
                if x_pos > 337 and x_pos < 407:
                    board[promotion_square_x][promotion_square_y] = WHITE_ROOK
                if x_pos > 407 and x_pos < 477:
                    board[promotion_square_x][promotion_square_y] = WHITE_BISHOP
                if x_pos > 477 and x_pos < 547:
                    board[promotion_square_x][promotion_square_y] = WHITE_KNIGHT

    if promotion_square_y == 0:
        square_1 = pygame.Rect(260, 365, 70, 70)
        square_2 = pygame.Rect(330, 365, 70, 70)
        square_3 = pygame.Rect(400, 365, 70, 70)
        square_4 = pygame.Rect(470, 365, 70, 70)
        pygame.draw.rect(WINDOW, BLUE, square_1)
        pygame.draw.rect(WINDOW, BLUE, square_2)
        pygame.draw.rect(WINDOW, BLUE, square_3)
        pygame.draw.rect(WINDOW, BLUE, square_4)
        WINDOW.blit(BLACK_QUEEN_SMALL, (267, 372))
        WINDOW.blit(BLACK_ROOK_SMALL, (337, 372))
        WINDOW.blit(BLACK_BISHOP_SMALL, (407, 372))
        WINDOW.blit(BLACK_KNIGHT_SMALL, (477, 372))
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x_pos = pos[0]
            y_pos = pos[1]
            if y_pos > 365 and y_pos < 435:
                if x_pos > 267 and x_pos < 337:
                    board[promotion_square_x][promotion_square_y] = BLACK_QUEEN
                if x_pos > 337 and x_pos < 407:
                    board[promotion_square_x][promotion_square_y] = BLACK_ROOK
                if x_pos > 407 and x_pos < 477:
                    board[promotion_square_x][promotion_square_y] = BLACK_BISHOP
                if x_pos > 477 and x_pos < 547:
                    board[promotion_square_x][promotion_square_y] = BLACK_KNIGHT
    
    pygame.display.update()





def can_castle_queenside(board, side):
    if side == 0:
        opponent = 1
        through_square = (3, 0)
    if side == 1:
        opponent = 0
        through_square = (3, 7)

    if is_in_check(board, side):
        return False
    if side == 0 and (board[3][0] or board[2][0] or board[1][0]):
        return False
    if side == 1 and (board[3][7] or board[2][7] or board[1][7]):
        return False
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces[opponent]:
                piece_function = piece_to_function[board[i][j]]
                for move in piece_function(board, opponent, i, j):
                    if move[1] == through_square:
                        return False
    global moves
    if side == 0:
        for move in moves["white"]:
            if move[0] == (4, 0) or move[0] == (0, 0):
                return False
    if side == 1:
        for move in moves["black"]:
            if move[0] == (4, 7) or move[0] == (0, 7):
                return False

    return True


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, RED)
    WINDOW.blit(draw_text, (70, 230))
    pygame.display.update()




def main():
    global board
    global promoting
    setup_board()
    turn = 0 #keeps track of whose turn it is, 0 is white 1 is black
    clicked = 0 #keeps track of whether or not player clicked a piece
    end_game = 0
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == 0:
                from_square_x, from_square_y = get_current_square()
                if board[from_square_x][from_square_y] and board[from_square_x][from_square_y] in pieces[turn]:
                    clicked = 1
                    selected_square_x = from_square_x
                    selected_square_y = from_square_y
            if clicked == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                to_square_x, to_square_y = get_current_square()
                if to_square_x != selected_square_x or to_square_y != selected_square_y:
                    clicked = 0
                    find_possible_function = piece_to_function[board[selected_square_x][selected_square_y]]
                    possible_moves = find_possible_function(board, turn, selected_square_x, selected_square_y, include_castling=1)
                    if ((selected_square_x, selected_square_y), (to_square_x, to_square_y)) in possible_moves and \
                        is_legal(board, turn, selected_square_x, selected_square_y, to_square_x, to_square_y):
                        move_piece(board, selected_square_x, selected_square_y, to_square_x, to_square_y, 1)
                        clicked = 0
                        if turn == 1:
                            turn = 0
                        else:
                            turn = 1
        if is_in_checkmate(board, turn):
            end_game = 1
            draw_board(board)
            if turn == 1:
                player_color = "WHITE"
            if turn == 0:
                player_color = "BLACK"
            draw_winner(f"{player_color} WINS")

        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(WINDOW, GREEN, squares[x][y])
                else:
                    pygame.draw.rect(WINDOW, WHITE, squares[x][y])
        draw_board(board)
        if check_promotion(board):
            promotion_x, promotion_y = check_promotion(board)
            promote(board, promotion_x, promotion_y)
            promoting = 1
        if is_in_checkmate(board, turn):
            draw_board(board)
            if turn == 1:
                player_color = "WHITE"
            if turn == 0:
                player_color = "BLACK"
            draw_winner(f"{player_color} WINS")
            WINDOW.blit(PLAY_AGAIN_BUTTON, (70, 378))
            WINDOW.blit(EXIT_BUTTON, (450, 378))
            pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                if pos_x > 70 and pos_x < 350 and pos_y > 378 and pos_y < 503:
                    main()
                if pos_x > 450 and pos_x < 730 and pos_y > 378 and pos_y < 503:
                    run = False
                    pygame.quit()
        pygame.display.update()



if __name__ == "__main__":
    main()






