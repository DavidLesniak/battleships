import pygame as pg

class Field:
	def __init__(self, x, y, size=50, color='#F7F7F7'):
		self.rect = pg.Rect(x+1, y+1, size-1, size-1)
		self.color = color

	def draw(self, surface):
		pg.draw.rect(surface, self.color, self.rect)
		

class Board:
	def __init__(self, x, y, size=501):
		self.x = x
		self.y = y
		self.board = pg.Rect(x, y, size, size)
		self.fields = []

		self.init_board()

	def init_board(self):
		for i in range(10):
			row = []

			for j in range(10):
				f = Field(self.x+(i*50), self.y+(j*50))
				row.append(f)

			self.fields.append(row)

	def draw(self, surface):
		pg.draw.rect(surface, 'lightgreen', self.board)

		for row in self.fields:
			for f in row:
				f.draw(surface)

		

