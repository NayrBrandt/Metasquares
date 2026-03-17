import pygame.sprite

from numpy import flip, zeros
from numpy.core._multiarray_umath import ndarray

class Player():

    def __init__(self, no):
        self.num = no
        self.name = ''
        self.score = 0
        self.marbles = []


class GameBoard:
    board: ndarray
    cols: int
    rows: int

    def __init__ (self, rows=8, cols=8):

        self.rows = rows
        self.cols = cols
        self.board = zeros((rows, cols))

    def print_board(self):
        print((self.board))

    def place_marble(self, row, col, marble):
        self.board[row][col] = marble

    def check_for_square(self):
        #import from another file? Put logic here?
        return True

    def is_valid_loc(self, row, col):
        '''
        the board row/col combo should be set
        to a value other than 0 if there is 
        a marble already placed.
        '''
        if row <8 and col <8:
            return self.board[row][col] == 0
    
    def win(self, score):
        if score > 150:
            return True



class Marble(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface((20,20))
        self.surf.fill('blue')

    def draw(self, surface, image, pos):
        surface.blit(image, pos)

