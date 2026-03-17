import math
import os
import sys

import pygame

from events import GameOver, MouseClickEvent, PiecePlaceEvent, bus
from game_data import GameData
from game_render import GameRender


class MetaSquares:

    game_data = GameData
    render = GameRender
    
    def __init__(self, game_data: GameData, render: GameRender):
        self.game_data = game_data
        self.render = render

    def quit(self):
        sys.exit()


    def score_square(self, square):

        '''
        Change scoring to be based on rows touched!
        
        '''

        # point 2 - point 1
        side1 = (((square[1][0] - square[0][0]) ** 2) + ((square[1][1] - square[0][1]) ** 2)) ** 0.5
        # point 4 - point 3
        side2 = (((square[3][0] - square[2][0]) ** 2) + ((square[3][1] - square[2][1]) ** 2)) ** 0.5

        area = (side1 +1) * (side2 +1)
        print("Area is " + str(area))

        return int(area)



    def update_players(self):
        all_sq = self.game_data.valid_squares

        p1_marb = self.game_data.player1_marbs
        p1_sq = self.game_data.player1_squares
        #p1_score = self.game_data.player1_score

        p2_marb = self.game_data.player2_marbs
        p2_sq = self.game_data.player2_squares
        #p2_score = self.game_data.player2_score

        for square in all_sq:
            if all(marble in p1_marb for marble in square):
                if square in p1_sq:
                    continue

                self.game_data.player1_score += self.score_square(square)
                print("this is the current square:  ")
                print(square)
                p1_sq.append(square)

            if all(marble in p2_marb for marble in square):
                if square in p2_sq:
                    continue
                
    
                self.game_data.player2_score += self.score_square(square)
                p2_sq.append(square)



    @bus.on("mouse:click")
    def mouse_click(self, event: MouseClickEvent):
        pygame.draw.rect(
            self.render.screen,
            (0,0,0),
            (0, 0, self.game_data.width, self.game_data.sq_size),
        )

        col: int = int(math.floor(event.x / self.game_data.sq_size))
        row: int = int(math.floor(event.y / self.game_data.sq_size))
        
        if self.game_data.game_board.is_valid_loc(row, col):

            marble = [row, col]
            self.game_data.game_board.place_marble(row, col, self.game_data.turn + 1)


            if self.game_data.turn == 0:
                self.game_data.player1_marbs.append(marble)
            elif self.game_data.turn == 1:
                self.game_data.player2_marbs.append(marble)


            self.draw()

            bus.emit(
                "piece:place", PiecePlaceEvent(self.game_data.game_board.board[row][col])
            )

            self.print_board()
            print("Col is " + str(col) + " and Row is "+ str(row))
            self.update_players()

            if self.game_data.game_board.win(self.game_data.player1_score):
                bus.emit(
                    "game:over", self.render, GameOver(False, self.game_data.turn + 1)
                )
                self.game_data.game_won = True
            elif self.game_data.game_board.win(self.game_data.player2_score):
                bus.emit(
                    "game:over", self.render, GameOver(False, self.game_data.turn + 1)
                )
                self.game_data.game_won = True

        
        pygame.display.update()



        # # Refactor this to be simpler
        # self.game_data.turn += 1
        # self.game_data.turn = self.game_data.turn % 2




    def update(self):
            
            
        if self.game_data.game_won:
            print(os.getpid())
            pygame.time.wait(5000)
            os.system("game.py")

    def draw(self):
        """
        Directs the game renderer to 'render' the game state to the audio and video devices.
        """
        self.render.draw(self.game_data)

    def print_board(self):
        """
        Prints the state of the board to the console.
        """
        self.game_data.game_board.print_board()