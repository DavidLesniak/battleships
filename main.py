import pygame as pg
from board import Board
from ship import Ship
from ui import UI
from player import Player

pg.init()
display = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()

p1 = Player("Dawid")
p2 = Player("Kacper")
move = p1

ui = UI(0,0)
ui.add_player(p1, 1)
ui.add_player(p2, 2)
ui.move_player(move)
ui.draw(display)

board_player_1 = Board(0, 100)
board_player_2 = Board(700-1, 100)


run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONUP:
            move.shot(board_player_1)

            if move == p1:
                move = p2
            else:
                move = p1

    if move == p1:
        board_player_2.update()
        
    if move == p2:
        board_player_1.update()
    
    board_player_1.draw(display)
    board_player_2.draw(display)

    pg.display.flip()
    clock.tick(60)

pg.quit()
