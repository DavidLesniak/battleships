import pygame as pg
from board import Board
from ship import Ship

pg.init()
display = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()

board_player_1 = Board(0, 0)
board_player_2 = Board(700-1, 0)

run = True

ship_one_1 = Ship(1, (10, 0), "hor")
ship_one_2 = Ship(1, (10, 1), "hor")
ship_one_3 = Ship(1, (10, 2), "hor")
ship_one_4 = Ship(1, (10, 3), "hor")
ship_two_1 = Ship(2, (10, 4), "hor")
ship_two_2 = Ship(2, (10, 5), "hor")
ship_two_3 = Ship(2, (10, 6), "hor")
ship_three_1 = Ship(3, (10, 7), "hor")
ship_three_2 = Ship(3, (10, 8), "hor")
ship_four = Ship(4, (10, 9), "hor")


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    board_player_1.draw(display)
    board_player_2.draw(display)

    ship_one_1.draw(display, 0, 3)
    ship_one_2.draw(display, 0, 3)
    ship_one_3.draw(display, 0, 3)
    ship_one_4.draw(display, 0, 3)
    ship_two_1.draw(display, 0, 3)
    ship_two_2.draw(display, 0, 3)
    ship_two_3.draw(display, 0, 3)
    ship_three_1.draw(display, 0, 3)
    ship_three_2.draw(display, 0, 3)
    ship_four.draw(display, 0, 3)


    pg.display.flip()
    clock.tick(60)

pg.quit()
