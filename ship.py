import pygame as pg

class Ship:
    def __init__(self, number_of_segment, position, orientation):
        self.number_of_segment = number_of_segment
        self.position = position
        self.orientation = orientation
        self.size = 50

    def draw(self, display):
        x_position, y_position = self.position
        vector_x, vector_y = (1, 0) if self.orientation == "hor" else (0, 1)
        for i in range(self.number_of_segment):
            x = (x_position + vector_x * i) * self.size
            y = (y_position + vector_y * i) * self.size
            rectangle = pg.Rect(x, y, self.size, self.size)
            pg.draw.rect(display, (0, 255, 0), rectangle)
            pg.draw.rect(display, (0, 100, 200), rectangle, 1)

pg.init()
display = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()
run = True
ship = Ship(4, (2, 3), "hor")

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    display.fill((0, 0, 0))
    ship.draw(display)
    pg.display.flip()
    clock.tick(60)
pg.quit()
