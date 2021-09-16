import pygame
import button

class InfoPanel():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.isDrawn = True

        self.closeButton = button.Button(self.x + self.width - 11, self.y - 10, 10, 10, (255, 0, 0), self.close)

    def draw(self, surface):
        if self.isDrawn:
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y - 11, self.width, 11), 0)
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

            self.closeButton.draw(surface)

    def update(self, events):
        if self.isDrawn:
            self.closeButton.update(events)

    def close(self):
        self.isDrawn = False

    def open(self):
        self.isDrawn = True
