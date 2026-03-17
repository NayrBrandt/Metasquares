import sys
import pygame
import pygame.locals
import pygame_menu

from game_elements import Player
from assets import (purple_img, green_img, tile_img, purple_line, green_line)
from events import GameOver, bus
from game_data import GameData

BLACK = (0, 0, 0)
PURPLE = (47, 14, 97)
GREEN = (10, 59, 8)




class GameRender:

    game_data: GameData



    def __init__(self, screen, game_data: GameData):
        
        self.screen = screen
        self.game_data = game_data

        pygame.display.set_caption("Metasquares")
        pygame.display.update()

    



    def draw(self, game_data: GameData):
        self.draw_board(game_data.game_board)
        self.draw_sidebar(game_data)

    def draw_stone(self, x, y, color):
        if color == 'green':
            self.screen.blit(green_img, (x, y))
        elif color == 'purple':
            self.screen.blit(purple_img, (x, y))
    

    def draw_line(self, start, end, color):
        
        dist = (((end[0] - start[0]) ** 2) + ((end[1] - start[1]) ** 2)) ** 0.5

        angle = pygame.math.Vector2(end[0] - start[0], end[1] - start[1]).angle_to((1,0))

        if color == 'green':
            line_img = green_line

        elif color == 'purple':
            line_img = purple_line

        rotation = angle

        stretch_tex = pygame.transform.scale(line_img, (int(dist), line_img.get_height() // 2))

        stretch_tex = pygame.transform.rotate(stretch_tex, rotation)

        self.screen.blit(stretch_tex, (start[0]+30, start[1]+30))
    
    def draw_square(self, square, color):
        coord1 = [square[0][0] * 100, square[0][1] * 100]
        coord2 = [square[1][0] * 100, square[1][1] * 100]
        coord3 = [square[2][0] * 100, square[2][1] * 100]
        coord4 = [square[3][0] * 100, square[3][1] * 100]

        # print("coord1 is " + str(coord1))
        # print("coord2 is " + str(coord2))   
        # print("coord3 is " + str(coord3))
        # print("coord4 is " + str(coord4))

        self.draw_line(coord1, coord2, color)
        #self.draw_line(coord1, coord3, color)
        #self.draw_line(coord2, coord4, color)
        #self.draw_line(coord3, coord4, color)


    def draw_tiles(self, x, y):
        self.screen.blit(tile_img, (x,y))

    def draw_sidebar(self, game_data: GameData):
        pygame.draw.rect(self.screen, BLACK, (game_data.width,
                                               0,
                                                game_data.sidebar_width,
                                                game_data.height))
        font = pygame.font.SysFont(None, 33)
        player1_text = font.render("Player 1 Score:", True, PURPLE)
        player1_score = font.render(str(game_data.player1_score), True, PURPLE)
        player2_text = font.render("Player 2 Score:", True, GREEN)
        player2_score = font.render(str(game_data.player2_score), True, GREEN)
        self.screen.blit(player1_text,
                          (game_data.width + 
                           game_data.sidebar_width // 2 - player1_text.get_width() // 2, 50))
        
        self.screen.blit(player1_score,
                          (game_data.width + 
                           game_data.sidebar_width // 2 - player1_score.get_width() // 2, 80))
        
        self.screen.blit(player2_text,
                          (game_data.width + 
                           game_data.sidebar_width // 2 - player2_text.get_width() // 2, 250))
        
        self.screen.blit(player2_score,
                          (game_data.width + 
                           game_data.sidebar_width // 2 - player2_score.get_width() // 2, 280))

    def draw_board(self, board):

        sq_size = 100
        width = 800
        height = 800


        for col in range(board.cols):
            for row in range(board.rows):
                self.draw_tiles(col * sq_size, row * sq_size)


        for col in range(board.cols):
            for row in range(board.rows):
                if board.board[row][col] == 1:
                    self.draw_stone(
                        int(col * sq_size) + 8,
                        int(row * sq_size ) + 8,
                        "purple"
                    )
                elif board.board[row][col] == 2:
                    self.draw_stone(
                        int(col * sq_size) + 8,
                        int(row * sq_size ) + 8,
                        "green"
                    )

        for square in self.game_data.player1_squares:
            self.draw_square(square, 'purple')

        for square in self.game_data.player2_squares:
            self.draw_square(square, 'green')

        pygame.display.update()

    @bus.on("game:over")
    def on_game_over(self, event: GameOver):
        if event.winner == 1:
            color = PURPLE
            score = self.game_data.player1_score
        if event.winner == 2:
            color = GREEN
            score = self.game_data.player2_score
        
        self.font = pygame.font.SysFont(None, 100)        
        self.text_label = self.font.render(f"PLAYER {event.winner} WINS!", 1, color)
        self.score_label = self.font.render("score: " + str(score), 1, color)
        self.text_rect = self.text_label.get_rect(center=((self.game_data.width +
                                            self.game_data.sidebar_width) // 2,
                                            self.game_data.height // 2 - 50))
        
        self.score_rect = self.score_label.get_rect(center=((self.game_data.width +
                                            self.game_data.sidebar_width) // 2,
                                            self.game_data.height // 2 + 100))
        
        
        self.popup_surf = pygame.Surface((700, 270), pygame.SRCALPHA)
        self.popup_surf.fill((255,255,255,128))

        self.screen.blit(self.popup_surf, ((self.game_data.width +
                                            self.game_data.sidebar_width) // 2 -
                                            self.popup_surf.get_width() // 2,
                                            self.game_data.height // 2 -
                                            self.popup_surf.get_height() // 2))
        self.screen.blit(self.text_label, self.text_rect)
        self.screen.blit(self.score_label, self.score_rect)
