import pygame as pg
from board import Board

pg.init()
display = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()

board_player_1 = Board(0, 0)
board_player_2 = Board(700-1, 0)

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    board_player_1.draw(display)
    board_player_2.draw(display)

    pg.display.flip()
    clock.tick(60)

pg.quit()