import pygame as pg

class UI:
	def __init__(self, x, y, color='red'):
		self.bar = pg.Rect(x, y, 1200, 100)
		self.color = color
		self.players = []
	
	def add_player(self, player, slot):
		if slot == 1:
			new_player = Text(0, 0, player.name)
			new_player.update()
			self.players.insert(0, new_player)
		
		if slot == 2:
			new_player = Text(700-1, 0, player.name)
			new_player.update()
			self.players.insert(1, new_player)

	def draw(self, surface):
		pg.draw.rect(surface, self.color, self.bar)

		for p in self.players:
			p.draw(surface) 

class Text:
	def __init__(self, x, y, text, text_color='#000000', font_size=36, font_family=None):
		self.text = str(text)
		self.text_color = text_color
		self.font_size = font_size
		self.font_family = font_family
		self.font = pg.font.SysFont(self.font_family, self.font_size)
		self.x = x
		self.y = y

	def update(self):
		self.image = self.font.render(self.text, True, self.text_color)
		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y

	def draw(self, surface):
		surface.blit(self.image, self.rect)