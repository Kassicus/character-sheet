import pygame
import button
import infopanel

class Toolbar():
    def __init__(self):
        self.x = 1400
        self.y = 0

        self.test = button.Button(self.x, self.y, 100, 20, None, "Roll Dice")

    def draw(self, surface):
        pygame.draw.line(surface, (63, 58, 114), (self.x, self.y), (self.x, self.y + 800))

        self.test.draw(surface)

    def update(self, events):
        self.test.update(events)

    def save(self):
        pass

    def load(self):
        pass