from game_elements import GameBoard
from typing import Tuple, List
import valid_squares

class GameData:

    radius: int
    height: int
    width: int
    sidebar_width: int

    tile_size: int
    size: Tuple[int, int]
    game_won: bool
    turn: int
    last_move_row: List[int]
    last_move_col: List[int]
    game_board: GameBoard

    player1_marbs: List[int]
    player1_score: int
    player2_marbs: List[int]
    player2_score: int
    
    '''
    The top left smallest square would be [[0,0][0,1],[1,0],[1,1]]
    and the square of the corners of the board would be [[0,0],[0,7],[7,0],[7,7]]
    '''
    


    def __init__(self):
        self.game_won = False
        self.turn = 0
        self.last_move_row = []
        self.last_move_col = []
        self.game_board = GameBoard()
        self.action = None

        self.player1_marbs = []
        self.player1_squares = []
        self.player1_score = 0
        self.player2_marbs = []
        self.player2_squares = []
        self.player2_score = 0

        self.sq_size: int = 100
        self.width: int = 8 * self.sq_size
        self.height: int = 8 * self.sq_size
        self.sidebar_width: int = 4 * self.sq_size
        self.size: Tuple[int, int] = (self.width + self.sidebar_width, self.height)
        self.radius: int = int(self.sq_size /2 - 5)

        self.valid_squares = valid_squares.get_squares(8)
        