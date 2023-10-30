from config import *
import config


class Text:
    def __init__(self, window, text, location, color, size):
        self.window = window
        self.text = text
        self.location = location
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont(None, self.size)
        self.rendered_text = self.font.render(self.text, True, self.color)

    def draw(self):
        self.window.blit(self.rendered_text, self.location)
    
    def change_text(self, text):
        self.text = text
        self.rendered_text = self.font.render(self.text, True, self.color)
