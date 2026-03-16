# This is a fork of my final Pythron project at Columbia, now in further development.

## Author
Ryan Brandt

## Project Title
Metasquares - a geometric puzzle game

## Project Description
The original Metasquares is a game that was featured on the America Online platform in the late 90s. It is played by two players (or one player vs a computer) on an 8x8 grid. The goal is to strategically place marbles/pips such that they form a sqaure with other marbles on the board, and to block your opponent from doing the same. Points are scored based on the size of the squares created, and the game ends at an arbitrary point value or when no more squares can be made. 

The motivation for this is partially nostalgia but also because I like puzzle games and I think it's a novel way to explore a tic-tac-toe mixed with Go type of game. 

The goals for creating this game starts with having a game board that one player can use to place marbles and create squares and then into local 2-player mode. From there, the game should be able to determine if there are any more squares that can be placed to end the game before marbles are placed extraneously. 

The next step from there is to allow a second player on their own client to connect remotely to play with another player.
A step further would be to create a computer player for solo play, potentially with levels of sophistication.

## Installation instructions

This should be playable on any Windows machine, although with PyGame I would like to allow cross-platform availability, especially mobile support.

Either run the install.sh directly in your terminal or make sure you have numpy, pygame, pygame_menu, and event_bus installed along with Python3


PyGame is the main library I plan to use for this project. It seems to have everything I need to create this game.

It is probably sufficient to create an array of vertices for acceptable squares, but this could potentially also be calculated at runtime based on angle/distance. The array seems simpler. This also means it should be straightforward for the game to know which 
squares are yet to be created, thus knowing to end the game if no more valid squares can be made to win, and force an end game state.

## Further information

![MetaSquaresDecisionMaking](https://github.com/coms-w3132/final-project-NayrBrandt/assets/4032216/d8896d19-e8e7-40ae-b321-7e8e9a3236dc)

This game is inspired by a game that can be found on https://www.metasquared.com/ 

A very in depth mathematical strategy for the game can be found here: https://www.degruyter.com/document/doi/10.2478/s12175-007-0042-3/html?lang=en

A simple explanation of the rules: http://www.papg.com/show?5SAX
