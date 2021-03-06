import pygame
import random
import button

class DiceRoller():
    def __init__(self):
        self.width = 800
        self.height = 600

        self.x = int((1500 / 2) - (self.width / 2))
        self.y = int((800 / 2) - (self.height / 2))

        self.isDrawn = False

        self.closeButton = button.Button(self.x + self.width - 30, self.y + 10, 20, 20, self.deactivate, app = "close")

    def draw(self, surface):
        if self.isDrawn:
            pygame.draw.rect(surface, (34, 32, 52), (self.x, self.y, self.width, self.height), 0)
            pygame.draw.rect(surface, (63, 58, 114), (self.x, self.y, self.width, self.height), 5, 5)

            self.closeButton.draw(surface)

    def update(self, events):
        self.closeButton.update(events)

    def deactivate(self):
        self.isDrawn = False

    def activate(self):
        self.isDrawn = True