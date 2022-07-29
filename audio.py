import pygame

class Audio:
	
	def __init__(self, ai_game):
		self.settings = ai_game.settings

	def play_bgmusic(self):
		"""Initialize attributes."""
		pygame.mixer.init()
		pygame.mixer.music.load("Audio/overdrive.mp3")
		pygame.mixer.music.play(loops=-1)