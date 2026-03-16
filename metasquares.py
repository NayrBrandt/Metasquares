import sys

import pygame
import pygame_menu

from events import MouseClickEvent, bus
from game_render import GameRender
from game_data import GameData
from game_logic import MetaSquares
import game_elements as be

def quit():
    sys.exit()

def start():
    data = GameData()
    screen = pygame.display.set_mode(data.size)
    game = MetaSquares(data, GameRender(screen, data))

    game.print_board()
    game.draw()

    pygame.display.update()
    pygame.time.wait(1000)

    while not game.game_data.game_won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quit()

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bus.emit("mouse:click",
                          game, 
                          MouseClickEvent(event.pos[0], event.pos[1]))
            
            game.update()
            game.draw()



def menu_loop():

    pygame.init()
    screen = pygame.display.set_mode(GameData().size)
    pygame.display.set_caption("Metasquares")

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        menu = pygame_menu.Menu(
        height=(640),
        width=(480),
        title = "Welcome"
        )

        menu.add.button('Start', start)
        menu.add.button('Quit', pygame_menu.events.EXIT)

        if menu.is_enabled():
            menu.mainloop(screen)

        pygame.display.flip()

    quit()
        


if __name__ == "__main__":
    menu_loop()
