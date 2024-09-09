import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLUMNS = 8, 8
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game!")
WHITE = (243, 243, 215)
GREEN = (104, 150, 73)
BLUE = (25, 33, 185)
RED = (255, 0, 0)
FPS = 60

WHITE_PAWN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wp.png")), (95, 95))
WHITE_ROOK = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wr.png")), (95, 95))
WHITE_ROOK_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wr.png")), (55, 55))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wn.png")), (95, 95))
WHITE_KNIGHT_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wn.png")), (55, 55))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wb.png")), (95, 95))
WHITE_BISHOP_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wb.png")), (55, 55))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wq.png")), (95, 95))
WHITE_QUEEN_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wq.png")), (55, 55))
WHITE_KING = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "wk.png")), (95, 95))
BLACK_PAWN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bp.png")), (95, 95))
BLACK_ROOK = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "br.png")), (95, 95))
BLACK_ROOK_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "br.png")), (55, 55))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bn.png")), (95, 95))
BLACK_KNIGHT_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bn.png")), (55, 55))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bb.png")), (95, 95))
BLACK_BISHOP_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bb.png")), (55, 55))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bq.png")), (95, 95))
BLACK_QUEEN_SMALL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bq.png")), (55, 55))
BLACK_KING = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bk.png")), (95, 95))



white_pieces = [WHITE_PAWN, WHITE_KNIGHT, WHITE_BISHOP, WHITE_ROOK, WHITE_QUEEN, WHITE_KING]
black_pieces = [BLACK_PAWN, BLACK_KNIGHT, BLACK_BISHOP, BLACK_ROOK, BLACK_QUEEN, BLACK_KING]
pieces = [white_pieces, black_pieces]

pygame.font.init()
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

square_size = 100
squares = [[0 for _ in range(8)] for __ in range(8)]
board = [[0 for _ in range(8)] for __ in range(8)]



for i in range(8):
    for j in range(8):
        squares[i][j] = pygame.Rect(i*100, (7-j)*100, square_size, square_size)
        

EXIT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "exit.png")), (280, 125))
PLAY_AGAIN_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "play-again.png")), (280, 125))