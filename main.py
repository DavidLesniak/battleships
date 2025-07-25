import pygame as pg


pg.init()
display = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()



run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
    clock.tick(60)

pg.quit()